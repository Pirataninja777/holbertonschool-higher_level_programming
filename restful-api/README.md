# HTTP vs HTTPS

## Differences Between HTTP and HTTPS

- **HTTP (Hypertext Transfer Protocol)** does not encrypt its data, making it vulnerable to eavesdropping and attacks.
- **HTTPS (Hypertext Transfer Protocol Secure)** adds a layer of encryption using SSL/TLS, making the data secure and unreadable to unauthorized users.
- Websites handling sensitive information, such as banking or email services, typically use **HTTPS** for security.

## Structure of an HTTP Request and Response

### HTTP Request Structure
A typical HTTP request consists of:
- **Method**: Specifies the action (e.g., GET, POST)
- **URL**: The resource being accessed
- **Headers**: Additional information (e.g., user-agent, authentication)
- **Body** (optional): Data sent to the server (used in POST, PUT)

Example:
```
GET /index.html HTTP/1.1
Host: www.example.com
User-Agent: Mozilla/5.0
```

### HTTP Response Structure
A typical HTTP response consists of:
- **Status Code**: Indicates the outcome (e.g., 200 OK, 404 Not Found)
- **Headers**: Additional metadata (e.g., content-type, server info)
- **Body** (optional): The actual content (HTML, JSON, etc.)

Example:
```
HTTP/1.1 200 OK
Content-Type: text/html
Content-Length: 1256

<html>...</html>
```

## Common HTTP Methods

| Method | Description | Use Case |
|--------|------------|----------|
| **GET** | Retrieves data from a server | Fetching a web page or API data |
| **POST** | Sends data to the server to create a resource | Submitting a form or uploading a file |
| **PUT** | Updates a resource or creates one if it does not exist | Updating user profile details |
| **DELETE** | Removes a resource from the server | Deleting a user account |

## Common HTTP Status Codes

| Status Code | Description | Scenario |
|------------|------------|----------|
| **200 OK** | Request was successful | A webpage loads correctly |
| **301 Moved Permanently** | The requested resource has been permanently moved | A website redirects to a new URL |
| **400 Bad Request** | The server cannot process the request due to client error | Sending an invalid JSON payload |
| **404 Not Found** | The requested resource could not be found | Accessing a non-existent webpage |
| **500 Internal Server Error** | A generic error on the server side | A web server crashes due to an issue |

---

### Additional Notes
- HTTP status codes are grouped by their first digit:
  - **1xx**: Informational
  - **2xx**: Success
  - **3xx**: Redirection
  - **4xx**: Client Errors
  - **5xx**: Server Errors
- Always prefer **HTTPS** over **HTTP** to ensure security, especially for handling sensitive user data.
