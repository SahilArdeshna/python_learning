import unittest
import exercise_script


class TestGame(unittest.TestCase):
    def test_input(self):
        answer = 6
        guess = 6
        result = exercise_script.run_guess(guess, answer)
        self.assertTrue(result)

    def test_input2(self):
        result = exercise_script.run_guess(5, 0)
        self.assertFalse(result)

    def test_input3(self):
        result = exercise_script.run_guess(5, 11)
        self.assertFalse(result)

    def test_input4(self):
        result = exercise_script.run_guess(5, "11")
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
