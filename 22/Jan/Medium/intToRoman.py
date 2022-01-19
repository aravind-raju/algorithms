class Solution:
    # @param A : integer
    # @return a strings
    def intToRoman(self, number):
        num = [1, 4, 5, 9, 10, 40, 50, 90,
            100, 400, 500, 900, 1000]
        sym = ["I", "IV", "V", "IX", "X", "XL",
            "L", "XC", "C", "CD", "D", "CM", "M"]
        i = 12
        roman = ""
        while number:
            div, number = divmod(number, num[i])
            while div:
                roman += sym[i]
                div -= 1
            i -= 1
        return roman