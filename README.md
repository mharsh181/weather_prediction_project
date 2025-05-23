
# 🌦️ Weather Predictor GUI

A simple Python-based GUI application for predicting weather conditions such as **Temperature** and **Evapotranspiration (ET0)** using a pre-trained machine learning model. Built with `Tkinter` for the user interface and `Pandas` for data handling.

---

## 🛠 Features

- Input weather parameters through an easy-to-use graphical interface
- Predict:
  - 🌡️ Mean Temperature (°C)
  - 💧 ET0 (Evapotranspiration in mm/day)
- Built-in error handling for invalid or missing inputs
- Beautifully styled UI with emojis and modern layout
- Lightweight and fast – no external GUI dependencies

---

## 📸 GUI Preview

> *![image](https://github.com/user-attachments/assets/85940334-2e78-4b2d-a273-f5448f5af727)
*

---

## 📦 Requirements

- Python 3.7+
- pandas
- tkinter (comes pre-installed with Python)
- A custom module `model_handler.py` with the `WeatherPredictor` class

Install dependencies (if not already installed):

```bash
pip install pandas
```

---

## 📁 Project Structure

```
weather_predictor_gui/
├── model_handler.py       # Your ML model and prediction logic
├── main.py                # GUI application script
├── README.md              # This file
```

---

## 🚀 Getting Started

1. Clone the repository:

```bash
git clone https://github.com/yourusername/weather-predictor-gui.git
cd weather_predictor_gui
```

2. Run the app:

```bash
python main.py
```

3. Enter weather data and click **"Predict"** to get the forecast.

---

## 🔧 `WeatherPredictor` Class

Make sure `model_handler.py` contains a class like this:

```python
class WeatherPredictor:
    def predict_temperature(self, data: pd.DataFrame) -> float:
        # Your model logic here
        pass

    def predict_et0(self, data: pd.DataFrame) -> float:
        # Your model logic here
        pass
```

---

## 📊 Example Inputs

| Date       | Temp (°C) | Precip (mm) | Season | Radiation | Wind (km/h) |
|------------|-----------|-------------|--------|-----------|-------------|
| 2025-07-15 | 28.5      | 5.2         | Summer | 25.6      | 12.3        |
| 2025-12-10 | 12.1      | 0.0         | Winter | 8.5       | 7.0         |

---

## 🧠 Future Improvements

- Add charts for predicted trends
- Export predictions to CSV
- Integrate weather API for real-time inputs
- Switch to `customtkinter` or `PyQt` for a modern UI

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.



---

## 👨‍💻 Author

**Harsh Mishra**  
*Made with ❤️ in Python*
