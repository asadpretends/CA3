from flask import Flask
app= Flask(__name__)

@app.route('/calculator/add')
def add(x,y):
    return x+y

@app.route('/calculator/multiply')
def multiply(x,y):
    return x*y
# Main calculator loop
add(1,1)
multiply(2,2)




