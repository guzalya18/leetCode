class Solution(object):
    def fizzBuzz(self, n):
        result_list = []
        for i in range(1,n+1):
            if i % 3 == 0 and i % 5 == 0:
                result_list.append("FizzBuzz")
            elif i % 3 == 0:
                result_list.append("Fizz")
            elif i % 5 == 0:
                result_list.append("Buzz")
            else:
               result_list.append(str(i))
        return result_list