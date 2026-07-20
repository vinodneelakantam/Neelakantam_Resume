#!/usr/bin/env python3
"""Convert an HTML file (or URL) to PDF using headless Edge/Chrome."""

from __future__ import annotations

import argparse
import os
import subprocess
import sys
from pathlib import Path
from urllib.parse import urlparse


def is_url(value: str) -> bool:
    parsed = urlparse(value)
    return parsed.scheme in {"http", "https", "file"}


def find_browser(explicit_path: str | None = None) -> Path:
    if explicit_path:
        candidate = Path(explicit_path).expanduser().resolve()
        if candidate.exists():
            return candidate
        raise FileNotFoundError(f"Browser not found at: {candidate}")

    env_candidates = [
        os.environ.get("EDGE_PATH"),
        os.environ.get("CHROME_PATH"),
    ]

    default_candidates = [
        r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    ]

    for item in env_candidates + default_candidates:
        if not item:
            continue
        candidate = Path(item)
        if candidate.exists():
            return candidate

    raise FileNotFoundError(
        "No supported browser found. Install Microsoft Edge/Google Chrome "
        "or pass --browser with a valid executable path."
    )


def resolve_html_input(html_input: str) -> str:
    if is_url(html_input):
        return html_input

    html_path = Path(html_input).expanduser().resolve()
    if not html_path.exists():
        raise FileNotFoundError(f"HTML input file not found: {html_path}")
    return html_path.as_uri()


def resolve_output_path(output: str | None, html_input: str) -> Path:
    if output:
        out_path = Path(output).expanduser().resolve()
    else:
        if is_url(html_input):
            out_path = Path.cwd() / "output.pdf"
        else:
            source = Path(html_input).expanduser().resolve()
            out_path = source.with_suffix(".pdf")

    out_path.parent.mkdir(parents=True, exist_ok=True)
    return out_path


def convert_html_to_pdf(browser: Path, html_uri: str, output_pdf: Path) -> None:
    command = [
        str(browser),
        "--headless",
        "--disable-gpu",
        f"--print-to-pdf={output_pdf}",
        "--no-pdf-header-footer",
        html_uri,
    ]

    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode != 0:
        stderr = (result.stderr or "").strip()
        stdout = (result.stdout or "").strip()
        details = stderr or stdout or "Unknown browser error"
        raise RuntimeError(f"PDF conversion failed: {details}")

    if not output_pdf.exists() or output_pdf.stat().st_size == 0:
        raise RuntimeError("PDF conversion failed: output file was not created.")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Convert an HTML file (or URL) to PDF using Edge/Chrome headless mode."
    )
    parser.add_argument(
        "--input",
        "-i",
        required=True,
        help="Path to HTML file or URL.",
    )
    parser.add_argument(
        "--output",
        "-o",
        help="Output PDF path. If omitted, uses input filename with .pdf.",
    )
    parser.add_argument(
        "--browser",
        "-b",
        help="Optional browser executable path (Edge/Chrome).",
    )
    return parser


def main() -> int:
    parser = build_parser()
    try:
        args = parser.parse_args()
    except SystemExit as exc:
        code = exc.code if isinstance(exc.code, int) else 1
        return code

    try:
        browser = find_browser(args.browser)
        html_uri = resolve_html_input(args.input)
        output_pdf = resolve_output_path(args.output, args.input)
        convert_html_to_pdf(browser, html_uri, output_pdf)
        print(f"PDF created: {output_pdf}")
        return 0
    except Exception as exc:  # noqa: BLE001
        print(f"Error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    main()
