from collections import defaultdict
import unittest
import sys

class TestUnicodeEmoji(unittest.TestCase):
    dir_path = "/usr/share/unicode/emoji/"

    def test_dummy(self):
        self.assertEqual(True, True)

    @unittest.expectedFailure
    def test_expected_failure(self):
        self.assertEqual(False, True)

    def test_emoji_data(self):
        self.parser(filename=self.dir_path+"emoji-data.txt")

    def test_emoji_sequences(self):
        self.parser(filename=self.dir_path+"emoji-sequences.txt")

    def test_emoji_zwj_sequences(self):
        self.parser(filename=self.dir_path+"emoji-zwj-sequences.txt")

    def parser(self, filename):
        file_content = list()
        report = defaultdict(dict)
        with open(filename, "r") as fobj:
            lines = fobj.readlines()

        count = 0
        curr_head = None
        for line in lines:

                def count_group_emoji(line, count):
                    '''
                    This function increments the count with the value inside "[ ]"
                    '''
                    if "[" in line:
                        return count + int(line.split("[")[1].split("]")[0])
                    return count + 1

                if line.startswith("\n"):
                    continue

                elif count == 0 and not line.startswith("#"):
                    curr_head = line.split(";")[0].strip()
                    count = count_group_emoji(line , count)
                    report[curr_head]['actual_count'] = count

                elif line.startswith("# Total elements"):
                    report[curr_head]['expected_count'] = int(line.split(":")[1])
                    count = 0

                elif not line.startswith("#"):
                    count = count_group_emoji(line ,count)
                    report[curr_head]['actual_count'] = count

        print(report)

        def validate(report):
            '''
            This function will validate if the actual_count equals expected_count
            '''
            for key,data in report.items():
                self.assertEqual(data['actual_count'],data['expected_count'])

        validate(report)

if __name__ == "__main__":
    unittest.main()
