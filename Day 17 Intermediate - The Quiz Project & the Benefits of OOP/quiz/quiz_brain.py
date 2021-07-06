
# steps

# asking the questions
# check answer
# check end of the quiz

class Quiz:
    def __init__(self,q_list):
        self.q_number=0
        self.q_list=q_list
        self.score=0
    
        
    def nextQuestion(self):
        current_q = self.q_list[self.q_number]
        # increase the question number
        self.q_number+=1
        user_answer = input("Q.{}:{}?(True/False)".format(self.q_number,current_q.text))
        self.checkAnswer(user_answer,current_q.answer)
        
    def hasMoreQuestion(self):
        return self.q_number<len(self.q_list)
    
    def checkAnswer(self,user_answer,correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!!!")
            self.score+=1
        else:
            print("That`s wrong!!!")   
        print("the correct answer is {}".format(correct_answer))   
        print("Your Score is {}/{}".format(self.score,self.q_number))
        print('\n')   
