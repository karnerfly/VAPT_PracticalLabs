inp_str = input("Enter string: ")

fin_str = ""
for ch in inp_str:
	if ch != ' ':
		fin_str += chr(ord(ch) - 47)
	else:
		fin_str += ch
print(fin_str)
