from flask import Flask

existing_models = ['Beedle', 'Crossroads', 'M2', 'Panique']

app = Flask(__name__)


@app.route('/')
def home():
    return "Welcome to Flatiron Cars"

#Route for specific model 

def model_info(model):
    if model.lower in existing_models:
        return f"Flatiron {model.capitalize()} is  in our  fleet!"
    else:
        return f"No models called {model.capitalize()} exists in our catalog."
    
if __name__ == '__main__':
    app.run(debug=True)
