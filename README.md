# 🚀 Secure Cloud Notes & AI Microservice

This project is a cloud-native microservice designed with "Clean Architecture" principles. It features AI-driven content categorization and robust security layers, developed using the FastAPI framework.

## 🛠 Tech Stack
* **Python & FastAPI**: Modern, high-performance web framework for building APIs.
* **Pydantic**: Data validation and settings management using Python type annotations.
* **Docker**: Containerization for consistent deployment across any environment.
* **AI Integration**: Rule-based natural language processing for automated tagging.

## ✨ Key Features

### 1. Clean Architecture
The codebase is logically structured into distinct layers: Data Models, AI Services, and API Endpoints. This separation ensures the application is scalable, maintainable, and easy to test.

### 2. AI-Driven Categorization
The microservice intelligently analyzes note content to suggest categories. 
* **Example**: If a note contains words like "bread" or "milk," the AI automatically assigns it to the **"Shopping"** category.

### 3. Security Basics
To protect against unauthorized access, the API is secured with a header-based **API Key** mechanism.
* **Header Key:** `x-api-key`
* **Secret Value:** `odev123`

### 4. Observability & Monitoring
Includes a built-in `/health` endpoint to monitor the system's status, ensuring the microservice is operational and healthy.

## 🚀 Getting Started

### Running with Docker:
```bash
# Build the image
docker build -t cloud-notes .

# Run the container
docker run -p 80:80 cloud-notes
