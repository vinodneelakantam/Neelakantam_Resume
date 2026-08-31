# Resume Generator with Python HTML

A portfolio-ready resume built as a data-driven HTML page, with a Python utility for PDF export.

## Overview

The resume is rendered in the browser from [`resume/V2/resume-data-v2.js`](resume/V2/resume-data-v2.js) by [`resume/V2/CV_Neelakantam_Embedded_Build_Devops_V2.html`](resume/V2/CV_Neelakantam_Embedded_Build_Devops_V2.html). The standard-library Python script [`html_to_pdf.py`](html_to_pdf.py) opens that HTML in headless Chrome or Edge and saves a PDF version.

![Python](https://img.shields.io/badge/Python-3-3776AB?logo=python&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=white)

## How it works

1. Resume content is stored in `resume-data-v2.js`.
2. The HTML template loads that data and renders the resume in a browser.
3. `html_to_pdf.py` accepts an HTML file (or URL) and uses a Chromium-based browser's headless print-to-PDF capability to create a PDF.

## Usage

Clone the repository, then open the resume locally with any static HTTP server:

```bash
python -m http.server 8000 --directory resume/V2
```

Visit [http://localhost:8000/CV_Neelakantam_Embedded_Build_Devops_V2.html](http://localhost:8000/CV_Neelakantam_Embedded_Build_Devops_V2.html).

To export the resume to PDF, install Google Chrome, Chromium, or Microsoft Edge, then run:

```bash
python html_to_pdf.py \
  --input resume/V2/CV_Neelakantam_Embedded_Build_Devops_V2.html \
  --output resume/V2/CV_Neelakantam_Embedded_Build_Devops_V2.pdf
```

The script uses only the Python standard library. Set `CHROME_PATH` or `EDGE_PATH`, or supply `--browser /path/to/browser`, when the browser is not in a default location.

## Live Demo

[View the resume on GitHub Pages](https://vinodneelakantam.github.io/Neelakantam_Resume/)

<!-- This link requires GitHub Pages to be enabled with the generated Pages artifact as its source. -->

## Contributing and license

Contributions are welcome. This repository does not currently declare a license.
