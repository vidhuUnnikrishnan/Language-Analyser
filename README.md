# Authorship Profiling

Basic language analyser is a program in python that investigates the linguistic characteristics of children suffering from some form of disorder.
The program works on the ENNI dataset which is a collection of narrative transcripts. Two sets of data were collected:
(i) Children diagnosed with Specific Language Impairment (SLI)
(ii) Children with Typical Development (TD)

Each of the narrative transcripts is a record of story telling tasked by The program focuses on the narrative produced by children.

The analyser is divided into 3 programs:
(i) Task 1 - Handling with File Contents and Pre-processing
(ii) Task 2 - Building a Class for Data Analysis
(iii) Task 3 - Building a Class for Data Visualisation

## 1. Task1
- Filter out CHI statements from the transcripts.
- Remove words that have either ‘[’ as prefix or ‘]’ as suffix but retain the following 3 symbols : [//], [/], and [* m:+ed]
- Retail words that have either ‘<’ as prefix or ‘>’ as suffix and these two symbols removed.
- Remove words that have prefixes of ‘&’ and ‘+’
- Retain words that have either ‘(’ as prefix or ‘)’ as suffix and these two symbols removed

## 2. Task2
Creates following statistics from the cleaned transcripts:
• Length of the transcript: Indicated by the number of statements
• Size of the vocabulary: Indicated by the number of unique words 
• Number of repetition for certain words or phrases: Indicated by the CHAT symbol [/] • Number of retracing for certain words or phrases: Indicated by the CHAT symbol [//] • Number of grammatical errors detected: Indicated by the CHAT symbol [* m:+ed] 
• Number of pauses made — indicated by the CHAT symbol (.)

## 3. Task3
Implements a class for visualising the statistics obtained from Task 2.
