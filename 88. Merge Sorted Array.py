class Solution:
    def merge(self, nums1, m, nums2, n):

        # i trỏ phần tử cuối cùng có giá trị trong nums1
        i = m - 1

        # j trỏ phần tử cuối nums2
        j = n - 1

        # k trỏ vị trí cuối cùng của nums1
        k = m + n - 1

        # So sánh từ cuối về đầu
        while i >= 0 and j >= 0:

            # Nếu phần tử nums1 lớn hơn
            if nums1[i] > nums2[j]:

                # Đưa nums1[i] về cuối
                nums1[k] = nums1[i]

                # Di chuyển i
                i -= 1

            else:
                # Ngược lại lấy nums2[j]
                nums1[k] = nums2[j]

                # Di chuyển j
                j -= 1

            # Di chuyển vị trí gán
            k -= 1

        # Nếu nums2 còn phần tử
        while j >= 0:

            nums1[k] = nums2[j]

            j -= 1
            k -= 1