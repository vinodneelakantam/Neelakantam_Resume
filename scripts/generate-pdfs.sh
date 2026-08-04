#!/usr/bin/env bash
# Builds the resume-pdf-tool Docker image and regenerates all resume/cover-letter PDFs with it.
set -euo pipefail

cd "$(dirname "$0")/.."

IMAGE="resume-pdf-tool:latest"

docker build -t "$IMAGE" .

run() {
    docker run --rm -v "$(pwd):/workspace" -w /workspace "$IMAGE" --input "$1" --output "$2"
}

run resume/2-page/CV_Neelakantam_Embedded_Build_Devops.html resume/2-page/CV_Neelakantam_Embedded_Build_Devops.pdf
run resume/3-page/CV_Neelakantam_Embedded_Build_Devops_3Page.html resume/3-page/CV_Neelakantam_Embedded_Build_Devops_3Page.pdf
run cover_letter/Cover_Letter_Vinod_Neelakantam.html cover_letter/Cover_Letter_Vinod_Neelakantam.pdf

echo "All PDFs generated via Docker."
