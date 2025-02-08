import random

QUESTION = "question"
CHOICES = "choice"
ANSWER = "answer"
quiz = [
    {
     QUESTION:"What's the capital of Rwanda",
     CHOICES : ['A. Kigali','B. Abuja','C. Kampala','D. Bujumbura'],
     ANSWER : 'A'
    },
    {
     QUESTION:"What's the capital of France",
     CHOICES : ['A. Berlin','B. Paris','C. Brussels','D. London'],
     ANSWER : 'B'
    },
    {
     QUESTION:"What's the capital of Belgium",
     CHOICES : ['A. Kigali','B. Nziza','C. London','D. Brussels'],
     ANSWER : 'D'
    }
]
score = 0

for item in enumerate(quiz,1):
  print()
  print(item[0],item[1][QUESTION])
  for choice in item[1][CHOICES]:
      print(choice)
  userChoice = input("Enter your answer: ").upper().strip()

  if(userChoice == item[1][ANSWER]):
      print("Correct!")
      score+=1
      print()
  else:
      print(f'Incorrect the answer is {item[1][ANSWER]}')
      print()
if(score == 3):
    print("Congratulations")
print(f'Quiz ended your score was {score} out of {len(quiz)}')