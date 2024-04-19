from flask import Flask, request, render_template, redirect, url_for, session, jsonify
from agents.fitnessagent import FitnessAgent
from agents.factsagent import FactsAgent
from agents.nutritionagent import NutritionAgent
import os

app = Flask(__name__)
app.jinja_env.filters['round'] = round
app.secret_key = os.environ.get('SECRET_KEY')
fitness_agent = FitnessAgent()
facts_agent = FactsAgent()
nutrition_agent = NutritionAgent()
nutrition_facts = facts_agent.get_nutrition_facts()
fitness_facts = facts_agent.get_fitness_facts()


@app.route('/')
def home():
    return render_template("index.html")

@app.route('/bodyinfo')
def bodyinfo():
    return render_template("bodyinfo.html")

@app.route('/copilot', methods=['POST'])
def copilot():
    session['agent'] = request.form.get('agent')
    session['name'] = request.form.get('name')
    session['age'] = request.form.get('age')
    session['weight'] = request.form.get('weight')
    session['height'] = request.form.get('height')
    session['gender'] = request.form.get('gender') 

    if session['agent'] == 'nutrition':
        return redirect(url_for('get_nutrition_suggestions'))
    elif session['agent'] == 'fitness':
        return redirect(url_for('get_fitness_suggestions'))
    else:
        return render_template("index.html")

@app.route('/nutrition', methods=['GET','POST'])
def get_nutrition_suggestions():
    name = session.get('name')
    age = session.get('age')
    weight = session.get('weight')
    height = session.get('height')
    gender = session.get('gender')
    food_intake = request.form.get('userInput')
    food_intake_list = ["1 cup rice", "200 gm chicken"]  
    if food_intake:
        food_intake_list = food_intake.split('\r\n')

    nutrition_info = nutrition_agent.get_nutrition_info(food_intake_list)
    nutrition_suggestions = nutrition_agent.get_suggestions(food_intake_list, nutrition_info, name, age, weight, height, gender)
    jsonify(nutrition_suggestions)
    if food_intake:
        return render_template("nutrition.html", food_intake=food_intake,  facts=nutrition_facts, nutrition_suggestions=nutrition_suggestions, nutrition_info=nutrition_info)
    else:
        return render_template("nutrition.html", food_intake="1 cup rice\n200 gm chicken",  facts=nutrition_facts, nutrition_suggestions=nutrition_suggestions, nutrition_info=nutrition_info)

@app.route('/fitness', methods=['GET','POST'])
def get_fitness_suggestions():
    name = session.get('name')
    age = session.get('age')
    weight = session.get('weight')
    height = session.get('height')
    gender = session.get('gender')
    fitness_goal = request.form.get('userInput')
    suggestions = fitness_agent.get_suggestions(fitness_goal, name, age, weight, height, gender)
    youtube_links = fitness_agent.get_youtube_links(suggestions)
    jsonify(suggestions)
    jsonify(youtube_links)
    if fitness_goal: 
        return render_template("fitness.html", facts = fitness_facts, fitness_goal=fitness_goal, suggestions=suggestions, youtube_links=youtube_links)
    else:
        return render_template("fitness.html", facts = fitness_facts, fitness_goal="Reduce weight by 10kg", suggestions=suggestions, youtube_links=youtube_links) 

if __name__ == '__main__':
    app.run(host='0.0.0.0')