import os
import json
import time
from utils.pipeline import run_pipeline


def run_batch(image_dir, limit=50, output_file="batch_results.json"):
    images = [
        f for f in sorted(os.listdir(image_dir))
        if f.lower().endswith(".png")
    ][:limit]

    results = []
    total_time = 0.0

    for idx, img in enumerate(images, start=1):
        img_path = os.path.join(image_dir, img)
        print(f"[{idx}/{len(images)}] Processing {img_path}")

        start = time.time()
        output = run_pipeline(img_path)
        elapsed = round(time.time() - start, 2)

        # ⬇️ ADDITIONS START HERE
        output["processing_time_sec"] = elapsed
        # ⬆️ ADDITIONS END HERE

        results.append(output)
        total_time += elapsed

    with open(output_file, "w") as f:
        json.dump(results, f, indent=2)

    return {
        "images_processed": len(results),
        "avg_time_per_image": round(total_time / len(results), 2),
        "total_time_sec": round(total_time, 2)
    }
