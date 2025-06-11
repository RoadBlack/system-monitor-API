# System Monitor API

This project is a simple REST API built with FastAPI that provides basic system monitoring statistics such as CPU, RAM, and disk usage. It is designed as a DevSecOps portfolio project and is intended to be containerized with Docker and deployed to the cloud.

## Features
- Exposes endpoints to check system health and resource usage
- Built with FastAPI and Python
- Returns CPU, RAM, and disk usage statistics
- Ready for Dockerization and cloud deployment

## Endpoints
- `/` - Root endpoint with a welcome message
- `/stats` - Returns current CPU, RAM, and disk usage
- `/health` - Returns a simple health check status

## Getting Started

### Prerequisites
- Python 3.8+
- [pip](https://pip.pypa.io/en/stable/)
- [Docker](https://www.docker.com/) (for containerization)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/RoadBlack/system-monitor-api.git
   cd system-monitor-api
   ```
2. (Optional) Create and activate a virtual environment:
   ```bash
   python -m venv env
   source env/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running Locally
```bash
uvicorn main:app --reload
```

### Docker
1. Build the Docker image:
   ```bash
   docker build -t system-monitor-api .
   ```
2. Run the container:
   ```bash
   docker run -p 5000:5000 system-monitor-api
   ```

### Cloud Deployment
This project is ready to be deployed to any cloud provider supporting Docker containers (e.g. AWS, Azure, GCP).

## DevSecOps Focus
This project is part of a DevSecOps portfolio, demonstrating best practices in:
- Containerization
- Cloud deployment
- Secure API development
- Infrastructure as Code (IaC) (future)

## License
MIT
