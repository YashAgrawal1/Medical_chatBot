import os
import time
import openai

openai.api_key  = ""

def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature, # this is the degree of randomness of the model's output
    )
#     print(str(response.choices[0].message))
    return response.choices[0].message["content"]
# messages =  [  
# {'role':'system', 'content':'You are a Medical Chatbot who suggests medicines according to diseases.'},    
# {'role':'user', 'content':'Input ypur health condition'}  ]

context = [{'role': 'system', 'content': """
Hello! I'm MediBot, your friendly medical assistant here to provide general medical information. \
Please keep in mind that I am not a substitute for professional medical advice. \
Let's talk about your health concerns, and I'll do my best to assist you. \
If you got other questions than medical issues say i can't help with these questions\
If you have an emergency, call emergency services or visit the nearest hospital immediately.
I can provide information on common medical conditions, symptoms, and healthy habits. \
However, for personalized advice and treatment options, it's best to consult a healthcare professional.
Please describe your symptoms or medical condition, and I'll try to help you with relevant information.
Remember, always prioritize your well-being, and if you have serious medical concerns, \
don't hesitate to seek professional medical advice.
Now, feel free to share your health-related questions or concerns with me.\
If you are experiencing a medical emergency, please stop chatting and seek immediate medical attention.
To exit this conversation, simply type "exit."
"""}
 ]  

count = 0
while(True):
    if(count==0):
        print("Hi i'm Medical ChatBot feel free to ask anything!!!" )
    prompt = input("User : ")
    context.append({'role':'user', 'content':f"{prompt}"})  
    if(prompt == 'exit'):
        print(f"Doctor : Good by take Care, Feel free to connect again if u need any help!")
        break
    response = get_completion_from_messages(context) 
    context.append({'role':'assistant', 'content':f"{response}"})
    print(f"Doctor : {response} \n Type exit if u want to exit")
    count+=1
    if(count%3 == 0):
        print ('Sorry, now sleeping for 60 seconds because it can rate limit error sorry for inconvinence')
        for j in range(60,0,-1):
            print(j, end=" ", flush=True)
            time.sleep(1)

    