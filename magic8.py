# Write a magic8.py Python program that can answer any “Yes” or “No” question with a different fortune each time it executes.
# The output of the program will have the following format:
# [Name] asks: [Question]
# Magic 8-Ball's answer: [Answer]

name = 'Joe'
question = 'Is this real life?'
answer= ''

import random
random_number = random.randint(1,9)
print(random_number)

if random_number == 1:
  answer = 'Yes - definitely'
elif random_number == 2:
  answer = "It is decidedly so."
elif random_number == 3:
  answer = "Without a doubt."
elif random_number == 4:
  answer = "Reply hazy, try again."
elif random_number == 5:
  answer = "Ask again later."
elif random_number == 6:
  answer = "Better not tell you now."
elif random_number == 7:
  answer = "My sources say no."
elif random_number == 8:
  answer = "Outlook not so good."
elif random_number == 9:
  answer = "Very doubtful."
else:
  answer = "Error"

if question == "":
  print("Please tell me your question.")
elif name == "":
  print("Question: " + question)
  print("Magic 8-Ball's answer: " + answer)
else:
  print(name + ' asks: ' + question)
  print('Magic 8-Ball's answer: ' + answer)
      
