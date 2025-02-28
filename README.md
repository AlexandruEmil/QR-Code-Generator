# QR-Code-Generator
 
This project is a Flask application that converts any URL into a QR code. The application is containerized with Docker, and the infrastructure is managed with Terraform and configured with Ansible. The build and deployment process is automated using Jenkins.

# Features
```
QR Code Generation: Converts any URL into a QR code.
Containerization: The application runs in a Docker container.
Infrastructure as Code: The infrastructure is created and managed with Terraform.
Automation: The build and deployment process is automated with Jenkins.
```
# How to Use
## Requirements
Python 3.9
```
Docker
Terraform
Ansible
Jenkins 
```
## Installation
Clone the repository:
```
bash
git clone https://github.com/username/qr-code-generator.git
cd qr-code-generator
```
## Build and run the application with Docker:
```
bash
cd app
docker build -t qr-code-generator .
docker run -d -p 5000:5000 qr-code-generator
```
## Access the application at:

`http://localhost:5000/generate-qr?url=<your-url>`
# Infrastructure with Terraform
## Navigate to the terraform directory:
```
bash
cd terraform
```
Initialize and apply the Terraform configuration:
```
bash
terraform init
terraform apply
```
# Configuration with Ansible
## Navigate to the ansible directory:
```
bash
cd ansible
```
## Run the Ansible playbook:
```
bash
ansible-playbook -i inventory playbook.yml
Automation with Jenkins
```
## Set up a Jenkins job using the Jenkinsfile.

Jenkins will automatically build and deploy the application.

# Project Structure
```
qr-code-generator/
├── app/                  # Flask application
│   ├── app.py            # Python code for QR generation
│   ├── requirements.txt  # Python dependencies
│   └── Dockerfile        # Dockerfile for containerization
├── terraform/            # Terraform configuration
│   └── main.tf           # Terraform file for AWS
├── ansible/              # Ansible playbooks
│   └── playbook.yml      # Server configuration
├── jenkins/              # Jenkins configuration
│   └── Jenkinsfile       # Jenkins pipeline
└── README.md             # Project documentation
```
# License
This project is licensed under the MIT License.

> [!NOTE]  
On `main.tf` you must make an IAM user to have an `acces_key` and `secret_key`
