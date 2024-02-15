import tkinter as tk
from tkinter import Button
from PIL import Image, ImageTk
import sys
from pathlib import Path

def adjust_image_to_screen(image_path, screen_height):
    image = Image.open(image_path)
    # Resize the image to have the height equal to the screen height
    # and width adjusted to maintain the aspect ratio
    #Image is square (heigh=width)

    # Check if the application is running as a PyInstaller bundle
    if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
        # If so, use the _MEIPASS directory to find the image
        base_path = Path(sys._MEIPASS)
    else:
        # Otherwise, use the directory of this script file
        base_path = Path(__file__).parent
    
    # Construct the full path to the image
    full_image_path = base_path / image_path
    
    # Continue with your existing code to open the image
    image = Image.open(str(full_image_path))
    resized_image = image.resize((screen_height, screen_height), Image.ANTIALIAS)
    return ImageTk.PhotoImage(resized_image)