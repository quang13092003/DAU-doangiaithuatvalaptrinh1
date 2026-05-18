class Solution:
    def dayOfTheWeek(self, day, month, year):
        weeks = ["Friday", "Saturday", "Sunday", "Monday",
                 "Tuesday", "Wednesday", "Thursday"]

        days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]

        total_days = 0

        # cộng số ngày của các năm trước
        for y in range(1971, year):
            if (y % 400 == 0) or (y % 4 == 0 and y % 100 != 0):
                total_days += 366
            else:
                total_days += 365

        # cộng số ngày của các tháng trước
        for m in range(month - 1):
            total_days += days_in_month[m]

        # năm nhuận và qua tháng 2
        if month > 2:
            if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
                total_days += 1

        # cộng ngày hiện tại
        total_days += day - 1

        return weeks[total_days % 7]