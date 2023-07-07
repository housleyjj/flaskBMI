# BMI Flask Application
---
### Project Description
---
This application was the final challenge for the Udemy course [Python Flask for Beginners](https://www.udemy.com/course/python-flask-for-beginners/)

By entering weight in pounds and height in inches, your bmi will be calculated.  Entering a username will give you a personalizerd message.

**Note:** My main purpose in creating this application was to learn and practice construction of a flask application.  I also wanted to see if I could capture the data and send the results to another html page.  This means that data sanitization and error handling are at a minimum.  These are some features I hope to implement in the future.

Another goal of mine was to see how I could implement Docker.  I was able to run this application in a container without needing to setup a virtual environment on my host machine.

### Docker intstructions
Once you have pulled the applicaion, in your command prompt run:
   
   1. docker build -t bmi_flask:latest   
   2. docker run -d --rm --name bmi-app -p 5000:5000 bmi_flask:latest

Then using your browser of choice, goto localhost:5000
