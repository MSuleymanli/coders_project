# Villa and House Sales Platform - Capstone Project

## Introduction

This project is the culmination of a transformative 16-week program where we, the 'Mavericks' team, applied hands-on experience with cutting-edge technologies to create a live platform for selling villas and houses. Our project stood out among 13 other teams, thanks to the seamless integration of modern tools and technologies, including international payment systems.

The platform was deployed live at [shop.mansur.az](https://shop.mansur.az) using Cloudflare technology, showcasing the real-world application of both development and deployment skills.

---

## Table of Contents

- [Technologies Used](#technologies-used)
- [Project Features](#project-features)
- [Installation](#installation)
- [Usage](#usage)
- [Deployment](#deployment)
- [Stripe Payment Integration](#stripe-payment-integration)
- [Project Link](#project-link)
- [Contributors](#contributors)
- [License](#license)

---

## Technologies Used

During this project, we gained hands-on experience in the following technologies:

- **Frontend:**
  - HTML5
  - CSS3
  - JavaScript
  - Figma (Design Tool)

- **Backend:**
  - Python
  - Django
  - Django REST Framework

- **Database & Deployment:**
  - SQL
  - Cloud Deployment (Cloudflare)

- **Payment Integration:**
  - Stripe API for international payments

---

## Project Features

- **User Authentication:** 
  Users can register and login to access personalized features and manage their property listings.

- **Property Listings:**
  - Sellers can add, edit, and manage their property listings (villas and houses).
  - Users can browse and search properties based on various filters.

- **Interactive UI:**
  - Designed using Figma for a seamless user experience.
  - Modern, responsive layout optimized for both desktop and mobile devices.

- **International Payment Integration:** 
  - Integrated Stripe to enable secure and seamless international transactions for property purchases.
  
- **Admin Dashboard:**
  - Admins can view and manage user accounts, property listings, and transactions.

---

## Installation

To get started with the project locally, follow these steps:

### Prerequisites
Make sure you have the following installed on your machine:
- Python 3.x
- Django 3.x or later
- PostgreSQL (or any SQL-based database)
- Node.js (for frontend dependencies)
  
### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/MSuleymanli/coders_project.git
   cd coders_project
   ```
2. Install backend dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up the database and run migrations:
   ```bash
   python manage.py migrate
   ```
4. Start the development server:
   ```bash
   python manage.py runserver
   ```
5. Open your browser and go to http://127.0.0.1:8000/ to see the app in act
   

<h3>Usage</h3>
Once the platform is running locally, you can:

Register as a user or login if you already have an account.
Browse property listings, filter by criteria, and view individual property details.
If you're a seller, you can add new properties or edit existing listings.
Make payments for property purchases through the integrated Stripe payment system.

<h3>Deployment</h3>
The project is deployed live at shop.mansur.az. We used Cloudflare for deployment, ensuring fast loading times, improved security, and better global access.

<h3>Stripe Payment Integration</h3>
To ensure a seamless transaction experience, we integrated Stripe as an international payment system. This allows users from various countries to purchase properties in a secure manner.

Key features of the Stripe integration:

Secure and real-time payment processing
Multi-currency support for international users
Easy-to-use API integration for payments
Support for both one-time and subscription-based payments

<h3>Project Link</h3>
You can find the full project code on GitHub here: https://github.com/MSuleymanli/coders_project

GitHub Repository - coders_project
