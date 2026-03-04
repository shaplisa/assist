sudo nano /etc/systemd/system/assistant.service

[Unit]
Description=OPI Core Application
After=network.target

[Service]
Type=simple
User=root
WorkingDirectory=/root/assist/
ExecStart=/root/assist/.venv/bin/python /root/assist/app/main.py
Restart=always
RestartSec=5
StandardOutput=journal
StandardError=journal

[Install]
WantedBy=multi-user.target
