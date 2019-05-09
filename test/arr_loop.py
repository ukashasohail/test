arr = [2,6,0,8,95,65,88,41]

def test(a,b):
    for i in range(0,len(arr)):
        if a == arr[i]:
            collection = str(a)
        
        if b == arr[i]:
            collection = collection+" "+str(b)
            collection = collection.split()
            if str(a) and str(b) in collection:
                print(a,b, "both found")
            elif str(b) in collection:
                print(b, "found")
            elif str(a) in collection:
                print(a," found")
            else:
                print("none found")
test(2,41)
