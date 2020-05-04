from count_and_say import Solution
import unittest

class InsertTest(unittest.TestCase):

    def test_search(self):
        searched = Solution()
        assert searched.countAndSay([1,5]) == ['1', '11', '21', '1211', '111221']
        assert searched.countAndSay([2,7]) == ['1', '11', '21', '1211', '111221', '312211', '13112221']
        assert searched.countAndSay([3,8]) == ['1', '11', '21', '1211', '111221', '312211', '13112221', '1113213211']
        assert searched.countAndSay([1,10]) == ['1', '11', '21', '1211', '111221', '312211', '13112221', '1113213211', '31131211131221', '13211311123113112211']
    
if __name__ == '__main__':
    unittest.main()