from ultralytics import YOLO

MODEL_PATH = "models/best.pt"  # ensure model exists
model = YOLO(MODEL_PATH)

def detect_signature_stamp(image_path):
    result = model(image_path)[0]

    signature = {"present": False, "bbox": None}
    stamp = {"present": False, "bbox": None}

    for box in result.boxes:
        label = result.names[int(box.cls[0])]
        bbox = box.xyxy[0].tolist()

        if label == "signature":
            signature = {"present": True, "bbox": bbox}
        elif label == "stamp":
            stamp = {"present": True, "bbox": bbox}

    return {"signature": signature, "stamp": stamp}
