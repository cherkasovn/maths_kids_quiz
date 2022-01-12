# maths_kids_quiz
The simply python script creates printable A4 sheets with "number sentences" of various complexity as a daily exercise for kids.

What do you need?
- Any Python 3 with the following available (via PIP) module:
-   fpdf (needed to generate the pdf)

How to use it?
At the file beginning, you introduce the following parameters to adjust to your needs:

NUMBER_PAGES=20  # how many pages for each number
NUMBER_EXAMPLES_EASY=2  # number of examples as an easy start. The quiz start with something easy to start easily
NUMBER_EXAMPLES_PER_PAGE=11 # number of (non-easy) examples. The complexity is defined by the maximum number below
MAXIMUM_NUMBER=[21, 28]         # a list of maximum numbers . Here you either introduce the maximum number of a list of maximum numbers
MINIMUM_NUMBER=[int(n/4) for n in MAXIMUM_NUMBER] # the lowest possible number(s)   

FOLDER_OUTPUT=r'c:\Users\NC\Downloads'	# where to save the pdf generated

Also oyu may find the following lines in the main text relevant. In particular, ADDITION_PROBABILITY=0.7 that defines the ratio of addition and subtraction examples
lines_easy=generate_quiz_lines(NUMBER_EXAMPLES_EASY, MAX_NUMBER=min_number,MIN_NUMBER=0, ADDITION_PROBABILITY=0.7,EMPTY_SYMBOL=EMPTY_SYMBOL)
lines_proper=generate_quiz_lines(NUMBER_EXAMPLES_PER_PAGE, MAX_NUMBER=max_number,MIN_NUMBER=min_number, ADDITION_PROBABILITY=0.2,EMPTY_SYMBO

