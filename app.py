from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

subjects = ["Mahatma Gandhi", "Bengal Tiger", "Dr. B.R. Ambedkar", "A herd of Indian Elephant", 
            "Sachin Tendulkar", "One-horned Rhinoceros", "C.V. Raman", "Asiatic Lion", 
            "Rabindranath Tagore", "King Cobra", "Sardar Vallabhbhai Patel", "Snow Leopard", 
            "P.V. Sindhu", "Sloth Bear", "Amitabh Bachchan", "Red Panda"]

actions = ["launches", "cancels", "dances with", "eats", "declares war on", 
           "orders", "celebrates", "riding a Buffalo"]

places_or_things = ["at Red Fort", "Mumbai local train", "a plate of samosa", 
                    "inside the parliament", "during IPL match", "India Gate"]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/generate-headline')
def generate_headline():
    subject = random.choice(subjects)
    action = random.choice(actions)
    obj = random.choice(places_or_things)
    
    headline = f"BREAKING NEWS: {subject} {action} {obj}"
    return jsonify({'headline': headline})

if __name__ == '__main__':
    # Listen on all network interfaces for external access
    app.run(debug=False, host='0.0.0.0', port=5000)
