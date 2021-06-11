#-------#
# Challenge Print the Character at a Specific Index
#-------#

s = 'Hello';
i = 3;

if len(s) == 0:
	print("Empty String")
elif i < len(s):
	print(s[i])
else:
	print("i out of range")
