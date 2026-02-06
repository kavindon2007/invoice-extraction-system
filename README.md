# Document AI – Invoice Extraction System

## Overview

This project implements a lightweight Document AI system to extract structured information from invoice and quotation documents.  
It combines OCR-based text understanding with Computer Vision–based signature and stamp detection into a single pipeline.

The system is designed to be accurate, fast, cost-efficient, and easy to run on standard CPU environments.

---

## Extracted Fields

The following fields are extracted from each document:

- Dealer Name  
- Model Name  
- Horse Power (HP)  
- Asset Cost  
- Dealer Signature (presence + bounding box)  
- Dealer Stamp (presence + bounding box)

---

## Architecture (High Level)

1. Document ingestion (image or PDF)
2. OCR ensemble (EasyOCR + Tesseract)
3. Regex and fuzzy-based field extraction
4. YOLO-based signature and stamp detection
5. Fusion, confidence scoring, and post-processing
6. Structured JSON output generation

---

## Requirements

Install dependencies using:

```bash
pip install -r requirements.txt

How to Run

Run on a single image
python executable.py path/to/image.png

Example:
python executable.py ../data/train/sample.png
Run on multiple images (folder)
python executable.py path/to/folder/

Example:
python executable.py ../data/train/
Run on a PDF (optional)
python executable.py invoice.pdf
Multi-page PDFs are processed page by page.

Output
All results are written to:
sample_output/result.json
Each document entry includes:
doc_id
Extracted fields
Signature and stamp details
Confidence score
Processing time (seconds)
Cost estimate (USD)
Performance
Average latency: ~6–9 seconds per document (CPU)
Cost per document: ~$0.002
Designed for high document-level accuracy


---

