inp_str = input("Enter string: ")

fin_str = ""
for ch in inp_str:
	if ch >= 'A' and ch <= 'Z':
		fin_str += chr(ord(ch) + 13) if ch <= 'M' else chr(ord(ch) - 13)
	elif ch >= 'a' and ch <= 'z':
		fin_str += chr(ord(ch) + 13) if ch <= 'm' else chr(ord(ch) - 13)
	else:
		fin_str += ch
print(fin_str)
