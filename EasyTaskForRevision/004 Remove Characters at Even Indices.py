# -----------
# Remove Characters at Even Indices
# -----------

s = 'Brilliant'
new_s = ""

for i in range(len(s)):
	if i % 2 != 0:
		new_s += s[i]

print(new_s)