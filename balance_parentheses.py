'''
INSTRUCTIONS:

Write a program to determine if the the parentheses (),
the brackets [], and the braces {}, in a string are balanced.

For example:

{{)(}} is not balanced because ) comes before (

({)} is not balanced because ) is not balanced between {}
     and similarly the { is not balanced between ()

[({})] is balanced

{}([]) is balanced

{()}[[{}]] is balanced

'''


def balanced_parentheses(exp):
    open_chars = ('(','[','{')
    closed_chars = (')',']','}')
    mapping = dict(zip(open_chars, closed_chars))
    pilha = []
    balance = True
    for l in exp:
        if l in open_chars:
            pilha.append(l)
        elif l in closed_chars:
            if len(pilha) == 0:
                return False
            last_char = pilha.pop()
            if mapping.get(last_char) != l:
                return False
    return True