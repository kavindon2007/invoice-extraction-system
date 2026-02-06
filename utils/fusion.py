def fuse_yolo_ocr(yolo_out, ocr_out):
    return {
        "detections": yolo_out,
        "ocr": ocr_out
    }
