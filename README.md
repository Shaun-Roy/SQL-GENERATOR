
## SQL GENERATOR USING GEMINI AP

This Python web application utilizes the Gemini API to translate natural language descriptions into executable SQL queries.

Automates SQL query generation, saving developers time and effort.

Enables users with limited SQL knowledge to easily interact with databases.

Employs the powerful Gemini API for advanced natural language understanding.


## Used By

This project is useful for:

- Beginner Developers
- Educators
- Business Users


## Prerequisites

- Python
- Gemini API key 
- streamlit (python)

```cmd
  pip install streamlit
```
```cmd
  pip install google-generativeai
```
# Configuration

```cmd
GOOGLE_API_KEY = "enter key here"
genai.configure(api_key=GOOGLE_API_KEY)
```
```cmd
model = genai.GenerativeModel('gemini-pro')
```
 we use the gemini-pro version which is free rather than the gemini-pro-vision






## Screenshots

![Preview](https://github.com/Shaun-Roy/SQL-GENERATOR/blob/main/screenshots/Screenshot%202025-01-04%20085934.png)

![Preview](https://github.com/Shaun-Roy/SQL-GENERATOR/blob/main/screenshots/Screenshot%202025-01-04%20090001.png)



