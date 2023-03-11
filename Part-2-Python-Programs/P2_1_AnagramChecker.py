def is_anagram(str1, str2):
    # Remove any spaces from both strings and convert them to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    # Check if the lengths of the two strings are equal
    if len(str1) != len(str2):
        return False
    
    # Create dictionaries to store the frequency of each character in both strings
    freq1 = {}
    freq2 = {}
    
    # Count the frequency of each character in str1
    for char in str1:
        if char in freq1:
            freq1[char] += 1
        else:
            freq1[char] = 1
    
    # Count the frequency of each character in str2
    for char in str2:
        if char in freq2:
            freq2[char] += 1
        else:
            freq2[char] = 1
    
    # Check if the two dictionaries are equal
    if freq1 == freq2:
        return True
    else:
        return False

    
# Take input from the user
str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

# Call the function and print the result
if is_anagram(str1, str2):
    print("The two strings are anagrams of each other.")
else:
    print("The two strings are not anagrams of each other.")
