if __name__ == '__main__':
    x = int(input('Enter the value:'))
    y = int(input('Enter the value:'))
    z = int(input('Enter the value:'))
    n = int(input('Enter the value:'))
    Result = (list([i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1)  if i+j+k !=n))
    print(Result)