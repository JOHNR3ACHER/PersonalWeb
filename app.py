from flask import Flask, render_template,request

app = Flask(__name__)

@app.route("/")
def pageinfo():
    title = "Welcome to my site"
    header = "Information: "
    details = readDetails("static/details.txt")
    return render_template("base.html", name1=title ,name2 = header,aboutMe = details)



def readDetails(filepath):
    with open(filepath, 'r') as f:
        return [line for line in f]

@app.route('/form', methods=['GET', 'POST']) #GET Retreives information & POST posts information
def formDemo():
    name = None #Intialization
    if request.method == 'POST':
        # if request.form['name']:
        #     name=request.form['name']
        if request.form['message']:
            write2file('static/comments.txt', request.form['message'])
    return render_template('form.html', name=name)

def write2file(filename,message):
    with open(filename, 'a') as f:
        f.write(message)

if __name__ == "__main__":
    app.run(debug=True)