sentence = "This is a common inteview question"
charFrequency = {}
for char in sentence:
    if char in charFrequency:
        charFrequency[char] += 1
    else:
        charFrequency[char] = 1

charFrequencySorted = sorted(
    charFrequency.items(),
    key=lambda kv:kv[1],
    reverse=True)

print(charFrequencySorted[0])