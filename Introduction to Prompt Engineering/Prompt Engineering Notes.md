## Introduction:

### Two types of Large Language Models (LLMs):
1. Base LLM -
    - trained to predict nect word
    - based on text training data

2. Instruction Tuned LLM -
    - trained to follow instructions
    - fine tuned instructions 
    - good attempts at following the instructions
    - typyically trained on base llm with huge amounts of data and further fine tune with inputs and outputs that are instructions

## Guidelines:
### Principles and Tatics while working with LLMs like ChatGPT:

Principles of Prompting are:
1. Clear and specific instructions - 
    - Clear does not mean short
    - Tactic 1: Use demlimeters to clearly indicate distinct parts of the input. Seperate different parts of text from the prompt. Eg: triple quotes """, triple backticks ```, triple dashes ---, angle brackets <>, XML tags <tag></tag>
    - Tactic 2: Ask for structured output like HTML or JSON
    - Tactic 3: Check whether conditioned are satisfied. Check assumptions required to do the task and can stop task to return something else if conditions are not satisfied.
    - Tactic 4: Few shot prompting. Give successful examples of completing tasks before asking model to perform the task. 

2. Give model time to think - 
    - If you give a model a complex task for it to complete in a short amount of time or in a small number of words, it may make up a guess that is likely to be incorrect. 
    - Can instruct model to think longer about a model to spend more computational effort on a task
    - Tactic 1: Specify the steps required to complete a task in a sequence. 
    - Tactic 2: Instruct model to work out its own solution before rushing to a conclusion
    
### Jupyter Notebook Exercises:
- Use open AI python library in jupyter notebook to access open AI API
- Install open AI library using command: !pip install openai
- Run code set up in the course on jupyter notebook to test different prompts and analyse the different outputs/results

### Model Limitations:
Hallucination - 
- Make statements that sound plausible but are not actually true
- Can try answer questions on obsure topics and make things up
- Happens because model does not knwo boundary of the vast amount of information data received on taining
- Method to Reduce hallucinations: Ask model to first find any relevant information on the text and use the quotes to answer the questions

## Iterative:

### Iterative Prompt Develoment:
- Analyse Prompt output and identify errors or changes needed
- Iteratively develop prompt to get better results based on application requirements
- Developing prompts also is an iterative process as it has to be refined based on prompt guidelines for getting desired outputs.
- Can add word limit to output
- Can ask prompt to focus on the aspects that are relevant to the intended audience
- Can ask the prompt to extract information and organize it in a table
- Run code set up in the course on jupyter notebook to test the different prompts and analyse the different outputs/results

## Summarizing:

### Summarize text:
- Run code set up in the course on jupyter notebook to test the different prompts and analyse the different summarized outputs/results
- Can summarize text with a word/sentence/character limit
- Can ask prompt to summarize text to focus on a specific purpose. eg: Summarize a product review within a given word limit to give feedback to shipping deparment and should focus on any aspects that mention shipping and delivery of the product.
- Can extract only relevant information from text 
- Can summarize multiple texts

## Inferring:

### Understanding text inference with LLMs:
- Takes texts as input and forms an analysis eg: extracting labels, names, sentiments
- To extract positive or negative sentiment in a text 
- Prompt to extract sentiment in text 
- Can get answer in a single word as either positive or negative when extracting sentiment
- can identify the different types of emotions expressed in the text 
- Can check if text is expressed in an angry tone
- can infer multiple things from a text at once
- Can infer topics discussed in a text
- Check if text contains certain topics which can be used to make news alerts for certain topics

## Transforming:

### Text Transformations with LLMs:
- transform text inputed and transforming or translating text
- LLMs are trained with muliple sources in many languages which gives the model the ability to translate languages
- Can also transform formats such as inputing HTML and outputting JSON
- can help proofread texts by checking spelling and grammar of the texts
- Can translate text from one language to another and can be used as a universal translator
- Can identify which language the text is written in
- can make multiple transaltions at once
- can translate text to another language based on informal or formal tones
- Transform tone of text. Eg: convert informal text into formal text

## Expanding:

### Text Expansion with LLMs:
- Exapanding is a task of taking a shorter piece of text such as set of instructions or a list of topics and using LLMs to generate a longer piece of text such as an email or an essay.
- Can create automated replies with LLM
- Can be useful as a brainstroming partner
- Temparture is an input parameter of a model which allows to vary the degree of exploration or randomness or creativity in the model's response
- For tasks that require reliability, predictability use temprature = 0 so degree of randomness or variety is not there
- For tasks that require variety use higher temperature like 0.3
- for tasks that reuquire alot of variety and randomness, use much higher temperatures like 0.7

# Chatbot:

### Understand how to build Custom Chatbots using LLMs:
- Open AI API call can take prompt message in role of user and return back result from the LLM
- Messages sent to LLM can have role of system, user and assistant
- Your message to ChatGPT on the web interface are the user messages
- ChatGPT's responses messages are the assistant messages
- Message set in role of system helps set the behaviour and persona of the assisstant or LLM
- Can send message in role of system as a friendly chatbot and the AI will act like that
- Have to send all previous or relevant messages to the model as each conversation with LLM is a stand alone conversation. Must provide earlier exchanges to the model
- Have to collect user and assitant messages to add to the context to send the model. Each converstation to the model is stored in a list of messages. Eg: messages = [system, user, assistant, user, assisstant] and will keep adding messages to the list with every next converstation

### How to build OrderBot Chatbot:
- Chatbot to take orders at a pizza restaurant
- Have automate the collection of user prompts and system responses to build the chatbot
- Define a helper function to collect user and system messages and store into memory
- Define context or behaviour of the LLM using message with role of system. Here, set LLM as an automated service that collects orders for a pizza restaurant. Create with higher temperature for chatbot 
- GUI set for user to add inputs and view responses
- Append another system message to instruct the model to create a json summary of the order     with details on size, toppings, sides or drink and total price. Create this message with lower temperature