class Solution:
    def deleteDuplicates(self, head):

        # curr dùng để duyệt linked list
        curr = head

        # Chạy khi:
        # curr tồn tại
        # và curr.next tồn tại
        while curr and curr.next:

            # Nếu 2 node liên tiếp bị trùng
            if curr.val == curr.next.val:

                # Bỏ node trùng
                # nối trực tiếp sang node kế tiếp nữa
                curr.next = curr.next.next

            else:
                # Nếu không trùng
                # di chuyển sang node tiếp theo
                curr = curr.next

        # Trả về linked list sau khi xóa trùng
        return head