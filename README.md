# Kindle Vocabulary Flashcard Generator 📚🎓🧠
Enhance your vocabulary learning with Kindle Vocabulary Flashcard Generator!

This application leverages your Kindle's dictionary lookup history to create personalised Anki flashcards.

The word definitions, etymology and pronunciation are generated from the OpenAI GPT API. 

By integrating historical word lookups with detailed linguistic information, this tool aids in efficient and effective vocabulary retention.

# Key Features
- **Automatic Word Extraction**: Directly pulls words from your Kindle's `vocab.db` file, ensuring all recently looked-up words are captured for review.
- **Flexible**: Alternatively create your own list of words using `vocab.txt` instead. 

- **Comprehensive Linguistic Details**:
  - **Definitions**: Understand the meanings of words in depth.
  - **Pronunciations**: Learn how to correctly pronounce each word.
  - **Word Classes**: Identify parts of speech to improve grammatical knowledge.
  - **Etymologies**: Discover the historical origins of words to enhance memory retention.

- **Contextual Usage**:
  - **Example Sentences**: See how words are used in standard contexts.
  - **Actual Kindle Usage**: Review the exact sentences from your Kindle where each word was looked up.

- **Anki Integration**:
  - **Easy Import**: Generates a `.csv` file that can be directly imported into Anki, a popular flashcard tool.
  - **Spaced Repetition**: Utilizes Anki's algorithm to optimize learning intervals, helping you memorize words more effectively.


# Example
* The front of the card is the word, the back shows the definition (and other useful information). 
* Using Anki, you self-score how well you knew the answer.
* The algorithm then determines how often to show each card to ensure maximum retention. 
* Example card:
  
![back_v2](https://github.com/user-attachments/assets/dbdee676-848e-41f2-bf4e-682abe49dcd1)



## Explanation & Features

- The Kindle ebook device retains all your historical dictionary lookups in a file named `vocab.db`. 
- This file is used to 1) retrieve words that have been looked up and 2) the context in which they were used (ie. the sentence).
- The words are extracted and parsed using the OpenAI GPT API which is packaged into the below info for the reverse of a flash card: 
    - Definition
    - Word class
    - Pronunciation 
    - Etymology 
    - Example Usage 
    - Actual Usage (from Kindle, if available)

- The result is saved into a .CSV file. 
- This file can be uploaded directly into an Anki deck. 
- More details on Anki can be found here: https://apps.ankiweb.net/. 

## Usage

To run the application, simply run it from your command line:

`python kindle-vocabulary-flashcard-generator.py`

Ensure to place the `vocab.db` file in the same directory as the script (or alternatively `vocab.txt` containing a list of words on each line). 

The `.csv` file is saved in the same directory. 

Head over to your Anki application (either web or mobile) and select the import via text option. 

Start reviewing your cards! 

## Installation

Before running the script, you need to ensure you have Python installed on your system and the necessary Python package:

```
pip install -r requirements.txt
```
Note that you can run add your OpenAI API Key into the `config.py` file, for authenticating requests. You can also set it as an environment variable for security purposes.

## Dependencies

- Python 3.x
- OpenAI Python library
