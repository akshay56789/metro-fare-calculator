# metro-fare-calculator



Metro Fare Calculator is a simple web application designed to help users calculate the fare for their metro rides. With this application, users can easily determine the cost of their metro ride based on their starting and ending stations.



The application is built using the Django framework and is designed to be responsive and easy to use. Users simply select their starting station and ending station from a dropdown menu, and the application calculates the fare based on the distance between the two stations.


![Metro Fare - Google Chrome 19-04-2023 20_39_29 (2)](https://user-images.githubusercontent.com/130206125/233120574-f736e375-7014-452c-b1e9-cc00664972f8.png)

![Screenshot (40)](https://user-images.githubusercontent.com/130206125/233118575-af100009-d9e5-47f9-8d16-b4e9e46a37f9.png)


If you are looking for a reliable and user-friendly metro fare calculator, this project is an excellent choice. It is free and open-source, so feel free to fork the repository and make contributions to improve the application further.

1. Install Python: If you haven't already, download and install the latest version of Python for your operating system from the official website: https://www.python.org/downloads/

2. Install Git: Download and install Git for your operating system from the official website: https://git-scm.com/downloads

3. Clone the project: Open your terminal or command prompt and navigate to the directory where you want to store the project. Then, run the following command to clone the project:

git clone https://github.com/username/project.git

4. Replace the username with the username of the person who created the project and the project with the name of the project.

5. Install virtualenv: Virtualenv is a tool that allows you to create isolated Python environments for each project, so you don't have to worry about dependencies conflicting with each other. To install virtualenv, run the following command:

pip install virtualenv

6. Create a virtual environment: Navigate to the project directory and create a new virtual environment by running the following command:

virtualenv env

7. Activate the virtual environment: Activate the virtual environment by running the following command:

For Windows:

env\Scripts\activate

For macOS or Linux:

source env/bin/activate

8. Install dependencies: Once the virtual environment is activated, install the required dependencies by running the following command:

pip install -r requirements.txt

9. Set up the database: Before you can run the Django project, you need to set up the database. Run the following commands in order:

python manage.py makemigrations

python manage.py migrate

10.Run the server: Finally, run the Django server by running the following command:

python manage.py runserver
