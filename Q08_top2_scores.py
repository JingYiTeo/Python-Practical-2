NStudents = int(input("Please Enter Number of Students: "))

Names = []
Scores = []

for i in range(NStudents):
    Name = str(input("Please enter Name: "))
    Score = int(input("Please enter Score: "))
    Names.append(Name)
    Scores.append(Score)
    Scores, Names = (list(t) for t in zip(*sorted(zip(Scores, Names))))


print("{} with {} marks has the highest score.\n {} with {} marks has the second highest score.".format(Names[len(Names)-1], Scores[len(Scores)-1], Names[len(Names)-2], Scores[len(Scores)-2]))
    
    

    
            
