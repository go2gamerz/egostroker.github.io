from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/feedback", methods=["POST"])
def feedback():
    text = request.form["text"]
    feedback_messages = [
        "Wow, I've never seen anyone work that slow before.",
        "Your work is so bad, it's almost impressive.",
        "Keep up the good work... of not doing any work.",
        "I'm amazed at how little effort you put in.",
        "You really know how to make my job harder.",
        "If only I could be as lazy as you.",
        "Well, at least you tried. Sort of.",
        "That was... something.",
    "You're making me reconsider my career choices.",
    "You're a true inspiration... to people who don't care about their job.",
    "You're like a superhero, except without the powers or motivation.",
    "Great job! If you were trying to fail.",
    "At least you're consistent... in being terrible.",
    "Just when I think you couldn't do any worse, you surprise me.",
    "Your work is a great example of what not to do.",
    "I hope you're not planning on putting this on your resume.",
    "I didn't know it was possible to mess up this badly.",
    "You're like a broken clock... always wrong.",
    "I'm impressed by your ability to do the bare minimum.",
    "That was terrible, but don't worry, there's always room for improvement.",
    "You're making the rest of us look bad.",
    "You're really living up to the low expectations I have for you.",
    "I think you missed the point of the task, but good effort anyways.",
    "I'd give you a gold star, but you haven't earned it.",
    "Congratulations on meeting the bare minimum requirements.",
    "You're a great example of what happens when you don't try.",
    "You're like a bad movie... I can't believe I wasted my time on you.",
    "You're the reason why we can't have nice things.",
    "You're really living up to your potential... which isn't saying much.",
    "I'm sorry, I didn't realize we were aiming for mediocrity.",
    "Your work is so bad, it's almost impressive.",
    "I've seen better work from a toddler.",
    "If only there was an award for doing the least amount of work.",
    "I'm not sure what you did, but I'm pretty sure it wasn't what I asked for.",
    "I'm amazed at how little effort you put in.",
    "You're a real asset to the team... said no one ever.",
    "You're really taking the term 'underachiever' to the next level.",
    "You're like a car crash... I can't look away.",
    "You really know how to make a bad situation worse.",
    "I don't know what's worse, your work or your attitude.",
    "You're a real inspiration to people who don't care about their job.",
    "I'm impressed by your ability to disappoint me.",
    "You're really raising the bar for mediocrity.",
    "That was... something. I'm just not sure what.",
    "You're the reason why we can't have nice things.",
    "You're really living up to your potential... which isn't saying much.",
    "If only there was an award for doing the least amount of work.",
    "I'm sorry, I didn't realize we were aiming for mediocrity.",
    "Your work is so bad, it's almost impressive.",
    "I've seen better work from a toddler.",
    "I'm amazed at how little effort you put in.",


    ]
    feedback_message = random.choice(feedback_messages)
    return render_template("feedback.html", text=text, feedback_message=feedback_message)

if __name__ == "__main__":
    app.run(debug=True)
