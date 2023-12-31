
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

#convert the unicode to binary representation
binary = [bin(num)[2:].zfill(8) for num in string]

print("input binary: ", binary)

#XOR key
XORnum = 13

print("XOR num: ", XORnum)
#Convert XOR key to binary representation
binary2 = [bin(XORnum)[2:].zfill(8)]

print("XOR binary: ", binary2)

binary2 = binary2 * len(binary)

#initialise list
XORedList = []

#Perform XOR operation on each bit of binary representation 
for i in range(len(binary)):


	XORed = ''.join(str(int(bit1) ^ int(bit2)) for bit1, bit2 in zip(binary[i], binary2[i]))

	XORedList.append(XORed)


print("XORed result: ", XORedList)

#Convert binary to decimals 
decimals = [int(binary, 2) for binary in XORedList]


print("Decimals: ", decimals)

#Convert decimals to characters
text = [chr(decimal) for decimal in decimals]

resultText = ''.join(text)

print("Final result: ", resultText)

