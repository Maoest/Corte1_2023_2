# def conteo(num):
#     a=0
#     for i in range(num+1):    # de modo normal
#         a+=i
#         print(i)
    
def conteo(num):
    if num>0:
        num-=1
        conteo(num)     # rescursiva
    else:
        print(num)
    print(num+1)

if __name__=="__main__":
    n=int(input('Hasta que numero desea contar: '))
    conteo(n)