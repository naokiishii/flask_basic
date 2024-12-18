import os
from flask import Flask, render_template, request, redirect, url_for
import stripe

app = Flask(__name__)

public_key = 'sk_test_09l3shTSTKHYCzzZZsiLl2vA'

stripe.api_key = 'sk_test_09l3shTSTKHYCzzZZsiLl2vA'

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/thankyou')
def thankyou():
  return render_template('thankyou.html')

@app.route('/payment', methods = ['POST'])
def payment():
  
  # CUSTOMER INFO
  customer = stripe.Customer.create(email=request.form['stripeEmail'], source=request.form['stripeToken'])
  
  #PAYMENT INFORMATION
  charge = stripe.Charge.create(customer=customer.id, amount=1, currency='usd', description='Donation')
  
  return redirect(url_for('thankyou'))

if __name__ == '__main__':
  app.run(debug=True)