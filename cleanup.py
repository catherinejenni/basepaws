import csv
import pandas as pd

questions = [] 
answers = []
missed_rows = dict()

with open('survey.tab') as file:
    reader = csv.reader(file, delimiter='\t') 
    counter = 0
    for row in reader:
        try:
            if row[0]=='QUES':
                question = dict()
                question['row_count'] = counter
                question['platform'] = row[1]
                question['q_id'] = row[2]
                question['text'] = row[3]
                question['answers'] = row[4:]
                questions.append(question)
            elif row[0]=='RES':
                answer = dict()
                answer['row_count'] = counter
                answer['platform'] = row[1]
                answer['cat_id'] = row[2]
                answer['q_id'] = row[3]
                answer['text'] = row[4:]
                answers.append(answer)
            elif row[0]=='STAT':
                print('GENERAL STATISTICS ABOUT FILE')
                print(row)
            else:
                # row[0] since all missed rows have len < 1
                answers[-1]['text'].append(row[0])
            counter +=1
        except IndexError:
            pass

answers = pd.DataFrame(answers)
questions = pd.DataFrame(questions)

answers.to_csv('answers.csv', index=False)
questions.to_csv('questions.csv', index=False)

# GENERAL STATISTICS ABOUT FILE
# ['STAT', 'typeform', 'question_count', '600']
# GENERAL STATISTICS ABOUT FILE
# ['STAT', 'typeform', 'response_count', '4567']
# GENERAL STATISTICS ABOUT FILE
# ['STAT', 'typeform', 'response_matched_count', '3589']
# GENERAL STATISTICS ABOUT FILE
# ['STAT', 'basepaws', 'question_count', '208']
# GENERAL STATISTICS ABOUT FILE
# ['STAT', 'basepaws', 'response_count', '5913']
# GENERAL STATISTICS ABOUT FILE
# ['STAT', 'basepaws', 'response_matched_count', '5748']