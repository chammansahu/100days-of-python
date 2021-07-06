
# steps

# asking the questions
# check answer
# check end of the quiz

class Quiz:
    def __init__(self,q_list):
        self.q_number=0
        self.q_list=q_list
        
    def nextQuestion(self):
        current_q = self.q_list[self.q_number]
        # increase the question number
        self.q_number+=1
        input("Q.{}:{}?(True/False)".format(self.q_number,current_q.text))
            
        