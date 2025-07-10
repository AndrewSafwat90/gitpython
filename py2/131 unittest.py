import unittest


class myTest(unittest.TestCase):
    def test_one(self):
        self.assertTrue(3 * 8 == 24, "3 times 8 should be 24")

    def test_two(self):
        self.assertEqual(3 * 8, 24, "3 times 8 should be 24")


if __name__ == '__main__':
    unittest.main()


# assert 3*8 == 23, "3 times 8 should be 24"


# def test_assert():
#     assert 3*8 == 24, "3 times 8 should be 24"


# def test_assert_fail():
#     assert 3*8 == 24, "3 times 8 should be 24"


# if __name__ == '__main__':
#     test_assert()
#     test_assert_fail()

#     print("All tests passed.")
