from flask import Flask, request, redirect, render_template, url_for
import string, random

app = Flask(__name__)

# Store short -> long mapping
url_mapping = {}

def generate_short_code(length=6):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=length))

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        original_url = request.form['url']
        # Generate unique short code
        short_code = generate_short_code()
        while short_code in url_mapping:
            short_code = generate_short_code()
        url_mapping[short_code] = original_url
        short_url = request.host_url + short_code
        return render_template('result.html', short_url=short_url)
    return render_template('index.html')

@app.route('/<short_code>')
def redirect_to_url(short_code):
    long_url = url_mapping.get(short_code)
    if long_url:
        return redirect(long_url)
    print("sdfsd")
    return "URL not found!", 404

if __name__ == '__main__':
    app.run(debug=True)
