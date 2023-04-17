# This is the boilerplate for the Arithmetic Formatter project. 
# Instructions for building your project can be found at 
# https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/arithmetic-formatter

def my_formatter(input: str):
  other_operators = ['/', '*', '^', '%']
  left, operator = "", None
  for index, value in enumerate(input):
    if value == ' ':
      continue
    if value == '-' and index == 0:
      left += value
      continue
    if value == '+' or value == '-':
      operator = value
      index += 1
      break
    if not value.isdigit():
      if value in other_operators:
        return False, "Error: Operator must be \'+\' or \'-\'."
      return False, "Error: Numbers must only contain digits."
    if len(left) == 4:
      return False, "Error: Numbers cannot be more than four digits."
    left += value

  right = ""
  for value in input[index:]:
    if value == ' ':
      continue
    if not value.isdigit():
      return False, "Error: Numbers must only contain digits."
    if len(right) == 4:
      return False, "Error: Numbers cannot be more than four digits."
    right += value

  return True, (left, right, operator)


class Operations:

  def __init__(self, values: tuple):
    self.left, self.right, self.operator = values
    self.my_size = max(len(self.right), len(self.left)) + 2

  def eval(self):
    if self.operator == '+':
      return str(int(self.left) + int(self.right))
    else:
      return str(int(self.left) - int(self.right))

  def str_to_line(self, i: int):
    if i == 0:
      return ' ' * (self.my_size - len(self.left)) + self.left

    if i == 1:
      return self.operator + ' ' * (self.my_size - len(self.right) -
                                    1) + self.right

    if i == 2:
      return '-' * self.my_size

    if i == 3:
      self.value = self.eval()
      return ' ' * (self.my_size - len(self.value)) + self.value


def arithmetic_arranger(*problems):
  problems = list(problems)
  to_calculate=False
  if len(problems)>1:
    to_calculate = True
  operations = problems[0]

  if len(operations) > 5:
    print(operations)
    return "Error: Too many problems."

  all_operations = []
  for p in operations:
    possible, values = my_formatter(p)
    if not possible:
      return values
    all_operations.append(values)

  all_operations = [Operations(p) for p in all_operations]

  output = ''
  t = 3 if not to_calculate else 4
  for i in range(t):
    for index, op_class in enumerate(all_operations):
      output += op_class.str_to_line(i)
      if index < len(all_operations) - 1:
        output += ' ' * 4
    if i < t - 1:
      output += '\n'

  return output
