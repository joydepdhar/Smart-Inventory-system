# 📦 Smart Inventory Management System

A backend-focused, scalable **Inventory Management System** built with **Django REST Framework** and **React**.
This project is designed to handle real-world inventory operations with auditability, performance, and extensibility in mind.

---

## 🚀 Features

### Core Modules

* Product & Category Management
* Warehouse Management
* Stock Tracking (multi-warehouse)
* Purchase & Supplier Management
* Sales & Order Management
* Stock Movement History (audit trail)

### Smart Features

* Low stock detection
* Demand estimation (basic analytics)
* Auto reorder suggestions
* Dead stock identification

---

## 🧱 Tech Stack

### Backend

* Django
* Django REST Framework
* PostgreSQL (recommended)
* JWT Authentication

### Frontend

* React
* Axios / Fetch API

### Optional (Planned / Advanced)

* Redis (caching)
* Celery (background jobs)
* Docker (deployment)

---

## 📂 Project Structure

```
inventory_system/
├── users/
├── products/
├── inventory/
├── orders/
├── suppliers/
├── warehouse/
├── analytics/
├── common/
```

---

## 🧠 System Design Highlights

* **Stock Movements as Source of Truth**

  * All inventory changes are tracked via `StockMovement`
  * Ensures full audit history and traceability

* **Service Layer Architecture**

  * Business logic separated from views
  * Cleaner, scalable, and testable code

* **Normalized Database Design**

  * Avoids redundancy
  * Supports future SaaS expansion

---

## ⚙️ Installation

### 1. Clone the repository

```
git clone https://github.com/your-username/inventory-system.git
cd inventory-system
```

### 2. Create virtual environment

```
python -m venv venv
source venv/bin/activate  
venv\Scripts\activate
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file:

```
DEBUG=True
SECRET_KEY=your_secret_key
DB_NAME=inventory_db
DB_USER=postgres
DB_PASSWORD=your_password
```

### 5. Run migrations

```
python manage.py makemigrations
python manage.py migrate
```

### 6. Run server

```
python manage.py runserver
```

---

## 🔌 API Overview

### Products

* `GET /api/products/`
* `POST /api/products/`

### Inventory

* `GET /api/inventory/`
* `POST /api/inventory/move/`

### Orders

* `POST /api/orders/`
* `GET /api/orders/`

### Analytics

* `GET /api/analytics/low-stock/`

---

## 📊 Future Improvements

* Barcode scanning
* Multi-tenant SaaS architecture
* Advanced demand forecasting (ML)
* Role-based dashboards
* Real-time notifications

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome.

---

## 📄 License

This project is open-source and use it for educational purpose only not in business sector

---

## 👨‍💻 Author

Developed by **[Joydep Dhar & Teams]**
Backend-focused Full Stack Developer (Django + React)

---

