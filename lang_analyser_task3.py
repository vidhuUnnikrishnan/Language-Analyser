''' Basic Language Analyser
Task 3: Building a Class for Data Visualisation.
The program creates a visualisation from the statistics obtained from Task 2.
Program independently ran with the Analyser from task 2 being imported in.
Visualisation on the average of the statistical analysis of each group and mean difference
are plotted.
'''

from task2_29860660 import Analyser  # Import Analyser class created for task 2

import numpy as np
import matplotlib.pyplot as plt  # Import matplotlib package for graphical visualisaton


class Visualiser:

    def __init__(self, data):  # Constructor to initialise the instance variables
        self.statistics_numpy = np.array(data)  # Converting the statistics to numpy array
        self.average_list = []  # List to store the average result of statistics
        self.mean_difference = []  # List to store the mean difference between SLI & TD statistics
        self.visualise_result = {}  # Result dictionary that stores the average and mean statistics

    def display_statistics(self):  # Returns the numpy converted statistical data in tabular format
        row, column = self.statistics_numpy.shape
        print("Length\t\tWord\tRepetition\tRetrace\t\tErrors\tPauses")
        print("___________________________________________________________\n")
        for r in range(row):
            print('{:4d}{:11d}{:12d}{:9d}{:12d}{:9d}'.format(self.statistics_numpy[r][0], self.statistics_numpy[r][1],
                                                             self.statistics_numpy[r][2], self.statistics_numpy[r][3],
                                                             self.statistics_numpy[r][4], self.statistics_numpy[r][5]))

    def get_average_list(self):  # Returns the computed average list
        return self.average_list

    def get_mean_differnece(self):  # Returns the mean difference list
        return self.mean_difference

    def compute_averages(self):  # Computes the statistics average of all the transcripts falling to a group
        row, column = self.statistics_numpy.shape  # Get the shape of the numpy
        for c in range(column):  # For loop to iterate through the numpy array column wise
            sum = 0
            for r in range(row):
                sum += self.statistics_numpy[r][c]
            self.average_list.append(sum / 10)  # Appends the average of the column to list

    def compute_mean_difference(self, in_data):  # Calculates the mean difference among the statistical lists
        self.visualise_result['SLI_Average'] = in_data
        self.visualise_result['TD_Average'] = self.average_list
        for index in range(len(self.average_list)):
            self.mean_difference.append(round(abs(self.average_list[index] - in_data[index]), 2))

        # visualise_result is the result data structure
        self.visualise_result['Mean_Difference'] = self.mean_difference

    def visualise_statistics(self):  # Function to visualise the statistical inferences
        bar_width = 0.3  # Set width of the bar
        sli_bar = self.visualise_result['SLI_Average']  # The bars to be displayed
        td_bar = self.visualise_result['TD_Average']

        # Set the x position of the bars
        r1 = np.arange(len(sli_bar))
        r2 = [x + bar_width for x in r1]

        # Plot the bars
        plt.bar(r1, sli_bar, width=bar_width, color='blue', edgecolor='black', capsize=7, label='SLI')
        plt.bar(r2, td_bar, width=bar_width, color='cyan', edgecolor='black', capsize=7, label='TD')

        # Names on the x axis
        plt.xticks([r + bar_width for r in range(len(sli_bar))],
                   ['Length', 'Word', 'Repetition', 'Retrace', 'Errors', 'Pauses'])

        plt.legend()  # Display the legend on the plot
        plt.title("SLI and TD Average Statistics")  # Set title of the plot
        plt.ylabel("Values")  # Set Y label
        plt.show()  # Display the graph

        bar_height = self.visualise_result['Mean_Difference']  # Input
        bars = ('Length', 'Word', 'Repetition', 'Retrace', 'Errors', 'Pauses')
        y_pos = np.arange(len(bars))
        plt.bar(y_pos, bar_height)  # Plot the bars
        plt.xticks(y_pos, bars)
        plt.title("Bar chart of Mean Difference")
        plt.ylabel("Values")
        plt.show()


if __name__ == "__main__":

    analyse_SLI = Analyser()  # Defining Analyser instances
    analyse_TD = Analyser()

    for i in range(1, 11):  # Loading inputs for both SLI and TD analysis
        sli_file = "ENNI Dataset/SLI_cleaned/SLI-" + str(i) + "_cleaned.txt"
        analyse_SLI.analyse_script(sli_file)
        td_file = "ENNI Dataset/TD_cleaned/TD-" + str(i) + "_cleaned.txt"
        analyse_TD.analyse_script(td_file)

    sli_statistics = analyse_SLI.list_manipulation()  # Retrieving output of Analyser in List format
    td_statistics = analyse_TD.list_manipulation()

    visualise_SLI = Visualiser(sli_statistics)  # Defining Visualiser instances
    visualise_TD = Visualiser(td_statistics)

    print("\nThe SLI statistics  are: \n")
    visualise_SLI.display_statistics()  # Display the statistics
    visualise_SLI.compute_averages()  # Invoke computer averages function to perform average calculation

    print("\nThe TD statistics are: \n")
    visualise_TD.display_statistics()
    visualise_TD.compute_averages()

    print("\nAverage of SLI statistics is\t: \t", visualise_SLI.get_average_list())     # Display the average
    print("Average of TD statistics is\t\t: \t", visualise_TD.get_average_list())

    # Invoke function to computer the mean difference
    visualise_TD.compute_mean_difference(visualise_SLI.get_average_list())

    print("Mean difference is\t\t\t\t: \t", visualise_TD.get_mean_differnece()) # Display the mean difference
    visualise_TD.visualise_statistics()     # Invoke visualise_statistics function to create the graphs
