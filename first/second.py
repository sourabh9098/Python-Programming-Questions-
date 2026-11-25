a = [ 54 , 54 , -float('inf') , 20 ,10 , 543,121]

def second_large(n):

    if len(n)> 1 :
        largest = n[0]
        sec = None

        for ele in n:
            if ele > largest:
                sec = largest
                largest = ele

            elif sec!=None and largest > ele> sec:
                sec = ele
            elif sec == None and ele < largest:
                sec = ele

        return sec
    return "Collection Not Valid"

print(second_large(a))