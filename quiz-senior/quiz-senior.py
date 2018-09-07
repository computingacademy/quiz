import random
import csv

from collections import namedtuple
from string import ascii_lowercase

from sheets import get_raw_sheet_data

Question = namedtuple("Question", "question answer choices correct")

def quiz(questions):
  """The actual quiz.

  Takes in a list of Questions, randomises the order of options
  and appends the choice letter to the possible choice.
  """
  score = 0
  for question in questions:
    print(question.question)
    random.shuffle(question.choices)
    for option in zip(ascii_lowercase, question.choices):
      if option[1] == question.answer:
        question.correct.append(f'{option[0]}')
      print(f'{option[0]}) {option[1]}')
    user_guess = input("Your answer > ").lower()
    if user_guess in [ans.lower() for ans in question.correct]:
      print("Correct!")
      score += 1
    else:
      print(f"Incorrect, the answer was {question.answer}")
  print(f"{score} out of {len(questions)} which is {score/len(questions)*100}%")

def get_questions_from_csv(file):
  """Get questions from a csv fileself.

  Returns:
    questions, a list of questions of type namedtuple
  """
  questions = []
  with open(file) as f:
    reader = csv.reader(f)
    for line in reader:
      (question, answer, choices, correct) = line
      choices = choices.split(',')
      correct = correct.split(',')
      q = Question(question, answer, choices, correct)
      questions.append(q)
  return questions

def get_questions_from_sheets():
  values = get_raw_sheet_data('Sheet1!A1:D')
  questions = []
  if not values:
    print('No data found.')
  else:
    for row in values:
      (question, answer, choices, correct) = row
      choices = choices.split(',')
      correct = correct.split(',')
      q = Question(question, answer, choices, correct)
      questions.append(q)
  return questions

if __name__ == "__main__":
  # questions = get_questions_from_csv('quiz.csv')
  questions = get_questions_from_sheets()
  quiz(questions)
