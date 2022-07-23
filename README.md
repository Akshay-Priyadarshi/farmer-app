# FARMERZ APPLICATION - FINSTACK ASSIGNMENT

## Steps to start the application

1. Clone the repository.

    ```CMD
    git clone https://github.com/Akshay-Priyadarshi/farmer-app.git
    ```

1. Make a .env file in the root folder by copying the content of example.env file and providing the environment variables.

1. Install the required dependencies as mentioned in the requirement.txt file by running -

    ```CMD
    pip install -r requirements.txt
    ```

1. Next, we need to migrate all the models to our database and for that we have to run -

    ```CMD
    python manage.py migrate
    ```

1. To start the server run -

    ```CMD
    python manage.py runserver 8080
    ```

    _Here PORT = 8080, You can specify the PORT no of your choice here_

1. Navigate to **_localhost:8080/admin_** for the admin login and **_localhost:8080/_** for the actual application in the web browser.
