#!/bin/bash

# Job Portal - Start Development Servers (macOS/Linux)
# This script starts both backend and frontend servers

echo ""
echo "========================================"
echo "  JOB PORTAL - START DEVELOPMENT"
echo "========================================"
echo ""
echo "Starting Backend Server on port 8000..."
echo "Starting Frontend Server on port 5173..."
echo ""
echo "Press Ctrl+C to stop all servers"
echo ""

# Start backend
cd Server
npm run dev &
BACKEND_PID=$!

# Wait for backend to start
sleep 3

# Start frontend
cd ../Client
npm run dev &
FRONTEND_PID=$!

echo ""
echo "[OK] Both servers are starting..."
echo "[INFO] Frontend: http://localhost:5173"
echo "[INFO] Backend: http://localhost:8000"
echo ""
echo "Open your browser and navigate to: http://localhost:5173"
echo ""

# Wait for both processes
wait $BACKEND_PID $FRONTEND_PID

# Cleanup on exit
trap "kill $BACKEND_PID $FRONTEND_PID 2>/dev/null" EXIT
