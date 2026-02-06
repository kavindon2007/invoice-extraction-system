import re
from utils.fuzzy_matcher import fuzzy_match


# -------------------------------
# Domain Dictionaries
# -------------------------------

KNOWN_DEALERS = [
    "MAHINDRA TRACTORS",
    "MASSEY FERGUSON TRACTORS",
    "EICHER TRACTORS",
    "SWARAJ TRACTORS",
    "SONALIKA TRACTORS",
    "ESCORTS TRACTORS"
]

KNOWN_MODELS = [
    "275 DI",
    "575 DI",
    "735 FE",
    "742 XT",
    "744 FE",
    "855 FE",
    "843 XM",
    "241 DI",
    "245 DI",
    "9500",
    "DI 42",
    "DI 45"
]


# -------------------------------
# Normalization
# -------------------------------

def normalize(text):
    text = text.upper()
    text = text.replace(":", " ")
    text = text.replace("-", " ")
    text = text.replace("/", " ")
    text = text.replace(",", " ")
    return " ".join(text.split())


# -------------------------------
# Field Extraction
# -------------------------------

def extract_fields(texts):
    joined = normalize(" ".join(texts))

    fields = {
        "dealer_name": None,
        "model_name": None,
        "horse_power": None,
        "asset_cost": None
    }

    # ---------- DEALER ----------
    dealer_patterns = [
        r"M/S\s+[A-Z ]{5,}",
        r"[A-Z ]{5,}\s+TRACTORS",
        r"[A-Z ]{5,}\s+AGENCIES",
        r"AUTHORIZED\s+DEALER\s+OF\s+[A-Z ]+"
    ]

    for p in dealer_patterns:
        m = re.search(p, joined)
        if m:
            fields["dealer_name"] = m.group().strip()
            break

    # Fuzzy fallback
    if not fields["dealer_name"]:
        fields["dealer_name"] = fuzzy_match(joined, KNOWN_DEALERS, 0.85)


    # ---------- MODEL ----------
    model_patterns = [
        r"\b\d{3}\s*(DI|XP|FE|XT|XM)\b",
        r"\bDI\s*\d{2}\b"
    ]

    for p in model_patterns:
        m = re.search(p, joined)
        if m:
            fields["model_name"] = m.group().strip()
            break

    # Fuzzy fallback
    if not fields["model_name"]:
        fields["model_name"] = fuzzy_match(joined, KNOWN_MODELS, 0.80)


    # ---------- HORSE POWER ----------
    hp_patterns = [
        r"(\d{2,3})\s*H\.?P\.?",
        r"HORSE\s*POWER\s*(\d{2,3})",
        r"POWER\s*(\d{2,3})"
    ]

    for p in hp_patterns:
        m = re.search(p, joined)
        if m:
            fields["horse_power"] = int(m.group(1))
            break


    # ---------- ASSET COST ----------
    cost_patterns = [
        r"(₹|RS\.?)\s*([\d\s,]{5,})",
        r"TOTAL\s*(AMOUNT|COST)?\s*([\d\s,]{5,})"
    ]

    for p in cost_patterns:
        m = re.search(p, joined)
        if m:
            value = re.sub(r"\D", "", m.group())
            if value:
                fields["asset_cost"] = int(value)
                break

    return fields
