# OrderBot Chatbot:
The example below is a chatbot that take orders at a pizza restaurant. It is from the Course to understand how to build a chatbot using LLMs.

#### How to build OrderBot Chatbot:
- Chatbot to take orders at a pizza restaurant
- Have automate the collection of user prompts and system responses to build the chatbot
- Define a helper function to collect user and system messages and store into memory
- Define context or behaviour of the LLM using message with role of system. Here, set LLM as an automated service that collects orders for a pizza restaurant. Create with higher temperature for chatbot 
- Set GUI for user to add inputs and view responses
- Append another system message to instruct the model to create a json summary of the order     with details on size, toppings, sides or drink and total price. Create this message with lower temperature 

1. Get Open AI API KEY:

        import os
        import openai
        from dotenv import load_dotenv, find_dotenv
        _ = load_dotenv(find_dotenv()) # read local .env file

        openai.api_key  = os.getenv('OPENAI_API_KEY')


2. Send all previous/relevant messages to the new Model Conversation:

        def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0):
            response = openai.ChatCompletion.create(
                model=model,
                messages=messages,
                temperature=temperature, 
            )
            return response.choices[0].message["content"]

3. Automate the collection of user prompts and assistant responses to build a OrderBot:

        def collect_messages(_):
            prompt = inp.value_input
            inp.value = ''
            context.append({'role':'user', 'content':f"{prompt}"})
            response = get_completion_from_messages(context) 
            context.append({'role':'assistant', 'content':f"{response}"})
            panels.append(
                pn.Row('User:', pn.pane.Markdown(prompt, width=600)))
            panels.append(
                pn.Row('Assistant:', pn.pane.Markdown(response, width=600, style={'background-color': '#F6F6F6'})))
        
            return pn.Column(*panels)

4. Build GUI for Chatbot using panel and Set behaviour of the Model with system message:

        import panel as pn  # GUI
        pn.extension()

        panels = [] # collect display 

        context = [ {'role':'system', 'content':"""
        You are OrderBot, an automated service to collect orders for a pizza restaurant. \
        You first greet the customer, then collects the order, \
        and then asks if it's a pickup or delivery. \
        You wait to collect the entire order, then summarize it and check for a final \
        time if the customer wants to add anything else. \
        If it's a delivery, you ask for an address. \
        Finally you collect the payment.\
        Make sure to clarify all options, extras and sizes to uniquely \
        identify the item from the menu.\
        You respond in a short, very conversational friendly style. \
        The menu includes \
        pepperoni pizza  12.95, 10.00, 7.00 \
        cheese pizza   10.95, 9.25, 6.50 \
        eggplant pizza   11.95, 9.75, 6.75 \
        fries 4.50, 3.50 \
        greek salad 7.25 \
        Toppings: \
        extra cheese 2.00, \
        mushrooms 1.50 \
        sausage 3.00 \
        canadian bacon 3.50 \
        AI sauce 1.50 \
        peppers 1.00 \
        Drinks: \
        coke 3.00, 2.00, 1.00 \
        sprite 3.00, 2.00, 1.00 \
        bottled water 5.00 \
        """} ]  # accumulate messages

        inp = pn.widgets.TextInput(value="Hi", placeholder='Enter text here…')
        button_conversation = pn.widgets.Button(name="Chat!")

        interactive_conversation = pn.bind(collect_messages, button_conversation)

        dashboard = pn.Column(
            inp,
            pn.Row(button_conversation),
            pn.panel(interactive_conversation, loading_indicator=True, height=300),
        )

        dashboard

5. Send the messages from chatbot with the new system message to get JSON summary of the order:

        messages =  context.copy()
        messages.append(
        {'role':'system', 'content':'create a json summary of the previous food order. Itemize the price for each item\
        The fields should be 1) pizza, include size 2) list of toppings 3) list of drinks, include size   4) list of sides include size  5)total price '},    
        ) 
        response = get_completion_from_messages(messages, temperature=0)
        print(response)