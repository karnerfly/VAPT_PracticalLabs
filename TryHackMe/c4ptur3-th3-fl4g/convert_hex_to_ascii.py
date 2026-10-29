hex_str = input("Enter hex string: ")

hex_lst = hex_str.split()

fin_str = ""
for b in hex_lst:
        hex_int = int(b, 16)
        fin_str += chr(hex_int)
print(fin_str)
