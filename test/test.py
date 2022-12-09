
import sys
import cv2
import os
import unittest
import PIL
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
import amazoncaptcha.solve
here = os.path.abspath(os.path.dirname(__file__))

class TestAmazonCaptchaSolver(unittest.TestCase):
    def test_image(self):
        self.Solver = amazoncaptcha.solve.AmazonCaptchaSolver()
        img_array = cv2.imread(os.path.join(
            here, "Captcha_doyufigqoe.jpg"))
        result = self.Solver.solve(Image=img_array)
        self.assertEqual(result, "YEYJPJ")
        print("Passed")


if __name__ == '__main__':
    unittest.main()
