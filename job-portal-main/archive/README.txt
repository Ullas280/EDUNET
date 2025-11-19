Archived Node backend backup

Location: archive/server_node_backup_20251116_120000/

What was moved:
- The entire `Server/` folder (original Node/Express backend).
- Root helper scripts: `setup.bat`, `setup.sh`, `setup.js`, `start-dev.bat`, `start-dev.sh`.

Why:
- The project backend was migrated to Django + MySQL under `server_django/` as requested.

How to restore:
1. Copy the archived `Server/` folder back to the repository root.
2. Copy any helper scripts you need back to the repo root.
3. Run `npm install` inside `Server/` and `Client/` if needed.

Notes:
- The archive is a safety snapshot; files were removed from the repo root after archiving.
- If you want the archive removed permanently, tell me and I will delete it.
