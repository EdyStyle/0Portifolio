from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

@app.route('/')
def my_home():
    lang = request.args.get('lang')

    if lang == 'en':
        return render_template('en_index.html', lang='en')
    else:
        return render_template('index.html', lang='pt-BR')

@app.route('/<string:page_name>')
def html_page(page_name):
    lang = request.args.get('lang')

    if lang == 'en':
        return render_template(f'en_{page_name}', lang='en')
    else:
        return render_template(f'en_{page_name}', lang='en')


def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n{email}, {subject}, {message}')


def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_for():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'Did not save to database'
    else:
        return 'Something Went Wrong. Try Again!'
