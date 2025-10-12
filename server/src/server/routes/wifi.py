import fastapi
import os
from fastapi.routing import APIRoute
from pydantic import BaseModel


def custom_generate_unique_id(route: APIRoute) -> str:
    tag = route.tags[0] if route.tags else "default"
    safe_name = "".join(c if c.isalnum() else "_" for c in route.name)
    method = sorted(route.methods)[0].lower() if route.methods else "get"
    return f"{tag}_{safe_name}_{method}"


router = fastapi.APIRouter(
    prefix="/api", generate_unique_id_function=custom_generate_unique_id
)


class Credentials(BaseModel):
    ssid: str
    password: str


class ErrorResponse(BaseModel):
    detail: str


WPA_SUPPLICANT_CONF = "/etc/wpa_supplicant/wpa_supplicant.conf"


def add_wifi(ssid, password) -> None:
    if os.geteuid() != 0:
        raise PermissionError("You need to run this script as root")

    network_block = f"""
network={{
    ssid="{ssid}"
    psk="{password}"
}}
"""
    with open(WPA_SUPPLICANT_CONF, "a") as f:
        f.write(network_block)


@router.post(
    "/set_credentials",
    responses={401: {"model": ErrorResponse, "description": "Unauthorized"}},
)
def set_credentials(credentials: Credentials) -> bool:
    print(f"Got credentials: {credentials}")
    try:
        add_wifi(credentials.ssid, credentials.password)
    except PermissionError as e:
        raise fastapi.HTTPException(status_code=401, detail=str(e))
    return True
