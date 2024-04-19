from agents.llms import LLMS
from dotenv import load_dotenv
from flask import jsonify

load_dotenv()

class FitnessAgent:
    def __init__(self):
        None

    def get_youtube_links(self, suggestions):
        if suggestions:  
            prompt = f"""
                    Based on the workout plan given which are {suggestions}, Could you provide 3 youtube links that would help me achieve my workout plan mentioned above?

                    Provide the above youtube links like this : 
                    ["<iframe width="660" height="315" src="https://www.youtube.com/embed/iSSAk4XCsRA?si=Jer8uzljnBwddAnZ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>",
                    "<iframe width="660" height="315" src="https://www.youtube.com/embed/1fbU_MkV7NE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>"]
                    """
            model = LLMS("GEMINI")
            result = model.run(prompt)
            
            print(result.candidates[0].content.parts[0].text)
            print(jsonify(result.candidates[0].content.parts[0].text))
            return result.candidates[0].content.parts[0].text if result.candidates[0] else result.text
        else:
            return None

    def get_suggestions(self, fitness_goal, name, age, weight, height, gender):
        if fitness_goal:  
            prompt = f"""
                    As a fitness coach for Me {name} {age} year old {gender} with {height} cm  height , {weight} kgs weight,I have a fitness goal of {fitness_goal}. Could you provide a workout plan that would help me achieve this goal?
                    Give workout plan respective to the above body information.
                    Provide workout plan in this format : 
                    ["<h2>Workout Plan for You</h2>",
                    "<p><strong>Goal:</strong> {fitness_goal}</p>",
                    "<p><strong>Height:</strong> {height}</p>",
                    "<p><strong>Weight:</strong> {weight}</p>",
                    "<p><strong>Age:</strong> {age}</p>",
                    "<h3>Workout Schedule:</h3>",
                    "<p><strong>Frequency:</strong> 5-6 days per week</p>",
                    "<p><strong>Duration:</strong> 45-60 minutes per session</p>",
                    "<h3>Warm-up (5 minutes)</h3>",
                    "<p>Jumping jacks, Arm circles, Leg swings</p>",
                    "<h3>Cardiovascular Exercise (20-30 minutes)</h3>",
                    "<p>Running, Jogging, Swimming, Cycling, Rowing</p>",
                    "<h3>Strength Training (20-30 minutes)</h3>",
                    "<p>Squats, Push-ups, Planks, Lunges, Bench press</p>",
                    "<h3>Cool-down (5 minutes)</h3>",
                    "<p>Stretching, Walking, Yoga</p>",
                    "<h3>Sample Workout Plan:</h3>",
                    "<p><strong>Monday:</strong> Cardio (running for 30 minutes) + Strength Training (squats, push-ups, planks)</p>",
                    "<p><strong>Tuesday:</strong> Rest</p>",
                    "<p><strong>Wednesday:</strong> Cardio (swimming for 45 minutes) + Strength Training (lunges, bench press)</p>",
                    "<p><strong>Thursday:</strong> Rest</p>",
                    "<p><strong>Friday:</strong> Cardio (cycling for 30 minutes) + Strength Training (squats, push-ups, planks)</p>",
                    "<p><strong>Saturday:</strong> Rest</p>",
                    "<p><strong>Sunday:</strong> Yoga</p>",
                    "<h3>Additional Tips:</h3>",
                    "<p><strong>Nutrition:</strong> Focus on a nutrient-rich diet with plenty of fruits, vegetables, whole grains, and lean protein. Avoid processed foods, sugary drinks, and excessive amounts of saturated fat.</p>",
                    "<p><strong>Hydration:</strong> Drink plenty of water throughout the day, especially before, during, and after exercise.</p>",
                    "<p><strong>Rest:</strong> Get 7-9 hours of sleep per night.</p>",
                    "<p><strong>Consistency:</strong> Stick to your workout schedule as much as possible.</p>",
                    "<p><strong>Listen to your body:</strong> If you experience any pain or discomfort, stop exercising and consult a healthcare professional.</p>",
                    "<h3>Note:</h3>",
                    "<p>This is a sample workout plan and may need to be adjusted based on Indu's fitness level and progress. It's recommended to consult with a certified fitness professional for personalized guidance.</p>"]
                    """
            model = LLMS("GEMINI")
            result = model.run(prompt)
            
            # Split the result into a list of strings
            return result.candidates[0].content.parts[0].text if result.candidates[0] else result.text
        else:
            return None

agent = FitnessAgent()
#print(agent.get_suggestions("Reduce weight by 10kg", "Indu", 19,65, 164,"Female"))