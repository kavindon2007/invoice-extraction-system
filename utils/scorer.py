def score(texts):
    if not texts:
        return 0.0
    clean = [t for t in texts if len(t.strip()) >= 3]
    if not clean:
        return 0.1
    avg_len = sum(len(t) for t in clean) / len(clean)
    return min(avg_len / 20.0, 1.0)
