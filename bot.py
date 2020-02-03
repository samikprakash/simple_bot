class Bot:
    main_dict = {"courses":(["courses","course","offered","sem","semester","list","offer","which"],"Loading the course directory..."),"greeting":(["hi","hello","how","are","you","good","morning","afternoon","evening"],"Hi how are you today"),
            "thank":(["thanks","thank","you","helpful","ok","okay"],"Happy to help!"),"bye":(["goodbye","bye",],"See you soon!"),"options":(["what","can","you","do","how","help","me","use","do","provide","support",],"I can guide you through courses offered in college, Professors offering those courses, past record for the courses, prereqs required for this course"),
            "profs":(["what","prof","professor","which","teach","teaches","name","courses","profs","teaching"],"Loading the professor directory..."),"prereq":(["prereqs","prereq","prerequisites","prerequisite","pre","requisite","requisites","course"],"Loading pre requisite data..."),
            "past_year":(["previous","year","past","years","record","records","average","score"],"Loading previous year's data...")}
    
    ignore_words = ["a","an","the","what","is","are","this","there","in","of","to","for"]

    def __init__(self):
        pass

    def del_punct(self,x):
        x = list(x)
        punctuations = ["!",",",".","?",]
        for i in punctuations:
            if i in x:
                x.pop(x.index(i))
                
        return "".join(x)
    
    def clean(self,sentence):
        answerlist = []
        for i in sentence:
            if i not in self.ignore_words:
                answerlist.append(i)
        return answerlist
    
    def predict(self,sentence): #sentence is a list
        sent1 = self.clean(sentence)
        # print(sent1)
        probables = []
        for x in self.main_dict:
            count = 0
            for y in self.main_dict[x][0]:
                
                for i in sent1:
                    # print(i,y)
                    if i == y:
                        count += 1
            if count/len(sent1)>0.1:
                probables.append((x,count/len(sent1)))

        # print(probables)
        return probables
                    
    def response(self,sentence):
        prob = self.predict(sentence)
        prob.sort(key = lambda l:l[1],reverse = True)
        if len(prob) == 0:
            return
        else:
            return self.main_dict[prob[0][0]][1]

    def output(self,sentence):
        ans = self.response(sentence)
        if ans == None:
            
            return
        else:
            return ans

if __name__ == "__main__":
    siri = Bot()
    print("Enter quit to exit.")
    x = ""
    flag = True
    while x != "quit":
        x = input("(User): ").lower()
        x = siri.del_punct(x)
        if x=="quit":
            print("(Bot): See you soon!")
            break
        x = x.split()
        if siri.output(x)!= None and flag==True:
            print("(Bot): " + siri.output(x))
        
        elif siri.output(x) == None:
            if flag==True:
                print("Sorry I am unable to understand you, A human will be with you soon!")
            flag = False
        
        if flag == False:    
            
            a = input("(Human): ")

            if a.lower() == "bot":
                
                flag = True
