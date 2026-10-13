import psutil
import time
import threading
from pypresence.presence import Presence
import pystray
from PIL import Image, ImageDraw
import sys
import os

CLIENT_ID = 1559658894165278890

class Zelda64DiscordPresence:
    def __init__(self):
        self.rpc = None
        self.is_connected = False
        self.is_running = True
        self.process_running = False
        self.game_start_time = None  # Almacena el tiempo para evitar reinicios constantes
        
    def create_image(self):
        """Load icon from assets folder"""
        icon_path = os.path.join(os.path.dirname(__file__), 'assets', 'icon.png')
        if os.path.exists(icon_path):
            return Image.open(icon_path)
        # Fallback to simple icon if file not found
        width = 64
        height = 64
        image = Image.new('RGB', (width, height), 'darkblue')
        dc = ImageDraw.Draw(image)
        dc.rectangle([width // 4, height // 4, width * 3 // 4, height * 3 // 4], fill='gold')
        return image
    
    def is_zelda64_running(self):
        """Check if Zelda64Recompiled.exe is currently running"""
        for proc in psutil.process_iter(['name']):
            try:
                if proc.info['name'] and proc.info['name'].lower() == 'zelda64recompiled.exe':
                    return True
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
        return False
    
    def connect_rpc(self):
        """Connect to Discord RPC"""
        try:
            if not self.rpc:
                self.rpc = Presence(CLIENT_ID)
            self.rpc.connect()
            self.is_connected = True
            print("Connected to Discord RPC")
        except Exception as e:
            print(f"Failed to connect to Discord RPC: {e}")
            self.is_connected = False
    
    def update_presence(self):
        """Update Discord Rich Presence for Zelda 64 Recompiled"""
        try:
            if self.rpc and self.is_connected:
                # CORREGIDO: Textos cambiados específicamente para Majora's Mask y Termina
                self.rpc.update(
                    state="Exploring Termina",
                    details="The Legend of Zelda: Majora's Mask",
                    large_image="logo",
                    large_text="Zelda 64: Recompiled",
                    start=self.game_start_time  # Mantiene el tiempo fluido sin reinicios
                )
                print("Discord presence updated")

        except Exception as e:
            print(f"Failed to update presence: {e}")
    
    def disconnect_rpc(self):
        """Disconnect from Discord RPC"""
        try:
            if self.rpc and self.is_connected:
                self.rpc.clear()  # Clear the presence first
                self.rpc.close()
                self.is_connected = False
                print("Disconnected from Discord RPC")
        except Exception as e:
            print(f"Error disconnecting: {e}")
    
    def monitor_process(self):
        """Monitor Zelda64Recompiled.exe and manage Discord RPC"""
        while self.is_running:
            zelda_running = self.is_zelda64_running()

            if zelda_running and not self.process_running:
                print("Zelda64Recompiled.exe detected! Connecting to Discord...")
                self.process_running = True
                self.game_start_time = int(time.time())  # Se fija el tiempo justo al arrancar el juego
                self.connect_rpc()

                if self.is_connected:
                    self.update_presence()

            elif not zelda_running and self.process_running:
                print("Zelda64Recompiled.exe closed. Disconnecting from Discord...")
                self.process_running = False
                self.game_start_time = None
                self.disconnect_rpc()

            time.sleep(5)  # Check every 5 seconds
    
    def on_quit(self, icon, item):
        """Handle quit action from system tray"""
        print("Quitting...")
        self.is_running = False
        self.disconnect_rpc()
        icon.stop()
        sys.exit(0)
    
    def run(self):
        """Start the monitoring thread and system tray icon"""
        # Start monitoring thread
        monitor_thread = threading.Thread(target=self.monitor_process, daemon=True)
        monitor_thread.start()
        
        # Create system tray icon
        icon = pystray.Icon(
            "Zelda 64 Recompiled Discord Presence",
            self.create_image(),
            "Zelda 64 Recompiled Discord Presence",
            menu=pystray.Menu(
                pystray.MenuItem("Quit", self.on_quit)
            )
        )
        
        print("Zelda 64 Recompiled Discord Presence is running in system tray...")
        icon.run()

if __name__ == "__main__":
    app = Zelda64DiscordPresence()
    app.run()
