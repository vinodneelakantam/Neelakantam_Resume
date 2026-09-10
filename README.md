# Resume & Cover Letter Portfolio

This repository maintains resumes and cover letters for multiple people as styled HTML files, each exported to PDF using a local headless browser (or Docker). Content is organized per person under `people/<person>/` so each person's documents, data files, and supporting notes stay self-contained.

## Naming Convention

The layout is deliberately generic so adding a new person, resume variant, or cover letter doesn't require touching any script:

```text
people/<person>/
|- assets/              # optional: photo, person-specific images
|- inputs/              # optional: raw/source CVs used to build the resume
|- resume/
|  `- <variant>/        # e.g. "v2", "hil-test-engineer" - one folder per resume version/role focus
|     |- resume.html
|     |- resume.pdf
|     `- resume-data.js
|- cover-letter/
|  |- cover-letter.html
|  `- cover-letter.pdf
`- notes/               # optional: interview prep, gap analyses, other career notes
```

- `<person>` is a lowercase slug (`vinod`, `vamsi`, ...).
- `<variant>` is a lowercase-kebab-case slug describing the resume revision or role focus (`v2`, `hil-test-engineer`, ...). Every variant folder uses the same generic filenames (`resume.html` / `resume.pdf` / `resume-data.js`), so tooling can discover them with a simple glob instead of hardcoded names.
- `scripts/generate-pdfs.sh` walks `people/*/**/resume.html` and `people/*/**/cover-letter.html` automatically - no edits needed when a new person or variant is added.

All build/conversion tooling (Dockerfile, `.dockerignore`, the `html_to_pdf.py` script, and `scripts/generate-pdfs.sh`) lives under `infra/`, kept separate from the `people/` content.

## Repository Contents

```text
.
|- people/
|  |- vinod/
|  |  |- assets/
|  |  |  `- photo.jpeg
|  |  |- resume/
|  |  |  `- v2/
|  |  |     |- resume.html
|  |  |     |- resume.pdf
|  |  |     `- resume-data.js
|  |  |- cover-letter/
|  |  |  |- cover-letter.html
|  |  |  `- cover-letter.pdf
|  |  `- notes/
|  |     |- interview-qna/
|  |     |  `- 01..10-*.md
|  |     `- cybersecurity-devsecops-gap-analysis.md
|  `- vamsi/
|     |- inputs/
|     |  |- vamsi-kavety-cv-2020.pdf
|     |  `- vamsi-kavety-cv-latest.pdf
|     |- resume/
|     |  `- hil-test-engineer/
|     |     |- resume.html
|     |     |- resume.pdf
|     |     `- resume-data.js
|     |- cover-letter/
|     |  |- cover-letter.html
|     |  `- cover-letter.pdf
|     `- notes/
|        |- interview-qna/
|        |  `- 01..07-*.md
|        `- test-automation-gap-analysis.md
|- infra/
|  |- scripts/
|  |  `- generate-pdfs.sh
|  |- html_to_pdf.py
|  |- Dockerfile
|  `- .dockerignore
|- skills.md
`- README.md
```

## Vinod Kumar Neelakantam

Embedded Platform Integration Engineer based in Neu Ulm, Germany, with 12+ years of experience across automotive ECU and ADAS software programs: embedded software integration, build and release automation, ASPICE-aligned delivery practices, and cybersecurity-aware release governance.

| Area | Profile Strength |
| --- | --- |
| Embedded Platform Integration | ADAS and ECU software integration, multi-variant builds, dependency governance, board/platform delivery support |
| CI/CD and Release Engineering | Jenkins, CloudBees, CMake, Artifactory, Docker, Kubernetes, automated release workflows, quality gates |
| Automotive Cybersecurity | TARA support, ISO/SAE 21434 alignment, CSMS/SUMS evidence readiness, secure release controls |
| Build and Dependency Management | C/C++, Python, Groovy, Shell, Yocto, Zephyr, AOSP, artifact traceability, CVE triage |
| Process and Compliance | ASPICE SWE.5 integration practices, audit-ready documentation, validation strategy, release lifecycle ownership |

- Resume: [people/vinod/resume/v2](people/vinod/resume/v2) (HTML + PDF + [resume-data.js](people/vinod/resume/v2/resume-data.js))
- Cover letter: [people/vinod/cover-letter](people/vinod/cover-letter)
- Interview prep: [people/vinod/notes/interview-qna](people/vinod/notes/interview-qna)
- Gap analysis: [people/vinod/notes/cybersecurity-devsecops-gap-analysis.md](people/vinod/notes/cybersecurity-devsecops-gap-analysis.md)
- LinkedIn: [linkedin.com/in/vinodneelakantam](https://www.linkedin.com/in/vinodneelakantam) | GitHub: [github.com/vinodneelakantam](https://github.com/vinodneelakantam)

Target roles: Embedded Platform Integration Engineer, Automotive Software Integration Engineer, CI/CD and Release Integration Engineer, Embedded DevOps Engineer, Automotive Cybersecurity Integration Engineer.

## Vamsi Krishna Sai Kavety

HIL/SIL Test Engineer and automotive software integrator based in Regensburg, Germany, with 11+ years across HIL rig ownership (Vector VT System, RT Rack, Fault Insertion Unit), AUTOSAR-based Gateway/Telematics/Body ECU integration, and a growing DevOps/AI skill set (Docker, Kubernetes, Terraform, Ansible).

- Resume: [people/vamsi/resume/hil-test-engineer](people/vamsi/resume/hil-test-engineer) (HTML + PDF + [resume-data.js](people/vamsi/resume/hil-test-engineer/resume-data.js))
- Cover letter: [people/vamsi/cover-letter](people/vamsi/cover-letter)
- Interview prep: [people/vamsi/notes/interview-qna](people/vamsi/notes/interview-qna)
- Gap analysis: [people/vamsi/notes/test-automation-gap-analysis.md](people/vamsi/notes/test-automation-gap-analysis.md)
- Source CVs used as input: [people/vamsi/inputs](people/vamsi/inputs)

Target roles: HIL/SIL Test Engineer, Software Integration Engineer (AUTOSAR/Gateway/Telematics), DevOps-Aligned Test Automation Engineer.

## Generate PDFs

The project includes a small Python utility that uses a local Chromium-based browser, such as Microsoft Edge or Google Chrome, to print the HTML documents to PDF.

```bash
python3 infra/html_to_pdf.py --input people/vinod/resume/v2/resume.html --output people/vinod/resume/v2/resume.pdf
python3 infra/html_to_pdf.py --input people/vinod/cover-letter/cover-letter.html --output people/vinod/cover-letter/cover-letter.pdf
python3 infra/html_to_pdf.py --input people/vamsi/resume/hil-test-engineer/resume.html --output people/vamsi/resume/hil-test-engineer/resume.pdf
python3 infra/html_to_pdf.py --input people/vamsi/cover-letter/cover-letter.html --output people/vamsi/cover-letter/cover-letter.pdf
```

Or use the VS Code **Run and Debug** panel with the "HTML to PDF (Resume - Vinod v2)" / "HTML to PDF (Cover Letter - Vinod)" / "HTML to PDF (Resume - Vamsi hil-test-engineer)" / "HTML to PDF (Cover Letter - Vamsi)" launch configurations ([.vscode/launch.json](.vscode/launch.json)).

## Generate PDFs with Docker

A [Dockerfile](infra/Dockerfile) is included so PDF generation doesn't depend on a locally installed Edge/Chrome browser. The image bundles Python and headless Chromium.

Build the image once (build context is `infra/`):

```bash
docker build -t resume-pdf-tool:latest -f infra/Dockerfile infra
```

Run it against any HTML file in this repo by mounting the repository into the container (paths are relative to `/workspace`, which is the repo root):

```bash
docker run --rm -v "$(pwd):/workspace" -w /workspace resume-pdf-tool:latest \
  --input people/vinod/resume/v2/resume.html \
  --output people/vinod/resume/v2/resume.pdf
```

Or regenerate every PDF (all people, all variants) in one step with the helper script, which also builds the image and auto-discovers every `resume.html`/`cover-letter.html` under `people/`:

```bash
./infra/scripts/generate-pdfs.sh
```

These are also available as VS Code tasks (**Terminal > Run Task...**): "Docker: Build PDF Tool Image", "Docker: Generate All PDFs", "Docker: Generate Resume (Vinod v2)", "Docker: Generate Cover Letter (Vinod)", "Docker: Generate Resume (Vamsi hil-test-engineer)", and "Docker: Generate Cover Letter (Vamsi)" ([.vscode/tasks.json](.vscode/tasks.json)).
