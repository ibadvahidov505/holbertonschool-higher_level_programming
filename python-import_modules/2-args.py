import sys
uzun=len(sys.argv)-1
if uzun==0 :
	print('0 arguments.')
elif uzun==1:
	print(f"{uzun} argument:")
else :
	print(f"{uzun} arguments:")
	for i in range (1,uzun+1):
		print (f"{i}: {sys.argv[i]}",'\n')
