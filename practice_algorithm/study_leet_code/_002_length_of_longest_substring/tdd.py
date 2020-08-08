import unittest


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.first_input = "abcabcbb"

    def test_final(self):
        pass
        # actual = Solution().lengthOfLongestSubstring("abcabcbb")
        # expected = 3
        # self.assertEqual(expected, actual)
        #
        # actual = Solution().lengthOfLongestSubstring("bbbbb")
        # expected = 1
        # self.assertEqual(expected, 1)
        #
        # actual = Solution().lengthOfLongestSubstring("pwwkew")
        # expected = 3
        # self.assertEqual(expected, 3)

    # 덩어리로 확인할 수 없으니 문자열을 쪼개야 한다.
    # python은 문자열을 이미 배열로 가지고 있다.
    # dict와 다른 점 테스트
    def test_access_string_index_key(self):
        # input_data index 키에 원소를 넣을 수 없다.
        with self.assertRaises(TypeError):
            print('a' == self.first_input['a'])

    # integer 값을 넣어서 가져온다.
    def test_access_string_index(self):
        self.assertEqual('a', self.first_input[0])
        self.assertEqual('a', self.first_input[3])
        self.assertEqual('b', self.first_input[4])

    def test_get_first_pattern(self):
        actual = get_first_pattern("abcabcbb")
        expected = ('abc', 3)
        self.assertEqual(expected[1], actual)

    def test_bbbbbbb(self):
        actual2 = get_first_pattern('bbbbbbb')
        expected2 = ('b', 1)
        self.assertEqual(expected2[1], actual2)

    def test_pwwkew(self):
        actual3 = get_first_pattern("pwwkew")
        expected3 = ('wke', 3)
        self.assertEqual(expected3[1], actual3)

    def test_aab(self):
        actual = get_first_pattern("aab")
        expected = ('ab', 2)
        self.assertEqual(expected[1], actual)

    def test_bdb(self):
        actual = get_first_pattern("bdb")
        expected = ('bd', 2)
        self.assertEqual(expected[1], actual)

    def test_empty_input(self):
        self.assertEqual(0, get_first_pattern(""))

    def test_high_pass(self):
        actual = get_first_pattern("brnk")
        expected = 4
        self.assertEqual(expected, actual)

        actual3 = get_first_pattern("au")
        expected3 = ('au', 2)
        self.assertEqual(expected3[1], actual3)

    def test_cdd(self):
        actual = get_first_pattern("cdd")
        expected = 2
        self.assertEqual(expected, actual)

    def test_aaca(self):
        actual = get_first_pattern("aaca")
        expected = 2
        self.assertEqual(expected, actual)

    def test_abcb(self):
        actual = get_first_pattern("abcb")
        expected = 3
        self.assertEqual(expected, actual)

    def test_dvdf(self):
        actual = get_first_pattern("dvdf")
        expected = 3
        self.assertEqual(expected, actual)

    def test_dict_sort(self):
        ss = {'abc': 2, 'abcd': 1, 'abcf': 30}
        ss['bcsa'] = 3
        for ss in sorted(ss.items(),
                         key=lambda x: x[1],
                         reverse=True):
            print(ss[0], ss[1])

        print(type(ss))


def get_first_pattern(s: str) -> int:
    length = len(s)

    if length == 0:
        return 0

    acc = s[0] or ""

    if acc * len(s) == s:
        return 1

    if is_high_pass_not_match(s):
        return len(s)

    dictionary = dict()

    for i in range(length - 1):
        l1, l2 = s[i], s[i + 1]

        if acc.__contains__(l2):
            add_dict(dictionary, acc)
            acc = acc[acc.index(l2) + 1:]

        acc += l2

    add_dict(dictionary, acc)
    return result_int(dictionary)


def add_dict(dictionary, acc):
    dictionary.__setitem__(acc, dictionary.get(acc) if acc in dictionary else 1)
    # print(dictionary)


def result_int(dictionary: {}) -> int:
    if len(dictionary) == 1:
        return len(dictionary.popitem()[0])

    max_item = dictionary.popitem()
    for i in sorted(dictionary.items(),
                    key=lambda x: x[1],
                    reverse=True):
        if max_item[1] > i[1]:
            return max_item

        if max_item[1] < i[1]:
            max_item = i
        elif max_item[1] == i[1] and len(max_item[0]) < len(i[0]):
            max_item = i

    return len(max_item[0])


def is_high_pass_not_match(s):
    for z in range(1, len(s)):
        if s[z - 1] == s[z]:
            return False


if __name__ == '__main__':
    unittest.main()
