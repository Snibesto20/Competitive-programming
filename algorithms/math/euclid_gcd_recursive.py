# Time complexity: O(log min(a,b))

def gcd(a, b):
    if b == 0: return a
    return gcd(b, a % b)