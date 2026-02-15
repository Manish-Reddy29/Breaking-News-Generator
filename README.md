# 🎬 Breaking News Generator - Website Edition

A fun and interactive website for generating hilarious fake headlines with Indian themes!

## Features

✨ **Lively & Interactive Design**
- Colorful gradient background with modern UI
- Smooth animations and transitions
- Responsive design for mobile and desktop
- Real-time headline generation

🎯 **Fun Elements**
- News ticker animati on
- Live indicator with pulsing animation
- Counter to track generated headlines
- One-click copy to clipboard
- Celebration animations

📱 **User-Friendly**
- Click button or press Enter to generate news
- Timestamp for each generated headline
- Beautiful feature cards
- Mobile-optimized interface

## Installation

### Step 1: Install Flask
Run this command in PowerShell or Command Prompt:

```powershell
pip install -r requirements.txt
```

Or install Flask directly:

```powershell
pip install Flask
```

## Running the Website

### Step 1: Open Terminal
Navigate to the project folder in PowerShell:

```powershell
cd "c:\Users\Manish Reddy Y\Desktop\Python Applications"
```

### Step 2: Run the Flask App
```powershell
python app.py
```

You should see output like:
```
 * Running on http://127.0.0.1:5000
```

### Step 3: Open in Browser
- Open your web browser
- Go to: **http://localhost:5000**
- Start generating funny headlines!

## How to Use

1. **Generate Headlines**: Click the "📰 Generate News" button
2. **Keyboard Shortcut**: Press **Enter** to generate headlines
3. **Copy Headline**: Click "📋 Copy News" to copy to clipboard
4. **Track Count**: Watch the counter increase with each generation

## Features in Action

- **LIVE Indicator**: Shows real-time generation
- **News Ticker**: Scrolling text animation
- **Animated Cards**: Shake effect when generating
- **Counter**: Tracks total headlines generated
- **Responsive Design**: Works on phones, tablets, and desktops

## File Structure

```
Python Applications/
├── app.py                 # Flask backend
├── Fake_Headline_Generator.py  # Original Python script
├── requirements.txt       # Python dependencies
├── templates/
│   └── index.html        # Website HTML
└── static/
    ├── style.css         # Website styling
    └── script.js         # Interactive JavaScript
```

## Customization

Want to add more subjects, actions, or places?

Edit `app.py` and modify these lists:

```python
subjects = ["Add more subjects here"]
actions = ["Add more actions here"]
places_or_things = ["Add more places here"]
```

## Troubleshooting

**Port Already in Use?**
Change the port in `app.py`:
```python
app.run(debug=True, port=5001)  # Use 5001 instead of 5000
```

**Flask Not Installed?**
```powershell
pip install Flask
```

**Website Not Loading?**
- Make sure the Flask app is running (you should see the "Running on" message)
- Clear browser cache (Ctrl + Shift + Delete)
- Try http://127.0.0.1:5000 instead of localhost:5000

## Enjoy! 🎉

Have fun generating the most hilarious headlines! Share your favorite ones with friends!
