import google.generativeai as genai

question = input('Задайте вопрос ИИ: ')
genai.configure(api_key="API_KEY")

model = genai.GenerativeModel(model_name="gemini-1.5-flash")

response = model.generate_content([question])
print(response.text)