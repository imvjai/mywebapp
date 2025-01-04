🚀 Vijay Chaurasia's Professional Website 🚀
Welcome to the repository for Vijay Chaurasia's Professional Website! This project is built using Django, containerized with Docker, and deployed on AWS LightSail with Nginx as the reverse proxy. Below, you'll find all the details to set up, update, and maintain the website.

📋 Table of Contents
Prerequisites

Project Setup

Running the Application

Updating Web Pages

Running Migrations

Deployment

Troubleshooting

Contributing

🛠️ Prerequisites
Before you begin, ensure you have the following installed:

Docker 🐳: Install Docker

Docker Compose 🐙: Install Docker Compose

Git 📂: Install Git

Python 3.9+ 🐍: Install Python

AWS CLI (optional, for deployment): Install AWS CLI

🚀 Project Setup
1. Clone the Repository
bash
Copy
git clone https://github.com/imvjai/mywebapp.git
cd mywebapp
2. Set Up Environment Variables
Create a .env file in the root directory with the following variables:

plaintext
Copy
DATABASE_URL=postgres://postgres:postgres@db:5432/mywebapp_db
SECRET_KEY=your-secret-key-here
DEBUG=True  # Set to False in production
3. Build and Start the Containers
bash
Copy
docker-compose build
docker-compose up -d
🏃‍♂️ Running the Application
Once the containers are up and running, your website will be accessible at:

Local Development: http://localhost:8000

Production: https://imvijaychaurasia.com

✏️ Updating Web Pages
To update the content of your web pages:

Edit Templates:

The HTML templates are located in main_app/templates/.

For example, update index.html to modify the homepage.

Edit Static Files:

Static files (CSS, JS, images) are located in main_app/static/.

For example, update styles.css to change the styling.

Restart the Containers:
After making changes, restart the containers to apply them:

bash
Copy
docker-compose down
docker-compose up -d
🛠️ Running Migrations
When you make changes to your Django models, you need to run migrations:

Open a Shell in the web Container:

bash
Copy
docker-compose exec web bash
Create and Apply Migrations:

bash
Copy
python manage.py makemigrations
python manage.py migrate
🚀 Deployment
Deploying to AWS LightSail
SSH into Your LightSail Instance:

bash
Copy
ssh -i /path/to/your-key.pem ubuntu@your-instance-ip
Clone the Repository:

bash
Copy
git clone https://github.com/imvjai/mywebapp.git
cd mywebapp
Start the Containers:

bash
Copy
docker-compose up -d
Configure Nginx:

Update the Nginx configuration file (/etc/nginx/sites-available/default) to proxy requests to the Django container.

Restart Nginx:

bash
Copy
sudo systemctl restart nginx
Secure the Site with Let's Encrypt:

bash
Copy
sudo apt install certbot python3-certbot-nginx
sudo certbot --nginx -d imvijaychaurasia.com
🚨 Troubleshooting
Common Issues
Database Connection Errors:

Ensure the db container is running and the credentials in .env match those in docker-compose.yml.

Static Files Not Loading:

Ensure STATIC_URL and STATICFILES_DIRS are correctly configured in settings.py.

Run python manage.py collectstatic in production.

Nginx Errors:

Check Nginx logs for errors:

bash
Copy
docker-compose logs -f nginx
🤝 Contributing
Contributions are welcome! If you'd like to contribute:
