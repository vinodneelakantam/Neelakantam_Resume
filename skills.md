# Resume Prep Setup

## Goal

This workspace is set up to maintain a resume and a cover letter as styled HTML files, then export each one to PDF using a local browser in headless mode.

## What This Project Contains

```text
Resume_prep/
|- html_to_pdf.py
|- assets/
|  \- photo.jpeg
|- resume/
|  |- CV_Neelakantam_Embedded_Build_Devops.html
|  \- CV_Neelakantam_Embedded_Build_Devops.pdf
\- cover_letter/
   |- CL_Neelakantam_Embedded_Devops.html
   \- CL_Neelakantam_Embedded_Devops.pdf
```

## How It Works

1. The resume and cover letter are authored directly as standalone HTML files.
2. Styling is embedded inside each HTML file, so no external CSS build step is required.
3. Shared static content, such as the profile image, lives in `assets/`.
4. `html_to_pdf.py` opens the HTML file in headless Microsoft Edge or Google Chrome.
5. The browser prints the page to a PDF file.

## Resume Page Layout

The current guide did not originally explain page 1 and page 2 layout rules. The resume HTML is intentionally structured so the print version is split into a first page and continuation pages.

### Screen Layout

On screen, the resume uses one `container` with:

- a left sidebar for profile image, links, and skills
- a main content column for contact, personal information, summary, competencies, certifications, role focus, and work experience

### Print Layout for the Resume

When printed to PDF, the HTML creates a print-only structure inside `#printDocument`.

### Page 1 should contain

- the sidebar content on the left
- the header with name and title
- contact section
- personal information section
- about me section
- core competencies section
- certifications section
- current role focus section

This first page is built as a two-column layout using:

- `print-page-one`
- `print-sidebar`
- `print-main`

### Page 2 should contain

- the `Work Experience` heading
- all job entries after that heading

The second page starts because the print CSS forces `print-rest` onto a new page using:

- `break-before: page`
- `page-break-before: always`

### How the page split is decided

The JavaScript in the resume file looks through the main content and finds the `h2` heading named `Work Experience`.

Everything before `Work Experience` is cloned into page 1.

Everything from `Work Experience` onward is cloned into page 2 and later pages.

That means the intended layout is:

- Page 1: profile, summary, competencies, and short supporting sections
- Page 2+: experience-heavy continuation

### Important rule when editing the resume

If you want the page split to stay stable, keep the `Work Experience` section heading as an `h2` with the exact text `Work Experience`.

If you rename that heading, the print split logic may no longer place experience on page 2.

### Cover Letter Layout

The cover letter does not currently define a separate page 1 and page 2 split.

Its layout is:

- left sidebar with contact, personal information, links, and value proposition
- right main column with name, title, date, subject, letter body, and signature

For print, the cover letter uses A4 sizing and tighter spacing, but it remains a single continuous container instead of generating a dedicated page-2 section.

## Prerequisites

You need the following installed on Windows:

- Python 3
- Microsoft Edge or Google Chrome

The script checks these browser locations automatically:

- `C:\Program Files\Microsoft\Edge\Application\msedge.exe`
- `C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe`
- `C:\Program Files\Google\Chrome\Application\chrome.exe`
- `C:\Program Files (x86)\Google\Chrome\Application\chrome.exe`

You can also override browser detection with:

- `EDGE_PATH`
- `CHROME_PATH`
- `--browser <path-to-exe>`

## Main Script

The conversion entry point is `html_to_pdf.py`.

Supported options:

- `--input` or `-i`: required, accepts an HTML file path or URL
- `--output` or `-o`: optional, sets the output PDF path
- `--browser` or `-b`: optional, points to a specific Edge or Chrome executable

If `--output` is omitted:

- local HTML files are exported next to the source file with the same base name and a `.pdf` extension
- URLs are exported to `output.pdf` in the current working directory

## Typical Workflow

### 1. Edit the source files

Update the content in:

- `resume/CV_Neelakantam_Embedded_Build_Devops.html`
- `cover_letter/CL_Neelakantam_Embedded_Devops.html`

If the image is referenced in either HTML file, keep `assets/photo.jpeg` in place.

### 2. Generate the resume PDF

Run from the workspace root:

```powershell
python .\html_to_pdf.py --input .\resume\CV_Neelakantam_Embedded_Build_Devops.html
```

This produces:

```text
resume/CV_Neelakantam_Embedded_Build_Devops.pdf
```

### 3. Generate the cover letter PDF

```powershell
python .\html_to_pdf.py --input .\cover_letter\CL_Neelakantam_Embedded_Devops.html
```

This produces:

```text
cover_letter/CL_Neelakantam_Embedded_Devops.pdf
```

### 4. Generate to a custom output file

```powershell
python .\html_to_pdf.py --input .\resume\CV_Neelakantam_Embedded_Build_Devops.html --output .\resume\CV_custom.pdf
```

### 5. Use a specific browser executable

```powershell
python .\html_to_pdf.py --input .\resume\CV_Neelakantam_Embedded_Build_Devops.html --browser "C:\Program Files\Microsoft\Edge\Application\msedge.exe"
```

## Useful Notes

- The converter accepts either a local HTML file or a URL.
- Local file paths are converted to `file:///` URIs before printing.
- The script creates the output folder automatically if it does not already exist.
- If the browser fails to print or the PDF is empty, the script returns an error.

## Troubleshooting

### Browser not found

If the script reports that no supported browser was found:

- install Microsoft Edge or Google Chrome
- set `EDGE_PATH` or `CHROME_PATH`
- pass `--browser` explicitly

### HTML input file not found

Check that:

- you are running the command from the workspace root, or
- the path passed to `--input` is correct

### PDF was not created

Check that:

- the HTML file renders correctly in a normal browser window
- image references and local asset paths are valid
- the browser path is correct if `--browser` is used

## Purpose of This Setup

This setup is intended to keep application documents editable in HTML, visually controlled with inline CSS, and easy to export into recruiter-friendly PDF files without requiring Word, Google Docs, or a separate design toolchain.