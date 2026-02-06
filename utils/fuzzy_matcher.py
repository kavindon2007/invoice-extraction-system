from difflib import SequenceMatcher

def fuzzy_match(text, candidates, threshold=0.85):
    best_match = None
    best_score = 0.0

    for candidate in candidates:
        score = SequenceMatcher(None, text, candidate).ratio()
        if score > best_score:
            best_score = score
            best_match = candidate

    if best_score >= threshold:
        return best_match
    return None
