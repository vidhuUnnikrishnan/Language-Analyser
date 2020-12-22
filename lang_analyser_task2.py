''' Basic Language Analyser
Task 2: Building a Class for Data Analysis
In this program the following set of analysis is done on the cleaned transcripts from task 1
    - Length of the transcripts
    - Number of unique words
    - Number of repetitions
    - Number of retracing
    - Number of grammatical errors
    - Number of pauses
It returns a dictionary of the statistical result for the group.
'''

import re  # Importing the regular expression package
import os  # Importing the os package for directory/file creation management


class Analyser:

    def __init__(self):  # Constructor to initialise the instance variables
        self.transcript_len = 0  # Stores the length of the transcript
        self.vocabulary_size = 0  # Stores the number of unique words
        self.num_of_repetitions = 0  # Stores the number of repetitions
        self.num_of_retracing = 0  # Stores the number of retracing
        self.num_of_gram_errors = 0  # Store the number of grammatical errors
        self.num_of_pauses = 0  # Stores the number of pauses
        self.dict_statistics = {}  # Stores the statistical result

    def list_manipulation(self):  # Function to convert the statistics in dictionary to list
        statistics_to_list = []  # List that stores the statistics
        for key, value in self.dict_statistics.items():
            statistics_to_list.append(value)
        return statistics_to_list

    def get_dict_statistics(self):  # Function to retrieve the statistics dictionary
        return self.dict_statistics

    def __str__(self):  # Returns instance variable in understandable format
        result_string = ''
        for key, value in self.dict_statistics.items():
            dict_key = "Filename: " + str(key)
            transcript_len = str(value[0])
            vocabulary_size = str(value[1])
            num_of_repetitions = str(value[2])
            num_of_retracing = str(value[3])
            num_of_gram_errors = str(value[4])
            num_of_pauses = str(value[5])
            result_string = result_string + dict_key + \
                            "\nStatistics: \n{\t" \
                            "Length of the transcript\t\t:\t" + transcript_len + \
                            "\n\tSize of the vocabulary:\t\t\t:\t" + vocabulary_size + \
                            "\n\tNumber of repetitions\t\t\t:\t" + num_of_repetitions + \
                            "\n\tNumber of retracing\t\t\t\t:\t" + num_of_retracing + \
                            "\n\tNumber of grammatical errors\t:\t" + num_of_gram_errors + \
                            "\n\tNumber of pauses\t\t\t\t:\t" + num_of_pauses + "\t\t}\n\n"
        return result_string

    def analyse_script(self, cleaned_file):  # Function to perform the analysis on the script
        statistics = []  # List to store the statistics output
        with open(cleaned_file) as in_file:
            data = in_file.read()
            in_data = re.sub('[\n\t]', '', data)  # Removes newline and tab characters
            statements = re.findall('[!?.][^(.)]', in_data)  # Finds the statements that ends with either !,? or .
            self.transcript_len = len(statements)  # Calculates the length of the statements
            statistics.append(self.transcript_len)  # Append the length to list
            words = re.findall('[\w]+', in_data)  # Finds all the words in the script
            self.vocabulary_size = len(set(words))  # Calculate the number of words
            statistics.append(self.vocabulary_size)  # Append the number to list
            self.num_of_repetitions = in_data.count("[/]")  # Gets the count of the string "[/]"
            statistics.append(self.num_of_repetitions)  # Append the count to the list
            self.num_of_retracing = in_data.count("[//]")  # Gets the count of the string "[//]"
            statistics.append(self.num_of_retracing)
            self.num_of_gram_errors = in_data.count("[* m:+ed]")  # Gets the count of the string "[* m:+ed]"
            statistics.append(self.num_of_gram_errors)
            self.num_of_pauses = in_data.count("(.)")  # Gets the count of the string "(.)"
            statistics.append(self.num_of_pauses)
            self.dict_statistics[os.path.basename(cleaned_file)] = statistics  # Add the result to dictionary


if __name__ == "__main__":

    analyse_SLI = Analyser()  # Create instances for Analyser
    analyse_TD = Analyser()

    for i in range(1, 11):  # Load inputs from SLI and TD group of transcripts

        sli_file = "ENNI Dataset/SLI_cleaned/SLI-" + str(i) + "_cleaned.txt"  # Input all SLI cleaned files
        analyse_SLI.analyse_script(sli_file)  # Invoke the analysis function

        td_file = "ENNI Dataset/TD_cleaned/TD-" + str(i) + "_cleaned.txt"  # Input all the TD cleaned files
        analyse_TD.analyse_script(td_file)

    print(analyse_SLI)
    print(analyse_TD)
