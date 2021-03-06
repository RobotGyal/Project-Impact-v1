from flask import Flask, request, render_template, redirect, url_for
import matplotlib.pyplot as plt
import pandas as pd
# import data_analysis
import os


app = Flask(__name__)




# Main route
@app.route('/')
def home():
    '''Main page setup function'''
    # print(data_analysis.meteor)
    # meteor_kv = data_analysis.meteor_kv  # take data from data_analysis.py
    # meteor = data_analysis.meteor # take data from data_analysis.py
        # print(meteors)    
    return render_template('index_new.html') # meteor_kv = meteor_kv




# @app.route('/table')
# def table():
#     # meteor_2000 = data_analysis.api_meteor_data
#     # html = meteor_2000.to_html()
#     text_file = open("templates/table.html", "w")
#     text_file.write(html)
#     text_file.close()
#     return render_template('table.html', html = html)




@app.route('/visuals')
def visuals():
    return render_template('visuals.html')



# @app.route('/notebook')
# def notebook():
#     return render_template('data_analysis_web.html')



if __name__=='__main__':
    app.run(debug = True, host='0.0.0.0', port=os.environ.get('PORT', 5000))