# Zelda64 Discord Presence

A Python program that automatically displays Discord Rich Presence when Zelda 64 Recompiled (Zelda64Recompiled.exe) is running.

This is a custom modification for personal use, based on the original work by [Inkflow59](https://github.com/Inkflow59).

## Features

- Automatically detects when Zelda64Recompiled.exe is running
- Displays "The Legend of Zelda: Majora's Mask" in Discord Rich Presence
- Runs silently in the system tray
- Clean quit option from system tray

## Credits & Acknowledgments
This project is a custom fork of the repository **[SoH-DiscordPresence](https://github.com/Inkflow59/SoH-DiscordPresence)** developed by **[Inkflow59](https://github.com/Inkflow59)**. All credits for the core logic, process monitoring loop, system tray integration, and compilation workflow go to the original author.

## Setup Instructions

### 1. Create a Discord Application (Optional)

The application is already configured with a Discord Application ID. If you want to use your own:

1. Go to https://discord.com/developers/applications
2. Click "New Application"
3. Name it "The Legend of Zelda: Ocarina of Time" or similar
4. Go to "Rich Presence" → "Art Assets" and upload an icon (optional - use `assets/logo.png`)
5. Copy your Application ID from the "General Information" tab
6. Open `main.py` and replace the `CLIENT_ID` value with your Application ID

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Program

```bash
python main.py
```

### 4. Build as EXE

```bash
build.bat
```

or manually:

```bash
pyinstaller --onefile --windowed --icon=assets\icon.ico --add-data "assets;assets" --name=SoHDiscordPresence main.py
```

The executable will be in the `dist` folder.

## Usage

1. Run Zelda64DiscordPresence.exe
2. The program will run in your system tray (look for the custom icon)
3. Launch Ship of Harkinian (Zelda64Recompiled.exe)
4. Discord Rich Presence will automatically activate
5. When you close Zelda64Recompiled.exe, the presence will be removed
6. Right-click the tray icon and select "Quit" to exit the program

## Notes

- Discord must be running for Rich Presence to work
- The program checks for Zelda64Recompiled.exe every 5 seconds
- You can customize the presence message in `main.py`
