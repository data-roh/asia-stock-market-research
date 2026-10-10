# Asia Stock Market Research (ASMR)

Asia Stock Market Research (ASMR) is a static research workspace for Asian disclosures, financial institutions, market overlays and quantitative research. Version 0.1 uses only clearly labeled synthetic market data. It contains no licensed, confidential, employer-owned or live market data.

## The Data Flow

```text
Python
	↓
static/data/*.json
	↓
SvelteKit load function
	↓
Svelte components
	↓
Chart.js
	↓
npm run build
	↓
build/
	↓
GitHub Pages
```

Python remains the analysis layer. It writes reviewed, publication-safe JSON, and SvelteKit loads that JSON for the site. Chart.js draws the market chart in the browser. The production build is a set of static files, which GitHub Actions can publish to GitHub Pages.

## Project Structure

```text
.
├── .github/workflows/deploy.yml  # Build and deploy to GitHub Pages
├── pipeline/build_web_data.py    # Standard-library Python data builder
├── src/
│   ├── lib/
│   │   ├── components/           # Reusable cards, chart and track page
│   │   ├── content/              # Research track copy and topics
│   │   └── types/                # Shared TypeScript data contract
│   └── routes/
│       ├── +page.svelte          # Homepage
│       ├── disclosures/          # Disclosure research
│       ├── core-concepts/        # Financial concepts
│       ├── market-overlay/       # Market indicators
│       └── quant/                # Quant research
├── static/
│   └── data/market_summary.json  # Reviewed synthetic data, intentionally public
├── .gitignore
├── eslint.config.js
├── package.json
├── package-lock.json
└── vite.config.ts
```

## Web Concepts

- **JavaScript (JS)** is the programming language that makes web pages interactive in a browser. Chart.js uses JavaScript to draw the market chart.
- **TypeScript (TS)** is JavaScript with extra type checks. It helps catch mistakes such as passing a string where a market percentage is expected. The browser ultimately runs generated JavaScript.
- **Svelte** lets us describe a page using components and markup. **SvelteKit** organizes those components into routes, loads page data and can render pages ahead of time as static HTML.
- **Vite** is the development server and build tool used by SvelteKit here. It serves the local preview and rebuilds changed files while you work.
- **npm** is Node.js's package manager. It installs the project's JS tools from `package.json` and runs named commands such as `npm run dev`.
- A **route** is a URL-backed page. For example, `src/routes/quant/+page.svelte` creates the `/quant/` page.
- A **component** is a reusable piece of interface. `MarketCard.svelte` renders one market summary, and `MarketBarChart.svelte` renders the chart.
- **JSON** is a text format for structured data. The Python script writes market fields to JSON, then the homepage load function fetches and types that data before rendering it.
- A **build** compiles the application and pre-renders its pages. Here, `npm run build` writes deployable files to `build/`.
- A **deployment** publishes those built files to a host. GitHub Actions runs the checks and build, then GitHub Pages serves the artifact.

### Where the Website Files Live

The project is in the folder `D:\ASMR` on this computer. The browser address `http://127.0.0.1:5173/` is only the local preview; it is not where the source files are stored.

- `src/routes/+page.svelte` is the homepage layout and copy.
- `src/routes/quant/+page.svelte` and the other folders under `src/routes/` are the four research pages.
- `src/lib/components/` contains reusable cards, charts and page sections.
- `src/routes/app.css` contains the visual styles, and `src/app.css` imports them.
- `pipeline/build_web_data.py` creates the demo data; `static/data/market_summary.json` is the JSON file it generates.
- `src/routes/+page.ts` loads that JSON for the homepage.
- `vite.config.ts` configures the local server, static build and GitHub Pages base path.
- `.github/workflows/deploy.yml` tells GitHub how to build and publish the site after a push.

### What Is Running on Localhost?

When `npm run dev` is running, Node.js starts Vite, which starts the SvelteKit development server. That server reads the files in this folder and sends the page to your browser. The browser runs the page's JavaScript and displays the result. Saving a source file makes Vite refresh the preview. Keep the terminal process running while using the preview; stop it with `Ctrl+C` when finished. Other people cannot access your `127.0.0.1` address over the internet.

The Python script is a separate step. It writes the sample JSON file to disk; it does not run the website server. The site reads that file when SvelteKit prepares the homepage.

## First Run

Install Node.js 24 LTS and Python 3. On Windows, the Python launcher may be named `py` rather than `python`. This workspace uses npm.

```sh
npm ci
python pipeline/build_web_data.py
npm run dev
```

On Windows, if `python` is not on PATH, use:

```powershell
py pipeline/build_web_data.py
npm.cmd run dev
```

Open the local URL printed by Vite, usually `http://localhost:5173/`. In PowerShell installations that block `npm.ps1`, run `npm.cmd` instead of `npm`.

## Commands

| Command | What it does |
| --- | --- |
| `python pipeline/build_web_data.py` | Generate the reviewed synthetic JSON file |
| `npm run dev` | Start the local development server with hot reload |
| `npm run check` | Type-check the project and report Svelte diagnostics |
| `npm run lint` | Run ESLint on the project |
| `npm run build` | Pre-render and write the static site to `build/` |
| `npm run preview` | Serve the most recent production build locally |
| `npm run validate` | Run check, lint and production build in sequence |

`npm run dev` starts a local server that updates as files change. `npm run build` makes the production version. A static build is ordinary HTML, CSS, JavaScript and data files, with no server process required to serve each page. The `build/` directory is the complete publishable output, including `index.html`, route pages, `404.html`, browser assets and the market JSON.

## Routes and Components

Routes live under `src/routes/`. Add a new page by creating a folder and a `+page.svelte` file, for example `src/routes/new-topic/+page.svelte`. Add a unique `<svelte:head>` title and description, then link to it with SvelteKit's `resolve()` helper.

Reusable interface pieces live under `src/lib/components/`. Keep shared data shapes in `src/lib/types/market.ts` and track copy in `src/lib/content/research-tracks.ts`, rather than duplicating those definitions in page components.

## Updating Market Data

Edit the synthetic observations in `pipeline/build_web_data.py`, then run:

```sh
python -m py_compile pipeline/build_web_data.py
python pipeline/build_web_data.py
```

On Windows, `py -m py_compile ...` and `py pipeline/build_web_data.py` are equivalent alternatives. The builder writes UTF-8 JSON with readable indentation to `static/data/market_summary.json`; the homepage loads that file through SvelteKit's enhanced `fetch` and the `asset()` path helper. Do not maintain a second market dataset in a Svelte component.

## Public Data Boundary

- `data/raw/` is never public.
- `data/processed/` is never public.
- `data/private/` is never public.
- `static/data/` is intentionally public and downloadable. Review every file there before committing it.

The `.gitignore` rules protect raw, processed, private and licensed research data, local environments, secrets and Parquet files. The generated synthetic JSON is not ignored because GitHub Pages needs it at build time. Removing a file later does not erase it from Git history. Never add credentials, tokens, `.env` files or employer-owned data to this repository.

## GitHub Pages

The Vite configuration derives the SvelteKit base path from `BASE_PATH` for production builds. Internal links use `resolve()` and static files use `asset()`, so the same app works at a repository subpath instead of assuming it lives at the domain root. Development uses an empty base path. The current SvelteKit 3 project configures the adapter and paths in `vite.config.ts`; SvelteKit 3 no longer supports a separate `svelte.config.js`.

The workflow sets `BASE_PATH` from the actual GitHub repository name, runs `npm ci`, checks and lints the project, builds the static output and deploys the `build/` artifact. No application secrets are needed. After the workflow has been pushed, configure the repository once if needed:

```text
Repository
→ Settings
→ Pages
→ Build and deployment
→ Source
→ GitHub Actions
```

The expected project URL format is `https://<github-username>.github.io/<repository-name>/`. If you create a repository named `asia-stock-market-research`, the URL will be `https://data-roh.github.io/asia-stock-market-research/`. The workflow reads the actual repository name, so the app does not hardcode the username or repository path.

This workspace currently has no GitHub remote configured. The `main` branch already has an `init` commit, so create a new GitHub repository without adding a README or license, then connect it. For example, create `data-roh/asia-stock-market-research` and run:

```sh
git remote add origin https://github.com/data-roh/asia-stock-market-research.git
git push -u origin main
```

Before pushing, inspect `git status`, `git diff` and `git diff --cached`, then commit the changes you intend to upload. The repository currently open in the browser is `data-roh/apac-market-lab`, a separate repository; it is not connected to this project. GitHub Pages availability for a private repository depends on the GitHub plan and repository settings. If Pages is unavailable for a private repo, publishing a public website requires a public repository.

## Before Pushing

```sh
python pipeline/build_web_data.py
npm run dev
npm run check
npm run lint
npm run build
```

For a GitHub Pages-style local build, set `BASE_PATH` to the repository subpath. In PowerShell:

```powershell
$env:BASE_PATH = '/asia-stock-market-research'
npm.cmd run build
Remove-Item Env:BASE_PATH
```

In a Bash shell:

```sh
BASE_PATH=/asia-stock-market-research npm run build
```

Then check that `build/index.html`, `build/404.html`, `build/data/market_summary.json`, and the four route directories are present. The pre-rendered HTML uses relative links so it works under the repository subpath.

## Weekly Update Workflow

1. Run the Python analysis.
2. Generate reviewed public JSON.
3. Start the local site.
4. Check numbers, labels and sources.
5. Run validation commands.
6. Commit.
7. Push.
8. Confirm GitHub Pages deployment in the Actions tab.

## Troubleshooting

- **`npm` is blocked in PowerShell:** run `npm.cmd` instead, for example `npm.cmd run check`.
- **Python is not found:** use `py` on Windows, or select/install Python 3 and verify `python --version`.
- **The market JSON does not load:** regenerate it, check that the file exists in `static/data/`, and make sure the request uses `asset('data/market_summary.json')` rather than a root-relative `/data/...` URL.
- **Pages shows a blank page or missing assets:** check the Actions log and confirm that the production build received `BASE_PATH` for the repository name.
- **A route returns 404 on Pages:** confirm the route was prerendered in `build/`, keep the trailing slash convention, and select GitHub Actions as the Pages source.
- **A private file was committed:** remove it from the working tree and follow your organization's process for removing exposed secrets or data from Git history. A normal delete does not erase prior commits.
