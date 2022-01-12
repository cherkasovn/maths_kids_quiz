# the script generates printable maths exercises ("number sentences") for kids
#
# version 0.4, updated 31 Dec 2021 by Nikolay Cherkasov
# generating maths exercises for kids


# NUMBER_PAGES=4  # so many pages with maximum number
# NUMBER_EXAMPLES_EASY=2  # number of examples as an easy start
# NUMBER_EXAMPLES_PER_PAGE=11 # number of (non-easy) examples
# MAXIMUM_NUMBER=[21, 27] # a list of maximum numbers  
# MINIMUM_NUMBER=[8,  12] # the lowest possible number(s)   

NUMBER_PAGES=20  # so many pages with maximum number
NUMBER_EXAMPLES_EASY=2  # number of examples as an easy start
NUMBER_EXAMPLES_PER_PAGE=11 # number of (non-easy) examples
MAXIMUM_NUMBER=[21, 28]         # a list of maximum numbers  
MINIMUM_NUMBER=[int(n/4) for n in MAXIMUM_NUMBER] # the lowest possible number(s)   


FOLDER_OUTPUT=r'c:\Users\NC\Downloads'

import random
import fpdf
from datetime import datetime
import os
EMPTY_SYMBOL="[     ]"   #the symbol to be filled

random.seed()
# the function generates a single quiz
def generate_quiz(MAX_NUMBER,MIN_NUMBER=0,ADDITION_PROBABILITY=0.5,EMPTY_SYMBOL="[   ]"):
    #generate_quiz(MAX_NUMBER,ADDITION_PROBABILITY=0.5):
    # MAX_NUMBER - maximum number containing in the quiz
    # ADDITION_PROBABILITY - (0.0-1.0) probability for having addition/subtraction
    
    operand=random.random()<=ADDITION_PROBABILITY
    equal=random.randint(0,1)
    unknown=random.randint(0,2)

    if operand: #addition: 1=sum; 0 - minus
        n1=random.randint(MIN_NUMBER,int(MAX_NUMBER/2))
        n2=random.randint(MIN_NUMBER,int(MAX_NUMBER/2))
        result=n1+n2
    else:
        n1=random.randint(MIN_NUMBER,MAX_NUMBER)
        n2=random.randint(MIN_NUMBER,MAX_NUMBER)

        if (n1-n2)<0: 
            n1,n2=n2,n1
        result=n1-n2
    # print(n1,n2,result,operand,equal,unknown)
    digits=[str(n1),str(n2),str(result)]
    digits[unknown]=EMPTY_SYMBOL
    if equal:   # last position
        if operand: #sum?
            quiz=digits[0]+"+"+digits[1]+"="+digits[2]
        else:
            quiz=digits[0]+"-"+digits[1]+"="+digits[2]
    else:
        if operand: #sum?
            quiz=digits[2]+"="+digits[0]+"+"+digits[1]
        else:
            quiz=digits[2]+"="+digits[0]+"-"+digits[1]
    return quiz

def generate_quiz_lines(NR_LINES, MAX_NUMBER=10,MIN_NUMBER=2,ADDITION_PROBABILITY=0.5,EMPTY_SYMBOL="[   ]"):
    lines=list()
    for _ in range(NR_LINES):
            line=generate_quiz(MAX_NUMBER,MIN_NUMBER,ADDITION_PROBABILITY,EMPTY_SYMBOL)
            lines.append(line)
    return lines


#generating pdf
pdf = fpdf.FPDF('P', 'mm', 'A4')
# Add a page
font_name="Courier"
page_current=0
page_max=NUMBER_PAGES*len(MAXIMUM_NUMBER)
for index,max_number in enumerate(MAXIMUM_NUMBER):
    if len(MINIMUM_NUMBER)==1: 
        min_number=MINIMUM_NUMBER
    else:
        min_number=MINIMUM_NUMBER[index]
        
    for n_page in range(NUMBER_PAGES):
        pdf.add_page()
        # writing the header:
        page_current+=1
        pdf.set_font(font_name, "I" , size = 12)
        header="Page "+str(page_current)+" of "+str(page_max)+". Maximum number "+str(max_number)
        pdf.cell(220,15, txt=header)
        #writing the lines
        lines_easy=generate_quiz_lines(NUMBER_EXAMPLES_EASY, MAX_NUMBER=min_number,MIN_NUMBER=0, ADDITION_PROBABILITY=0.7,EMPTY_SYMBOL=EMPTY_SYMBOL)
        lines_proper=generate_quiz_lines(NUMBER_EXAMPLES_PER_PAGE, MAX_NUMBER=max_number,MIN_NUMBER=min_number, ADDITION_PROBABILITY=0.2,EMPTY_SYMBOL=EMPTY_SYMBOL)
        lines=lines_easy+lines_proper
        pdf.set_font(font_name, size = 40)
        for line in lines:
            pdf.ln()
            pdf.multi_cell(200,10, txt = line)
          
# save the pdf with name .pdf
file_name=datetime.today().strftime(r'math_%d%m%Y_%H%M%S.pdf')
file_name=os.path.join(FOLDER_OUTPUT, file_name)
pdf.output(file_name)   
#□







