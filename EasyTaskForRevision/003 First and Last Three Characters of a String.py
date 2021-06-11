# -----------
# First and Last Three Characters of a String
# -----------

s = "Miracle"

if len(s)<6:
	print("")
else:
	new_string = s[:3] +s[len(s)-3:]
	print(new_string)