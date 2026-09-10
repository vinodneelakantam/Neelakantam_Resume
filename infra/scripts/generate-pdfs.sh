#!/usr/bin/env bash
# Builds the resume-pdf-tool Docker image and regenerates all resume/cover-letter PDFs with it.
set -euo pipefail

cd "$(dirname "$0")/../.."

IMAGE="resume-pdf-tool:latest"

docker build -t "$IMAGE" -f infra/Dockerfile infra

run() {
    docker run --rm -v "$(pwd):/workspace" -w /workspace "$IMAGE" --input "$1" --output "$2"
}

# Every resume/cover-letter variant follows people/<person>/{resume,cover-letter}/[<variant>/]{resume,cover-letter}.html
# so new people or variants are picked up automatically without editing this script.
while IFS= read -r -d '' html; do
    run "$html" "${html%.html}.pdf"
done < <(find people -type f \( -name "resume.html" -o -name "cover-letter.html" \) -print0 | sort -z)

echo "All PDFs generated via Docker."
