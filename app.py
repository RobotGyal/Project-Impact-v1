from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)




# Main route
@app.route('/')
def home():
    '''Main page setup function'''
    return render_template('index.html')



if __name__=='__main__':
    app.run(Debug = True, host='0.0.0.0', port=os.environ.get('PORT', 5000))