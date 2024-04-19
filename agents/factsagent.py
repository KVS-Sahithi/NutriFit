from agents.llms import LLMS

class FactsAgent:
    def __init__(self):
        None

    def get_nutrition_facts(self):
        prompt = """
            Provide 30 interesting nutrition facts, each in one sentences, that can raise awareness about healthy eating habits. 

            Here is the example on it should be printed, the result should be given strictly in this format:

            ["Dark chocolate (at least 70% cacao) is a good source of antioxidants and can improve heart health in moderation.","Drinking plenty of water throughout the day keeps you hydrated and can aid in weight management."]
            Give output like the example above
            """
        model = LLMS("GEMINI")
        result = model.run(prompt)
        
        return result.candidates[0].content.parts[0].text if result.candidates[0] else result.text
    
    def get_fitness_facts(self):
        prompt = """
            Provide 30 interesting fitness facts, each in one sentences, that can raise awareness about healthy body habits

            Here is the example on it should be printed, the result should be given strictly in this format:

            ["Any amount of activity is better than none at all.","Just don't exercise too close to bedtime, or you may be too energized to go to sleep."]
            Give output like the example above
            """
        model = LLMS("GEMINI")
        result = model.run(prompt)
        
        return result.candidates[0].content.parts[0].text if result.candidates[0] else result.text

agent = FactsAgent()
# print(agent.get_facts())