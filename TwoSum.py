def twoSum(nums, target):
    # Brute force method: check every pair
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return None

def main():
    # Take user input for the list of numbers
    nums_input = input("Enter numbers separated by spaces: ")
    nums = list(map(int, nums_input.split()))

    # Take user input for the target value
    target = int(input("Enter the target number: "))

    result = twoSum(nums, target)

    if result:
        print("Indices found:", result)
        print("Numbers are:", nums[result[0]], "and", nums[result[1]])
    else:
        print("No solution found.")


if __name__ == "__main__":
    main()
