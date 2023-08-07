import openai
import csv

CRED = '\033[91m'
CRBLUE = '\033[94m'
CRCYAN = '\033[96m'
CRGREEN = '\033[92m'
CEND = '\033[0m'

openai.api_key = "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"

# Choose a model
MODEL_ENGINE = "text-davinci-003"

def get_response(prompt):
    """Returns the response for the given prompt using the OpenAI API."""
    completions = openai.Completion.create(
             engine = MODEL_ENGINE,
             prompt = prompt,
         max_tokens = 512,
        temperature = 0.7,
    )
    return completions.choices[0].text

def handle_input(
               input_str : str,
    conversation_history : str,
                USERNAME : str,
                 AI_NAME : str,
                 ):
    """Updates the conversation history and generates a response using GPT-3."""
    # Update the conversation history
    conversation_history += f"{USERNAME}: {input_str}\n"
   
    # Generate a response using GPT-3
    message = get_response(conversation_history)

    # Update the conversation history
    conversation_history += f"{AI_NAME}: {message}\n"

    # Print the response
    print(CRBLUE +f'{AI_NAME}: {message}'+ CEND)
    
    return str(message)

# Set the initial prompt to include a personality and habits
INITIAL_PROMPT = ('''''')
conversation_history = INITIAL_PROMPT + "\n"

USERNAME = "Input"
AI_NAME = "AI Ouputs"

rowNo=0
with open('C:/Users/ahnaf/OneDrive/Desktop/example.csv', mode='r') as inputFile:
    csvFile=csv.reader(inputFile)
    
    for rowList in csvFile:
        if(rowNo>4):
            break
        for row in rowList:
            user_input=row
            conversation_history=handle_input(user_input, conversation_history, USERNAME, AI_NAME)
            with open('C:/Users/ahnaf/OneDrive/Desktop/output.csv', mode='a') as outputFile:
                outputCSVFile=csv.writer(outputFile)
                outputCSVFile.writerow([conversation_history])
        rowNo+=1