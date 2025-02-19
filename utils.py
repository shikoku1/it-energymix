def decimate_with(arr,n):
    result=[]
    for i in range(0,int(len(arr)/n)):
        lol=sum(arr[i*n:(i+1)*n])/n
        result+=[lol]
        
    return result

assert decimate_with([1,2,3,4,5,6,7,8,9,10],2)==[1.5,3.5,5.5,7.5,9.5]
assert decimate_with([1,2,3,4,5,6,7,8,9,10],3)==[2,5,8]
assert decimate_with([1,2,3,4,5,6,7,8,9,10],4)==[2.5,6.5]
