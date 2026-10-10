import adapter from '@sveltejs/adapter-static';
import { sveltekit } from '@sveltejs/kit/vite';
import { defineConfig } from 'vite';
import { argv, env } from 'node:process';

const configuredBase = env.BASE_PATH;
const basePath = argv.includes('dev') || !configuredBase
	? ''
	: configuredBase.startsWith('/')
		? (configuredBase as `/${string}`)
		: '';

export default defineConfig({
	plugins: [
		sveltekit({
			adapter: adapter({ fallback: '404.html' }),
			paths: {
				base: basePath
			},
			compilerOptions: {
				// Force runes mode for the project, except for libraries. Can be removed in svelte 6.
				runes: ({ filename }) =>
					filename.split(/[/\\]/).includes('node_modules') ? undefined : true
			}
		})
	]
});
