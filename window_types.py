import tkinter as tk
from tkinter import ttk
from tkinter import Button
from PIL import Image, ImageTk
import sys
from pathlib import Path
import windows_visuals as vis
import buttons as butt
import objects as obj

def open_players_window():

    window = tk.Tk()
    window.attributes('-fullscreen', True)
    screen_height = window.winfo_screenheight()
    screen_width = window.winfo_screenwidth()
    window.geometry(f"{screen_width}x{screen_height}")  # Full screen

    # Top section with instructions
    top_frame = tk.Frame(window, height=screen_height // 5)
    top_frame.pack(side=tk.TOP, fill=tk.X)
    top_frame.pack_propagate(False)  # Prevents frame from shrinking to fit its contents
    instructions = tk.Label(top_frame, text="Ονόματα αρχηγών και ομάδων:", font=("Helvetica", 76))
    instructions.pack()

    # Left side for Leader 1 and Team 1
    left_side = tk.Frame(window, width=screen_width // 2, height=screen_height * 4 // 5)
    left_side.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    left_side.grid_propagate(False)  # Prevents frame from shrinking

    tk.Label(left_side, text="Αρχηγός 1:", font=("Helvetica", 14)).grid(row=0, column=0, padx=20, pady=(20, 10))
    leader1_entry = tk.Entry(left_side)
    leader1_entry.grid(row=0, column=1, padx=10, pady=(20, 10))

    tk.Label(left_side, text="Ομάδα 1:", font=("Helvetica", 14)).grid(row=1, column=0, padx=20, pady=10)
    team1_entry = tk.Entry(left_side)
    team1_entry.grid(row=1, column=1, padx=10, pady=10)

    # Right side for Leader 2 and Team 2
    right_side = tk.Frame(window, width=screen_width // 2, height=screen_height * 4 // 5)
    right_side.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
    right_side.grid_propagate(False)
    tk.Label(right_side, text="Αρχηγός 2:", font=("Helvetica", 14)).grid(row=0, column=0, padx=10, pady=(20, 10))
    leader2_entry = tk.Entry(right_side)
    leader2_entry.grid(row=0, column=1, padx=10, pady=(20, 10))
    tk.Label(right_side, text="Ομάδα 2:", font=("Helvetica", 14)).grid(row=1, column=0, padx=10, pady=10)
    team2_entry = tk.Entry(right_side)
    team2_entry.grid(row=1, column=1, padx=10, pady=10)

    # #Inserting names to teams and leaders
    # leader1 = obj.Player(name=leader1_entry.get(), isLeader=True)
    # leader2 = obj.Player(name=leader2_entry.get(), isLeader=True)

    # # Create team objects with the leaders
    # team1 = obj.Team(leader=leader1, players=[leader1], points=0)  # Assuming leader is part of the team
    # team2 = obj.Team(leader=leader2, players=[leader2], points=0)

    # # Assuming team names might be used differently as this example does not incorporate team names directly into Team class
    # team1_name = team1_entry.get()
    # team2_name = team2_entry.get()

    def create_leaders_and_teams():
        leader1 = obj.Player(name=leader1_entry.get(), isLeader=True)
        leader2 = obj.Player(name=leader2_entry.get(), isLeader=True)

        # Create team objects with the leaders
        team1 = obj.Team(leader=leader1, players=[leader1], points=0)  # Assuming leader is part of the team
        team2 = obj.Team(leader=leader2, players=[leader2], points=0)

        # Assuming team names might be used differently as this example does not incorporate team names directly into Team class
        team1_name = team1_entry.get()
        team2_name = team2_entry.get()

        print(f"Team 1 - Leader: {leader1.name}, Team Name: {team1_name}")
        print(f"Team 2 - Leader: {leader2.name}, Team Name: {team2_name}")

    # OK button to trigger the creation of leaders and teams
    ok_button = tk.Button(window, text="OK", font=("Helvetica", 16), command=create_leaders_and_teams)
    ok_button.grid(row=4, column=0, pady=20)

def open_main_menu():
    # Initialize window
    window = tk.Tk()
    window.attributes('-fullscreen', True)
    screen_height = window.winfo_screenheight()

    #########################
    #LEFT SCREEN SIDE, IMAGE#
    #########################

    # Adjust the image size based on the screen height
    photo = vis.adjust_image_to_screen("logo.png", screen_height)

    # Create a label to display the image, covering the left part of the screen
    image_label = tk.Label(window, image=photo)
    image_label.pack(side="left", fill="y")

    ###################
    #RIGHT SCREEN SIDE#
    ###################

    right_frame = tk.Frame(window)
    right_frame.pack(side="right", fill="both", expand=True)

    # Divide the right frame into three sections
    text_frame = tk.Frame(right_frame, height=screen_height//4)
    text_frame.pack(side="top", fill="x")
    button1_frame = tk.Frame(right_frame, height=screen_height//4)
    button1_frame.pack(fill="x")
    button2_frame = tk.Frame(right_frame, height=screen_height//4)
    button2_frame.pack(fill="x")
    button3_frame = tk.Frame(right_frame, height=screen_height//4)
    button3_frame.pack(fill="x")

    #Game title
    text_label = tk.Label(text_frame, text="QuizPaul", font=("Helvetica", 76, "bold"))
    text_label.pack(expand=True)

    #Buttons
    butt.play_now = tk.Button(button1_frame, text="Νέο παιχνίδι", font=("Helvetica", 20), command=butt.play_now)
    butt.play_now.pack(fill="both", expand=True)
    butt.create_question = tk.Button(button2_frame, text="Προσθήκη ερώτησης", font=("Helvetica", 20), command=lambda: print("Button 2 clicked"))
    butt.create_question.pack(fill="both", expand=True)
    button3 = tk.Button(button3_frame, text="Έξοδος", font=("Helvetica", 20), command=window.destroy)
    button3.pack(fill="both", expand=True)

    window.mainloop()