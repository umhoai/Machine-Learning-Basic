import re

text = "M 9 AM 7 PM TU 4 AM 9 PM"

hour_pair_pattern = re.compile(r"\b([1-9]|1[0-2])\s*[APap][mM]\s*([1-9]|1[0-2])\s*[APap][mM]\b")

masked_text = hour_pair_pattern.sub("[MASK]", text)

print(masked_text)
