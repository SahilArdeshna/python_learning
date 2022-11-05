import unittest
import main


class TestMain(unittest.TestCase):
    def setUp(self):
        print("about to run a function")

    def test_do_stuff(self):
        """Hi from test_do_stuff"""
        test_params = 10
        result = main.do_stuff(test_params)
        self.assertEqual(result, 15)

    def test_do_stuff2(self):
        test_params = "hiiii"
        result = main.do_stuff(test_params)
        self.assertIsInstance(result, ValueError)

    def test_do_stuff3(self):
        test_params = None
        result = main.do_stuff(test_params)
        self.assertEqual(result, "please enter number")

    def test_do_stuff4(self):
        test_params = ""
        result = main.do_stuff(test_params)
        self.assertEqual(result, "please enter number")

    def test_do_stuff5(self):
        test_params = 0
        result = main.do_stuff(test_params)
        self.assertEqual(result, "please enter number")

    def tearDown(self):
        print("cleaning up")


if __name__ == "__main__":
    unittest.main()
