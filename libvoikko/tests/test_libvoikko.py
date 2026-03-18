import unittest
import sys
import subprocess
import libvoikko

class TestLibvoikko(unittest.TestCase):

    def test_dummy(self):
        self.assertEqual(True, True)

    @unittest.expectedFailure
    def test_expected_failure(self):
        self.assertEqual(False, True)

    def test_spell(self):
        voikko = libvoikko.Voikko('fi')
        self.assertEqual(voikko.spell('kissa'), True)
        self.assertEqual(voikko.spell('kisssa'), False)

    def test_suggest(self):
        voikko = libvoikko.Voikko('fi')
        self.assertEqual(
            voikko.suggest('kisssa'),
            ['kissa', 'kissaa', 'kisassa', 'kisussa', 'Kiassa'])

    def test_voikkospell(self):
        cp  = subprocess.run(['echo kissa | voikkospell'], encoding='UTF-8', text=True, shell=True, capture_output=True)
        self.assertEqual(cp.stdout, 'C: kissa\n')
        self.assertEqual(cp.stderr, '')
        self.assertEqual(cp.returncode, 0)
        cp  = subprocess.run(['echo kisssa | voikkospell'], encoding='UTF-8', text=True, shell=True, capture_output=True)
        self.assertEqual(cp.stdout, 'W: kisssa\n')
        self.assertEqual(cp.stderr, '')
        self.assertEqual(cp.returncode, 0)

    def test_voikkohyphenate(self):
        cp  = subprocess.run(['echo kissa | voikkohyphenate'], encoding='UTF-8', text=True, shell=True, capture_output=True)
        self.assertEqual(cp.stdout, 'kis-sa\n')
        self.assertEqual(cp.stderr, '')
        self.assertEqual(cp.returncode, 0)

    def test_voikkogc_tokenize(self):
        cp  = subprocess.run(['echo "kissa." | voikkogc --tokenize'], encoding='UTF-8', text=True, shell=True, capture_output=True)
        self.assertEqual(cp.stdout, 'W: "kissa"\nP: "."\n')
        self.assertEqual(cp.stderr, '')
        self.assertEqual(cp.returncode, 0)

if __name__ == "__main__":
    unittest.main()
