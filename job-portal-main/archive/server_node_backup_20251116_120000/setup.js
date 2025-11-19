#!/usr/bin/env node

/**
 * Job Portal - Automated Setup Script (Cross-platform)
 * Run with: node setup.js
 */

const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

const colors = {
  reset: '\x1b[0m',
  bright: '\x1b[1m',
  red: '\x1b[31m',
  green: '\x1b[32m',
  yellow: '\x1b[33m',
  blue: '\x1b[34m',
};

const log = {
  info: (msg) => console.log(`${colors.blue}[INFO]${colors.reset} ${msg}`),
  success: (msg) => console.log(`${colors.green}[OK]${colors.reset} ${msg}`),
  error: (msg) => console.log(`${colors.red}[ERROR]${colors.reset} ${msg}`),
  warning: (msg) => console.log(`${colors.yellow}[WARN]${colors.reset} ${msg}`),
  header: (msg) => console.log(`\n${colors.bright}${colors.blue}${msg}${colors.reset}\n`),
};

function checkNodeInstalled() {
  try {
    const version = execSync('node --version', { encoding: 'utf8' }).trim();
    log.success(`Node.js is installed: ${version}`);
    return true;
  } catch (error) {
    log.error('Node.js is not installed!');
    console.log('Please download and install from: https://nodejs.org/');
    process.exit(1);
  }
}

function installDependencies(folder, folderName) {
  const folderPath = path.join(process.cwd(), folder);
  const nodeModulesPath = path.join(folderPath, 'node_modules');

  console.log(`[STEP] Installing ${folderName} dependencies...`);

  if (fs.existsSync(nodeModulesPath)) {
    log.info(`${folderName} node_modules already exists, skipping...`);
    return true;
  }

  try {
    log.info(`Running: npm install in ${folderName}`);
    execSync('npm install', { cwd: folderPath, stdio: 'inherit' });
    log.success(`${folderName} dependencies installed`);
    return true;
  } catch (error) {
    log.error(`Failed to install ${folderName} dependencies!`);
    return false;
  }
}

function checkEnvFile() {
  const envPath = path.join(process.cwd(), 'Server', '.env');

  console.log('[STEP] Checking environment configuration...');

  if (!fs.existsSync(envPath)) {
    log.warning('Server/.env file not found!');
    log.info('A template .env file should have been created.');
    console.log(`${colors.yellow}[ACTION REQUIRED]${colors.reset} Please edit Server/.env with your credentials:`);
    console.log('  - MONGODB_URI: Your MongoDB connection string');
    console.log('  - CLOUDINARY_API_KEY: Your Cloudinary API key');
    console.log('  - CLOUDINARY_SECRET_KEY: Your Cloudinary secret key');
    console.log('  - CLOUDINARY_NAME: Your Cloudinary name');
    return false;
  } else {
    log.success('Server/.env file exists');
    return true;
  }
}

function printSummary() {
  console.log(`\n${colors.bright}========================================${colors.reset}`);
  console.log(`${colors.green}[OK] All dependencies installed successfully!${colors.reset}`);
  console.log(`${colors.bright}========================================${colors.reset}\n`);

  console.log(`${colors.bright}Next steps:${colors.reset}`);
  console.log(`  1. Update ${colors.bright}Server/.env${colors.reset} with your MongoDB and Cloudinary credentials`);
  console.log(`  2. Start Backend: ${colors.bright}cd Server && npm run dev${colors.reset}`);
  console.log(`  3. Start Frontend (new terminal): ${colors.bright}cd Client && npm run dev${colors.reset}`);
  console.log(`  4. Open browser: ${colors.bright}http://localhost:5173${colors.reset}\n`);

  console.log(`${colors.bright}Optional: Start both servers simultaneously${colors.reset}`);
  console.log(`  - On Windows: Run ${colors.bright}start-dev.bat${colors.reset}`);
  console.log(`  - On macOS/Linux: Run ${colors.bright}./start-dev.sh${colors.reset}\n`);

  console.log(`For more information, see ${colors.bright}README.md${colors.reset}`);
  console.log(`${colors.bright}========================================${colors.reset}\n`);
}

async function main() {
  log.header('JOB PORTAL - AUTOMATED SETUP SCRIPT');

  checkNodeInstalled();
  console.log('');

  if (!installDependencies('Server', 'Server')) {
    process.exit(1);
  }
  console.log('');

  if (!installDependencies('Client', 'Client')) {
    process.exit(1);
  }
  console.log('');

  checkEnvFile();
  console.log('');

  log.header('SETUP COMPLETE');
  printSummary();
}

main().catch((error) => {
  log.error('Setup failed!');
  console.error(error);
  process.exit(1);
});
