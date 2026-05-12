class Solution:
    def mergeTwoLists(self, list1, list2):

        # Tạo node giả ban đầu
        # dummy giúp dễ xử lý và trả về kết quả
        dummy = ListNode(0)

        # current dùng để duyệt và nối node mới
        current = dummy

        # Chạy khi cả 2 list còn phần tử
        while list1 and list2:

            # Nếu giá trị list1 nhỏ hơn list2
            if list1.val < list2.val:

                # Nối node list1 vào kết quả
                current.next = list1

                # Di chuyển list1 sang node tiếp theo
                list1 = list1.next

            else:
                # Ngược lại nối node list2
                current.next = list2

                # Di chuyển list2
                list2 = list2.next

            # Di chuyển current sang node vừa nối
            current = current.next

        # Sau vòng lặp:
        # Một trong hai list sẽ còn dư

        # Nếu list1 còn node
        if list1:
            current.next = list1

        # Ngược lại nối phần còn lại của list2
        else:
            current.next = list2

        # dummy.next là đầu danh sách kết quả
        return dummy.next