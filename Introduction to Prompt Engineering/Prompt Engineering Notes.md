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
- Run code set up in the course on jupyter notebook to test different prompt outputs/results

### Model Limitations:
Hallucination - 
- Make statements that sound plausible but are not actually true
- Can try answer questions on obsure topics and make things up
- Happens because model does not knwo boundary of the vast amount of information data received on taining
- Method to Reduce hallucinations: Ask model to first find any relevant information on the text and use the quotes to answer the questions