#!/usr/bin/env python3
"""build_cv.py -- LaTeX CV builder with 1-page enforcement.

Usage:
    python scripts/build_cv.py --input profile/cv.tex --output profile/cv_builds/cv_mistral_20260528.pdf
    python scripts/build_cv.py --input /tmp/cv_adapted.tex --output /tmp/cv_out.pdf

The script:
  1. Copies the input .tex to a temp directory
  2. Runs pdflatex twice (for correct cross-references)
  3. Reads page count from pdflatex output
  4. If pages > 1: exits with error code 1 and suggestions
  5. If pages == 1: copies PDF to output path
  6. Cleans up temp directory

Requirements:
    pdflatex on PATH.
    - Windows: MiKTeX  https://miktex.org
    - Mac:     MacTeX  https://www.tug.org/mactex/
    - Linux:   sudo apt install texlive-full

No pip packages required.
"""

from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


def find_latex_cmd() -> str | None:
    for cmd in ("pdflatex", "xelatex", "lualatex"):
        if shutil.which(cmd):
            return cmd
    return None


def parse_page_count(pdflatex_stdout: str) -> int | None:
    """Parse 'Output written on cv.pdf (2 pages, ...)' from pdflatex output."""
    m = re.search(r"Output written on .+?\((\d+) page", pdflatex_stdout)
    return int(m.group(1)) if m else None


def count_pages_fallback(pdf_path: Path) -> int | None:
    """Fallback: scan raw PDF bytes for /Count entries."""
    try:
        content = pdf_path.read_bytes().decode("latin-1", errors="replace")
        counts = [int(c) for c in re.findall(r"/Count\s+(\d+)", content)]
        return max(counts) if counts else None
    except Exception:
        return None


def build(input_tex: Path, output_pdf: Path) -> None:
    cmd = find_latex_cmd()
    if not cmd:
        sys.exit(
            "ERROR: pdflatex not found on PATH.\n"
            "  Windows: https://miktex.org\n"
            "  Mac:     https://www.tug.org/mactex/\n"
            "  Linux:   sudo apt install texlive-full"
        )

    input_tex = input_tex.expanduser().resolve()
    if not input_tex.exists():
        sys.exit(f"ERROR: Input file not found: {input_tex}")

    output_pdf = output_pdf.expanduser().resolve()
    output_pdf.parent.mkdir(parents=True, exist_ok=True)

    with tempfile.TemporaryDirectory() as tmpdir:
        tmp_tex = Path(tmpdir) / "cv.tex"
        shutil.copy(input_tex, tmp_tex)

        last_result = None
        for pass_num in range(1, 3):
            result = subprocess.run(
                [cmd, "-interaction=nonstopmode", "-output-directory", tmpdir, str(tmp_tex)],
                capture_output=True,
                text=True,
                cwd=tmpdir,
            )
            last_result = result
            if result.returncode != 0 and pass_num == 2:
                print("ERROR: pdflatex failed. Last 20 lines:", file=sys.stderr)
                for line in (result.stdout + result.stderr).splitlines()[-20:]:
                    print(f"  {line}", file=sys.stderr)
                sys.exit(1)

        tmp_pdf = Path(tmpdir) / "cv.pdf"
        if not tmp_pdf.exists():
            sys.exit("ERROR: pdflatex ran but no PDF was produced.")

        pages = parse_page_count(last_result.stdout) or count_pages_fallback(tmp_pdf)
        print(f"Built: {pages or '?'} page(s)")

        if pages and pages > 1:
            print(file=sys.stderr)
            print(f"ERROR: CV is {pages} pages. Maximum is 1 page.", file=sys.stderr)
            print(file=sys.stderr)
            print("Suggestions:", file=sys.stderr)
            print("  - Remove 1-2 bullets from older or less relevant experiences", file=sys.stderr)
            print("  - Shorten the summary by 1 line", file=sys.stderr)
            print("  - Use \\vspace{-3pt} before section headers to reclaim space", file=sys.stderr)
            sys.exit(1)

        shutil.copy(tmp_pdf, output_pdf)
        print(f"OK  PDF saved: {output_pdf}")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Build a LaTeX CV to PDF and enforce the 1-page constraint.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Build the base CV:
  python scripts/build_cv.py --input profile/cv.tex --output profile/cv_builds/cv_base.pdf

  # Build an adapted version (agent writes a temp .tex first):
  python scripts/build_cv.py \\
    --input /tmp/cv_mistral_adapted.tex \\
    --output profile/cv_builds/cv_mistral_20260528.pdf
        """,
    )
    parser.add_argument("--input", required=True, help="Path to the .tex source file")
    parser.add_argument("--output", required=True, help="Path for the output .pdf")
    args = parser.parse_args()

    build(Path(args.input), Path(args.output))


if __name__ == "__main__":
    main()
