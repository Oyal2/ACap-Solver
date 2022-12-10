<p align="center">
<img src="https://user-images.githubusercontent.com/13637813/206646958-70ee6325-f0d0-4570-b78e-9826b0668f80.png" height="300" />
</p>
<h2 align="center">ACap Solver</h2>
<div align="center">

  [![Status](https://img.shields.io/badge/status-active-success.svg)]()
  [![GitHub Issues](https://img.shields.io/github/issues/Oyal2/ACap-Solver.svg)](https://github.com/Oyal2/ACap-Solver/issues)
  [![GitHub Pull Requests](https://img.shields.io/github/issues-pr/kylelobo/The-Documentation-Compendium.svg)](https://github.com/Oyal2/ACap-Solver/pulls)
  [![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)
</div>

---
<p align="center"> This package is meant to solve 
<a href="https://www.amazon.com/errors/validateCaptcha">Amazon's text captcha</a>
    <br> 
</p>

# 📝 Table of Contents
+ [About](#about)
+ [How it works](#working)
+ [Usage](#usage)
  
# 🧐 About <a name = "about"></a>
Solve your annoying text captchas that amazon gives you in a matter of milliseconds. This package can take input as a captcha image or a url to the image link. Get your problem solved in 1-2 lines of code with ACap solver.


# 💭 How it works <a name = "working"></a>

ACap Solver uses image classification to detect letters. The algorithm is trained using a convolutional neural network model, AlexNet, with a model acurracy of 99.67%.

<img src="https://user-images.githubusercontent.com/13637813/206654693-6727e5f2-6ca0-46a0-a981-f9b0075806cf.png" height="500" width="500"/>

The program uses openCV to find and isolate each letter where it then goes to the CNN model and predicts each letter. After predicting each letter youre returned with a solution. 

# 🎈 Usage <a name = "usage"></a>

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