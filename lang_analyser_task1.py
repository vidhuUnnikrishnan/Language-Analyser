''' Basic Language Analyser
Task 1: Handling with File Contents and Pre-processing.
In this program a set of filtering processes are done on the input
so as to obtain clean files with narratives produced by children.
The input are transcripts of both SLI and TD groups.
'''

import re  # Importing the regular expression package
import os  # Importing the os package for directory/file creation management


def filter_process(input_file, output_file, dest_dir):  # Function to handle the filtering process

    result = [] # List to store the filtered strings
    with open(input_file) as in_file:   # Open input file
        data = in_file.read()   # Read the input as a string
        chi_result = re.findall('\*CHI.*\n?[^%*]*[\..]*', data)  # Returns list of *CHI statements
        for val in chi_result:
            # Replaces *CHI with empty string
            filter = re.sub('\*CHI:\s', '', val.rstrip())
            # Removes words that have either ‘[’ as prefix or ‘]’ as suffix
            filter_a = re.sub(r"\[[^\*][^/\[]+\]", '', filter)
            # Removes words with combination of character followed by /
            filter_a = re.sub("\[[^/][^+]*\]", '', filter_a)
            # Retain words that have either ‘<’ as prefix or ‘>’ as suffix but these two symbols are removed
            filter_b = re.sub("<|>", '', filter_a)
            # Remove words that have prefixes of ‘&’ and ‘+’
            filter_c = re.sub("[+&][^e\s]+", '', filter_b)
            # Retain words that have either ‘(’ as prefix or ‘)’ as suffix but these two symbols are removed
            filter_d = re.sub("\((\w)\)", r'\1', filter_c)
            # Removes strings of (..) (...)
            filter_d = re.sub('\(\.[\.]+\)', '', filter_d)
            result.append(filter_d) # Append the resulted filtered string to result list
    output_path = os.path.join(dest_dir, output_file)   # Create output path
    with open(output_path, 'w+') as out_file:   # Open output file
        for values in result:
            out_file.write(values + '\n')   # Write result strings to output file


if __name__ == '__main__':

    SLI_dir = "ENNI Dataset/SLI_cleaned"    # Output directory locations
    TD_dir = "ENNI Dataset/TD_cleaned"

    try:
        os.makedirs(TD_dir)
        os.makedirs(SLI_dir)
    except OSError:
        pass

    for i in range(1, 11):  # Loading inputs for both SLI and TD analysis

        SLI_file = "ENNI Dataset/SLI/SLI-" + str(i) + ".txt"
        SLI_output = "SLI-" + str(i) + "_cleaned.txt"
        filter_process(SLI_file, SLI_output, SLI_dir)

        TD_file = "ENNI Dataset/TD/TD-" + str(i) + ".txt"
        TD_output = "TD-" + str(i) + "_cleaned.txt"
        filter_process(TD_file, TD_output, TD_dir)
