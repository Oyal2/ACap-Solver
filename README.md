<p align="center">
<img src="https://user-images.githubusercontent.com/13637813/206646958-70ee6325-f0d0-4570-b78e-9826b0668f80.png" height="300" />
</p>

# ACap Solver

Solve your annoying text captchas that amazon gives you in a matter of milliseconds. This package can take input as a captcha image or a url to the image link. Get your problem solved in 1-2 lines of code with ACap solver.

---
This package is meant to solve [Amazon's text captcha](https://www.amazon.com/errors/validateCaptcha)

# Introduction

ACap Solver uses image classification to detect letters. The algorithm is trained using a convolutional neural network model, AlexNet, with a model acurracy of 99.67%.

<img src="https://user-images.githubusercontent.com/13637813/206654693-6727e5f2-6ca0-46a0-a981-f9b0075806cf.png" height="500" width="500"/>

The program uses openCV to find and isolate each letter where it then goes to the CNN model and predicts each letter. After predicting each letter youre returned with a solution. 

# Code Snippets

## Fetch Answer From Image Url
```python
from amazoncaptcha.solve import AmazonCaptchaSolver

solver = AmazonCaptchaSolver()
answer = solver.solve(Url='https://images-na.ssl-images-amazon.com/captcha/lqbiackd/Captcha_tcvqeczslf.jpg')
#answer: ULJLFL
```

## Fetch Answer From Captcha Image
```python
from amazoncaptcha.solve import AmazonCaptchaSolver

img_array = cv2.imread("Captcha_doyufigqoe.jpg")
answer = self.Solver.solve(Image=img_array)
#answer: YEYJPJ
```
