AI Based Smart Attendance Using Face Recognition

UPDATED NAVIGATION
- Added a mobile-style "← Back" button to feature screens.
- Pressing Back closes the current feature and returns to the dashboard.
- The Escape key also works as Back.
- Existing images, logos, button artwork, dimensions, and screen layouts are preserved.
- The dashboard remains the main navigation screen.
- Image paths in the dashboard/login/register screens were made portable so the project can be moved after unzipping.

RUN
1. Make sure MySQL Server is running.
2. Open this folder in VS Code/PyCharm.
3. Activate your existing .venv, or create a new environment.
4. Install dependencies: pip install -r requirements.txt
5. Run login.py for the normal application flow.

DATABASE
The existing MySQL database names and credentials in the original project have not been changed.
If MySQL is configured differently on the submission computer, update the existing connection settings in the relevant Python files.

NOTE
The supplied project contains the original virtual-environment files. For a clean transfer, a fresh virtual environment can be created using requirements.txt instead.


APPLICATION FLOW
=================
1. Start the project using START_APPLICATION.bat (or run main.py).
2. The Login screen opens first automatically.
3. New User Register and Forgot Password are available from Login.
4. After successful login, the Dashboard opens in the same application window.
5. Feature pages have a left-side <- Back button to return to the Dashboard.
6. You do not need to open login.py separately.

IMAGE PATHS
===========
Existing image paths were intentionally left unchanged.
