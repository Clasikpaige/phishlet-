# Phishing Server (Educational Purpose Only)

This repository contains a simple phishing server for educational purposes. It simulates a phishing attack by capturing credentials from a fake login page.

## Disclaimer
**This project is for educational purposes only. Do not use this for any malicious activities. Unauthorized phishing attacks are illegal and unethical. Always obtain explicit permission before conducting any security tests.**

## Setup and Usage

### Prerequisites
- Python 3.x

### Installation

1. Clone the repository:
    ```
    git clone https://github.com/Clasikpaige/phishlet-.git
    cd phishlet-
    ```

2. Install the required packages:
    ```
    pip install -r requirements.txt
    ```

### Running the Server

1. Start the server:
    ```
    python server.py
    ```

2. Access the phishing page by navigating to `http://localhost:8080` in your web browser.

3. Enter any credentials to see them captured and printed in the console.

### Files

- `server.py`: The main server script that handles HTTP requests.
- `requirements.txt`: Lists the dependencies required for the project.
- `LICENSE`: The license for this project.
