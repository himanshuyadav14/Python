def ambiguousCoordinates(s):
    def valid_parts(s):
        n = len(s)
        res = []
        # Without decimal point
        if s == '0' or (s[0] != '0'):  # no leading zeros except for single '0'
            res.append(s)
        # With decimal point
        for i in range(1, n):
            left, right = s[:i], s[i:]
            if (left == '0' or left[0] != '0') and right[-1] != '0':  # valid decimal point placement
                res.append(left + '.' + right)
        return res
    
    # Remove parentheses and extract the core part of the string
    s = s[1:-1]
    res = []
    
    # Split string into two parts and generate valid combinations
    for i in range(1, len(s)):
        left, right = s[:i], s[i:]
        left_parts = valid_parts(left)
        right_parts = valid_parts(right)
        
        for l in left_parts:
            for r in right_parts:
                res.append(f"({l}, {r})")
    
    return res

# Example Usage
s1 = "(123)"
print(ambiguousCoordinates(s1))  # Output: ["(1, 2.3)", "(1, 23)", "(1.2, 3)", "(12, 3)"]

s2 = "(0123)"
print(ambiguousCoordinates(s2))  # Output: ["(0, 1.23)", "(0, 12.3)", "(0, 123)", "(0.1, 2.3)", "(0.1, 23)", "(0.12, 3)"]

s3 = "(00011)"
print(ambiguousCoordinates(s3))  # Output: ["(0, 0.011)", "(0.001, 1)"]
