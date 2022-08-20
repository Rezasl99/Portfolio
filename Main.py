from flask import Flask, render_template, request
from markupsafe import escape
import csv

app = Flask(__name__)
# print(__name__)


@app.route("/")
def Home_page():
    return render_template('index.html')

@app.route("/<string:page_name>")
def Home_page2(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        database.write(f'\n  EMAIL: {email} \n SUBJECT:{subject} \n MESSAGE: {message}')

def write_to_csv(data):
  with open('database2.csv', newline='', mode='a') as database2:
    email = data["email"]
    subject = data["subject"]
    message = data["message"]
    csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow([email,subject,message])



@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
      try:
        data = request.form.to_dict()
        # write_to_file(data)
        write_to_csv(data)
        write_to_file(data)
        return render_template('/message_received.html')
      except:
        return 'did not save to database'
    else:
      return 'something went wrong. Try again!'


