import customtkinter as ctk


class SettingsUI:
    def __init__(self, root, on_start):
        self.root = root
        self.on_start = on_start

        self.root.title("HIT & BLOW - SETTINGS")
        self.root.geometry("420x500")
        self.root.resizable(False, False)
        self.root.configure(fg_color="#F5F6F8")

        self.create_widgets()

    def create_widgets(self):
        ctk.CTkLabel(
            self.root,
            text="HIT & BLOW",
            font=("Zen Maru Gothic", 28, "bold"),
            text_color="#202938"
        ).pack(pady=(35, 5))

        ctk.CTkLabel(
            self.root,
            text="GAME SETTINGS",
            font=("Zen Maru Gothic", 13),
            text_color="#64748B"
        ).pack(pady=(0, 30))

        ctk.CTkLabel(
            self.root,
            text="桁数",
            font=("Zen Maru Gothic", 15, "bold"),
            text_color="#202938"
        ).pack(anchor="w", padx=40)

        self.digit_entry = ctk.CTkEntry(
            self.root,
            placeholder_text="桁数を入力（1〜10）",
            height=45,
            font=("Zen Maru Gothic", 14)
        )
        self.digit_entry.pack(fill="x", padx=40, pady=(8, 25))

        ctk.CTkLabel(
            self.root,
            text="数字の重複",
            font=("Zen Maru Gothic", 15, "bold"),
            text_color="#202938"
        ).pack(anchor="w", padx=40)

        self.rule_option = ctk.CTkOptionMenu(
            self.root,
            values=[
                "重複なし",
                "重複あり（処理1）",
                "重複あり（処理2）"
            ],
            height=45,
            font=("Zen Maru Gothic", 14)
        )
        self.rule_option.pack(fill="x", padx=40, pady=(8, 30))

        self.error_label = ctk.CTkLabel(
            self.root,
            text="",
            font=("Zen Maru Gothic", 12),
            text_color="#DC2626"
        )
        self.error_label.pack()

        ctk.CTkButton(
            self.root,
            text="GAME START",
            height=48,
            corner_radius=12,
            font=("Zen Maru Gothic", 15, "bold"),
            command=self.start_game
        ).pack(fill="x", padx=40, pady=10)

    def start_game(self):
        digit_text = self.digit_entry.get().strip()

        if not digit_text.isdigit():
            self.error_label.configure(
                text="桁数を数字で入力してください"
            )
            return

        digits = int(digit_text)

        if not 1 <= digits <= 10:
            self.error_label.configure(
                text="桁数は1〜10で指定してください"
            )
            return

        rule = self.rule_option.get()
        self.on_start(digits, rule)


def run_settings(root, on_start):
    return SettingsUI(root, on_start)