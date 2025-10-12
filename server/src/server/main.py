import json
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from typer import Typer
import uvicorn

from .routes.wifi import router as wifi_router

cli = Typer()


def build_app(serve: bool):
    app = FastAPI()

    app.include_router(wifi_router)
    if serve:
        app.mount(
            "/", StaticFiles(packages=[("server", "build")], html=True), name="spa"
        )

    return app


@cli.command()
def serve(port: int = 8080):
    uvicorn.run(host="0.0.0.0", app=build_app(serve=True), port=port)
    pass


@cli.command()
def export_schema():
    app = build_app(serve=False)
    schema = app.openapi()
    print(json.dumps(schema))
