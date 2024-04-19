import requests
from agents.llms import LLMS
import os
from dotenv import load_dotenv

load_dotenv()

class NutritionAgent:
    def __init__(self):
        None
    
    def get_nutrition_info(self, food_intake):
        url = 'https://api.edamam.com/api/nutrition-details'
        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json',
        }
        data = {
            "title": "string",
            "ingr": food_intake,
            "url": "https://api.edamam.com/api/nutrition-details",
            "summary": "string",
            "yield": "string",
            "time": "string",
            "img": "string",
            "prep": "string"
        }

        params = {
            'app_id': os.getenv('EDAMAM_APPID'),
            'app_key': os.getenv('EDAMAM_KEY'),
            'beta': 'true',
            'force': 'true',
        }

        response = requests.post(url, headers=headers, params=params, json=data)

        if response.status_code == 400 or response.status_code == 200:
                output = response.json()
                if 'calories' not in output:
                      return "This food is not available in our data."
                self.calories = output.get("calories")

                total_nutrients = output.get("totalNutrients", {})

                self.protein = total_nutrients.get("PROCNT", {}).get("quantity", 0)
                self.total_fat = total_nutrients.get("FAT", {}).get("quantity", 0)
                self.saturated_fat = total_nutrients.get("FASAT", {}).get("quantity", 0)
                self.monounsaturated_fat = total_nutrients.get("FAMS", {}).get("quantity", 0)
                self.polyunsaturated_fat = total_nutrients.get("FAPU", {}).get("quantity", 0)
                self.cholesterol = total_nutrients.get("CHOLE", {}).get("quantity", 0)
                self.sodium = total_nutrients.get("NA", {}).get("quantity")
                self.potassium = total_nutrients.get("K", {}).get("quantity", 0)
                self.total_carbohydrates = total_nutrients.get("CHOCDF", {}).get("quantity", 0)
                self.dietary_fiber = total_nutrients.get("FIBTG", {}).get("quantity", 0)
                self.sugars = total_nutrients.get("SUGAR", {}).get("quantity", 0)
                self.vitamin_a = total_nutrients.get("VITA_RAE", {}).get("quantity", 0)
                self.vitamin_c = total_nutrients.get("VITC", {}).get("quantity", 0)
                self.vitamin_d = total_nutrients.get("VITD", {}).get("quantity", 0)
                self.vitamin_e = total_nutrients.get("TOCPHA", {}).get("quantity", 0)
                self.vitamin_k = total_nutrients.get("VITK1", {}).get("quantity", 0)
                self.calcium = total_nutrients.get("CA", {}).get("quantity", 0)
                self.iron = total_nutrients.get("FE", {}).get("quantity", 0)
                self.magnesium = total_nutrients.get("MG", {}).get("quantity", 0)
                self.phosphorus = total_nutrients.get("P", {}).get("quantity", 0)
                self.zinc = total_nutrients.get("ZN", {}).get("quantity", 0)
                self.riboflavin = total_nutrients.get("RIBF", {}).get("quantity", 0)
                self.niacin = total_nutrients.get("NIA", {}).get("quantity", 0)
                self.vitamin_b6 = total_nutrients.get("VITB6A", {}).get("quantity", 0)
                self.vitamin_b12 = total_nutrients.get("VITB12", {}).get("quantity", 0)

                # Extracting diet and health labels
                self.diet_labels = total_nutrients.get("diet_labels", [])
                self.health_labels = total_nutrients.get("healthLabels", [])
                nutrition_info = {
                                    "calories": self.calories,
                                    "protein": self.protein,
                                    "total_fat": self.total_fat,
                                    "saturated_fat": self.saturated_fat,
                                    "monounsaturated_fat": self.monounsaturated_fat,
                                    "polyunsaturated_fat": self.polyunsaturated_fat,
                                    "cholesterol": self.cholesterol,
                                    "sodium": self.sodium,
                                    "potassium": self.potassium,
                                    "total_carbohydrates": self.total_carbohydrates,
                                    "dietary_fiber": self.dietary_fiber,
                                    "sugars": self.sugars,
                                    "vitamin_a": self.vitamin_a,
                                    "vitamin_c": self.vitamin_c,
                                    "vitamin_d": self.vitamin_d,
                                    "vitamin_e": self.vitamin_e,
                                    "vitamin_k": self.vitamin_k,
                                    "calcium": self.calcium,
                                    "iron": self.iron,
                                    "magnesium": self.magnesium,
                                    "phosphorus": self.phosphorus,
                                    "zinc": self.zinc,
                                    "riboflavin": self.riboflavin,
                                    "niacin": self.niacin,
                                    "vitamin_b6": self.vitamin_b6,
                                    "vitamin_b12": self.vitamin_b12,
                                    "diet_labels": self.diet_labels,
                                    "health_labels": self.health_labels
                                }
                return nutrition_info
        else:
            print("Request failed with status code:", response.status_code)
            return None
    
    def get_suggestions(self, food_intake, nutrition_info, name, age, weight, height, gender):
        if nutrition_info:
            prompt = f"""
                    As a Dietician for {name}, a {age} year old {gender} with height {height} cm and weight {weight} kg, analyze my food intake {food_intake} for today.
                    **Today's Nutrition:** {nutrition_info}
                    **Analyze and Advise:**
                    Please analyze my food intake for today based on recommended daily intake. 
                    1. Identify any areas where my intake falls short of recommendations (macronutrients, micronutrients, calories). 
                    2. Based on the analysis, suggest specific adjustments to my diet to achieve a more balanced intake. 
                    **Additional Information:**
                    (Optional) You can include any additional information here that might be relevant, such as your current activity level or any dietary restrictions.
                    Prove the above information in this format:
                    ["<h2>Nutritional Assessment Report</h2>",
                    "<h3>Nutritional Gaps:</h3>",
                    "<p><strong>Calories:</strong> Your calorie intake of 148 is significantly below the recommended daily intake of 2,000-2,400 calories for a female of your age, height, and weight.</p>",
                    "<p><strong>Protein:</strong> Your protein intake of 7.686 g falls short of the recommended daily intake of 0.8-1.2 grams per kilogram of body weight. This equates to approximately 52-78 grams of protein per day.</p>",
                    "<p><strong>Total Carbohydrates:</strong> Your total carbohydrate intake of 11.712 g is extremely low for an active individual. The recommended daily intake is 45-65% of total calories, which translates to approximately 250-364 grams of carbohydrates.</p>",
                    "<p><strong>Dietary Fiber:</strong> Your dietary fiber intake is 0.0 g, which is significantly below the recommended intake of 25-38 grams per day.</p>",
                    "<p><strong>Vitamin C:</strong> Your vitamin C intake is 0.0 mg, falling short of the recommended daily intake of 75-90 mg.</p>",
                    "<h3>Dietary Adjustments:</h3>",
                    "<p><strong>Increase calorie intake:</strong> Aim to consume around 2,000-2,400 calories per day. This can be achieved by adding healthy snacks between meals, such as fruits, yogurt, or nuts.</p>",
                    "<p><strong>Increase protein intake:</strong> Include lean protein sources in your meals, such as chicken, fish, tofu, beans, or lentils. Aim for a daily protein intake of around 52-78 grams.</p>",
                    "<p><strong>Increase carbohydrate intake:</strong> Add whole grains, fruits, and vegetables to your meals. Start by gradually increasing your carbohydrate intake to 250-300 grams per day.</p>",
                    "<p><strong>Increase dietary fiber intake:</strong> Include fiber-rich foods in your diet, such as fruits, vegetables, whole grains, and legumes. Aim for a daily fiber intake of 25-38 grams.</p>",
                    "<p><strong>Increase vitamin C intake:</strong> Include citrus fruits, berries, or fortified foods in your diet to boost your vitamin C intake.</p>",
                    "<h3>Additional Considerations:</h3>",
                    "<p>Your current activity level is not mentioned, but if you are physically active, you may need to increase your calorie and carbohydrate intake further.</p>",
                    "<p>Any dietary restrictions should be taken into account when making dietary adjustments.</p>",
                    "<p>If you have any concerns or questions, it is advisable to consult with a registered dietitian or healthcare professional for personalized guidance.</p>"
                    ]
                    """            
            model = LLMS("GEMINI")
            result = model.run(prompt)

            return result.candidates[0].content.parts[0].text if result.candidates[0] else result.text
        else:
            return None

agent = NutritionAgent()