import { writable } from 'svelte/store';

export type Locale = 'en' | 'ko';

export const locale = writable<Locale>('en');

export function setLocale(nextLocale: Locale): void {
	locale.set(nextLocale);
	if (typeof window !== 'undefined') window.localStorage.setItem('asmr-locale', nextLocale);
}