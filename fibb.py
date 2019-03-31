def fibb(n):
    if n == 0:
       return 0
    elif n == 1:
        return 1
    else:
        res = fibb(n-1) + fibb(n-2)
    return res

if __name__ == '__main__':
   res = fibb(50)
   print(res)
