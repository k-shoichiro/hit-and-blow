import customtkinter as ctk
from settings import run_settings
from ui import GameUI


def start_game(digits, rule):
    for widget in root.winfo_children():
        widget.destroy()

    root.title("HIT & BLOW")
    root.geometry("900x600")
    root.minsize(700, 450)

    app = GameUI(root, digits, rule)


if __name__ == "__main__":
    ctk.set_appearance_mode("light")

    root = ctk.CTk()

    run_settings(root, start_game)

    root.mainloop()