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
