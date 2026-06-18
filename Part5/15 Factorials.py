# Write your solution here
def factorials(n: int):
    new_dictionary_local = {}
    for i in range(1,n+1):
        total = 1
        for j in range(1,i+1):
            total *= j
        new_dictionary_local[i] = total
    
    return new_dictionary_local
        

if __name__ == "__main__":
    k = factorials(5)
    print(k)
    print(k[1])
    print(k[3])
    print(k[5])
