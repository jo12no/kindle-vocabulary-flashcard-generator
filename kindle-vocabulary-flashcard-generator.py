"""Main entry point for kindle-vocabulary-flashcard-generator."""

import core.gpt_fetcher as gpt_fetcher
import core.kindle_input_parser as kindle_input_parser
import core.user_input_source as user_input_source
import csv
import config
import os
import sys

OUTPUT_FILE_PATH = config.Constants.OUTPUT_FILE_PATH
TXT_FILE_PATH = config.Constants.TXT_FILE_PATH


def extract_kindle():
    """
    Extracts data from exported Kindle device data using the Kindle parser.

    This function initializes an instance of the Kindle class from the 
    kindle_input_parser module.

    It then calls the `query` method of this instance to retrieve specific information 
    or data.

    Returns:
        list: Parsed Kindle query results, usually consisting of a list of
              tuples where each tuple represents a word and its usage example.
    """
    kindle = kindle_input_parser.Kindle()
    return kindle.query()


def extract_txt():
    """
    Extracts words from a text file.

    Raises:
        SystemExit: If the text file does not exist at the expected path.

    Returns:
        list: A list of words stripped of leading and trailing whitespace.
    """
    if not os.path.exists(TXT_FILE_PATH):
        print(f"Required text files with words not found at location: {TXT_FILE_PATH}")
        sys.exit(0)

    with open(TXT_FILE_PATH, "r") as f:
        results = [line.strip() for line in f.readlines()]

    return results


def get_user_input():
    """
    Retrieves user input on the desired source of word extraction.

    Returns:
        UserInput: An instance of UserInput class, containing the user's selection.
    """
    user_input = user_input_source.UserInput()
    return user_input.get_user_selection()


def write_to_csv(data):
    """
    Writes a list of data to a CSV file specified in the OUTPUT_FILE_PATH.

    Parameters:
        data (list): Data to be written to the CSV, typically containing word and its related info.

    Returns:
        None: Prints a confirmation message indicating that the data has been saved.
    """
    with open(OUTPUT_FILE_PATH, "a", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(data)
    print(f"Saved output {data[0]}: {OUTPUT_FILE_PATH}")


def format_input_results(input_data):
    """
    Formats the extracted input data into a usable format.

    Parameters:
        input_data (list): The input data to format, usually containing a word and usage example.

    Returns:
        tuple: A tuple containing the word and formatted usage information.

    Raises:
        Exception: If there is an error in parsing the input data.
    """
    try:
        word = input_data[0]
        usage = f"\n\nUsage:\n{input_data[1]}"
    except Exception as e:
        print(f"Unable to parse: {input_data}... {e}")
    return word, usage


def main():
    """
    Main function to orchestrate the word extraction and processing workflow based on user input.

    Steps:
        1. Gets user's choice of input source.
        2. Extracts words based on the chosen source.
        3. Fetches additional GPT-generated responses for the words.
        4. Writes results to a CSV file.

    Returns:
        None: The final operation status is printed to the console.
    """
    input_source = get_user_input().name

    if input_source == "KINDLE_DB":
        results = extract_kindle()
    elif input_source == "TXT_FILE":
        results = extract_txt()

    fetcher = gpt_fetcher.GptFetcher()

    for input in results:
        try:
            if input_source == "KINDLE_DB":  # kindle returns word + usage
                response = fetcher.fetch_gpt_response(input[0])
                word, usage = format_input_results(input)
                output = [word, f"{response}{usage}"]
            elif input_source == "TXT_FILE":  # would just be word
                response = fetcher.fetch_gpt_response(input)
                output = [input, f"{response}"]

            write_to_csv(output)
        except Exception as e:
            print(f"Error {input}: {e}")
            print("Skipping...")

    print("Completed")


main()
