import customtkinter as ctk


class GameUI:
    def __init__(self, root, digits=4, rule="重複なし"):
        self.root = root
        self.digits = digits
        self.rule = rule
          
        self.root.title("HIT & BLOW")
        self.root.geometry("900x600")
        self.root.minsize(700, 450)

        self.bg_color = "#F5F6F8"
        self.card_color = "#FFFFFF"
        self.text_color = "#202938"
        self.sub_text_color = "#64748B"
        self.accent_color = "#2563EB"
        self.font_family = "Zen Maru Gothic"

        self.root.configure(fg_color=self.bg_color)

        self.attempts = 0
        
        self.create_layout()

    def create_layout(self):
        self.main_frame = ctk.CTkFrame(
            self.root,
            fg_color="transparent"
        )
        self.main_frame.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

        self.main_frame.grid_columnconfigure(0, weight=2)
        self.main_frame.grid_columnconfigure(1, weight=3)
        self.main_frame.grid_rowconfigure(0, weight=1)

        # 左側：履歴パネル
        self.history_frame = ctk.CTkFrame(
            self.main_frame,
            fg_color=self.card_color,
            corner_radius=20
        )
        self.history_frame.grid(
            row=0, column=0,
            sticky="nsew",
            padx=(0, 10)
        )

        # 右側：ゲームパネル
        self.game_frame = ctk.CTkFrame(
            self.main_frame,
            fg_color=self.card_color,
            corner_radius=20
        )
        self.game_frame.grid(
            row=0, column=1,
            sticky="nsew",
            padx=(10, 0)
        )

        self.create_history_area()
        self.create_game_area()
        
        self.error_label = ctk.CTkLabel(
            self.game_frame,
            text="",
            font=(self.font_family, 12),
            text_color="#DC2626"
        )
        self.error_label.pack(anchor="w", padx=30, pady=(5, 0))
        
        self.number_entry.bind("<Return>", lambda event: self.on_guess())

    # -------------------------
    # 左側：履歴
    # -------------------------
    def create_history_area(self):
        title = ctk.CTkLabel(
            self.history_frame,
            text="HISTORY",
            font=("self.font_family", 16, "bold"),
            text_color=self.text_color
        )
        title.pack(fill="x", padx=20, pady=20)

        # 履歴一覧
        self.history_list = ctk.CTkScrollableFrame(
            self.history_frame,
            fg_color="transparent"
        )
        self.history_list.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=(0, 15)
        )

    # 履歴を追加するためのメソッド
    def add_history(self, number, hit, blow):
        item = ctk.CTkFrame(
            self.history_list,
            fg_color="#F5F6F8",
            corner_radius=10
        )
        item.pack(fill="x", pady=5)

        ctk.CTkLabel(
            item,
            text=number,
            font=("self.font_family", 16, "bold"),
            text_color=self.text_color
        ).pack(side="left", padx=12, pady=12)

        ctk.CTkLabel(
            item,
            text=f"{hit} HIT  /  {blow} BLOW",
            font=("self.font_family", 12),
            text_color=self.sub_text_color
        ).pack(side="right", padx=12)

    # ゲーム画面の表示を更新する
    def update_game_status(self, attempts, hit, blow):
        self.attempt_label.configure(text=str(attempts))
        self.hit_label.configure(text=str(hit))
        self.blow_label.configure(text=str(blow))        

    # -------------------------
    # 右側：ゲーム画面
    # -------------------------
    def create_game_area(self):
        title = ctk.CTkLabel(
            self.game_frame,
            text="HIT & BLOW",
            font=("self.font_family", 20, "bold"),
            text_color=self.text_color
        )
        title.pack(fill="x", padx=20, pady=20)

        # 試行回数
        ctk.CTkLabel(
            self.game_frame,
            text="ATTEMPTS",
            font=("self.font_family", 12),
            text_color=self.sub_text_color
        ).pack(pady=(15, 0))

        self.attempt_label = ctk.CTkLabel(
            self.game_frame,
            text="0",
            font=("self.font_family", 36, "bold"),
            text_color=self.text_color
        )
        self.attempt_label.pack()

        # HIT / BLOW 表示
        result_frame = ctk.CTkFrame(
            self.game_frame,
            fg_color="transparent"
        )
        result_frame.pack(fill="x", padx=30, pady=20)

        result_frame.grid_columnconfigure((0, 1), weight=1)

        self.hit_label = self.create_result_card(
            result_frame, "HIT", "0", 0, "#EFF6FF", "#2563EB"
        )

        self.blow_label = self.create_result_card(
            result_frame, "BLOW", "0", 1, "#F1F5F9", "#475569"
        )

        # 入力欄
        ctk.CTkLabel(
            self.game_frame,
            text="NUMBER",
            font=("self.font_family", 12, "bold"),
            text_color=self.sub_text_color
        ).pack(anchor="w", padx=30, pady=(15, 5))

        self.number_entry = ctk.CTkEntry(
            self.game_frame,
            placeholder_text="数字を入力",
            height=45,
            corner_radius=10,
            font=("self.font_family", 16),
            border_color="#D1D5DB"
        )
        self.number_entry.pack(fill="x", padx=30)

        # GUESSボタン
        self.guess_button = ctk.CTkButton(
            self.game_frame,
            text="GUESS",
            height=45,
            corner_radius=10,
            fg_color=self.accent_color,
            hover_color="#1D4ED8",
            font=("self.font_family", 14, "bold"),
            command=self.on_guess
        )
        self.guess_button.pack(fill="x", padx=30, pady=20)

    # HIT / BLOW のカードを作る
    def create_result_card(self, parent, title, value, column, bg, fg):
        card = ctk.CTkFrame(
            parent,
            fg_color=bg,
            corner_radius=12
        )
        card.grid(
            row=0,
            column=column,
            sticky="ew",
            padx=5
        )

        ctk.CTkLabel(
            card,
            text=title,
            font=("self.font_family", 13, "bold"),
            text_color=fg
        ).pack(pady=(10, 0))

        value_label = ctk.CTkLabel(
            card,
            text=value,
            font=("self.font_family", 28, "bold"),
            text_color=fg
        )
        value_label.pack(pady=(0, 10))

        return value_label

    # ボタンを押したときの処理
    def on_guess(self):
        number = self.number_entry.get().strip()

        # エラー表示をリセット
        self.error_label.configure(text="")

        # 未入力チェック
        if not number:
            self.error_label.configure(text="数字を入力してください")
            return

        # 数字チェック
        if not number.isdigit():
            self.error_label.configure(text="数字のみ入力できます")
            return

        # 桁数チェック
        if len(number) != 4:
            self.error_label.configure(text="4桁の数字を入力してください")
            return

        # 試行回数を更新
        self.attempts += 1

        # 仮の結果を表示
        hit = 2
        blow = 1

        self.add_history(number, hit, blow)
        self.update_game_status(self.attempts, hit, blow)

        # 入力欄をクリア
        self.number_entry.delete(0, "end")
        self.number_entry.focus()


def run():
    ctk.set_appearance_mode("light")
    root = ctk.CTk()
    app = GameUI(root)
    root.mainloop()
