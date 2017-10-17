#! /usr/bin/env python3
import sys
import code
LIMIT = 1000

class Factor_Sieve:


    def __init__(self, limit=100):
        self.extend(limit)
                

                

    def get(self, n= None):
        if n is None:
            return self.sieve;
        else:
            if n >= len(self.sieve):
                self.extend(n+1)
                
            return [x for x in self.sieve[n] if x!= n]
            

    def extend(self, limit):
        self.sieve = [[] for x in range(limit)]
        for x in range(1,len(self.sieve)):
            y = x            
            while y < len(self.sieve):
                self.sieve[y].append(x)
                y+=x
                
    def limit(self):
        return len(self.sieve)
        
def is_amicable(a, f):
    """Tests if number is amicable """
    b = sum(f.get(a))
    if b == a:
        return False
    if b >= f.limit():
        f.extend(b+1)
    return a == sum(f.get(b))
    

        
if __name__ == '__main__':
    maximum = int(sys.argv[1])
    f = Factor_Sieve(maximum)    
    amicable = []
    for a in range(1,maximum):
        factors = f.get(a)
        if is_amicable(a,f):
            print(a,sum(factors), factors)
            amicable.append(a)
    print(amicable)
    print(sum(amicable))

