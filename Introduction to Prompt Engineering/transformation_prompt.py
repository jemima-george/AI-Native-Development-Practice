'''
Transformation Prompt Examples - Jupyter Notebook Exercises:
The prompt examples below are from the Course to understand how to transform texts using LLMs.

'''

# Translation
# This prompt example translates text from English to Spanish.

prompt = f"""
Translate the following English text to Spanish: \ 
```Hi, I would like to order a blender```
"""

# Universal Translator
# This prompt example shows how LLMs can be used as a universal translator as it can translate user text messages from one language to another

user_messages = [
  "La performance du système est plus lente que d'habitude.",  # System performance is slower than normal         
  "Mi monitor tiene píxeles que no se iluminan.",              # My monitor has pixels that are not lighting
  "Il mio mouse non funziona",                                 # My mouse is not working
  "Mój klawisz Ctrl jest zepsuty",                             # My keyboard has a broken control key
  "我的屏幕在闪烁"                                               # My screen is flashing
] 

for issue in user_messages:
    prompt = f"""
    Translate the following  text to English \
    and Korean: ```{issue}```
    """

# Tone Transformation
# This prompt example transforms the informal text into a business letter with formal tone.

prompt = f"""
Translate the following from slang to a business letter: 
'Dude, This is Joe, check out this spec on this standing lamp.'
"""

# Format Conversion
# This prompt example transforms the JSON format dictionary into HTML format table

data_json = { "resturant employees" :[ 
    {"name":"Shyam", "email":"shyamjaiswal@gmail.com"},
    {"name":"Bob", "email":"bob32@gmail.com"},
    {"name":"Jai", "email":"jai87@gmail.com"}
]}

prompt = f"""
Translate the following python dictionary from JSON to an HTML \
table with column headers and title: {data_json}
"""

# Spellcheck/Grammar check
# This prompt example check if the texts are correct and rewrites them if there are errors.

text = [ 
  "The girl with the black and white puppies have a ball.",  # The girl has a ball.
  "Yolanda has her notebook.", # ok
  "Its going to be a long day. Does the car need it’s oil changed?",  # Homonyms
  "Their goes my freedom. There going to bring they’re suitcases.",  # Homonyms
  "Your going to need you’re notebook.",  # Homonyms
  "That medicine effects my ability to sleep. Have you heard of the butterfly affect?", # Homonyms
  "This phrase is to cherck chatGPT for speling abilitty"  # spelling
]
for t in text:
    prompt = f"""Proofread and correct the following text
    and rewrite the corrected version. If you don't find
    and errors, just say "No errors found". Format response 
    as JSON format with Text and Corected Version as the keys. 
    Text:  ```{t}```"""


