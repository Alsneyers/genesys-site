from flask import Flask, render_template, request, redirect, url_for, session
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a secure secret key

# Routes for the main pages
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/car-insurance')
def car_insurance():
    return render_template('car_insurance.html')

@app.route('/home-insurance')
def home_insurance():
    return render_template('home_insurance.html')

@app.route('/travel-insurance')
def travel_insurance():
    return render_template('travel_insurance.html')

@app.route('/support')
def support():
    return render_template('support.html')

@app.route('/chat', methods=['GET', 'POST'])
def chat():
    if 'chat_history' not in session:
        session['chat_history'] = []

    if request.method == 'POST':
        user_message = request.form['message']
        # Append user's message to chat history
        session['chat_history'].append({'sender': 'You', 'message': user_message})

        # Generate a response (placeholder)
        support_response = "Thank you for reaching out. How can I assist you further?"

        # Append support's response to chat history
        session['chat_history'].append({'sender': 'Support', 'message': support_response})

        # Save the updated chat history in the session
        session.modified = True

    return render_template('chat.html', chat_history=session['chat_history'])

@app.route('/claim', methods=['GET', 'POST'])
def claim():
    if request.method == 'POST':
        # Process claim form data
        claim_data = {
            'name': request.form['name'],
            'policy_number': request.form['policy_number'],
            'details': request.form['details']
        }
        # You can add code here to save the claim data to a database
        return redirect(url_for('home'))
    return render_template('claim.html')

if __name__ == '__main__':
    # Adjust the host and port for Replit
    app.run(host='0.0.0.0', port=8080)
