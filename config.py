"""Config file for kindle-vocabulary-flashcard-generator."""

import os 
from datetime import datetime 

class Constants:
    """
    General configuration settings. 

    Attributes:
        DB_FILE_PATH (str): Default location for the Kindle DB file. 
        SESSION_PROMPT (str): Instructions provided to the model.

                              Example input: The word is "paroxysm"

        SAFETY_SETTINGS (dict): Remove censoring filters for senitive words. 

    """
    current_time = datetime.now().strftime('%Y-%m-%d_%H_%M_%S')
    OUTPUT_FILE_PATH = os.path.join(os.path.dirname(__file__), f"output_{current_time}.csv")

    DB_FILE_PATH = os.path.join(os.path.dirname(__file__), "vocab.db")
    TXT_FILE_PATH = os.path.join(os.path.dirname(__file__), "vocab.txt")

    SESSION_PROMPT = """
            
            Define the provided word following the below output. Please ensure the output uses standard ASCII characters only.




            INPUT_WORD

            ===

            [Word class]
            [Pheontic pronouncation]

            Definitions 

            Example Usage

            [Etymology]


            Here is an example for "casuistry":

            [ noun ]
            [ kazh-oo-uh-stree ]

            Definitions
            1. specious, deceptive, or oversubtle reasoning, especially in questions of morality; fallacious or dishonest application of general principles; sophistry.
            2. the application of general ethical principles to particular cases of conscience or conduct.

            Example Usage
            This excellent book provides the best evidence yet for reconsidering the merits of casuistry for clinical care. 

            Etymology
            c. 1600, "one who studies and resolves cases of conscience," from French casuiste (17c.) or Spanish casuista (the French word also might be from Spanish), Italian casista, all from Latin casus "case" (see case (n.1)) in its Medieval Latin sense "case of conscience." Often since 17c. in a sinister or contemptuous sense "over-subtle reasoner, sophist." Related: Casuistic; casuistical; casuistically.
        """
    

class OpenAIConfig:
    """
    Configuration settings for OpenAI's GPT model.

    Attributes:
        API_KEY (str): The API key for authenticating requests to OpenAI's API.
                       It is recommended to set this as an environment variable for 
                       security purposes.
        MODEL_PARAMS (dict): Parameters for configuring the GPT model, including model 
                             name, number of samples, temperature, and max tokens.
        SESSION_PROMPT (str): A prompt inherited from Constants that provides 
                              instructions for generating music recommendations using 
                              OpenAI's model.
    """
    API_KEY = ""

    # Constants
    MODEL_PARAMS = {
        "model": "gpt-4",
        "n": 1,  # of samples
        "temperature": 1.0,
        "max_tokens": 2048,
    }

    SESSION_PROMPT = Constants.SESSION_PROMPT

