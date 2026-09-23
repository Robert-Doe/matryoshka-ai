import './style.css';
import { LogisticRegression2D, makeBlobs, type Point } from './logisticRegression';

const app = document.querySelector<HTMLDivElement>('#app')!;

app.innerHTML = `
  <div class="topbar">
    <div class="brand">🪆 matryoshka-ai</div>
    <div class="links">
      <a href="https://github.com/Robert-Doe/matryoshka-ai" target="_blank" rel="noopener">GitHub</a>
      <a href="https://robertdoe.com">← robertdoe.com</a>
    </div>
  </div>

  <div class="hero">
    <h1>Matryoshka <span class="accent">AI</span></h1>
    <p class="tagline">
      AI is a set of nested layers, like a matryoshka doll. Below is the mental model from the
      course README, then a real logistic regression, the same algorithm module_04_supervised
      trains on the Iris dataset, learning live in your browser via gradient descent.
    </p>
  </div>

  <div class="nest-card">
    <h2>The nesting-doll model</h2>
    <p class="sub">Artificial Intelligence ⊃ Machine Learning ⊃ Deep Learning ⊃ Generative AI / LLMs</p>
    <div class="nest-rings" id="nest-rings"></div>
  </div>

  <div class="section">
    <div class="section-head">
      <div class="eyebrow">Module 04 &middot; Supervised Learning &middot; Live Port</div>
      <h2>Watch logistic regression learn</h2>
      <p>
        A real binary logistic regression — sigmoid output, binary cross-entropy loss,
        full-batch gradient descent — trained step by step on a small synthetic 2D dataset.
        Click <strong>Step</strong> to take one gradient-descent update, or <strong>Run</strong>
        to watch the decision boundary move as the loss actually decreases.
      </p>
    </div>

    <div class="demo-card">
      <div class="controls">
        <button id="btn-step">Step</button>
        <button id="btn-run" class="secondary">Run</button>
        <button id="btn-reset" class="secondary">Reset</button>
        <label class="field">
          learning rate
          <input type="range" id="lr" min="0.05" max="2" step="0.05" value="0.5" />
          <span id="lr-val">0.50</span>
        </label>
      </div>

      <canvas id="canvas" width="640" height="440"></canvas>

      <div class="stats">
        <div class="stat"><span class="k">Step</span><span class="v" id="stat-step">0</span></div>
        <div class="stat"><span class="k">Loss (BCE)</span><span class="v accent" id="stat-loss">–</span></div>
        <div class="stat"><span class="k">Train accuracy</span><span class="v" id="stat-acc">–</span></div>
      </div>

      <div class="legend">
        <span><span class="dot" style="background:#7dd3fc"></span>class 0</span>
        <span><span class="dot" style="background:#d4a017"></span>class 1</span>
        <span><span class="dot" style="background:#eeece6"></span>decision boundary (p = 0.5)</span>
      </div>
    </div>
  </div>

  <div class="footer">
    <span>Built as a real TypeScript port of <code>module_04_supervised</code> — no canned animation, actual gradient descent.</span>
    <span><code>matryoshka-ai/webapp</code></span>
  </div>
`;

// ---------------------------------------------------------------------------
// Nesting-doll intro diagram (presentational only)
// ---------------------------------------------------------------------------
const ringsHost = document.querySelector<HTMLDivElement>('#nest-rings')!;
ringsHost.innerHTML = `
<svg viewBox="0 0 460 240" width="460" xmlns="http://www.w3.org/2000/svg">
  <ellipse cx="230" cy="120" rx="220" ry="110" fill="none" stroke="#d4a017" stroke-opacity="0.35" stroke-width="1.5"/>
  <ellipse cx="230" cy="120" rx="165" ry="82" fill="none" stroke="#d4a017" stroke-opacity="0.55" stroke-width="1.5"/>
  <ellipse cx="230" cy="120" rx="110" ry="55" fill="none" stroke="#d4a017" stroke-opacity="0.75" stroke-width="1.5"/>
  <ellipse cx="230" cy="120" rx="55" ry="28" fill="#d4a017" fill-opacity="0.14" stroke="#d4a017" stroke-width="1.5"/>
  <text x="230" y="24" text-anchor="middle" fill="#9a9992" font-family="JetBrains Mono, monospace" font-size="13">Artificial Intelligence</text>
  <text x="230" y="52" text-anchor="middle" fill="#9a9992" font-family="JetBrains Mono, monospace" font-size="12">Machine Learning</text>
  <text x="230" y="78" text-anchor="middle" fill="#9a9992" font-family="JetBrains Mono, monospace" font-size="11">Deep Learning</text>
  <text x="230" y="124" text-anchor="middle" fill="#eeece6" font-family="Space Grotesk, sans-serif" font-weight="700" font-size="12">GenAI / LLMs</text>
</svg>
`;

// ---------------------------------------------------------------------------
// Real logistic regression demo
// ---------------------------------------------------------------------------
const canvas = document.querySelector<HTMLCanvasElement>('#canvas')!;
const ctx = canvas.getContext('2d')!;

const btnStep = document.querySelector<HTMLButtonElement>('#btn-step')!;
const btnRun = document.querySelector<HTMLButtonElement>('#btn-run')!;
const btnReset = document.querySelector<HTMLButtonElement>('#btn-reset')!;
const lrSlider = document.querySelector<HTMLInputElement>('#lr')!;
const lrVal = document.querySelector<HTMLSpanElement>('#lr-val')!;
const statStep = document.querySelector<HTMLSpanElement>('#stat-step')!;
const statLoss = document.querySelector<HTMLSpanElement>('#stat-loss')!;
const statAcc = document.querySelector<HTMLSpanElement>('#stat-acc')!;

let data: Point[] = makeBlobs(120, 42);
let model = new LogisticRegression2D(parseFloat(lrSlider.value));
let running = false;
let rafId: number | null = null;

// data-space bounds for plotting
const BOUND = 3;

function toCanvas(x: number, y: number): [number, number] {
  const px = ((x + BOUND) / (2 * BOUND)) * canvas.width;
  const py = canvas.height - ((y + BOUND) / (2 * BOUND)) * canvas.height;
  return [px, py];
}

function draw(): void {
  const w = canvas.width;
  const h = canvas.height;
  ctx.fillStyle = '#141416';
  ctx.fillRect(0, 0, w, h);

  // gridlines
  ctx.strokeStyle = 'rgba(154,153,146,0.15)';
  ctx.lineWidth = 1;
  for (let gx = -BOUND; gx <= BOUND; gx++) {
    const [px] = toCanvas(gx, 0);
    ctx.beginPath();
    ctx.moveTo(px, 0);
    ctx.lineTo(px, h);
    ctx.stroke();
  }
  for (let gy = -BOUND; gy <= BOUND; gy++) {
    const [, py] = toCanvas(0, gy);
    ctx.beginPath();
    ctx.moveTo(0, py);
    ctx.lineTo(w, py);
    ctx.stroke();
  }
  // axes
  ctx.strokeStyle = 'rgba(154,153,146,0.4)';
  const [ox, oy] = toCanvas(0, 0);
  ctx.beginPath();
  ctx.moveTo(ox, 0);
  ctx.lineTo(ox, h);
  ctx.moveTo(0, oy);
  ctx.lineTo(w, oy);
  ctx.stroke();

  // decision-boundary shading via a light probability field (cheap, coarse grid)
  const cell = 12;
  for (let py = 0; py < h; py += cell) {
    for (let px = 0; px < w; px += cell) {
      const x = (px / w) * (2 * BOUND) - BOUND;
      const y = BOUND - (py / h) * (2 * BOUND);
      const p = model.predictProba(x, y);
      const alpha = Math.abs(p - 0.5) * 0.35;
      ctx.fillStyle = p >= 0.5 ? `rgba(212,160,23,${alpha})` : `rgba(125,211,252,${alpha})`;
      ctx.fillRect(px, py, cell, cell);
    }
  }

  // decision boundary line: w1*x + w2*y + b = 0  =>  y = -(w1*x + b)/w2
  ctx.strokeStyle = '#eeece6';
  ctx.lineWidth = 2;
  ctx.beginPath();
  let started = false;
  if (Math.abs(model.w2) > 1e-6) {
    for (let x = -BOUND; x <= BOUND; x += 0.05) {
      const y = -(model.w1 * x + model.b) / model.w2;
      const [px, py] = toCanvas(x, y);
      if (!started) {
        ctx.moveTo(px, py);
        started = true;
      } else {
        ctx.lineTo(px, py);
      }
    }
  }
  ctx.stroke();

  // points
  for (const p of data) {
    const [px, py] = toCanvas(p.x, p.y);
    ctx.beginPath();
    ctx.arc(px, py, 5, 0, Math.PI * 2);
    ctx.fillStyle = p.label === 1 ? '#d4a017' : '#7dd3fc';
    ctx.fill();
    ctx.strokeStyle = 'rgba(0,0,0,0.35)';
    ctx.lineWidth = 1;
    ctx.stroke();
  }
}

function updateStats(loss: number | null): void {
  statStep.textContent = String(model.step_);
  statLoss.textContent = loss === null ? '–' : loss.toFixed(4);
  statAcc.textContent = `${(model.accuracy(data) * 100).toFixed(1)}%`;
}

function doStep(): number {
  const loss = model.step(data);
  return loss;
}

function stepAndRender(): void {
  const loss = doStep();
  draw();
  updateStats(loss);
}

function loop(): void {
  if (!running) return;
  const loss = doStep();
  draw();
  updateStats(loss);
  if (loss < 0.02 || model.step_ > 3000) {
    stopRun();
    return;
  }
  rafId = requestAnimationFrame(loop);
}

function startRun(): void {
  running = true;
  btnRun.textContent = 'Pause';
  loop();
}

function stopRun(): void {
  running = false;
  btnRun.textContent = 'Run';
  if (rafId !== null) cancelAnimationFrame(rafId);
}

btnStep.addEventListener('click', () => {
  if (running) stopRun();
  stepAndRender();
});

btnRun.addEventListener('click', () => {
  if (running) {
    stopRun();
  } else {
    startRun();
  }
});

btnReset.addEventListener('click', () => {
  stopRun();
  data = makeBlobs(120, Math.floor(Math.random() * 100000));
  model = new LogisticRegression2D(parseFloat(lrSlider.value));
  draw();
  updateStats(null);
});

lrSlider.addEventListener('input', () => {
  model.lr = parseFloat(lrSlider.value);
  lrVal.textContent = model.lr.toFixed(2);
});

draw();
updateStats(null);
