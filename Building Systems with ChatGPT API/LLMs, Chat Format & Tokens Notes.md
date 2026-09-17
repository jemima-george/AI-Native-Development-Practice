# Fundamentals of Building Systems with the ChatGPT API

## Language Models:
- Main tool to train LLM is supervised machine learning 
- Uses input and output mapping using labelled training data
- Process of supervised learning is to get labelled data, train model on data and then deploy and call the model

### Two types of Large Language Models (LLMs):
1. Base LLM -
    - trained to predict nect word
    - based on text training data

2. Instruction Tuned LLM -
    - trained to follow instructions
    - fine tuned instructions 
    - good attempts at following the instructions
    - typyically trained on base llm with huge amounts of data and further fine tune with inputs and outputs that are instructions

### How to make a Base LLM into instruction tuned LLM:
1. Train base LLM on model data
2. Further train model by fine tunning on examples where output follows input instructions
3. Obtain human ratings on quality of different LLM outputs - helpful, honest etc
4. Further tune LLM to increase probability that it generates the more highly rated outputs 

## Chat Format:
### System, User and Assistant Messages:
- Messages sent to LLM can have role of system, user and assistant
- Your message to ChatGPT on the web interface are the user messages
- ChatGPT's responses messages are the assistant messages
- Message set in role of system helps set the behaviour/tone/persona of the assisstant or LLM
- Can send message in role of system as a friendly chatbot and the AI will act like that

## Tokens:
- LLMs do not actually predict the next word, they predict next token
- LLM Takes a sequence of characters and group them to form tokens that comprise of commonly occuring sequences of characters
- Eg: If a phrase like 'Learning new things is fun' is passed into an LLM and all the words are commonly used words/sequences of characters, then it takes each word as a token.
- But if a phrase like 'Prompting is a powerful tool' is fun' is passed into an LLM and the word prompting is not a commonly used word so the word is broken down into more tokens/sequences which are more commonly occuring.
- different models have different token limits on the number tokens in input context and output completion 

### Function to Check how many tokens used with LLM chat:
Get LLM response content and Token count used in the prompt and response -
 
        def get_completion_and_token_count(messages, 
                                        model="gpt-3.5-turbo", 
                                        temperature=0, 
                                        max_tokens=500):
            
            response = openai.ChatCompletion.create(
                model=model,
                messages=messages,
                temperature=temperature, 
                max_tokens=max_tokens,
            )
            
            content = response.choices[0].message["content"]
            
            token_dict = {
                'prompt_tokens':response['usage']['prompt_tokens'],
                'completion_tokens':response['usage']['completion_tokens'],
                'total_tokens':response['usage']['total_tokens'],
            }

            return content, token_dict

Example LLM call -

        messages = [
            {'role':'system', 
            'content':"""You are an assistant who responds\
            in the style of Dr Seuss."""},    
            {'role':'user',
            'content':"""write me a very short poem \ 
            about a happy carrot"""},  
        ] 
        response, token_dict = get_completion_and_token_count(messages)

        print(response)

        print(token_dict)
