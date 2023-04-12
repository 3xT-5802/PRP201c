# Function is to check whether two strings are anagram of each other or not.
def isAnagram(a, b):
    if sorted(a) == sorted(b):
        return True
    else:
        return False


# {
#  Driver Code Starts

anal1_str1, anal1_str2 = 'heart', 'earth'
anal2_str1, anal2_str2 = 'python', 'typhon'
anal3_str1, anal3_str2 = 'Foot', 'tooth'
print("Anagram ('", anal1_str1,"', '", anal1_str2, "')  -> ", isAnagram(anal1_str1, anal1_str2))
print("Anagram ('", anal2_str1,"', '", anal2_str2, "')  -> ", isAnagram(anal2_str1, anal2_str2))
print("Anagram ('", anal3_str1,"', '", anal3_str2, "')  -> ", isAnagram(anal3_str1, anal3_str2))

# } Driver Code Ends