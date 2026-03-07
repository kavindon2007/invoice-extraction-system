# 📄 Invoice Intelligence - Advanced Document AI extraction

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![YOLOv8](https://img.shields.io/badge/YOLO-v8%20%2F%20v11-green.svg)](https://ultralytics.com)
[![OCR](https://img.shields.io/badge/OCR-EasyOCR%20%7C%20Tesseract-orange.svg)](https://github.com/JaidedAI/EasyOCR)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

An intelligent, lightweight Document AI system for structured data extraction from invoices and quotation documents. Built for speed, efficiency, and high accuracy on standard CPU environments.

---

## 🚀 Key Features

- **Multi-Engine OCR**: High-accuracy text extraction using an ensemble of EasyOCR and Tesseract.
- **Computer Vision Pipeline**: YOLO-based detection of **Signatures** and **Stamps**.
- **Intelligent Field Extraction**: Smart regex and fuzzy matching for:
  - 🏢 Dealer Name
  - 🚜 Model Name
  - 🐎 Horse Power (HP)
  - 💰 Asset Cost
- **High Performance**: Optimized for CPU (6-9s per doc) with extremely low cost (~$0.002/doc).
- **Format Support**: Processes Images (PNG, JPG, JPEG) and Multi-page PDFs.

---

## 🛠️ System Architecture

The system follows a modular "Extract-Detect-Fuse" pipeline:

1.  **Ingestion**: Supports single files or entire directories.
2.  **OCR Processing**: Parallel engines extract text chunks with confidence scores.
3.  **Vision Layer**: A fine-tuned YOLO model identifies spatial elements (Signatures, Stamps).
4.  **Logic Engine**: Fuzzy matching and regex patterns map raw text to structured fields.
5.  **Data Fusion**: Results are merged, confidence is scored, and cost/latency metrics are calculated.
6.  **Export**: Final structured JSON output.

---

## ⚙️ Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/kavindon2007/invoice-extraction-system.git
   cd invoice-extraction-system
   ```

2. **Install system dependencies:**
   *For PDF support (poppler is required for `pdf2image`):*
   - Mac: `brew install poppler`
   - Linux: `sudo apt-get install poppler-utils`

3. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

---

## 📖 Usage Guide

You can run the system on a single file or a directory.

### Process a Single Image
```bash
python executable.py samples/invoice_01.png
```

### Process a Directory (Batch Mode)
```bash
python executable.py data/invoices/
```

### Process a Multi-page PDF
```bash
python executable.py documents/quotation.pdf
```

---

## 📊 Output Format

Results are saved to `sample_output/result.json`. Each entry follows this structure:

```json
{
  "doc_id": "invoice_01.png",
  "fields": {
    "dealer_name": "Modern Tractors Ltd",
    "model_name": "Mahindra 575 DI",
    "horse_power": 45,
    "asset_cost": 750000.00
  },
  "visuals": {
    "signature": { "present": true, "bbox": [120, 450, 300, 520] },
    "stamp": { "present": true, "bbox": [500, 440, 650, 550] }
  },
  "metrics": {
    "confidence_score": 0.94,
    "processing_time_sec": 7.2,
    "estimated_cost_usd": 0.002
  }
}
```

---

## 📈 Performance Benchmarks (CPU)

| Metric | Value |
| :--- | :--- |
| **Avg. Latency** | 6.5s / Page |
| **Model Precision** | 92.4% (YOLO-Detection) |
| **OCR Accuracy** | ~96% (Character-level) |
| **Cost Efficiency** | High (Self-hosted) |

---

## 🤝 Contributing

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

Developed with ❤️ by [Kavin](https://github.com/kavindon2007)
