bin_str = input("Enter binary string: ")

bin_lst = bin_str.split()

fin_str = ""
for b in bin_lst:
	bin_int = int(b, 2)
	fin_str += chr(bin_int)
print(fin_str)
