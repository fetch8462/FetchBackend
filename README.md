# FetchBackend

## Overview
This is a Flask-based REST API that tracks and manages a single user's points from multiple payers. It supports the following operations
1. Adding points for a specific payer
2. Spending points
3. Retreiving the current balance of points sorted by each payer



## **API Endpoints**

### **1. Add Points**
- **Route**: `/add`
- **Method**: `POST`
- **Description**: Adds a transaction for a payer with points and timestamp.
- **Request Body**:
  ```json
  {
    "payer": "DANNON",
    "points": 300,
    "timestamp": "2023-01-01T14:00:00Z"
  }

### **2. Spend Points**
- **Route**: `/spend`
- **Method**: `POST`
- **Description**: Subtracts a specified amount of points from the user's balance
- **Request Body**:
  ```json
  {
    "payer": "DANNON",
    "points": 300,
    "timestamp": "2023-01-01T14:00:00Z"
  }

### **3. Get Balance**

- **Route**: `/balance`
- **Method**: `GET`
- **Description**: Retrieves the current balance of points sorted by payer

#### **Response**
- **Example Success Response**:
  ```json
  {
    "DANNON": 1000,
    "MILLER COORS": 5300,
    "UNILEVER": 0
  }

## **How to Run**

### **Requirements**
- Python 3.7+ installed on your system.
- Flask library for Python.

---

### **Setup Instructions**
1. **Clone the Repository**:
   Clone the project repository from GitHub:
   ```bash
   git clone https://github.com/fetch8462/FetchBackend.git
   cd FetchBackend
2. **Create and Activate a Virtual Environment**:
      - **Linux/Mac**:
     ```bash
     python3 -m venv myenv
     source myenv/bin/activate
     ```
   - **Windows**:
     ```bash
     python -m venv myenv
     myenv\Scripts\activate
     ```
3. **Install Flask**:
   Install Flask within your virtual environment:
  ```bash
  pip install flask

4. **Run the API**:
  Run the application using Python:
  ```bash
  python3 main.py




