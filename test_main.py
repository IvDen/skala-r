import unittest

from main import biggestPath, MAX_LENGTH


class TestBiggestPath(unittest.TestCase):
    def setUp(self) -> None:
        self.depth_for_dict_generate = 0

        def get_big_dict():
            temp_dict = {}
            self.depth_for_dict_generate += 1
            while self.depth_for_dict_generate < MAX_LENGTH:
                temp_dict = {'dir' + str(self.depth_for_dict_generate): get_big_dict()}
            return temp_dict

        def get_checker_for_big_dict():
            result = ''
            counter_iter = 1
            length_control = len(result)
            while length_control < MAX_LENGTH:
                result = result + '/' + ''.join('dir' + str(counter_iter))
                counter_iter += 1
                length_control = len(result)
            return result

        self.big_dict = get_big_dict()
        self.checker_for_big_dict = get_checker_for_big_dict()

    def test_biggestPath_base0(self):
        self.assertEqual(biggestPath({'dir1': {'dir2': {'dir3': ['file1']}}}), '/dir1/dir2/dir3/file1')

    def test_biggestPath_base1(self):
        self.assertEqual(biggestPath(
            {'dir1': {}, 'dir2': ['file1'], 'dir3': {'dir4': ['file2'], 'dir5': {'dir6': {'dir7': {}}}}}),
            '/dir3/dir5/dir6/dir7')

    def test_biggestPath_base2(self):
        self.assertEqual(biggestPath({'dir1': ['file1', 'file2', 'file2']}), '/dir1/file1')

    def test_biggestPath_not_valid_filename(self):
        self.assertEqual(biggestPath({'dir1': ['file1', 'file1']}), '/')

    def test_biggestPath_not_valid_dirname_notAZaz09(self):
        self.assertEqual(
            biggestPath({'dir1': {}, 'dir2': ['file1'], 'dir3': {'dir4': ['file2'], 'дир5': {'dir6': {'dir7': {}}}}}),
            '/dir3/dir4/file2')

    def test_biggestPath_not_valid_filename_notAZaz09(self):
        self.assertEqual(biggestPath({'dir1': ['файл1', 'file2']}), '/dir1/file2')

    def test_biggestPath_empty_input(self):
        self.assertEqual(biggestPath({}), '/')

    def test_biggestPath_more_than_255(self):
        self.assertEqual(biggestPath(self.big_dict), self.checker_for_big_dict)


if __name__ == "__main__":
    unittest.main()
