from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return render_template ("index.html") # Return the string 'Hello World!' as a response

# from flask import Flask  # Import Flask to allow us to create our app
# app = Flask(__name__)    # Create a new instance of the Flask class called "app"
# @app.route('/Hi/<name>')          # The "@" decorator associates this route with the function immediately following
# def hello_world(name):
#     return f"Hi {name}"

# @app.route('/repeat/<int:num>/<string:word>')          # The "@" decorator associates this route with the function immediately following
# def repeat_word(num,word):
#     return f"{word * num} "
# #     output = ""
# # for i in range(0,len.num):

    
    




if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)  

        
# @app.route('/success')
# def success():
#     return "success"
    