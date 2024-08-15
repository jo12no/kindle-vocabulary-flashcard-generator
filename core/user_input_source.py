import enum
import sys


class UserInput:
    class WordSource(enum.Enum):
        KINDLE_DB = 1
        TXT_FILE = 2

    def get_user_selection(self):
        """
        Prompt the user to select a word source from the given options, and exit or return their choice.

        Raises:
            SystemExit: If the user decides to quit the application.

        Returns:
            WordSource: An enum member corresponding to the user's choice of word source.
        """
        print(
            "\nImport words from Kindle 'vocab.db' or 'vocab.txt' file list? Place the file this directory."
        )
        print("[1] Kindle vocab.db \n[2] vocab.txt")

        while True:
            try:
                choice = input("\nEnter your choice or [q] to quit: ")
                if choice.lower() == "q":
                    print("Exiting...")
                    sys.exit(1)

                choice = int(choice)
                return UserInput.WordSource(choice)
            except Exception as e:
                print(f"Invalid selection. Please try again {e}.")
