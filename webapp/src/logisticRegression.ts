/**
 * logisticRegression.ts
 *
 * A real, from-scratch port of the binary logistic regression that
 * module_04_supervised/classify_iris.py trains via sklearn's
 * `LogisticRegression`. Sklearn solves the same optimization problem
 * internally (minimize binary cross-entropy via gradient-based
 * optimization); here we do it explicitly, one gradient-descent step
 * at a time, so it can be watched live in the browser.
 *
 * Model:   z = w . x + b
 *          p = sigmoid(z)                (predicted probability of class 1)
 * Loss:    L = -mean( y*log(p) + (1-y)*log(1-p) )    (binary cross-entropy)
 * Gradient (standard logistic regression result):
 *          dL/dw_j = mean( (p - y) * x_j )
 *          dL/db   = mean( p - y )
 * Update:  w -= lr * dL/dw ,  b -= lr * dL/db
 */

export interface Point {
  x: number;
  y: number;
  label: 0 | 1;
}

export function sigmoid(z: number): number {
  // numerically stable sigmoid
  if (z >= 0) {
    const e = Math.exp(-z);
    return 1 / (1 + e);
  }
  const e = Math.exp(z);
  return e / (1 + e);
}

export class LogisticRegression2D {
  w1 = 0;
  w2 = 0;
  b = 0;
  lr: number;
  step_ = 0;
  lossHistory: number[] = [];

  constructor(lr = 0.5) {
    this.lr = lr;
    this.reset();
  }

  reset(): void {
    // small random init, mirrors the course's habit of starting from
    // near-zero weights rather than a lucky guess
    this.w1 = (Math.random() - 0.5) * 0.2;
    this.w2 = (Math.random() - 0.5) * 0.2;
    this.b = 0;
    this.step_ = 0;
    this.lossHistory = [];
  }

  predictProba(x1: number, x2: number): number {
    return sigmoid(this.w1 * x1 + this.w2 * x2 + this.b);
  }

  /** One full-batch gradient descent step over the whole dataset. Returns the loss BEFORE the update. */
  step(data: Point[]): number {
    const n = data.length;
    let dW1 = 0;
    let dW2 = 0;
    let dB = 0;
    let loss = 0;

    for (const p of data) {
      const pred = this.predictProba(p.x, p.y);
      const clipped = Math.min(Math.max(pred, 1e-9), 1 - 1e-9);
      loss += -(p.label * Math.log(clipped) + (1 - p.label) * Math.log(1 - clipped));

      const err = pred - p.label; // dL/dz
      dW1 += err * p.x;
      dW2 += err * p.y;
      dB += err;
    }

    loss /= n;
    dW1 /= n;
    dW2 /= n;
    dB /= n;

    this.w1 -= this.lr * dW1;
    this.w2 -= this.lr * dW2;
    this.b -= this.lr * dB;

    this.step_ += 1;
    this.lossHistory.push(loss);
    return loss;
  }

  accuracy(data: Point[]): number {
    let correct = 0;
    for (const p of data) {
      const pred = this.predictProba(p.x, p.y) >= 0.5 ? 1 : 0;
      if (pred === p.label) correct += 1;
    }
    return correct / data.length;
  }
}

/** Two roughly-linearly-separable Gaussian blobs, a small synthetic 2D dataset. */
export function makeBlobs(n = 120, seed = 42): Point[] {
  let s = seed;
  const rand = () => {
    // simple mulberry32 PRNG for reproducibility
    s |= 0;
    s = (s + 0x6d2b79f5) | 0;
    let t = Math.imul(s ^ (s >>> 15), 1 | s);
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
  const gaussian = () => {
    // Box-Muller
    const u1 = Math.max(rand(), 1e-9);
    const u2 = rand();
    return Math.sqrt(-2 * Math.log(u1)) * Math.cos(2 * Math.PI * u2);
  };

  const points: Point[] = [];
  const half = Math.floor(n / 2);
  for (let i = 0; i < half; i++) {
    points.push({ x: -1.2 + gaussian() * 0.6, y: -0.8 + gaussian() * 0.6, label: 0 });
  }
  for (let i = 0; i < n - half; i++) {
    points.push({ x: 1.2 + gaussian() * 0.6, y: 0.8 + gaussian() * 0.6, label: 1 });
  }
  return points;
}
