import re

text = "I woke up at 6:30am and went to bed at 11:00pm. I had lunch at 1:00pm."

hour_pattern = re.compile(r"\b([1-9]|1[0-2]):[0-5][0-9]\s*[APap][mM]\b")

masked_text = hour_pattern.sub("[MASK]", text)

print(masked_text)
