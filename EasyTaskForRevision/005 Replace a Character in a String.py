# -----------
# Replace a Character in a String
# -----------

s = "Illusion"
new_s = ""

char = "l"
new_char = "r"

for char in s:
	if char == new_char:
		new_s += new_char
	else:
		new_s += char

print(new_s)

### Option (2)

# print(s.replace(curr_char, new_char))
