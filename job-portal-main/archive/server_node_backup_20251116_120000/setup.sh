#!/bin/bash

# Job Portal - Complete Setup Script for macOS/Linux
# This script will install all dependencies and prepare the project

echo ""
echo "========================================"
echo "  JOB PORTAL - AUTOMATED SETUP SCRIPT"
echo "========================================"
echo ""

# Check if Node.js is installed
if ! command -v node &> /dev/null
then
    echo "[ERROR] Node.js is not installed!"
    echo "Please download and install Node.js from: https://nodejs.org/"
    exit 1
fi

echo "[OK] Node.js is installed"
node --version
echo ""

# Navigate to Server and install dependencies
echo "[STEP 1/4] Installing Server dependencies..."
cd Server
if [ -d "node_modules" ]; then
    echo "[INFO] Server node_modules already exists, skipping..."
else
    echo "[INFO] Running: npm install"
    npm install
    if [ $? -ne 0 ]; then
        echo "[ERROR] Failed to install server dependencies!"
        exit 1
    fi
fi
echo "[OK] Server dependencies installed"
cd ..
echo ""

# Navigate to Client and install dependencies
echo "[STEP 2/4] Installing Client dependencies..."
cd Client
if [ -d "node_modules" ]; then
    echo "[INFO] Client node_modules already exists, skipping..."
else
    echo "[INFO] Running: npm install"
    npm install
    if [ $? -ne 0 ]; then
        echo "[ERROR] Failed to install client dependencies!"
        exit 1
    fi
fi
echo "[OK] Client dependencies installed"
cd ..
echo ""

# Check if .env file exists
echo "[STEP 3/4] Checking environment configuration..."
if [ ! -f "Server/.env" ]; then
    echo "[ERROR] Server/.env file not found!"
    echo "[INFO] A template .env file should have been created."
    echo "[ACTION REQUIRED] Please edit Server/.env with your credentials:"
    echo "  - MONGODB_URI: Your MongoDB connection string"
    echo "  - CLOUDINARY_API_KEY: Your Cloudinary API key"
    echo "  - CLOUDINARY_SECRET_KEY: Your Cloudinary secret key"
    echo "  - CLOUDINARY_NAME: Your Cloudinary name"
    echo ""
else
    echo "[OK] Server/.env file exists"
fi
echo ""

# Summary
echo "[STEP 4/4] Setup Summary"
echo "========================================"
echo "[OK] All dependencies installed successfully!"
echo ""
echo "Next steps:"
echo "  1. Update Server/.env with your MongoDB and Cloudinary credentials"
echo "  2. Start Backend: cd Server && npm run dev"
echo "  3. Start Frontend (in another terminal): cd Client && npm run dev"
echo "  4. Open browser: http://localhost:5173"
echo ""
echo "For more information, see README.md"
echo "========================================"
