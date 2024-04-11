# Zena Content Validation App

This is a REST application made with Django Rest Framework. This is a toy project for a content validation system. It consists of API endpoints which allows user to:
- Create and Manage different guidelines for the content.
- Upload/Update the content
- Review the content

### To setup
- Install Python (ideal version 3.10.x)
- Install all the dependencies using the following command:
    ```
    pip install -r requirements.txt
    ```
- Set up your database by running following command:
    ```
    python manage.py migrate
    ```
- Start the sever:
    ```
    python manange.py runserver
    ```

### Admin Panel
- To login to the Admin Panel, create a super user by running the following command:
    ```
    python manage.py createsuperuser
    ```
- Then, Go to `https://localhost:8000/admin` to login as superuser

### API documentation:
- Refer to the `Zena Content App.postman_collection.json` file for the postman collection and api documentation.

