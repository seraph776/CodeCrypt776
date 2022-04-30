
def sumdigits_nonrecursive(n: int) -> int:
    """sumdigits_nonrecursive"""
    while True:
        n = sum([int(i) for i in str(n)])
        if len(str(n)) == 1:
            break
    return n
  
if __name__ == '__main__':  
    print(sumdigits_nonrecursive(123874)) # 7
    print(sumdigits_nonrecursive(14)) # 5





        
