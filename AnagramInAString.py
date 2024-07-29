from collections import Counter
def findAnagrams(s: str, p: str):
    p_counter=Counter(p)
    s_counter =Counter(s[:len(p)])
    a=[]
    if p_counter == s_counter:
        a.append(0)
    for i in range(len(p),len(s)):
        s_counter[s[i]] += 1
        s_counter[s[i - len(p)]] -= 1
        if s_counter == p_counter:
            a.append(i - len(p) + 1)
    return a


s= input("Enter the string :")
p= input("Enter the pattern :")
print("All Anagrams at :",findAnagrams(s,p))