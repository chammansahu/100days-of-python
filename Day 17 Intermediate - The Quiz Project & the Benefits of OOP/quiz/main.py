from question_model import Question
from data import question_data
import pprint
from quiz_brain import Quiz
question_bank=[]

# import static data

for question in question_data:
    q_text = question["text"]
    q_ans = question["answer"]
    
    new_q = Question(q_text,q_ans)
    question_bank.append(new_q)
    
# print(question_bank[0].text)
# print(question_bank[0].answer)

quiz = Quiz(question_bank)
quiz.nextQuestion()
