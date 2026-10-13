@echo off
echo Building Zelda 64 Recompiled Discord Presence...
pyinstaller --onefile --windowed --icon=assets\icon.ico --add-data "assets;assets" --name=Zelda64DiscordPresence main.py
echo Build complete! Check the 'dist' folder for Zelda64DiscordPresence.exe
pause
