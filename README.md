# Invoice System

A simple invoice system built with Flask, storing data in-memory. This project includes Docker setup for easy deployment.

## Project Structure


## Requirements

- Python 3.9+
- Docker (optional for Docker setup)
- Docker Compose (optional for Docker Compose setup)

## Setup Instructions

### 1. Clone the repository

### ```bash
### git clone https://github.com/yourusername/invoice_system.git
### cd invoice_system

### python3 -m venv venv

### source venv/bin/activate

### python -m venv venv

### venv\Scripts\activate

### pip install -r requirements.txt

### python app.py

### docker build -t invoice_system .

### docker run -p 5000:5000 invoice_system

### docker-compose up --build

## API Endpoints
## Create an Invoice
## POST /invoices


{
    "date": "2023-08-01",
    "items": [
        {
            "name": "Item 1",
            "amount": 2,
            "cost": 10.0
        },
        {
            "name": "Item 2",
            "amount": 1,
            "cost": 20.0
        }
    ]
}


## Response:
{
    "message": "Invoice created!"
}

## GET /invoices

[
    {
        "id": 1,
        "date": "2023-08-01",
        "items": [
            {
                "name": "Item 1",
                "amount": 2,
                "cost": 10.0
            },
            {
                "name": "Item 2",
                "amount": 1,
                "cost": 20.0
            }
        ]
    }
]



### Saving the `README.md`

Create a file named `README.md` in the root of your project directory and copy the above content into it. This will provide a comprehensive guide for setting up and running the invoice system.


