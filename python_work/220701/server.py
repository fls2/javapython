from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return '''<!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Document</title>
            <style>
                p::first-letter{font-size: 3em;}
                p::first-line{color: red;}
            </style>
        </head>
        <body>
            <h1>head</h1>
            <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Eveniet odio eaque incidunt unde, in veniam facere maiores minima porro doloremque doloribus optio maxime ut ullam consequatur reprehenderit fuga, nemo omnis?</p>
            <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Natus eveniet impedit nostrum fugit, obcaecati quidem pariatur dolore, laudantium expedita temporibus neque qui facilis deleniti in totam maiores numquam amet reprehenderit.</p>
        </body>
        </html>'''

app.run(host="192.168.0.12",port=5000)