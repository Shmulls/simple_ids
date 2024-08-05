# Simple Intrusion Detection System (IDS)

This project demonstrates a basic Intrusion Detection System (IDS) that monitors network traffic for suspicious activities and generates alerts. The system captures network packets, analyzes them for potential threats, and displays real-time traffic statistics and alerts through a web interface.

## Setup Instructions
### Prerequisites
- Python 3.7+
- pip (Python package installer)

## Installation
1. Clone the repository or download the project files:
```bash
git clone <repository_url>
cd simple_ids
```
2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```
3. Install the required packages:
```bash
pip install -r requirements.txt
```
4. Run the Flask application:
```bash
python app.py
```
By default, the application will run on http://127.0.0.1:5001. If port 5001 is occupied, the Flask server can be started on a different port by modifying the app. Run line in app.py.

## Configuration
Ensure that the network interface specified in ids.py is correct for your environment:


```python
def start_sniffing(interface='en0'):  # Mac Users - en0 / Windows users - eth0
```

## Running the Application
1. Start the Flask server:

```bash
python app.py
```
- If its not working, try:
```bash
python3 app.py
```
2. Open a web browser and navigate to:
```bash
http://127.0.0.1:5001
```
You will see the Intrusion Detection System Dashboard displaying real-time traffic statistics and alerts.

## Autors
### Shmuel Malikov and Sharon Angado - Project for Software Security Course
