# Headless-Chromium tool image for converting the resume/cover-letter HTML files to PDF.
FROM python:3.12-slim

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        chromium \
        fonts-liberation \
        fonts-noto-color-emoji \
        fonts-dejavu-core \
    && rm -rf /var/lib/apt/lists/*

ENV CHROME_PATH=/usr/bin/chromium

WORKDIR /workspace

COPY html_to_pdf.py /usr/local/bin/html_to_pdf.py
RUN chmod +x /usr/local/bin/html_to_pdf.py

ENTRYPOINT ["python3", "/usr/local/bin/html_to_pdf.py"]
