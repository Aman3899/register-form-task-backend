# Flask + Pandas Backend API

> A lightweight REST API built with Flask and Pandas for collecting and storing form submissions in CSV format.

[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/flask-2.0+-green.svg)](https://flask.palletsprojects.com/)
[![Pandas](https://img.shields.io/badge/pandas-1.3+-orange.svg)](https://pandas.pydata.org/)
[![Deployment](https://img.shields.io/badge/deployed-PythonAnywhere-success.svg)](https://amanullah1.pythonanywhere.com/)

---

## 🎯 Overview

This backend service provides a simple yet robust API endpoint for collecting form submissions from frontend applications. It leverages Flask for the web framework and Pandas for efficient CSV data management.

### Key Features

✅ **RESTful API** - Single endpoint for form submissions  
✅ **CSV Storage** - Persistent data storage using Pandas DataFrames  
✅ **CORS Enabled** - Cross-origin requests supported  
✅ **Input Validation** - Server-side validation for all fields  
✅ **Error Handling** - Comprehensive error responses  
✅ **Production Ready** - Deployed on PythonAnywhere  

### Tech Stack

| Technology | Purpose | Version |
|------------|---------|---------|
| Python | Backend Language | 3.8+ |
| Flask | Web Framework | 2.0+ |
| Pandas | Data Management | 1.3+ |
| Flask-CORS | Cross-Origin Support | 3.0+ |
| PythonAnywhere | Hosting Platform | - |

---

## 🌐 Live Deployment

**Production API URL:**
```
https://amanullah1.pythonanywhere.com/submit
```

**Status:** 🟢 Active  
**Uptime:** Monitored via PythonAnywhere  
**Response Time:** < 500ms average

### Quick Test

```bash
curl -X POST https://amanullah1.pythonanywhere.com/submit \
  -H "Content-Type: application/json" \
  -d '{"name":"Test User","email":"test@example.com","age":23}'
```

**Expected Response:**
```json
{
  "success": true,
  "row_index": 42,
  "age": 33
}
```

---

## 🏗️ Architecture

### System Flow Diagram

```
┌─────────────┐         ┌──────────────┐         ┌─────────────┐
│   Frontend  │ ──POST─→│  Flask API   │ ──CSV─→ │ submissions │
│  (Lovable)  │         │  /submit     │         │   .csv      │
└─────────────┘         └──────────────┘         └─────────────┘
      │                        │                        │
      │                        ├─ Validation           │
      │                        ├─ Pandas DataFrame     │
      └────── JSON Response ───┴─ Append to CSV ──────┘
```

<img src="https://github.com/Aman3899/register-form-task-backend/blob/main/Architecture%20of%20whole%20backend.png?raw=true" alt="LeetCode Stats">

### Component Breakdown

```
project-root/
│
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── submissions.csv        # Data storage (auto-created)
├── mindmap.svg           # Visual architecture diagram
├── README.md             # This file
└── .gitignore            # Git ignore rules
```

### Mind Map

A visual representation of the system architecture is available in this repository:

📊 **[View Mind Map](./)**

The mind map illustrates:
- Data flow from frontend to backend
- API endpoint structure
- Request/response cycle
- Error handling paths
- Storage mechanism

---

## 📡 API Documentation

### Endpoint: `POST /submit`

Accepts form submissions and stores them in a CSV file.

#### Request Format

**URL:** `https://amanullah1.pythonanywhere.com/submit`  
**Method:** `POST`  
**Content-Type:** `application/json` or `application/x-www-form-urlencoded`

#### Request Body (JSON)

```json
{
  "name": "John Doe",
  "email": "john.doe@example.com",
  "age": 44
}
```

#### Request Body (Form-Encoded)

```
name=John+Doe&email=john.doe@example.com&age=28
```

#### Field Specifications

| Field | Type | Required | Max Length | Validation |
|-------|------|----------|------------|------------|
| `name` | string | ✅ Yes | 100 chars | Non-empty |
| `email` | string | ✅ Yes | 150 chars | Email format |
| `age` | number | ❌ No | 1000 chars | Any number |

#### Response Formats

##### Success Response (200 OK)

```json
{
  "success": true,
  "row_index": 15,
  "age": 44
}
```

| Field | Type | Description |
|-------|------|-------------|
| `success` | boolean | Always `true` for successful requests |
| `row_index` | integer | The row number in the CSV file |
| `age` | number | Age |

##### Validation Error (400 Bad Request)

```json
{
  "success": false,
  "error": "Missing field: email"
}
```

**Common Validation Errors:**
- `"Missing field: name"`
- `"Missing field: email"`
- `"Invalid email format"`
- `"Name cannot be empty"`

##### Server Error (500 Internal Server Error)

```json
{
  "success": false,
  "error": "Internal error saving submission"
}
```

**Possible Causes:**
- CSV file permission issues
- Disk space full
- Pandas DataFrame operation failure
- File system errors

#### HTTP Status Codes

| Code | Meaning | Description |
|------|---------|-------------|
| 200 | OK | Submission saved successfully |
| 400 | Bad Request | Validation error or missing fields |
| 405 | Method Not Allowed | Non-POST request to /submit |
| 500 | Internal Server Error | Server-side error occurred |

---

## 💾 Data Storage

### CSV File Structure

**Filename:** `submissions.csv`  
**Location:** Same directory as `app.py`  
**Format:** UTF-8 encoded CSV

#### Schema

```csv
name,email,age
John Doe,john@example.com,44
Jane Smith,jane@example.com,22
```

| Column | Data Type | Description | Example |
|--------|-----------|-------------|---------|
| `name` | string | User's full name | "John Doe" |
| `email` | string | User's email address | "john@example.com" |
| `age` | number | User's age | 22 |

### Data Persistence

- **Auto-Creation:** If `submissions.csv` doesn't exist, it's created automatically on first submission
- **Append Mode:** New submissions are appended without overwriting existing data
- **No Duplicates Check:** System allows duplicate entries (by design)
- **Backup:** Recommended to backup CSV file regularly

### Storage Limitations

⚠️ **Important Considerations:**

1. **Concurrency:** CSV file access is not thread-safe. For high-traffic applications, consider:
   - File locking mechanisms
   - Migrating to SQLite/PostgreSQL
   - Using a queue system

2. **File Size:** CSV grows indefinitely. Monitor file size and implement:
   - Regular archiving
   - Log rotation
   - Database migration for large datasets (1000+ rows)

3. **Data Integrity:** No ACID guarantees. For production use cases requiring data consistency, upgrade to a proper database.

---

## 💻 Local Development

### Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.8 or higher** ([Download](https://www.python.org/downloads/))
- **pip** (comes with Python)
- **virtualenv** (recommended): `pip install virtualenv`
- **Git** (for cloning repository)

### Installation Steps

#### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/backend-flask-pandas.git
cd backend-flask-pandas
```

#### 2. Create Virtual Environment

**On Windows (PowerShell):**
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**On Windows (Command Prompt):**
```cmd
python -m venv .venv
.venv\Scripts\activate.bat
```

**On macOS/Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

#### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

**`requirements.txt` contents:**
```
Flask==2.3.0
pandas==2.0.0
flask-cors==4.0.0
Werkzeug==2.3.0
```

#### 4. Verify Installation

```bash
python -c "import flask, pandas; print('✅ All dependencies installed')"
```

### Running the Application

#### Method 1: Direct Python Execution

```bash
python app.py
```

#### Method 2: Flask CLI

**On Windows (PowerShell):**
```powershell
$env:FLASK_APP = "app.py"
$env:FLASK_ENV = "development"
flask run --host=0.0.0.0 --port=5000
```

**On macOS/Linux:**
```bash
export FLASK_APP=app.py
export FLASK_ENV=development
flask run --host=0.0.0.0 --port=5000
```

#### Expected Output

```
 * Serving Flask app 'app.py'
 * Debug mode: on
 * Running on http://127.0.0.1:5000
 * Running on http://192.168.1.100:5000
Press CTRL+C to quit
```

### Development Configuration

#### Enable Debug Mode

In `app.py`:
```python
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
```

#### Configure CORS Origins

For development, allow all origins:
```python
from flask_cors import CORS

CORS(app)  # Allow all origins
```

For production, specify allowed origins:
```python
CORS(app, origins=["https://yourfrontend.com"])
```

---

## 🚀 Deployment Guide

### PythonAnywhere Deployment

#### Step 1: Create PythonAnywhere Account

1. Go to [PythonAnywhere.com](https://www.pythonanywhere.com/)
2. Sign up for a free account
3. Verify your email

#### Step 2: Upload Code

**Option A: Using Git**
```bash
# In PythonAnywhere Bash console
git clone https://github.com/yourusername/backend-flask-pandas.git
cd backend-flask-pandas
```

**Option B: Using File Upload**
1. Go to **Files** tab
2. Upload `app.py`, `requirements.txt`
3. Create `submissions.csv` (empty file)

#### Step 3: Setup Virtual Environment

```bash
# Create virtualenv
mkvirtualenv --python=/usr/bin/python3.10 vide-backend

# Activate virtualenv
workon vide-backend

# Install dependencies
cd ~/backend-flask-pandas
pip install -r requirements.txt
```

#### Step 4: Configure Web App

1. Go to **Web** tab
2. Click **Add a new web app**
3. Choose **Manual configuration**
4. Select **Python 3.10**
5. Click through the wizard

#### Step 5: Edit WSGI Configuration

Click on **WSGI configuration file** link and replace contents:

```python
import sys
import os

# Add your project directory to the sys.path
project_home = '/home/amanullah1/backend-flask-pandas'
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# Set environment variables if needed
os.environ['FLASK_ENV'] = 'production'

# Import the Flask app
from app import app as application
```

#### Step 6: Set Virtual Environment Path

In the **Web** tab, under **Virtualenv** section:
```
/home/amanullah1/.virtualenvs/vide-backend
```

#### Step 7: Configure Static Files (Optional)

If you have static files:
- URL: `/static/`
- Directory: `/home/amanullah1/backend-flask-pandas/static/`

#### Step 8: Reload Web App

Click the **Reload** button (big green button)

#### Step 9: Test Deployment

```bash
curl -X POST https://amanullah1.pythonanywhere.com/submit \
  -H "Content-Type: application/json" \
  -d '{"name":"Deploy Test","email":"test@deploy.com","age":33}'
```

### File Permissions

Ensure CSV file is writable:
```bash
chmod 664 ~/backend-flask-pandas/submissions.csv
```

### Monitoring Logs

**Error Log:** Check for Python exceptions
```
Web tab → Log files → Error log
```

**Server Log:** Check for HTTP requests
```
Web tab → Log files → Server log
```

**Access Log:** Check for all requests
```
Web tab → Log files → Access log
```

### Custom Domain (Optional)

#### Using Cloudflare

1. **Add CNAME Record:**
   - Name: `api` (or your subdomain)
   - Target: `amanullah1.pythonanywhere.com`
   - Proxy: ✅ Enabled (orange cloud)

2. **SSL/TLS Settings:**
   - Mode: **Full** or **Full (Strict)**
   - Edge Certificates: Ensure **Always Use HTTPS** is ON

3. **PythonAnywhere Configuration:**
   - Go to **Web** tab
   - Add your custom domain in **CNAME setup** section
   - Wait for DNS propagation (5-30 minutes)

---

## 🔌 Frontend Integration

### JavaScript (Fetch API)

```javascript
async function submitForm(formData) {
  try {
    const response = await fetch('https://amanullah1.pythonanywhere.com/submit', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        name: formData.name,
        email: formData.email,
        age: formData.age
      })
    });

    const result = await response.json();

    if (result.success) {
      console.log('✅ Submission successful!', result);
      alert('Thank you! Your submission has been received.');
    } else {
      console.error('❌ Submission failed:', result.error);
      alert(`Error: ${result.error}`);
    }
  } catch (error) {
    console.error('❌ Network error:', error);
    alert('Network error. Please try again.');
  }
}

// Usage
const formData = {
  name: 'John Doe',
  email: 'john@example.com',
  age: 22
};

submitForm(formData);
```

### JavaScript (Axios)

```javascript
import axios from 'axios';

const API_URL = 'https://amanullah1.pythonanywhere.com/submit';

async function submitForm(formData) {
  try {
    const response = await axios.post(API_URL, formData, {
      headers: {
        'Content-Type': 'application/json'
      }
    });

    if (response.data.success) {
      console.log('✅ Success:', response.data);
      return { success: true, data: response.data };
    }
  } catch (error) {
    console.error('❌ Error:', error.response?.data || error.message);
    return { 
      success: false, 
      error: error.response?.data?.error || 'Network error' 
    };
  }
}
```

### React Example

```jsx
import React, { useState } from 'react';

function ContactForm() {
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    age: ''
  });
  const [status, setStatus] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    setStatus('Submitting...');

    try {
      const response = await fetch('https://amanullah1.pythonanywhere.com/submit', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(formData)
      });

      const result = await response.json();

      if (result.success) {
        setStatus('✅ Submission successful!');
        setFormData({ name: '', email: '', age: '' }); // Reset form
      } else {
        setStatus(`❌ Error: ${result.error}`);
      }
    } catch (error) {
      setStatus('❌ Network error. Please try again.');
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        placeholder="Name"
        value={formData.name}
        onChange={(e) => setFormData({...formData, name: e.target.value})}
        required
      />
      <input
        type="email"
        placeholder="Email"
        value={formData.email}
        onChange={(e) => setFormData({...formData, email: e.target.value})}
        required
      />
      <textarea
        placeholder="Age"
        value={formData.age}
        onChange={(e) => setFormData({...formData, age: e.target.value})}
      />
      <button type="submit">Submit</button>
      {status && <p>{status}</p>}
    </form>
  );
}
```

### HTML Form (No JavaScript)

```html
<form action="https://amanullah1.pythonanywhere.com/submit" method="POST">
  <input type="text" name="name" placeholder="Name" required>
  <input type="email" name="email" placeholder="Email" required>
  <input name="number" placeholder="number"></input>
  <button type="submit">Submit</button>
</form>
```

**Note:** Direct form submission (no JavaScript) will redirect to a JSON response page. Use JavaScript for better UX.

---

## ⚙️ Configuration

### Environment Variables

Create a `.env` file (optional, for advanced configuration):

```bash
FLASK_APP=app.py
FLASK_ENV=production
SECRET_KEY=your-secret-key-here
CSV_FILE_PATH=submissions.csv
MAX_MESSAGE_LENGTH=1000
ALLOWED_ORIGINS=https://yourfrontend.com,https://www.yourfrontend.com
```

### Loading Environment Variables

Install `python-dotenv`:
```bash
pip install python-dotenv
```

In `app.py`:
```python
from dotenv import load_dotenv
import os

load_dotenv()

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'default-secret-key')
CSV_PATH = os.getenv('CSV_FILE_PATH', 'submissions.csv')
```

### CORS Configuration

**Allow Specific Origins:**
```python
from flask_cors import CORS

CORS(app, resources={
    r"/submit": {
        "origins": ["https://yourfrontend.com", "http://localhost:3000"],
        "methods": ["POST"],
        "allow_headers": ["Content-Type"]
    }
})
```

**Allow All Origins (Development Only):**
```python
CORS(app)
```

### Rate Limiting (Optional)

Install Flask-Limiter:
```bash
pip install Flask-Limiter
```

Configure in `app.py`:
```python
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

limiter = Limiter(
    app=app,
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"]
)

@app.route('/submit', methods=['POST'])
@limiter.limit("10 per minute")
def submit():
    # Your code here
    pass
```

---

## 🧪 Testing

### Manual Testing

#### Test Success Case

```bash
curl -X POST http://localhost:5000/submit \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Test User",
    "email": "test@example.com",
    "age": 22
  }'
```

**Expected:** `{"success": true, "row_index": X, "age": 22}`

#### Test Missing Name

```bash
curl -X POST http://localhost:5000/submit \
  -H "Content-Type: application/json" \
  -d '{
    "email": "test@example.com",
    "age": 91
  }'
```

**Expected:** `{"success": false, "error": "Missing field: name"}`

#### Test Invalid Email

```bash
curl -X POST http://localhost:5000/submit \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Test User",
    "email": "invalid-email",
    "age": 26
  }'
```

**Expected:** `{"success": false, "error": "Invalid email format"}`

#### Test Form-Encoded Data

```bash
curl -X POST http://localhost:5000/submit \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "name=Test User&email=test@example.com&age=Form encoded test"
```

**Expected:** `{"success": true, ...}`

### Automated Testing (pytest)

Install pytest:
```bash
pip install pytest pytest-flask
```

Create `test_app.py`:
```python
import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_submit_success(client):
    response = client.post('/submit', json={
        'name': 'Test User',
        'email': 'test@example.com',
        'age': 22
    })
    assert response.status_code == 200
    assert response.json['success'] == True

def test_submit_missing_name(client):
    response = client.post('/submit', json={
        'email': 'test@example.com',
        'age': 22
    })
    assert response.status_code == 400
    assert 'error' in response.json

def test_submit_invalid_email(client):
    response = client.post('/submit', json={
        'name': 'Test',
        'email': 'invalid',
        'age': 21
    })
    assert response.status_code == 400
```

Run tests:
```bash
pytest test_app.py -v
```

### Load Testing (Optional)

Install Locust:
```bash
pip install locust
```

Create `locustfile.py`:
```python
from locust import HttpUser, task, between

class SubmissionUser(HttpUser):
    wait_time = between(1, 3)

    @task
    def submit_form(self):
        self.client.post("/submit", json={
            "name": "Load Test User",
            "email": "loadtest@example.com",
            "age": 23
        })
```

Run load test:
```bash
locust -f locustfile.py --host=http://localhost:5000
```

---

## 🔧 Troubleshooting

### Common Issues & Solutions

#### Issue 1: CORS Error in Browser

**Symptom:**
```
Access to fetch at 'https://amanullah1.pythonanywhere.com/submit' from origin 'https://yourfrontend.com' has been blocked by CORS policy
```

**Solution:**
1. Install flask-cors: `pip install flask-cors`
2. Enable CORS in `app.py`:
   ```python
   from flask_cors import CORS
   CORS(app)
   ```
3. Redeploy application

#### Issue 2: 500 Internal Server Error

**Symptom:**
```json
{"success": false, "error": "Internal error saving submission"}
```

**Debug Steps:**
1. Check PythonAnywhere error log (Web tab → Error log)
2. Verify CSV file exists and is writable:
   ```bash
   ls -la submissions.csv
   chmod 664 submissions.csv
   ```
3. Check disk space: `df -h`
4. Test Pandas operations:
   ```python
   import pandas as pd
   df = pd.DataFrame([{'name': 'test', 'email': 'test@test.com', 'age': 21}])
   df.to_csv('test.csv', index=False)
   ```

#### Issue 3: Missing CSV File

**Symptom:**
Error on first submission: `FileNotFoundError: submissions.csv`

**Solution:**
Add auto-creation logic in `app.py`:
```python
import os

CSV_FILE = 'submissions.csv'

# Create CSV if it doesn't exist
if not os.path.exists(CSV_FILE):
    df = pd.DataFrame(columns=['name', 'email', 'age'])
    df.to_csv(CSV_FILE, index=False)
```

#### Issue 4: Duplicate Rows

**Symptom:**
Multiple identical rows in CSV

**Cause:**
User clicking submit button multiple times

**Solution:**
Add client-side button disabling:
```javascript
const button = document.querySelector('button[type="submit"]');
button.disabled = true;
// ... make request ...
button.disabled = false;
```

#### Issue 5: CSV File Corrupted

**Symptom:**
```
ParserError: Error tokenizing data
```

**Solution:**
1. Backup current CSV: `cp submissions.csv submissions_backup.csv`
2. Try to read and fix:
   ```python
   df = pd.read_csv('submissions.csv', error_bad_lines=False)
   df.to_csv('submissions_fixed.csv', index=False)
   ```
3. Restore from backup if needed

#### Issue 6: PythonAnywhere Web App Not Starting

**Symptom:**
"Something went wrong" error page

**Debug Steps:**
1. Check error log for Python exceptions
2. Verify WSGI configuration points to correct file
3. Confirm virtualenv path is correct
4. Test import manually:
   ```bash
   workon vide-backend
   python -c "from app import app; print('OK')"
   ```
5. Check file permissions: `ls -la app.py`

#### Issue 7: Slow Response Times

**Symptom:**
API responses take > 2 seconds

**Solutions:**
1. **Optimize CSV Operations:**
   ```python
   # Bad: Reading entire CSV on each append
   df_existing = pd.read_csv(CSV_FILE)
   df_new = pd.concat([df_existing, new_row])
   
   # Good: Append mode without reading
   new_row.to_csv(CSV_FILE, mode='a', header=False, index=False)
   ```

2. **Add Caching** (if read operations exist)
3. **Consider Database Migration** for large datasets (1000+ rows)

#### Issue 8: Email Validation Too Strict/Loose

**Symptom:**
Valid emails rejected or invalid emails accepted

**Solution:**
Use robust email validation:
```python
import re

def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None
```

### Getting Help

If you encounter issues not covered here:

1. **Check Logs:**
   - PythonAnywhere: Web tab → Log files
   - Local: Terminal output

2. **Search Issues:**
   - GitHub Issues: [Your repo]/issues
   - Stack Overflow: [flask] [pandas] [pythonanywhere]

3. **Contact Support:**
   - PythonAnywhere Forums: https://www.pythonanywhere.com/forums/
   - Create GitHub Issue with:
     - Error message
     - Steps to reproduce
     - Relevant log snippets


---
