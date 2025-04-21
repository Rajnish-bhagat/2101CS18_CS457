# React Auth App with Supabase

This project is a React application with authentication and role-based access control using Supabase.

## Prerequisites

- Node.js (v18 or higher)
- npm (comes with Node.js)
- A Supabase project with the following environment variables:
  - `VITE_SUPABASE_URL`
  - `VITE_SUPABASE_ANON_KEY`

## Getting Started

1. Install dependencies:
```bash
npm install
```

2. Start the development server:
```bash
npm run dev
```

3. Open your browser and navigate to the local server URL.

## Features

- User authentication (login/register)
- Role-based access control (admin/user)
- Protected routes
- Admin panel
- User dashboard
- Secure profile management

## Available Routes

- `/` - Home/Login page
- `/register` - User registration
- `/login` - User login
- `/dashboard` - User dashboard (protected)
- `/admin` - Admin panel (protected, admin only)