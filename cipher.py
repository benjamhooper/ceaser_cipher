def encrypt(msg,offset):
	eMsg = ""
	for letter in msg:
		ci = plain.find(letter)
		ci = (offset + ci) % len(plain)
		eMsg = eMsg + plain[ci]
	return eMsg

def decrypt(msg,offset):
	dMsg = ""
	for letter in msg:
		ci = plain.find(letter)
		ci = (ci - offset) % len(plain)
		dMsg = dMsg + plain[ci]
	return dMsg

plain = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ 1234567890,'"
offset = 3
msg = "Hello Washburn, It's 2018"
print("Inital Msg ====> ", msg)
enMsg = encrypt(msg,3)
print("Encrpyt Msg ==> ", enMsg)
deMsg = decrypt(enMsg,3)
print("Decrypted Msg ==> ", deMsg)


while True:
	msg = input("Enter a message or Q to quit: ")
	if msg.strip() == 'Q':
		break
	enMsg = encrypt(msg,offset)
	print(" Initial Msg ====> ", msg)
	enMsg = encrypt(msg,3)
	print("Encrypted Msg ==> ", enMsg)
	deMsg = decrypt(enMsg,3)
	print("Decryped Msg ==> ", deMsg)

