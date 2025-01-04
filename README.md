
# 🚀 **Vijay Chaurasia's Professional Website** 🚀

Welcome to the repository for **Vijay Chaurasia's Professional Website**!  
This project is built using **Django**, containerized with **Docker**, and deployed on **AWS LightSail** with **Nginx** as the reverse proxy.

---

## 📋 **Table of Contents**

1. [🛠️ Prerequisites](#-prerequisites)
2. [🚀 Project Setup](#-project-setup)
3. [🏃‍♂️ Running the Application](#-running-the-application)
4. [✏️ Updating Web Pages](#-updating-web-pages)
5. [🛠️ Running Migrations](#-running-migrations)
6. [🚀 Deployment](#-deployment)
7. [🚨 Troubleshooting](#-troubleshooting)
8. [🤝 Contributing](#-contributing)

---

## 🛠️ **Prerequisites**

Before you begin, ensure you have the following installed:

- **Docker** 🐳: [Install Docker](https://docs.docker.com/get-docker/)
- **Docker Compose** 🐙: [Install Docker Compose](https://docs.docker.com/compose/install/)
- **Git** 📂: [Install Git](https://git-scm.com/downloads)
- **Python 3.9+** 🐍: [Install Python](https://www.python.org/downloads/)
- **AWS CLI** (optional, for deployment): [Install AWS CLI](https://aws.amazon.com/cli/)

---

## 🚀 **Project Setup**

### 1. **Clone the Repository**

```bash
git clone https://github.com/imvjai/mywebapp.git
cd mywebapp
```

### 2. **Set Up Environment Variables**

Create a `.env` file in the root directory with the following variables:

```plaintext
DATABASE_URL=postgres://postgres:postgres@db:5432/mywebapp_db
SECRET_KEY=your-secret-key-here
DEBUG=True  # Set to False in production
```

### 3. **Build and Start the Containers**

```bash
docker-compose build
docker-compose up -d
```

---

## 🏃‍♂️ **Running the Application**

Once the containers are up and running, your website will be accessible at:

- **Local Development**: [http://localhost:8000](http://localhost:8000)  
- **Production**: [https://imvijaychaurasia.com](https://imvijaychaurasia.com)

---

## ✏️ **Updating Web Pages**

To update the content of your web pages:

1. **Edit Templates**  
   - HTML templates are located in `main_app/templates/`.  
   - Example: Update `index.html` to modify the homepage.

2. **Edit Static Files**  
   - Static files (CSS, JS, images) are located in `main_app/static/`.  
   - Example: Update `styles.css` to change the styling.

3. **Restart the Containers**  
   After making changes, restart the containers to apply them:

   ```bash
   docker-compose down
   docker-compose up -d
   ```

---

## 🛠️ **Running Migrations**

When you make changes to your Django models, you need to run migrations:

1. **Open a Shell in the `web` Container**  

   ```bash
   docker-compose exec web bash
   ```

2. **Create and Apply Migrations**  

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

---

## 🚀 **Deployment**

### Deploying to AWS LightSail

1. **SSH into Your LightSail Instance**  

   ```bash
   ssh -i /path/to/your-key.pem ubuntu@your-instance-ip
   ```

2. **Clone the Repository**  

   ```bash
   git clone https://github.com/imvjai/mywebapp.git
   cd mywebapp
   ```

3. **Start the Containers**  

   ```bash
   docker-compose up -d
   ```

4. **Secure the Site with Let's Encrypt**  

   ```bash
   sudo apt install certbot python3-certbot-nginx
   sudo certbot --nginx -d imvijaychaurasia.com -d imvijaychaurasia.in
   ```

---

## 🚨 **Troubleshooting**

### Common Issues

1. **Database Connection Errors**  
   - Ensure the `db` container is running and the credentials in `.env` match those in `docker-compose.yml`.

2. **Static Files Not Loading**  
   - Ensure `STATIC_URL` and `STATICFILES_DIRS` are correctly configured in `settings.py`.
   - Run `python manage.py collectstatic` in production.

3. **Nginx Errors**  
   - Check Nginx logs for errors:

     ```bash
     docker-compose logs -f nginx
     ```

---
