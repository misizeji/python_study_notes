#!/usr/bin/python3

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']

for q, a in zip(questions, answers):
    print('what is your {0}? It is {1}.'.format(q, a))