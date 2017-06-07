# -*- coding: utf-8 -*-
mycomma = ','
curly = '{'
reversecurly = '}'
towritefile = open("towritefile.txt","w")
with open("AktivasyonFormKaydet request.txt", "rb") as f:
	while True:
		c = f.read(1)
		if not c:
			print ("End of file")
			break
	if ord(c) == ord(curly) or ord(c) == ord(reversecurly):
		towritefile.write('\n')
		towritefile.write(c)
	if ord(c) == ord(mycomma):
		towritefile.write('\n')