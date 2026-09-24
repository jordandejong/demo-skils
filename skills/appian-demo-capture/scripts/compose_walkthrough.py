#!/usr/bin/env python3
"""Stitch numbered screenshots + narration wavs into a 16:9 walkthrough mp4."""
from __future__ import annotations

import argparse
import subprocess
import sys
import tempfile
from pathlib import Path

VIDEO_W, VIDEO_H = 1920, 1080


def stems(shots: Path, narration: Path) -> list[str]:
    pngs = {p.stem: p for p in shots.glob("*.png")}
    wavs = {p.stem: p for p in narration.glob("*.wav")}
    keys = sorted(set(pngs) & set(wavs))
    if not keys:
        sys.exit(f"no matching stems in {shots} and {narration}")
    return keys


def duration_seconds(wav: Path) -> float:
    out = subprocess.check_output(
        [
            "ffprobe",
            "-v",
            "error",
            "-show_entries",
            "format=duration",
            "-of",
            "csv=p=0",
            str(wav),
        ],
        text=True,
    ).strip()
    return float(out)


def render_scene(png: Path, wav: Path, dest: Path, tail: float) -> None:
    dur = duration_seconds(wav) + tail
    vf = (
        f"scale={VIDEO_W}:{VIDEO_H}:force_original_aspect_ratio=decrease,"
        f"pad={VIDEO_W}:{VIDEO_H}:(ow-iw)/2:(oh-ih)/2:color=0x020A51,"
        "format=yuv420p"
    )
    subprocess.check_call(
        [
            "ffmpeg",
            "-y",
            "-loop",
            "1",
            "-framerate",
            "30",
            "-t",
            f"{dur:.3f}",
            "-i",
            str(png),
            "-i",
            str(wav),
            "-vf",
            vf,
            "-c:v",
            "libx264",
            "-tune",
            "stillimage",
            "-pix_fmt",
            "yuv420p",
            "-c:a",
            "aac",
            "-shortest",
            "-movflags",
            "+faststart",
            str(dest),
        ],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )


def concat(parts: list[Path], out: Path) -> None:
    lst = out.with_suffix(".concat.txt")
    lst.write_text("".join(f"file '{p.resolve()}'\n" for p in parts), encoding="utf-8")
    try:
        subprocess.check_call(
            [
                "ffmpeg",
                "-y",
                "-f",
                "concat",
                "-safe",
                "0",
                "-i",
                str(lst),
                "-c",
                "copy",
                "-movflags",
                "+faststart",
                str(out),
            ],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
    finally:
        lst.unlink(missing_ok=True)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--shots", type=Path, required=True)
    ap.add_argument("--narration", type=Path, required=True)
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--tail", type=float, default=0.4, help="silence after each line")
    args = ap.parse_args()
    args.out.parent.mkdir(parents=True, exist_ok=True)
    keys = stems(args.shots, args.narration)
    with tempfile.TemporaryDirectory(prefix="walkthrough-") as tmp:
        parts = []
        for key in keys:
            dest = Path(tmp) / f"{key}.mp4"
            render_scene(
                next(args.shots.glob(f"{key}.png")),
                next(args.narration.glob(f"{key}.wav")),
                dest,
                args.tail,
            )
            parts.append(dest)
        concat(parts, args.out)
    print(args.out.resolve())


if __name__ == "__main__":
    main()
