# This is an end to end ML project to predict Student performance in Maths.
mlproject is basically a web app, it has a main page which just says 'Welcome to home Page'.(can be made more beautiful in fututre but this is not the current objective of this repo).Then from there you got to predict page by just adding 'predictdata' to url of home page. Here you can fill the field and get your predicted scores in Math. This repos also contains notebook for EDA on data and also tying out different ML models to get highest scoring model.

## How to run the app

1. git clone https://github.com/kashif-flask/mlproject.git
2. Install all dependencies given in requirements.txt file in cmd using  pip install -r requirements.txt
3. run the file app.py in cmd , you will get local host http://127.0.0.1:5000/ 
4. Now open the url in web browser.
5. You can also create docker image by writing command in cmd:"docker build -t studentmarks . " and then just run the image cmd:docker run -p 5000:5000 studentmarks, now you can run the app on localhost:5000
6. Then you will see the home page
7. If you want to run just the app and don't need code, then pull image from my docker hub , write in cmd: docker pull kashif09/studentmarks:latest and then just run as in step 5

## How to use app
1. Once you see the home page
   ![alt text](https://github.com/kashif-flask/mlproject/blob/main/home.PNG)

2. Now add '/predictdata' to url, you will see the prediction page
   ![alt text](https://github.com/kashif-flask/mlproject/blob/main/predictpage.PNG)

3. Now fill in the details of fileds
   • Gender: The gender of the student (male/female)
   • Race/ethnicity: The student's racial or ethnic background (Asian, African-American, Hispanic, etc.), the dataset contain groups only and not the actual race
   • Parental level of education: The highest level of education attained by the student's parent(s) or guardian(s)
   • Lunch: Whether the student receives free or reduced-price lunch (yes/no)
   • Test preparation course: Whether the student completed a test preparation course (yes/no)
   • Reading score: The student's score on a standardized reading test
   • Writing score: The student's score on a standardized writing test

4. Then click on predict button to get prediction like:
   ![alt text](https://github.com/kashif-flask/mlproject/blob/main/predict.PNG)










