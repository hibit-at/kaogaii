# -*- coding: utf-8 -*-
from flask import Flask,render_template,request
import numpy as np
import csv

app = Flask(__name__)

@app.route('/')
def index():
    choice = request.args.get("choice")
    if choice is None:
        choice = "init"
        title = "title"
        url = "url"
        nums = []
        for i in range(9):
            nums.append(np.random.randint(0,3253))
        row1 = nums[0:3]
        row2 = nums[3:6]
        row3 = nums[6:9]
    else:
        with open('static/datalist.csv',encoding='utf-8') as f:
            reader = csv.reader(f)
            l = [row for row in reader]
        url = l[int(choice)][1]
        title = l[int(choice)][2]
        recos = []
        for i in range(9):
            recos.append(l[int(choice)][3+i])
        row1 = recos[0:3]
        row2 = recos[3:6]
        row3 = recos[6:9]
    return render_template("index.html", 
                            row1=row1,
                            row2=row2,
                            row3=row3,
                            choice=choice,
                            title=title,
                            url=url,
                            )

@app.route('/faq')
def faq():
    return render_template("faq.html")

if __name__ == '__main__':
    app.run(debug=True)