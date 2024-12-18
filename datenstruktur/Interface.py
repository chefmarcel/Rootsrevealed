import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

# Funktion für "Datei auswählen"-Button
def choose_file():
    file_path = filedialog.askopenfilename(
        title="Wähle eine GEDCOM-Datei aus",
        filetypes=[("GEDCOM-Dateien", "*.ged"), ("Alle Dateien", "*.*")]
    )
    if file_path:
        messagebox.showinfo("Datei ausgewählt", f"Datei: {file_path}")

# Funktion für "Datei ablegen"-Button
def drop_file():
    messagebox.showinfo("Datei ablegen", "Funktion 'Datei ablegen' ist noch nicht implementiert.")

# Hauptfenster erstellen
root = tk.Tk()
root.title("Roots Revealed - Ancestry Research")
root.geometry("800x600")  # Fenstergröße festlegen
root.resizable(False, False)

# Hintergrundbild laden
background_image_path = "h:\Downloads\startbildschirm.1.png"  # Pfad zu Ihrem hochgeladenen Bild
bg_image = Image.open(background_image_path)
bg_image = bg_image.resize((800, 600), Image.Resampling.LANCZOS)  # Größe anpassen
bg_photo = ImageTk.PhotoImage(bg_image)

# Canvas erstellen und Hintergrundbild setzen
canvas = tk.Canvas(root, width=800, height=600)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=bg_photo, anchor="nw")

# Button-Bilder laden
choose_file_image_path = "h:\Pictures\Fortnite.png"  # Ersetzen mit Ihrem "Datei auswählen"-Button-Bild
drop_file_image_path = "h:\Downloads\startbildschirm.1.png"  # Ersetzen mit Ihrem "Datei ablegen"-Button-Bild

choose_file_image = Image.open(choose_file_image_path)
choose_file_photo = ImageTk.PhotoImage(choose_file_image)

drop_file_image = Image.open(drop_file_image_path)
drop_file_photo = ImageTk.PhotoImage(drop_file_image)

# "Datei auswählen"-Button mit Bild
choose_file_btn = tk.Button(
    root, image=choose_file_photo, command=choose_file,
    borderwidth=0, bg="#2e2a27", activebackground="#2e2a27"
)
choose_file_btn.place(x=340, y=310)  # Position passend zum Bild

# "Datei ablegen"-Button mit Bild
drop_file_btn = tk.Button(
    root, image=drop_file_photo, command=drop_file,
    borderwidth=0, bg="#2e2a27", activebackground="#2e2a27"
)
drop_file_btn.place(x=360, y=370)  # Position passend zum Bild

# Hauptfenster starten
root.mainloop()
