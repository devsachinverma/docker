from flask import Flask
app=Flask(__name__)
#firstpage
@app.route('/home')
def hello():
    return "Hello this is my first page."


if __name__ == "__main__":
    app.run()


