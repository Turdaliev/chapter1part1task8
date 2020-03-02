# def choice_to_number(choice):
# """Convert choice to number."""
    # if choice == 'Usain':
    #     return 1
    # elif choice == 'Me':
    #     return 2
    # elif choice == 'Aybek':
    #     return 3
    # else:
    #     return choice
    
def choice_to_number(choice):
  return {'Usain': 1, 'Me': 2, 'Qazi': 3}[choice]
  
def number_to_choice(number):
  return {1: 'Usain', 2: 'Me', 3: 'Qazi'}[number]

def test_choice_to_number():
    assert choice_to_number('Usain') == 1
    assert choice_to_number('Me') == 2
    assert choice_to_number('Aybek') == 3
def test_number_to_choice():
    assert number_to_choice(1) == 'Usain'
    assert number_to_choice(2) == 'Me'
    assert number_to_choice(3) == 'Aybek'

def test_all():
try:
    test_choice_to_number()
    test_number_to_choice()
except AssertionError:
    print(‘WRONG’)
else:
    print(‘SUCCESS’)
test_all()