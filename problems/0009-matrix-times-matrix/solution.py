def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
    
    if len(a[0])!= len(b):
        return -1
    else:
        ans=[]
        for i in range(len(a)):
            ans.append([])
            for j in range(len(b[0])):
                ans[i].append(0)
                for k in range(len(a[0])):
                    ans[i][j]+=a[i][k]*b[k][j]
        return ans
                    

	# return c