import re

sequence = input()
pattern_threshold = r"\d"
pattern_emojies = r"(:{2}|\*{2})(?P<emoji>[A-Z][a-z]{2,})\1"

matches_threshold = re.findall(pattern_threshold, sequence)
matches_emojies = re.finditer(pattern_emojies, sequence)

cool_thresholds = [int(obj) for obj in matches_threshold]
threshold_sum = 1
valid_emojies = []
cool_emojies = []

for threshold in cool_thresholds:
    threshold_sum *= threshold

for match in matches_emojies:
    current_emoji_threshold = 0
    current_emoji = match.group()
    valid_emojies.append(current_emoji)
    for char in current_emoji[2:-2]:
        current_emoji_threshold += ord(char)
    if current_emoji_threshold >= threshold_sum:
        cool_emojies.append(current_emoji)

print(f"Cool threshold: {threshold_sum}")
print(f"{len(valid_emojies)} emojis found in the text. The cool ones are:")
for emoji in cool_emojies:
    print(emoji)
