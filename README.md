# Calry_Task

# Task1 : Meeting Scheduler

## Overview
The **Meeting Scheduler** optimizes meeting room bookings by merging overlapping or consecutive time slots, ensuring efficient use of resources.

### Example:
- **Input:** `[[9, 12], [11, 13], [14, 17], [16, 18]]`
- **Output:** `[[9, 13], [14, 18]]`

## Features
- **Merge Overlaps:** Combines overlapping or consecutive bookings.
- **Efficient for Large Data:** Handles up to 1,000 bookings efficiently.

## How It Works
1. **Input:** User provides booking times (start and end).
2. **Optimization:** 
   - Bookings are sorted by start time.
   - Overlapping or consecutive bookings are merged.
3. **Output:** Optimized booking times are printed.

## Sample Input/Output

### Input:
```
Number of test cases: 1
Number of bookings: 4
9 12
11 13
14 17
16 18
```

### Output:
```
Optimized bookings: [9, 13] [14, 18]
``` 

This program efficiently manages meeting schedules by merging overlapping bookings, making it ideal for busy workspaces.




# Task2 : Hotel Room Service Request API (No Database, No Auth)

## Overview
This project is a RESTful API designed to manage hotel room service requests efficiently using JSON for temporary data storage. It allows hotel staff to prioritize service requests based on urgency and guest status without requiring a database or authentication.

## Features
- **Create, Update, Retrieve, and Delete Requests:** Manage room service requests through various API endpoints.
- **Sorting:** Requests are automatically sorted by priority (lower numbers indicate higher priority) and status.
- **JSON Data Storage:** Data is stored in a JSON file for temporary storage and manipulated using thread-safe file operations.
- **Mark as Completed:** Ability to mark requests as completed.

## Fields for Requests
Each service request contains the following fields:
- `id` (string): Unique identifier for the request.
- `guestName` (string): Name of the guest making the request.
- `roomNumber` (number): Room number of the guest.
- `requestDetails` (string): Details of the request.
- `priority` (number): Lower numbers indicate higher priority.
- `status` (string): One of `'received' | 'in progress' | 'awaiting confirmation' | 'completed' | 'canceled'`.

## API Endpoints

### POST /requests
Create a new service request.
- **Request Body:**
  ```json
  {
    "guestName": "John Doe",
    "roomNumber": 101,
    "requestDetails": "Extra towels",
    "priority": 1
  }
  ```
- **Response:** Newly created request with a unique ID.

### GET /requests
Retrieve all service requests, sorted by priority and status.

### GET /requests/{id}
Retrieve a specific request by its ID.

### PUT /requests/{id}
Update an existing request's details or priority.
- **Request Body (example):**
  ```json
  {
    "priority": 2,
    "status": "in progress"
  }
  ```

### DELETE /requests/{id}
Delete a specific request by its ID (e.g., after completion or cancellation).

### POST /requests/{id}/complete
Mark a request as completed.

## Sorting Logic
- **Primary Sort:** Requests are sorted by `priority` (lower values first).
- **Secondary Sort:** If priorities are the same, requests are sorted by `status` in the following order:
  - `received`
  - `in progress`
  - `awaiting confirmation`
  - `completed`
  - `canceled`

## Installation and Setup
1. Clone the repository.
2. Install the required dependencies:
   ```bash
   pip install Flask
   ```
3. Run the application:
   ```bash
   python app.py
   ```

## Testing
Test the API using tools like Postman or cURL by sending requests to the available endpoints.

Example using cURL to add a request:
```bash
curl -X POST http://127.0.0.1:5000/requests \
-H "Content-Type: application/json" \
-d '{"guestName": "John Doe", "roomNumber": 101, "requestDetails": "Extra towels", "priority": 1}'
```

