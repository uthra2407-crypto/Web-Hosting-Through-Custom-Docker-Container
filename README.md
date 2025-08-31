# Web Hosting through Custom Docker Container

This project demonstrates a complete web hosting solution using custom Docker containers. It includes autoscaling, monitoring, and efficient resource management for hosting web applications with a backend, frontend, and NGINX proxy setup.

## Features

Custom Docker Containers for backend and frontend.

Autoscaling based on CPU usage with detailed logs.

Monitoring system for tracking container health and resource usage.

High CPU load simulation for testing scaling behavior.

Docker Compose setup for orchestrating multiple services.

Logging for scaling events (scaling_log.txt).

## Project Structure

autoscaler/ – Contains scripts and configuration for container autoscaling.

backend/ – Backend service code.

frontend/ – Frontend service code.

monitoring/ – Monitoring tools and scripts.

docker-compose.yml – Orchestration file for multi-container setup.

## Prerequisites

Docker (latest version recommended)

Docker Compose

Python 3.x (for high_cpu.py)

high_cpu.py – Script to simulate high CPU usage.

scaling_log.txt – Logs related to autoscaling events.

## Installation and Usage
1.Clone this repository:
```bash
git clone https://github.com/uthra2407-crypto/Web-Hosting-Through-Custom-Docker-Container.git
cd Web-Hosting-Through-Custom-Docker-Container
```
2.Start the services using Docker Compose:
```bash
docker-compose up --build -d
```
3.Access the frontend:
```bash
http://localhost:3000
```
4.Simulate high CPU usage (optional, for autoscaling test):
```bash
python3 high_cpu.py
```

