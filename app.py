from flask import Flask, render_template, request, redirect, url_for, flash, abort, session , jsonify
import json
import os.path
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = "fffffffffffffffffdskjhhhhhhhhhhhhhssssssssss"


@app.route("/")
def home():
    return render_template('home.html', codes=session.keys())


@app.route("/your_url", methods=['POST', 'GET'])
def about():
    if request.method == 'POST':
        urls = {}

        if os.path.exists('urls.json'):
            with open('urls.json') as urls_file:
                urls = json.load(urls_file)
        if request.form.get('code') in urls.keys():
            flash("Short name has already been taken.Please select another name.")
            return redirect(url_for('home'))
        if 'url1' in request.form.keys():
            urls[request.form.get('code')] = {'url': request.form.get('url1')}
        else:
            f = request.files.get("file1")
            full_name = request.form.get("code")+secure_filename(f.filename)
            # f.save('D:\Adithya\pybox\demoapp/'+full_name)
            f.save(r'D:\Adithya\pybox\demoapp\static\user_files/'+full_name)
            urls[request.form.get('code')] = {'file': full_name}

        with open("urls.json", 'w') as url_file:

            json.dump(urls, url_file)
            session[request.form.get('code')] = True

        return render_template('about.html', code=request.form.get('code'))
    else:
        return redirect(url_for('home'))


@app.route('/<string:code>')
def redirect_to_url(code):

    if os.path.exists('urls.json'):
        with open("urls.json", 'r') as urls_file:
            urls = json.load(urls_file)

            if code in urls.keys():
                if 'url' in urls[code].keys():
                    return redirect(urls[code]['url'])
                else:
                    return redirect(url_for('static', filename='user_files/'+urls[code]['file']))
    return abort(404)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

@app.route('/api')
def session_api():
    return jsonify(list(session.keys()))


if __name__ == "__main__":
    app.run(debug=True)
