import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


class Tournament(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry("1400x860")
        self.minsize(1400, 860)
        self.maxsize(1400, 860)

        self.title("Tournament Management System")

        self.points = [25, 18, 15]

        # Teams
        self.t1_scores = [tk.StringVar(value="0") for _ in range(5)]
        self.t2_scores = [tk.StringVar(value="0") for _ in range(5)]
        self.t3_scores = [tk.StringVar(value="0") for _ in range(5)]
        self.t4_scores = [tk.StringVar(value="0") for _ in range(5)]

        # Team totals points
        self.t1_total = tk.StringVar(value="0")
        self.t2_total = tk.StringVar(value="0")
        self.t3_total = tk.StringVar(value="0")
        self.t4_total = tk.StringVar(value="0")

        self.txtPoints1 = tk.StringVar(value="25")
        self.txtPoints2 = tk.StringVar(value="18")
        self.txtPoints3 = tk.StringVar(value="15")

        self.title_font = ("Arial", 40, "bold")
        self.component_font = ("Arial", 14, "bold")

        self.create_widgets()

    def create_widgets(self):
        title_label = tk.Label(self, text="Tournament Management System", font=self.title_font)
        title_label.pack(pady=20)

        frame = tk.Frame(self)
        frame.pack(padx=100, pady=1, fill="both", expand=True)

        points_frame = tk.Frame(self)
        points_frame.pack(pady=10)

        tk.Label(points_frame, text="Points 1:", font=self.component_font).grid(row=0, column=0, sticky="e")
        tk.Entry(points_frame, textvariable=self.txtPoints1, width=5, font=self.component_font).grid(row=0, column=1, sticky="w")

        tk.Label(points_frame, text="Points 2:", font=self.component_font).grid(row=0, column=2, sticky="e")
        tk.Entry(points_frame, textvariable=self.txtPoints2, width=5, font=self.component_font).grid(row=0, column=3, sticky="w")

        tk.Label(points_frame, text="Points 3:", font=self.component_font).grid(row=0, column=4, sticky="e")
        tk.Entry(points_frame, textvariable=self.txtPoints3, width=5, font=self.component_font).grid(row=0, column=5, sticky="w")

        # Adding the Reset and Exist buttons before the main frame
        button_frame = tk.Frame(self)
        button_frame.pack(pady=40)

        btnReset = tk.Button(button_frame, text="Reset", font=("Arial", 30, "bold"), width=20, bg="cadetblue")
        btnReset.pack(side=tk.LEFT, padx=5)

        btnExist = tk.Button(button_frame, text="Exist", font=("Arial", 30, "bold"), width=20, bg="cadetblue")
        btnExist.pack(side=tk.LEFT, padx=5)

        self.group_boxes = []
        for team_num in range(1, 5):
            group_box = tk.LabelFrame(frame, text=f"Team {team_num} Scores", padx=10, pady=10, font=self.component_font)
            group_box.grid(row=0, column=team_num - 1, padx=16, pady=10, sticky="n")

            scores = getattr(self, f't{team_num}_scores')
            for score_num in range(5):
                tk.Label(group_box, text=f"Score {score_num + 1}:", font=self.component_font).pack()

                cmb = ttk.Combobox(group_box, state="readonly", values=[0, 1, 2, 3, 4, 5], font=self.component_font)
                cmb.current(0)
                cmb.bind("<<ComboboxSelected>>", lambda e, tn=team_num, sn=score_num: self.on_score_change(tn, sn, e))
                cmb.pack()

                lbl = tk.Label(group_box, textvariable=scores[score_num], font=self.component_font)
                lbl.pack()

            tk.Label(group_box, text="Total", font=self.component_font).pack()
            tk.Label(group_box, textvariable=getattr(self, f't{team_num}_total'), font=self.component_font).pack()

            self.group_boxes.append(group_box)

    def on_score_change(self, team_num, score_num, event):
        cmb = event.widget
        index = int(cmb.get())

        point_value = self.points[index % 3]
        getattr(self, f't{team_num}_scores')[score_num].set(point_value)

        self.update_team_total(team_num)

    def update_team_total(self, team_num):
        scores = getattr(self, f't{team_num}_scores')
        total = sum(int(score.get()) for score in scores)
        getattr(self, f't{team_num}_total').set(str(total))


if __name__ == "__main__":
    app = Tournament()
    app.mainloop()
