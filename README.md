# Vinod Kumar Neelakantam - Resume Portfolio

This repository contains the resume and cover letter for Vinod Kumar Neelakantam, focused on embedded platform integration, automotive software delivery, CI/CD release engineering, and automotive cybersecurity.

## Profile Summary

Vinod Kumar Neelakantam is an Embedded Platform Integration Engineer based in Neu Ulm, Germany, with 12+ years of experience across automotive ECU and ADAS software programs. His work combines embedded software integration, build and release automation, ASPICE-aligned delivery practices, and cybersecurity-aware release governance.

He has led platform integration and multi-variant release workflows for automotive software products, with hands-on experience across C/C++ builds, Jenkins and CloudBees pipelines, Docker, Kubernetes, Artifactory, Python automation, and secure OTA/SOTA packaging.

## Core Focus Areas

| Area | Profile Strength |
| --- | --- |
| Embedded Platform Integration | ADAS and ECU software integration, multi-variant builds, dependency governance, board/platform delivery support |
| CI/CD and Release Engineering | Jenkins, CloudBees, CMake, Artifactory, Docker, Kubernetes, automated release workflows, quality gates |
| Automotive Cybersecurity | TARA support, ISO/SAE 21434 alignment, CSMS evidence readiness, SUMS evidence readiness, secure release controls |
| Build and Dependency Management | C/C++, Python, Groovy, Shell, Yocto, Zephyr, AOSP, artifact traceability, CVE triage |
| Process and Compliance | ASPICE SWE.5 integration practices, audit-ready documentation, validation strategy, release lifecycle ownership |

## Technical Profile

| Category | Tools and Methods |
| --- | --- |
| Programming and Automation | C, C++, Python, Groovy, Shell |
| Embedded Build Systems | CMake, Yocto, Zephyr, AOSP, custom automotive build environments |
| DevOps and CI/CD | Jenkins, CloudBees, Docker, Kubernetes, Artifactory, GitHub |
| Quality and Security | SAST, SCA, SBOM, SPDX, CycloneDX, package signing, integrity checks |
| Automotive Standards | ASPICE SWE.5, ISO/SAE 21434, UNECE R155, UNECE R156 |
| Interfaces and Debugging | CAN, Ethernet, UART, I2C, SPI, HIL/SIL validation, SW/HW debugging |

## Career Highlights

- Led ADAS platform integration and multi-variant C/C++ builds for Continental/AUMOVIO automotive platforms.
- Built and maintained CI/CD pipelines using Jenkins, CloudBees, Docker, Kubernetes, Artifactory, and Python automation.
- Supported secure OTA/SOTA delivery with package signing, partial update strategy, integrity checks, and release traceability.
- Contributed to TARA work products and ISO/SAE 21434-aligned cybersecurity release evidence.
- Implemented ASPICE SWE.5-aligned integration and release processes for automotive software programs.
- Delivered software integration across ADAS, surround-view systems, camera mirror replacement, radar, and engine management domains.

## Repository Contents

```text
.
|- assets/
|  `- photo.jpeg
|- cover_letter/
|  |- Cover_Letter_Vinod_Neelakantam.html
|  `- Cover_Letter_Vinod_Neelakantam.pdf
|- resume/
|  |- 2-page/
|  |  |- CV_Neelakantam_Embedded_Build_Devops.html
|  |  |- CV_Neelakantam_Embedded_Build_Devops.pdf
|  |  `- resume-data.js
|  `- V2/
|     |- CV_Neelakantam_Embedded_Build_Devops_V2.html
|     |- CV_Neelakantam_Embedded_Build_Devops_V2.pdf
|     `- resume-data-v2.js
|- scripts/
|  `- generate-pdfs.sh
|- html_to_pdf.py
|- Dockerfile
|- .dockerignore
|- skills.md
`- README.md
```

## Documents

| Document | Format | Purpose |
| --- | --- | --- |
| Resume (2-page) | HTML and PDF | Compact, dense-layout professional profile and work experience |
| Resume (V2) | HTML and PDF | Alternate 2-page layout with expanded profile content (About Me, Core Competencies, Current Role Focus) and more detailed work history |
| Cover Letter | HTML and PDF | Application-ready cover letter for embedded platform integration and release engineering roles |
| Resume Data (2-page) | JavaScript | Structured content used by the 2-page resume HTML ([resume-data.js](resume/2-page/resume-data.js)) |
| Resume Data (V2) | JavaScript | Structured, more detailed content used by the V2 resume HTML ([resume-data-v2.js](resume/V2/resume-data-v2.js)) |
| Conversion Script | Python | Converts local HTML documents into recruiter-friendly PDF files |

The two resume versions have independent data files, since V2 carries more detailed work history (e.g. separate AUMOVIO role entries, project/tooling specifics) than the condensed 2-page version. Update the matching data file for whichever version you're editing.

## Generate PDFs

The project includes a small Python utility that uses a local Chromium-based browser, such as Microsoft Edge or Google Chrome, to print the HTML documents to PDF.

Generate the resume (2-page):

```powershell
python .\html_to_pdf.py --input .\resume\2-page\CV_Neelakantam_Embedded_Build_Devops.html --output .\resume\2-page\CV_Neelakantam_Embedded_Build_Devops.pdf
```

Generate the resume (V2):

```powershell
python .\html_to_pdf.py --input .\resume\V2\CV_Neelakantam_Embedded_Build_Devops_V2.html --output .\resume\V2\CV_Neelakantam_Embedded_Build_Devops_V2.pdf
```

Or use the VS Code **Run and Debug** panel with the "HTML to PDF (Resume 2-Page)" / "HTML to PDF (Resume V2)" launch configurations ([.vscode/launch.json](.vscode/launch.json)).

Generate the cover letter:

```powershell
python .\html_to_pdf.py --input .\cover_letter\Cover_Letter_Vinod_Neelakantam.html --output .\cover_letter\Cover_Letter_Vinod_Neelakantam.pdf
```

## Generate PDFs with Docker

A [Dockerfile](Dockerfile) is included so PDF generation doesn't depend on a locally installed Edge/Chrome browser. The image bundles Python and headless Chromium.

Build the image once:

```bash
docker build -t resume-pdf-tool:latest .
```

Run it against any HTML file in this repo by mounting the repository into the container (paths are relative to `/workspace`, which is the repo root):

```bash
docker run --rm -v "$(pwd):/workspace" -w /workspace resume-pdf-tool:latest \
  --input resume/2-page/CV_Neelakantam_Embedded_Build_Devops.html \
  --output resume/2-page/CV_Neelakantam_Embedded_Build_Devops.pdf
```

Or regenerate every PDF (both resumes and the cover letter) in one step with the helper script, which also builds the image:

```bash
./scripts/generate-pdfs.sh
```

These are also available as VS Code tasks (**Terminal > Run Task...**): "Docker: Build PDF Tool Image", "Docker: Generate All PDFs", "Docker: Generate Resume (2-Page)", "Docker: Generate Resume (V2)", and "Docker: Generate Cover Letter" ([.vscode/tasks.json](.vscode/tasks.json)).

## Links

| Platform | Link |
| --- | --- |
| LinkedIn | [linkedin.com/in/vinodneelakantam](https://www.linkedin.com/in/vinodneelakantam) |
| GitHub | [github.com/vinodneelakantam](https://github.com/vinodneelakantam) |

## Professional Positioning

This profile is best aligned with roles such as:

- Embedded Platform Integration Engineer
- Automotive Software Integration Engineer
- CI/CD and Release Integration Engineer
- Embedded DevOps Engineer
- Automotive Cybersecurity Integration Engineer
- Build and Release Engineer for ADAS or ECU platforms

The overall profile emphasizes practical ownership of embedded software delivery: integrating complex automotive platforms, keeping release pipelines reliable, maintaining traceability, and supporting cybersecurity and process compliance expectations in production-oriented engineering environments.
