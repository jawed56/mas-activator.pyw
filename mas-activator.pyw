import tkinter as tk
from tkinter import messagebox, ttk
import subprocess
import time
import os

class MASInterface:
    def __init__(self, root):
        self.root = root
        # Vérifier si un environnement graphique est disponible
        if os.environ.get('DISPLAY', '') == '' and os.name != 'nt':
            print("Erreur : Aucune interface graphique disponible. Exécutez dans un environnement avec GUI.")
            return
        self.root.title("Scripts d'Activation Microsoft v3.1")
        self.root.geometry("600x500")
        self.root.configure(bg="#ffff00")

        # Canvas pour l'arrière-plan arc-en-ciel animé
        self.canvas = tk.Canvas(root, bg="#0a0a0a", highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        # Liste des couleurs de l'arc-en-ciel
        self.rainbow_colors = ["#ff0000", "#ff8000", "#ffff00", "#00ff00", "#0000ff", "#8000ff", "#ff00ff"]
        self.current_color_index = 0
        self.update_rainbow()

        # Style pour les boutons
        self.style = ttk.Style()
        self.style.theme_use("clam")
        self.style.configure("TButton", font=("Arial", 12), padding=8)
        self.style.map("TButton", background=[("active", "#00aaff")], foreground=[("active", "white")])

        # Conteneur principal
        main_frame = tk.Frame(self.root, bg="#ff0000")
        main_frame.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.9, relheight=0.9)

        # Titre
        title_label = tk.Label(
            main_frame,
            text=" Interface Graphique avec Python ®",
            font=("Arial", 18, "bold"),
            fg="#ffffff",
            bg="#0a0a0a"
        )
        title_label.pack(pady=(10, 15))

        # Section Activation Windows
        windows_frame = tk.LabelFrame(
            main_frame,
            text="Activation de Windows",
            font=("Arial", 14),
            fg="#ffffff",
            bg="#90ee90",
            bd=2,
            relief="groove"
        )
        windows_frame.pack(fill="x", pady=5)
        tk.Button(
            windows_frame,
            text="Activer Windows (HWID) 🖥️",
            command=lambda: self.activate("hwid"),
            bg="#0078d7",
            fg="white",
            font=("Arial", 14),
            relief="flat",
            activebackground="#00aaff"
        ).pack(pady=5, padx=10, fill="x")
        tk.Button(
            windows_frame,
            text="Activer avec KMS38 🔒",
            command=lambda: self.activate("kms38"),
            bg="#0078d7",
            fg="white",
            font=("Arial", 14),
            relief="flat",
            activebackground="#00aaff"
        ).pack(pady=5, padx=10, fill="x")
        tk.Button(
            windows_frame,
            text="Activer IoT Enterprise SK 🌐",
            command=lambda: self.activate("iot"),
            bg="#0078d7",
            fg="white",
            font=("Arial", 14),
            relief="flat",
            activebackground="#00aaff"
        ).pack(pady=5, padx=10, fill="x")
        tk.Button(
            windows_frame,
            text="Activer en mode silencieux 🤐",
            command=lambda: self.activate("silent"),
            bg="#0078d7",
            fg="white",
            font=("Arial", 14),
            relief="flat",
            activebackground="#00aaff"
        ).pack(pady=5, padx=10, fill="x")
        # Section Activation Office
        office_frame = tk.LabelFrame(
            main_frame,
            text="Activation d'Office",
            font=("Arial", 14),
            fg="#ffffff",
            bg="#90ee90",
            bd=2,
            relief="groove" )
        office_frame.pack(fill="x", pady=5)
        tk.Button(
            office_frame,
            text="Activer Office (Ohook) 📝",
            command=lambda: self.activate("ohook"),
            bg="#0078d7",
            fg="white",
            font=("Arial", 14),
            relief="flat",
            activebackground="#00aaff"
        ).pack(pady=5, padx=10, fill="x")

        # Section Outils
        tools_frame = tk.LabelFrame(
            main_frame,
            text="Outils",
            font=("Arial", 14),
            fg="#ffffff",
            bg="#90ee90",
            bd=2,
            relief="groove" )
        tools_frame.pack(fill="x", pady=5)
        tk.Button(
            tools_frame,
            text="Vérifie l'état d'activation ✅",
            command=self.check_status,
            bg="#0078d7",
            fg="white",
            font=("Arial", 14),
            relief="flat",
            activebackground="#00aaff"
        ).pack(pady=5, padx=10, fill="x")
        tk.Button(
            tools_frame,
            text="Activer avec KMS Offline (function coming soon)💾",
            command=lambda: self.activate("kmsoffline"),
            bg="#0078d7",
            fg="white",
            font=("Arial", 14),
            relief="flat",
            activebackground="#00aaff"
        ).pack(pady=5, padx=10, fill="x")

    def update_rainbow(self):
        # Mettre à jour l'arrière-plan avec une nouvelle couleur de l'arc-en-ciel
        if hasattr(self, 'canvas'):
            self.canvas.configure(bg=self.rainbow_colors[self.current_color_index])
        self.current_color_index = (self.current_color_index + 1) % len(self.rainbow_colors)
        self.root.after(1000, self.update_rainbow)

    def activate(self, method):
        try:
            # Simuler l'activation avec des fonctionnalités
            if method == "hwid":
                subprocess.run('powershell -Command "irm https://massgrave.dev/get | iex"', shell=True)
            elif method == "ohook":
                subprocess.run('powershell -Command "irm https://massgrave.dev/get | iex"', shell=True)
            elif method == "kms38":
                subprocess.run('powershell -Command "irm https://massgrave.dev/get | iex"', shell=True)
            elif method == "iot":
                subprocess.run('powershell -Command "irm https://massgrave.dev/get | iex -Args \'iot\'"', shell=True)
            elif method == "silent":
                subprocess.run('powershell -Command "irm https://massgrave.dev/get | iex -Silent"', shell=True)
            elif method == "kmsoffline":
                subprocess.run('powershell -Command "irm https://massgrave.dev/get | iex -Offline"', shell=True)
            messagebox.showinfo("Succès", f"Activation {method} réussie avec v3.2 !")
        except Exception as e:
            messagebox.showerror("Erreur", f"Échec de l'activation : {str(e)}")

    def check_status(self):
        try:
            result = subprocess.run(
                'cscript //nologo "%windir%\\system32\\slmgr.vbs" /xpr',
                capture_output=True,
                text=True,
                shell=True
            )
            messagebox.showinfo("État d'activation", result.stdout)
        except Exception as e:
            messagebox.showerror("Erreur", f"Erreur lors de la vérification : {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = MASInterface(root)
    root.mainloop()
