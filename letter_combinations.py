def letter_combinations(digits):
    if digits == "":
        return []

    mapping = {
        "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
        "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
    }

    res = []

    def backtrack(i, path):
        if i == len(digits):
            res.append(path)
            return

        for ch in mapping[digits[i]]:
            backtrack(i + 1, path + ch)

    backtrack(0, "")
    return res


digits = input("Enter digits (2-9): ")
print(letter_combinations(digits))
