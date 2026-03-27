import sys
nums=sys.argv
k=len(sys.argv)-1
s=0
for i in range (1,k+1):
	s=s+int(sys.argv[i])
print(s)
