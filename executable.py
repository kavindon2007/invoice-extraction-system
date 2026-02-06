import sys
import os
import json
import time
from utils.pipeline import run_pipeline

try:
    from pdf2image import convert_from_path
    PDF_SUPPORTED = True
except:
    PDF_SUPPORTED = False


OUTPUT_DIR = "sample_output"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "result.json")


def process_image(image_path):
    start = time.time()
    result = run_pipeline(image_path)
    result["processing_time_sec"] = round(time.time() - start, 2)
    return result


def process_pdf(pdf_path):
    if not PDF_SUPPORTED:
        raise RuntimeError("PDF support not available. Install pdf2image.")

    pages = convert_from_path(pdf_path)
    results = []

    for idx, page in enumerate(pages, start=1):
        temp_img = f"_temp_page_{idx}.png"
        page.save(temp_img, "PNG")
        results.append(process_image(temp_img))
        os.remove(temp_img)

    return results


def main():
    if len(sys.argv) < 2:
        print("Usage: python executable.py <file_or_folder>")
        sys.exit(1)

    input_path = sys.argv[1]
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    all_results = []

    # -------- Folder input --------
    if os.path.isdir(input_path):
        files = sorted(os.listdir(input_path))
        for f in files:
            full_path = os.path.join(input_path, f)
            if f.lower().endswith((".png", ".jpg", ".jpeg")):
                all_results.append(process_image(full_path))
            elif f.lower().endswith(".pdf"):
                all_results.extend(process_pdf(full_path))

    # -------- Single file input --------
    else:
        if input_path.lower().endswith(".pdf"):
            all_results = process_pdf(input_path)
        else:
            all_results = [process_image(input_path)]

    with open(OUTPUT_FILE, "w") as f:
        json.dump(all_results, f, indent=2)

    print(f"✅ Processed {len(all_results)} document(s)")
    print(f"📄 Output written to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
