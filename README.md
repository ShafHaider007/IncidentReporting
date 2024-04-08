# IncidentReporting
GeoSafe: Django GIS for housing society incident reporting. Map and report community incidents easily. Enhance safety together.

# Project Name

## Running the Project

Follow these steps to set up and run the project locally:

1. **Activate Virtual Environment:**
    - Open your terminal.
    - Navigate to the directory where your virtual environment is located.
    - Activate the virtual environment using the appropriate command based on your operating system (e.g., `source venv/bin/activate` for Unix/Linux, or `venv\Scripts\activate` for Windows).

2. **Navigate to Project Directory:**
    - Once the virtual environment is activated, navigate to your project directory using the `cd` command. For example:
      ```
      cd myproject
      ```

3. **Configure Database Settings:**
    - Open the `settings.py` file in your Django project (`myproject/settings.py`).
    - Locate the `DATABASES` configuration section.
    - Configure the database settings according to your requirements, including database engine, name, user, password, host, and port.

4. **Install Dependencies:**
    - If you haven't already, install the project dependencies by running:
      ```
      pip install -r requirements.txt
      ```

5. **Apply Database Migrations:**
    - Run the following command to apply any pending database migrations:
      ```
      python manage.py migrate
      ```

6. **Create Superuser (Optional):**
    - If you need to create a superuser account for administrative access, run:
      ```
      python manage.py createsuperuser
      ```

7. **Run the Development Server:**
    - Start the Django development server by running:
      ```
      python manage.py runserver
      ```
    - Once the server is running, you can access the application by navigating to `http://127.0.0.1:8000` in your web browser.

8. **Accessing the Application:**
    - Open a web browser and navigate to `http://127.0.0.1:8000`.
    - You should see the homepage of your Django project, indicating that the server is running successfully.

### Additional Notes:

- **Environment Variables:** If your project uses environment variables for sensitive information (e.g., database credentials), make sure to set them appropriately before running the server.
  
- **Custom Settings:** Depending on your project's specific configuration, you may need to adjust other settings in `settings.py` or elsewhere in your project directory.

- **Deployment:** For production deployment, follow Django's best practices for deploying applications to ensure security and performance.

Make sure to replace `myproject` with the actual name of your project directory. If there are any additional steps or specific configurations required for your project, feel free to include them in the documentation.
