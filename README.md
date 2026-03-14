![Python](https://img.shields.io/badge/Python-3.10-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Framework-green)
![MongoDB](https://img.shields.io/badge/MongoDB-Database-brightgreen)
![License](https://img.shields.io/badge/License-MIT-orange)

# 🚀 Smart Campus Lost & Found System

A modern **full-stack web application** that helps students report lost and found items on campus and automatically detect possible matches.

Built with **FastAPI, MongoDB, and an animated frontend**, this system makes it easier to return lost belongings to their rightful owners.

---

# ✨ Features

🔎 Report lost items
📦 Report found items
🤖 Automatic matching of items based on name and location
💾 MongoDB database storage
⚡ Fast REST API using FastAPI
🎨 Modern animated UI with glowing hover effects
🖥 Simple and user-friendly interface

---

# 🧰 Tech Stack

## Backend

Python
FastAPI
Uvicorn

## Database

MongoDB

## Frontend

HTML
CSS
JavaScript

---

# 🏗 Project Architecture

User Interface (Frontend)
⬇
FastAPI Backend API
⬇
MongoDB Database
⬇
Matching Algorithm

The backend checks the database when a new found item is reported and detects possible matches with lost items.

---

# 📂 Project Structure

lost-found-system

backend
│ main.py
│ database.py
│ models.py
│ requirements.txt

frontend
│ index.html
│ style.css
│ script.js

---

# ⚙️ How to Run the Project

### 1️⃣ Clone the repository

git clone https://github.com/poorthi12/SMART-CAMPUS-LOST-AND-FOUND-SYSTEM.git

### 2️⃣ Navigate to backend

cd backend

### 3️⃣ Install dependencies

pip install -r requirements.txt

### 4️⃣ Run the backend server

uvicorn main:app --reload

### 5️⃣ Open the frontend

Open `index.html` in your browser.

---

# 🔍 How the Matching Works

1️⃣ User reports a **lost item**
2️⃣ Item is stored in MongoDB
3️⃣ Another user reports a **found item**
4️⃣ Backend compares **item name + location**
5️⃣ If a match exists → system shows the owner details

---

# 🚀 Future Improvements

📷 Image upload for items
📧 Email notifications when match found
📱 SMS alerts
🗺 Map-based item location
🧠 AI image recognition for item matching
📊 Admin dashboard

---

# 👨‍💻 Authors

**POORNA DINESH H D**
**MANISH KUMAR**

---

# ⭐ If you like this project

Give it a ⭐ on GitHub!
