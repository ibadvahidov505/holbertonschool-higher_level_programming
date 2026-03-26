#!/usr/bin/python3
def uppercase(str):
	nstr=""
	for i in str:
		k=ord(i)
		if  k >= 97  and k < 123:
			k = k - 32
			nstr=nstr+chr(k)
		else:
			nstr = nstr + i 
	print(nstr)
