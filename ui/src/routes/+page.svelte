<script lang="ts">
	import type { Credentials } from '../client';
	import { defaultSetCredentialsPost } from '../client';

	let ssid = '';
	let password = '';
	async function handleSubmit(event: Event) {
		event.preventDefault();

		const credentials: Credentials = { ssid, password };

		try {
			const result = await defaultSetCredentialsPost({
				body: credentials,
				throwOnError: true
			});

			if (result.data !== undefined) {
				alert('API returned: ' + result.data);
			} else {
				alert('Unexpected response: ' + JSON.stringify(result));
			}
		} catch (err: unknown) {
			alert('API Error: ' + err);
		}
	}
</script>

<main class="flex min-h-screen flex-col items-center justify-center bg-gray-50 p-6">
	<div class="w-full max-w-md rounded-2xl bg-white p-8 shadow-lg">
		<h1 class="mb-4 text-center text-3xl font-bold text-blue-600">Enter WiFi credentials</h1>
		<p class="mb-8 text-center text-gray-600"></p>

		<form class="space-y-4" on:submit={handleSubmit}>
			<div>
				<label for="wifi" class="mb-1 block text-sm font-medium text-gray-700">Name</label>
				<input
					id="name"
					type="text"
					bind:value={ssid}
					placeholder="Wifi Name"
					class="w-full rounded-lg border border-gray-300 px-4 py-2 focus:ring-2 focus:ring-blue-400 focus:outline-none"
				/>
			</div>

			<div>
				<label for="Password" class="mb-1 block text-sm font-medium text-gray-700">Password</label>
				<input
					id="password"
					type="password"
					bind:value={password}
					placeholder="Password"
					required
					class="w-full rounded-lg border border-gray-300 px-4 py-2 focus:ring-2 focus:ring-blue-400 focus:outline-none"
				/>
			</div>

			<button
				type="submit"
				class="w-full rounded-lg bg-blue-600 px-4 py-2 font-semibold text-white transition-colors duration-200 hover:bg-blue-700"
			>
				Save
			</button>
		</form>
	</div>
</main>
