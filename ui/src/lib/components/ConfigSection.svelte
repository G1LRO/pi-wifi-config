<script lang="ts">
	import type { Snippet } from 'svelte';

	interface Props {
		title: string;
		enabled: boolean;
		children: Snippet;
		onToggle: (enabled: boolean) => void;
	}

	let { title, enabled, children, onToggle }: Props = $props();
</script>

<section
	class="rounded-lg border border-gray-200 bg-white p-6 shadow-sm {enabled ? '' : 'opacity-60'}"
>
	<div class="mb-4">
		<div class="flex items-center gap-3">
			<input
				type="checkbox"
				checked={enabled}
				onchange={(e) => onToggle(e.currentTarget.checked)}
				id="checkbox-{title.replace(/\s+/g, '-').toLowerCase()}"
				class="h-6 w-6 rounded border-2 border-gray-400 text-blue-600 focus:ring-2 focus:ring-blue-500 cursor-pointer"
			/>
			<label 
				for="checkbox-{title.replace(/\s+/g, '-').toLowerCase()}"
				class="cursor-pointer"
			>
				<h2 class="text-xl font-semibold text-gray-800">{title}</h2>
			</label>
		</div>
		<div class="ml-9 mt-1">
			<span class="text-sm text-gray-600 italic">
				Select to make changes to this section
			</span>
		</div>
	</div>
	<div class={enabled ? '' : 'pointer-events-none'}>
		{@render children()}
	</div>
</section>
