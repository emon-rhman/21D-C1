def findMedianSortedArrays(nums1, nums2):
    A, B = nums1, nums2
    m, n = len(A), len(B)

    if m > n:
        A, B, m, n = B, A, n, m

    total = m + n
    half = total // 2

    left, right = 0, m

    while left <= right:
        i = (left + right) // 2
        j = half - i

        A_left  = A[i - 1] if i > 0 else float('-inf')
        A_right = A[i]     if i < m else float('inf')

        B_left  = B[j - 1] if j > 0 else float('-inf')
        B_right = B[j]     if j < n else float('inf')

        if A_left <= B_right and B_left <= A_right:
            if total % 2 == 1:
                return min(A_right, B_right)
            return (max(A_left, B_left) + min(A_right, B_right)) / 2

        elif A_left > B_right:
            right = i - 1
        else:
            left = i + 1


# -------- USER INPUT -------
nums1 = list(map(int, input("Enter sorted list 1: ").split()))
nums2 = list(map(int, input("Enter sorted list 2: ").split()))

print(findMedianSortedArrays(nums1, nums2))
