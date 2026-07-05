"""
visualize.py  —  Module 03

A plot answers questions a table can't. We make three charts that tell the
story of the cleaned login data, and save them as PNGs so you can view them
without a display server.

Run:  python module_03_data/visualize.py
Then open the PNGs written into module_03_data/plots/.
"""

import os
import matplotlib
matplotlib.use("Agg")   # render to files, no GUI window needed
import matplotlib.pyplot as plt
import pandas as pd

CLEAN = "module_03_data/clean_data.csv"
OUTDIR = "module_03_data/plots"


def main():
    if not os.path.exists(CLEAN):
        raise SystemExit("Run clean_data.py first to produce clean_data.csv")
    os.makedirs(OUTDIR, exist_ok=True)
    df = pd.read_csv(CLEAN)

    # 1) DISTRIBUTION — histogram of bytes_sent. Shows the two populations:
    #    a cluster of normal logins and a far-right tail of exfil-sized events.
    plt.figure(figsize=(6, 4))
    plt.hist(df["bytes_sent"], bins=20, color="#4aa8ff", edgecolor="white")
    plt.title("Distribution of bytes_sent (note the far-right outliers)")
    plt.xlabel("bytes sent"); plt.ylabel("count")
    plt.tight_layout(); plt.savefig(f"{OUTDIR}/1_bytes_histogram.png", dpi=110); plt.close()

    # 2) COMPARISON — average failed_attempts by label. The signal, visualized.
    means = df.groupby("label")["failed_attempts"].mean()
    plt.figure(figsize=(5, 4))
    means.plot(kind="bar", color=["#3ddc84", "#ff6b6b"])
    plt.title("Avg failed login attempts: normal vs suspicious")
    plt.ylabel("mean failed_attempts"); plt.xticks(rotation=0)
    plt.tight_layout(); plt.savefig(f"{OUTDIR}/2_failed_by_label.png", dpi=110); plt.close()

    # 3) RELATIONSHIP — scatter of duration vs bytes, colored by label. Do the
    #    classes separate in feature space? If yes, a model can learn the boundary.
    colors = df["label"].map({"normal": "#3ddc84", "suspicious": "#ff6b6b"})
    plt.figure(figsize=(6, 4))
    plt.scatter(df["duration_sec"], df["bytes_sent"], c=colors, s=40, edgecolor="k", linewidth=.3)
    plt.title("duration vs bytes_sent (green=normal, red=suspicious)")
    plt.xlabel("duration (s)"); plt.ylabel("bytes sent")
    plt.tight_layout(); plt.savefig(f"{OUTDIR}/3_duration_vs_bytes.png", dpi=110); plt.close()

    print("Wrote 3 plots to", OUTDIR)
    for f in ["1_bytes_histogram.png", "2_failed_by_label.png", "3_duration_vs_bytes.png"]:
        print("   -", f)
    print("\nWhat the plots reveal:")
    print("  1) bytes_sent has two populations — normal cluster + exfil-sized tail.")
    print("  2) suspicious logins have MANY more failed attempts (a strong feature).")
    print("  3) suspicious points sit apart (short duration + huge bytes) — SEPARABLE,")
    print("     which means a classifier in Module 04 should learn this easily.")


if __name__ == "__main__":
    main()
