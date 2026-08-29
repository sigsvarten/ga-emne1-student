#build a sentence

adjective1 = input(' What is the first adjective?')
adjective2 = input(' What is this adjective?')

the_verb = input(' The verb is:' )
the_noun = input(' The noun is:')

sentence = ('This ' f'{adjective1} ' 'and ' + f'{adjective2} ' + f'{the_noun}' + ' wants to ' + f'{the_verb}' +  '.' )
print(sentence)

#print(f {'djective1}' + ' and' f' {adjective2}' + f'{the_noun}' + '. ' + 'It is ' + f' {the_verb}' )