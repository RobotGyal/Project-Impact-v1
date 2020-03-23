from flask import Flask, request, render_template, redirect, url_for
import data_analysis
import matplotlib.pyplot as plt


app = Flask(__name__)




# Main route
@app.route('/')
def home():
    '''Main page setup function'''
    # print(data_analysis.meteor)
    meteors = data_analysis.meteor_kv  # take data from data_analysis.py
    # print(meteors)    
    return render_template('index.html', meteors = meteors)

if __name__=='__main__':
    app.run(Debug = True, host='0.0.0.0', port=os.environ.get('PORT', 5000))