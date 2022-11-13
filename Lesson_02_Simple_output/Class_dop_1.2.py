name1_n = "Анна"
name2_n = "Пётр"
name3_n = "Олег"

name1_s = "Иванова"
name2_s = "Сидоров" 
name3_s = "Белов"

conv_name1 = ""
conv_name2 = ""
conv_name3 = ""

for symb in name1_n:
	conv_name1 += chr(ord(symb) + 1)

for symb in name2_n:
        conv_name2 += chr(ord(symb) + 1)

for symb in name3_n:
        conv_name3 += chr(ord(symb) + 1)

conv_name1 += " "
conv_name2 += " "
conv_name3 += " "

for symb in name1_s:
        conv_name1 += chr(ord(symb) + 1)

for symb in name2_s:
        conv_name2 += chr(ord(symb) + 1)

for symb in name3_s:
        conv_name3 += chr(ord(symb) + 1)

print(conv_name1, conv_name2, conv_name3, sep='\n')

