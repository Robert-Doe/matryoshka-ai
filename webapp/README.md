# Matryoshka AI — web demo

A real, interactive, in-browser port of `module_04_supervised`'s logistic regression:
sigmoid output, binary cross-entropy loss, and full-batch gradient descent — trained
live in TypeScript on a small synthetic 2D dataset, with the decision boundary and loss
redrawn on every step. No canned animation: click "Step" and it takes one real gradient
update; click "Run" and it trains until convergence.

Also includes a small presentational SVG of the AI ⊃ ML ⊃ DL ⊃ GenAI nesting-doll model
from the course README.

## Local development

```bash
cd webapp
npm install
npm run dev
```

Opens a local dev server (Vite) with hot reload.

## Build

```bash
cd webapp
npm install
npm run build
```

Outputs a static site to `webapp/dist/`. This must complete with zero errors before deploying.

## Deploy (static hosting)

Any static host works. Point it at this directory:

- **Root directory:** `webapp`
- **Build command:** `npm run build`
- **Output directory:** `dist`

### Vercel
```bash
vercel --cwd webapp
```
Or via the dashboard: import the repo, set root directory to `webapp`, build command `npm run build`, output directory `dist`.

### Netlify
Site settings → Build & deploy:
- Base directory: `webapp`
- Build command: `npm run build`
- Publish directory: `webapp/dist`

### Cloudflare Pages
- Root directory: `webapp`
- Build command: `npm run build`
- Build output directory: `dist`

## Source layout

- `src/logisticRegression.ts` — the ported algorithm (sigmoid, BCE loss, gradient descent, synthetic blob generator)
- `src/main.ts` — UI wiring, canvas rendering, and the nesting-doll intro diagram
- `src/style.css` — design system (dark theme, CSS custom properties)
