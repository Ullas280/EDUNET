@echo off
REM Job Portal - Start Development Servers (Windows)
REM This script starts both backend and frontend servers

echo.
echo ========================================
echo   JOB PORTAL - START DEVELOPMENT
echo ========================================
echo.
echo Starting Backend Server on port 8000...
echo Starting Frontend Server on port 5173...
echo.
echo NOTE: Close this window to stop both servers
echo.

REM Start backend in a new window
start "Job Portal - Backend" cmd /k "cd Server && npm run dev"

REM Wait a bit for backend to start
timeout /t 3 /nobreak

REM Start frontend in a new window
start "Job Portal - Frontend" cmd /k "cd Client && npm run dev"

echo.
echo [OK] Both servers are starting...
echo [INFO] Frontend: http://localhost:5173
echo [INFO] Backend: http://localhost:8000
echo.
echo Open your browser and navigate to: http://localhost:5173
pause
