questions = ["What is the Capital of Australia?", "Who are the best teachers?"]
answers = ["Canberra", "TCC lead teachers"]
options = ["a) Sydney\nb) Melbourne\nc) Canberra\nd) Brisbane","a) NSW teachers\nb) VIC teachers\nc) SA teachers\nd) TCC lead teachers"]
choice = ["c", "d"]

score = 0
for i in range(len(questions)):
  print(questions[i])
  print(options[i])
  guess = input('guess > ')
  if guess == choice[i]:
    print('Correct!')
    score += 1
  else:
    print(f'Incorrect! The answer was {answers[i]}')
pct = score/len(questions)*100
print(f'{score} out of {len(questions)} which is {pct}%')
