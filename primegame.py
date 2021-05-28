#This is primegame. this application gives the max difference between 2 primenumbers in a given range of numbers
def prime(n):
    if n<=1:
    	return False
    
    for i in range(2,n):
    	if n%i==0:
    		return False
    return True
k=int(input("no.of iterations"))
while k>0:
	l,m = [int(x) for x in input("enter numbers: ").split(" ")]
	fp=0
	lp=0
	for i in range(l,m+1):
		if prime(i):
			fp=i
			break
	for i in range(m,l-1,-1):
		if prime(i):
			lp=i
			break
			
	
	if fp!=lp:
		print(lp-fp)
	elif fp==lp and fp!=0:
		print(0)
	elif fp==0:
		print(-1)
    
	k-=1
    
    
    
    


