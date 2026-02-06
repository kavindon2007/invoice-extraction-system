import cv2
import os
import time
from utils.ocr import run_ocr_pipeline
from utils.field_extractor import extract_fields
from utils.detector import detect_signature_stamp

def run_pipeline(image_path):
    start_time = time.time()

    image = cv2.imread(image_path)
    if image is None:
        raise ValueError(f"Cannot read image: {image_path}")

    # OCR
    texts, ocr_conf = run_ocr_pipeline(image)

    # Field extraction
    fields = extract_fields(texts)

    # Signature / stamp detection
    visual = detect_signature_stamp(image_path)

    processing_time = round(time.time() - start_time, 2)

    return {
        "doc_id": os.path.basename(image_path),
        "fields": {
            "dealer_name": fields.get("dealer_name"),
            "model_name": fields.get("model_name"),
            "horse_power": fields.get("horse_power"),
            "asset_cost": fields.get("asset_cost"),
            "signature": visual.get("signature"),
            "stamp": visual.get("stamp")
        },
        "confidence": round(ocr_conf, 2),
        "processing_time_sec": processing_time,
        "cost_estimate_usd": 0.002
    }
