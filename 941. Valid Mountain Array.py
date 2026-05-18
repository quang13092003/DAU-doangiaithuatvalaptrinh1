class Solution:
    def validMountainArray(self, arr):
        n = len(arr)

        if n < 3:
            return False

        i = 0

        # đi lên
        while i + 1 < n and arr[i] < arr[i + 1]:
            i += 1

        # đỉnh không được ở đầu hoặc cuối
        if i == 0 or i == n - 1:
            return False

        # đi xuống
        while i + 1 < n and arr[i] > arr[i + 1]:
            i += 1

        return i == n - 1