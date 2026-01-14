# qa-infrastructure-project
# 🏗️ Full-Stack Infrastructure & DB Automation Framework

This project demonstrates an advanced automated testing environment using **Docker**, **MySQL**, and **Python**. It goes beyond simple API testing by validating data persistence and infrastructure orchestration.

## 🌟 Project Highlights
* **Infrastructure as Code (IaC):** Entire test environment (Database + Test Runner) is orchestrated using Docker Compose.
* **Database Integration Testing:** Validates that data is correctly stored and retrieved from a MySQL production-grade database.
* **Containerized Execution:** Tests run in a dedicated Linux environment, ensuring consistency across different machines (eliminating the "it works on my machine" problem).

## 🛠️ Tech Stack
* **Orchestration:** Docker, Docker Compose
* **Database:** MySQL 8.0
* **Language:** Python 3.9
* **Testing:** Pytest
* **Libraries:** mysql-connector-python, python-dotenv