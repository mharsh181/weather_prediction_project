import tkinter as tk
from tkinter import messagebox, ttk
import pandas as pd
from model_handler import WeatherPredictor

# Initialize model
wp = WeatherPredictor()

def predict():
    try:
        date = entry_date.get()
        temp = float(entry_temp.get())
        precip = float(entry_precip.get())
        season = season_var.get()
        radiation = float(entry_radiation.get())
        wind = float(entry_wind.get())

        new_data = pd.DataFrame({
            'time': [date],
            'temperature_2m_mean': [temp],
            'precipitation_sum': [precip],
            'season': [season],
            'shortwave_radiation_sum': [radiation],
            'windspeed_10m_max': [wind]
        })

        temp_pred = wp.predict_temperature(new_data)
        et0_pred = wp.predict_et0(new_data)

        messagebox.showinfo("Prediction Result",
                            f"🌡 Predicted Temperature: {temp_pred:.1f}°C\n💧 Predicted ET0: {et0_pred:.2f} mm/day")
    except Exception as e:
        messagebox.showerror("Error", f"⚠️ Invalid input or error occurred:\n{e}")

# Root window setup
root = tk.Tk()
root.title("🌦 Weather Predictor")
root.geometry("400x400")
root.configure(bg="#f0f8ff")  # Alice blue background

title_label = tk.Label(root, text="Weather Prediction System", font=("Helvetica", 16, "bold"), bg="#f0f8ff", fg="#003366")
title_label.pack(pady=10)

form_frame = tk.Frame(root, bg="#f0f8ff")
form_frame.pack(pady=10)

# Input fields
def create_label_entry(row, label_text, entry_widget):
    label = tk.Label(form_frame, text=label_text, font=("Arial", 10), bg="#f0f8ff", anchor="w")
    label.grid(row=row, column=0, sticky="w", padx=10, pady=5)
    entry_widget.grid(row=row, column=1, padx=10, pady=5)

entry_date = tk.Entry(form_frame, font=("Arial", 10))
create_label_entry(0, "📅 Date (YYYY-MM-DD):", entry_date)

entry_temp = tk.Entry(form_frame, font=("Arial", 10))
create_label_entry(1, "🌡 Mean Temp (°C):", entry_temp)

entry_precip = tk.Entry(form_frame, font=("Arial", 10))
create_label_entry(2, "🌧 Precipitation (mm):", entry_precip)

season_var = tk.StringVar()
season_menu = ttk.Combobox(form_frame, textvariable=season_var, values=["Summer", "Winter", "Spring", "Autumn"], font=("Arial", 10))
season_menu.set("Summer")
create_label_entry(3, "🗓 Season:", season_menu)

entry_radiation = tk.Entry(form_frame, font=("Arial", 10))
create_label_entry(4, "☀ Radiation (MJ/m²):", entry_radiation)

entry_wind = tk.Entry(form_frame, font=("Arial", 10))
create_label_entry(5, "💨 Wind Speed (km/h):", entry_wind)

# Predict button
predict_btn = tk.Button(root, text="🔍 Predict", command=predict,
                        bg="#007acc", fg="white", font=("Arial", 12, "bold"),
                        relief="groove", bd=3, padx=10, pady=5)
predict_btn.pack(pady=15)

root.mainloop()
