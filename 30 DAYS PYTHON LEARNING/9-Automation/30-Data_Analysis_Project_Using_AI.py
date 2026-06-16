import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import pandas as pd
import os

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt


class DataAnalyzer:

    def __init__(self, root):

        self.root = root
        self.root.title("Corporate Data Analyzer")
        self.root.geometry("1100x700")

        self.df = None
        self.report_df = None
        self.file_path = ""

        self.create_ui()

    def create_ui(self):

        top = ttk.Frame(self.root)
        top.pack(fill="x", padx=10, pady=5)

        ttk.Button(
            top,
            text="Browse File",
            command=self.browse_file
        ).pack(side="left")

        ttk.Button(
            top,
            text="Read",
            command=self.read_file
        ).pack(side="left", padx=5)

        self.file_lbl = ttk.Label(
            top,
            text="No File Selected"
        )

        self.file_lbl.pack(side="left", padx=10)

        self.info_lbl = ttk.Label(
            self.root,
            text=""
        )

        self.info_lbl.pack(anchor="w", padx=10)

        report_frame = ttk.LabelFrame(
            self.root,
            text="Report Builder"
        )

        report_frame.pack(
            fill="x",
            padx=10,
            pady=5
        )

        self.group_var = tk.StringVar()
        self.value_var = tk.StringVar()
        self.agg_var = tk.StringVar()
        self.chart_var = tk.StringVar()

        ttk.Label(
            report_frame,
            text="Group By"
        ).grid(row=0, column=0)

        self.group_cb = ttk.Combobox(
            report_frame,
            textvariable=self.group_var,
            state="readonly"
        )

        self.group_cb.grid(row=0, column=1)

        ttk.Label(
            report_frame,
            text="Value Column"
        ).grid(row=0, column=2)

        self.value_cb = ttk.Combobox(
            report_frame,
            textvariable=self.value_var,
            state="readonly"
        )

        self.value_cb.grid(row=0, column=3)

        ttk.Label(
            report_frame,
            text="Aggregation"
        ).grid(row=0, column=4)

        self.agg_cb = ttk.Combobox(
            report_frame,
            values=[
                "sum",
                "mean",
                "max",
                "min",
                "count",
                "median"
            ],
            textvariable=self.agg_var,
            state="readonly"
        )

        self.agg_cb.grid(row=0, column=5)

        ttk.Button(
            report_frame,
            text="Preview Report",
            command=self.preview_report
        ).grid(row=0, column=6, padx=5)

        ttk.Button(
            report_frame,
            text="Export Report",
            command=self.export_report
        ).grid(row=0, column=7)

        chart_frame = ttk.LabelFrame(
            self.root,
            text="Chart Builder"
        )

        chart_frame.pack(
            fill="x",
            padx=10,
            pady=5
        )

        self.chart_cb = ttk.Combobox(
            chart_frame,
            values=[
                "Bar",
                "Line",
                "Pie"
            ],
            textvariable=self.chart_var,
            state="readonly"
        )

        self.chart_cb.pack(side="left")

        ttk.Button(
            chart_frame,
            text="Preview Chart",
            command=self.preview_chart
        ).pack(side="left", padx=5)

        ttk.Button(
            chart_frame,
            text="Export Chart",
            command=self.export_chart
        ).pack(side="left")

        self.tree = ttk.Treeview(self.root)

        self.tree.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=5
        )

        self.chart_area = ttk.Frame(self.root)

        self.chart_area.pack(
            fill="both",
            expand=True
        )

    def browse_file(self):

        self.file_path = filedialog.askopenfilename(
            filetypes=[
                ("Excel/CSV",
                 "*.xlsx *.xls *.csv")
            ]
        )

        if self.file_path:
            self.file_lbl.config(
                text=os.path.basename(
                    self.file_path
                )
            )

    def read_file(self):

        if not self.file_path:
            messagebox.showerror(
                "Error",
                "Select file first"
            )
            return

        if self.file_path.endswith(".csv"):
            self.df = pd.read_csv(
                self.file_path
            )
        else:
            self.df = pd.read_excel(
                self.file_path
            )

        text_cols = self.df.select_dtypes(
            include="object"
        ).columns.tolist()

        num_cols = self.df.select_dtypes(
            include="number"
        ).columns.tolist()

        self.group_cb["values"] = text_cols
        self.value_cb["values"] = num_cols

        self.info_lbl.config(
            text=f"Rows: {len(self.df)} | "
                 f"Columns: {len(self.df.columns)}"
        )

    def preview_report(self):

        if self.df is None:
            messagebox.showerror(
                "Error",
                "Read file first"
            )
            return

        self.report_df = (
            self.df.groupby(
                self.group_var.get()
            )[self.value_var.get()]
            .agg(self.agg_var.get())
            .reset_index()
            .sort_values(
                by=self.value_var.get(),
                ascending=False
            )
        )

        self.tree.delete(
            *self.tree.get_children()
        )

        self.tree["columns"] = list(
            self.report_df.columns
        )

        self.tree["show"] = "headings"

        for col in self.report_df.columns:

            self.tree.heading(
                col,
                text=col
            )

            self.tree.column(
                col,
                width=150
            )

        for row in self.report_df.itertuples(
                index=False):

            self.tree.insert(
                "",
                "end",
                values=row
            )

    def export_report(self):

        if self.report_df is None:
            return

        output = os.path.join(
            os.path.dirname(
                self.file_path
            ),
            "Report.xlsx"
        )

        self.report_df.to_excel(
            output,
            index=False
        )

        messagebox.showinfo(
            "Success",
            "Report Exported"
        )

    def preview_chart(self):

        if self.report_df is None:
            return

        for w in self.chart_area.winfo_children():
            w.destroy()

        fig, ax = plt.subplots(
            figsize=(5, 3)
        )

        x = self.report_df.iloc[:, 0]
        y = self.report_df.iloc[:, 1]

        chart = self.chart_var.get()

        if chart == "Bar":
            ax.bar(x, y)

        elif chart == "Line":
            ax.plot(x, y)

        elif chart == "Pie":
            ax.pie(
                y,
                labels=x,
                autopct="%1.1f%%"
            )

        self.fig = fig

        canvas = FigureCanvasTkAgg(
            fig,
            self.chart_area
        )

        canvas.draw()

        canvas.get_tk_widget().pack(
            fill="both",
            expand=True
        )

    def export_chart(self):

        if not hasattr(
                self,
                "fig"):
            return

        path = os.path.join(
            os.path.dirname(
                self.file_path
            ),
            "Chart.png"
        )

        self.fig.savefig(path)

        messagebox.showinfo(
            "Success",
            "Chart Exported"
        )


root = tk.Tk()

app = DataAnalyzer(root)

root.mainloop()