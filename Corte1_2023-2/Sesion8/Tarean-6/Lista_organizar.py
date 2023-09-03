import random as r

def org_min_may():
    L=[]
    while len(L)!=15:
        L.append(r.randint(1,100))
    L.sort(reverse=True)
    print(L)

def main():
    org_min_may()

if __name__ == "__main__":
    main()