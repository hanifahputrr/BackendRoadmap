Building Data Science Applications with FastAPI
---
This chapter covers the foundational setup needed to work with Python and FastAPI efficiently, ensuring a robust and conflict-free development environment. The key focus is on configuring tools, managing dependencies, and preparing the system for API development.

**Python Development Environment Setup**
---
**Step 1**
1. Create python virtual environment:
to isolate project dependencies, avoiding conflicts across projects
  ```
    python -m venv venv
  ```
2. Activate the virtual environment:
   ```
     source venv/bin/activatee
   ```
3. Installing FastAPI and uvicorn
   ```
   pip install fastapi "uvicorn[standard]"
   ```

**Step 2: simple requests on a dummy API**

1. Installing the HTTPie command-line utility:
   ```
   pip install httpie
   ```

2. Perform a GET Request
   ```
    http GET https://603cca51f4333a0017b68509.mockapi.io/todos
   ```
- Output:
    
    ```
    [
        {
            "id": "1",
            "text": "Write the second edition of the book"
        }
    ]
    
    ```
    

**Result**: Successfully fetched data from the dummy API using the **GET** method. HTTPie displayed a clean, formatted JSON response with headers.


3. Perform a POST Request
   ```
    http -v POST https://603cca51f4333a0017b68509.mockapi.io/todos text="My new task"
    
    ```
    
- Output:
    
    ```
    {
        "id": "2",
        "text": "My new task"
    }
    
    ```
    

**Result**: Successfully created a new task in the dummy API using the **POST** method. The `-v` option displayed both the request and response for debugging.


4. Add Custom Headers
   ```
    http -v GET https://603cca51f4333a0017b68509.mockapi.io/todos "My-Header: My-Header-Value"
   ```
    
- Output received:
    
    ```
    [
        {
            "id": "1",
            "text": "Write the second edition of the book"
        },
        {
            "id": "2",
            "text": "My new task"
        }
    ]
    
    ```
    

**Result**: Successfully sent a **GET** request with a custom header. The API responded with data, and the headers were confirmed in the response.


### **Summary**
---

- All steps were executed successfully using HTTPie in VS Code. The API endpoints responded correctly to **GET** and **POST** requests.
- HTTPie proved to be a simple and efficient tool for API testing with formatted output and debugging features.
