
#!/usr/bin/env python3


def stringtoUni(input):
	#each character of input is converted into unicode format
	unicode = [ord(char) for char in input]

	return unicode

#string to be used as input
input = "label"

print("input word: ", input)

uni_characters = stringtoUni(input)

print("input unicode: ",uni_characters)


string = uni_characters


binary = [bin(num)[2:].zfill(8) for num in string]

print("input binary: ", binary)


XORnum = 13

print("XOR num: ", XORnum)

binary2 = [bin(XORnum)[2:].zfill(8)]

print("XOR binary: ", binary2)

binary2 = binary2 * len(binary)


XORedList = []


for i in range(len(binary)):


	XORed = ''.join(str(int(bit1) ^ int(bit2)) for bit1, bit2 in zip(binary[i], binary2[i]))

	XORedList.append(XORed)


print("XORed result: ", XORedList)


decimals = [int(binary, 2) for binary in XORedList]


print("Decimals: ", decimals)


text = [chr(decimal) for decimal in decimals]

resultText = ''.join(text)

print("Final result: ", resultText)

