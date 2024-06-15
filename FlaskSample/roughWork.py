from flask import Flask

app = Flask(__name__) #The __name__ variable is a special variable in Python that represents the name of the current module.
# It is used by Flask to determine the root path of the application.

@app.route('/')
def helloworld():
    return 'Hello World'

if __name__ == '__main__':
    app.run()


