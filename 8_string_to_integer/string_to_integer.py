class Solution:
    def myAtoi(self, str):
        # 0.
        str = str.strip()
        # 1.
        if str == "":
            return 0
        # 2.
        if str[0] != "+" and str[0] != "-" and not str[0].isnumeric():
            return 0
        # 3.
        if str[0] == "+" or str[0] == "-":
            sign = str[0]
            # 4.
            digits = self.convert(str[1:])
            # 5.
            if sign == "+":
                return min(digits, 2147483647)
            else:
                return max(0-digits, -2147483648)
        # 6.
        else:
            return min(self.convert(str), 2147483647)

    # Converts string to integer
    def convert(self, str):
        digits = 0
        for s in str:
            if not s.isnumeric():
                break
            digits = 10 * digits + int(s)
        return digits
