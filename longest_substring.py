def longest_substring(s):
    char_set = set()
    left = 0
    max_len = 0

    for right in range(len(s)):
        # If duplicate character found, shrink window
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1

        char_set.add(s[right])
        max_len = max(max_len, right - left + 1)

    return max_len


# --- User Input Section ---
string = input("Enter a string: ")

result = longest_substring(string)

print("Length of longest substring without repeating characters:", result)
