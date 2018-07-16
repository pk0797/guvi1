    import os
    p = int(input())
    k=list()
    for i in range(0, p):
        k.append(input())
     
    print(os.path.commonprefix(k))
