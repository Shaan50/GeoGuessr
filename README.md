# GeoGuessr Game 🗺️

A Python-based **GeoGuessr-style game** that drops players into random locations around the world using Google Street View and challenges them to guess their location on a map. Your score depends on how close your guess is to the actual coordinates.

---

## Features

- Randomized locations across multiple continents.
- Google Street View integration for realistic exploration.
- Interactive map for placing guesses.
- Scoring system based on distance from the actual location.
- Multi-round gameplay with cumulative scoring.
- Responsive and browser-based interface using Flask.

---

## How It Works

1. **Location Generation**  
   The game randomly generates coordinates within predefined continental ranges and fetches a Street View image from Google Maps.

2. **Gameplay**  
   - Players explore the Street View panorama.  
   - Click on the map to place a guess.  
   - Press "GUESS" to calculate the distance to the real location.  
   - Receive points based on proximity (closer guesses score more).

3. **Score Calculation**  
   The game uses a custom scoring formula:
   score = round(5000 * (1.25)^(-0.005 * distance_km))
   Scores accumulate across rounds.

4. **Next Round**  
After each guess, the correct location is revealed, and players can continue to the next round.

---

## Tech Stack

- **Python 3** – Core game logic and backend.
- **Flask** – Web server and HTML rendering.
- **Google Maps API** – Street View and interactive map.
- **PIL (Pillow)** – For image handling.
- **HTML / JavaScript** – Front-end interactivity.

---

## Installation

1. Clone the repository:  
```bash
git clone https://github.com/yourusername/geoguessr.git
cd geoguessr
pip install -r requirements.txt
api_key = "YOUR_API_KEY"
python webpy.py
http://127.0.0.1:5000/
```

---

## Folder Structure

geoguessr/
│
├─ geoguessr.py       # Game logic and coordinate generation
├─ webpy.py           # Flask web app and front-end HTML/JS
├─ requirements.txt   # Python dependencies
├─ README.md          # Project documentation
└─ streetview_image.jpg # Temporary downloaded Street View image

---

## License

This project is open-source and available under the MIT License.

## Author

Shaan Cheruvu
https://github/com/Shaan50
