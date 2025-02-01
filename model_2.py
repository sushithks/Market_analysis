import sqlite3
from tkinter import Tk, Label, Entry, Text, Button, filedialog, messagebox
from tkinter.scrolledtext import ScrolledText
from PIL import Image, ImageTk


# Initialize the database
def initialize_db():
    connection = sqlite3.connect("daily_summary.db")
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS DailySummary (
            Date TEXT PRIMARY KEY,
            Highlights TEXT,
            DayNote TEXT,
            DayChart BLOB,
            DayChartNote TEXT,
            OneHrChart BLOB,
            OneHrChartNote TEXT,
            FifteenMinChart BLOB,
            FifteenMinChartNote TEXT,
            FiveMinChart BLOB,
            FiveMinChartNote TEXT,
            HHinChart BLOB,
            HHinChartNote TEXT
        )
    """)
    connection.commit()
    connection.close()


# Save the data to the database
def save_data():
    date = date_entry.get()
    highlights = highlights_entry.get()
    day_note = day_note_text.get("1.0", "end-1c")
    day_chart_note = day_chart_note_text.get("1.0", "end-1c")
    one_hr_chart_note = one_hr_chart_note_text.get("1.0", "end-1c")
    fifteen_min_chart_note = fifteen_min_chart_note_text.get("1.0", "end-1c")
    five_min_chart_note = five_min_chart_note_text.get("1.0", "end-1c")
    hhin_chart_note = hhin_chart_note_text.get("1.0", "end-1c")

    # Read image files
    images = [day_chart_path.get(), one_hr_chart_path.get(), fifteen_min_chart_path.get(),
              five_min_chart_path.get(), hhin_chart_path.get()]
    image_data = []
    for img in images:
        if img:
            with open(img, "rb") as file:
                image_data.append(file.read())
        else:
            image_data.append(None)

    connection = sqlite3.connect("daily_summary.db")
    cursor = connection.cursor()
    try:
        cursor.execute("""
            INSERT INTO DailySummary (
                Date, Highlights, DayNote,
                DayChart, DayChartNote,
                OneHrChart, OneHrChartNote,
                FifteenMinChart, FifteenMinChartNote,
                FiveMinChart, FiveMinChartNote,
                HHinChart, HHinChartNote
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (date, highlights, day_note,
              image_data[0], day_chart_note,
              image_data[1], one_hr_chart_note,
              image_data[2], fifteen_min_chart_note,
              image_data[3], five_min_chart_note,
              image_data[4], hhin_chart_note))
        connection.commit()
        messagebox.showinfo("Success", "Data saved successfully!")
    except sqlite3.IntegrityError:
        messagebox.showerror("Error", "An entry for this date already exists.")
    finally:
        connection.close()


# Upload image function
def upload_image(entry_var):
    file_path = filedialog.askopenfilename(
        title="Select an Image",
        filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")]
    )
    if file_path:
        entry_var.set(file_path)


# Initialize the GUI
app = Tk()
app.title("Daily Summary Database")
app.geometry("800x800")

Label(app, text="Date (YYYY-MM-DD):").grid(row=0, column=0, padx=10, pady=5)
date_entry = Entry(app, width=30)
date_entry.grid(row=0, column=1, padx=10, pady=5)

Label(app, text="Highlights:").grid(row=1, column=0, padx=10, pady=5)
highlights_entry = Entry(app, width=50)
highlights_entry.grid(row=1, column=1, padx=10, pady=5)

Label(app, text="Day Note:").grid(row=2, column=0, padx=10, pady=5)
day_note_text = ScrolledText(app, width=50, height=5)
day_note_text.grid(row=2, column=1, padx=10, pady=5)

# Image fields and notes
image_labels = ["Day Chart", "1Hr Chart", "15Min Chart", "5Min Chart", "HHin Chart"]
image_paths = [day_chart_path := StringVar(), one_hr_chart_path := StringVar(),
               fifteen_min_chart_path := StringVar(), five_min_chart_path := StringVar(),
               hhin_chart_path := StringVar()]
image_notes = []

for i, label in enumerate(image_labels):
    Label(app, text=f"{label}:").grid(row=3 + i * 2, column=0, padx=10, pady=5)
    Button(app, text="Upload Image", command=lambda var=image_paths[i]: upload_image(var)).grid(row=3 + i * 2, column=1, padx=10, pady=5, sticky="w")
    Label(app, textvariable=image_paths[i], wraplength=400, anchor="w", justify="left").grid(row=3 + i * 2, column=2, padx=10, pady=5)
    Label(app, text=f"{label} Note:").grid(row=4 + i * 2, column=0, padx=10, pady=5)
    note_text = Text(app, width=50, height=3)
    note_text.grid(row=4 + i * 2, column=1, padx=10, pady=5)
    image_notes.append(note_text)

# Map notes for saving
(day_chart_note_text, one_hr_chart_note_text,
 fifteen_min_chart_note_text, five_min_chart_note_text,
 hhin_chart_note_text) = image_notes

# Save button
Button(app, text="Save Data", command=save_data).grid(row=13, column=1, pady=20)

initialize_db()
app.mainloop()