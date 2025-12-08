import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import re
import os

# --------- Core Log-Analysis Logic (backend) ---------
def analyze_log_file(file_path):
    """
    Analyze an HTTP access log file and return:
    - counts of common HTTP status codes
    - total request count
    - number of unique IPs
    """
    status_codes_of_interest = ["200", "301", "302", "403", "404", "500"]
    status_counts = {code: 0 for code in status_codes_of_interest}
    total_requests = 0
    unique_ips = set()

    # Regex patterns for IP and status code (Common Log Format-style)
    ip_pattern = re.compile(r"^(\d{1,3}(?:\.\d{1,3}){3})")
    status_pattern = re.compile(r'"\s+(\d{3})\s')

    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            total_requests += 1

            # Extract IP
            ip_match = ip_pattern.search(line)
            if ip_match:
                unique_ips.add(ip_match.group(1))

            # Extract status code
            status_match = status_pattern.search(line)
            if status_match:
                status = status_match.group(1)
                if status in status_counts:
                    status_counts[status] += 1

    return status_counts, total_requests, len(unique_ips)


# --------- Tkinter GUI Application ---------
class LogAnalyzerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Log Analyzer")
        self.root.geometry("600x400")

        # Selected file path
        self.selected_file = tk.StringVar()

        # ----- Top Frame: File selection -----
        top_frame = ttk.Frame(root, padding=10)
        top_frame.pack(fill="x")

        ttk.Label(top_frame, text="Log file:").pack(side="left")
        self.file_entry = ttk.Entry(top_frame, textvariable=self.selected_file, width=50)
        self.file_entry.pack(side="left", padx=5)

        browse_button = ttk.Button(top_frame, text="Browse...", command=self.browse_file)
        browse_button.pack(side="left")

        # ----- Middle Frame: Analyze button -----
        mid_frame = ttk.Frame(root, padding=10)
        mid_frame.pack(fill="x")

        analyze_button = ttk.Button(mid_frame, text="Analyze", command=self.run_analysis)
        analyze_button.pack(side="left")

        # ----- Results Frame -----
        results_frame = ttk.LabelFrame(root, text="Results", padding=10)
        results_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Treeview for status codes
        self.tree = ttk.Treeview(results_frame, columns=("status", "count"), show="headings", height=6)
        self.tree.heading("status", text="Status Code")
        self.tree.heading("count", text="Count")
        self.tree.column("status", width=100, anchor="center")
        self.tree.column("count", width=100, anchor="center")
        self.tree.pack(fill="x", pady=5)

        # Summary labels
        summary_frame = ttk.Frame(results_frame)
        summary_frame.pack(fill="x", pady=10)

        self.total_requests_label = ttk.Label(summary_frame, text="Total Requests: 0")
        self.total_requests_label.pack(anchor="w")

        self.unique_ips_label = ttk.Label(summary_frame, text="Unique IPs: 0")
        self.unique_ips_label.pack(anchor="w")

        # Status bar
        self.status_var = tk.StringVar(value="Select a log file and click Analyze.")
        status_bar = ttk.Label(root, textvariable=self.status_var, relief="sunken", anchor="w", padding=5)
        status_bar.pack(fill="x", side="bottom")

    def browse_file(self):
        file_path = filedialog.askopenfilename(
            title="Select log file",
            filetypes=[("Log files", "*.log *.txt"), ("All files", "*.*")]
        )
        if file_path:
            self.selected_file.set(file_path)
            self.status_var.set(f"Selected file: {os.path.basename(file_path)}")

    def run_analysis(self):
        file_path = self.selected_file.get().strip()
        if not file_path:
            messagebox.showwarning("No file", "Please select a log file first.")
            return

        if not os.path.exists(file_path):
            messagebox.showerror("File not found", "The selected file does not exist.")
            return

        try:
            status_counts, total_requests, unique_ip_count = analyze_log_file(file_path)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while analyzing the file:\n{e}")
            return

        # Clear table
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Fill table
        for status, count in status_counts.items():
            self.tree.insert("", "end", values=(status, count))

        # Update labels
        self.total_requests_label.config(text=f"Total Requests: {total_requests}")
        self.unique_ips_label.config(text=f"Unique IPs: {unique_ip_count}")

        self.status_var.set("Analysis complete.")


# --------- Main Entry Point ---------
if __name__ == "__main__":
    root = tk.Tk()
    app = LogAnalyzerGUI(root)
    root.mainloop()
