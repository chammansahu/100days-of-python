from question_model import Question
from data import question_data
from quiz_brain import Quiz
question_bank=[]

# import static data
score=0;
for question in question_data:
    q_text = question["text"]
    q_ans = question["answer"]
    
    new_q = Question(q_text,q_ans)
    question_bank.append(new_q)
    
# print(question_bank[0].text)
# print(question_bank[0].answer)

quiz = Quiz(question_bank)

def start():
    while quiz.hasMoreQuestion():
        quiz.nextQuestion()


                    
print("Congratulations you finished the Quiz!!!")
print("Your Final Score is {}/{}".format(quiz.score,len(quiz.q_list)))  
    

        
