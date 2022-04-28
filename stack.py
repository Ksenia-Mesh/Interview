bracket_dictionaty = {
                      '(': ')',
                      '[': ']',
                      '{': '}'
                      }
bracket_1 = [
              '(((([{}]))))',
              '[([])((([[[]]])))]{()}',
              '{{[()]}}'
             ]
bracket_2 = [
             '}{}',
             '{{[(])]}}',
             '[[{())}]'
             ]

# Задача 1
class Stack(list):

    def isEmpty(self):
        return len(self) == 0  # or len(self) != 0

    def push(self, х):
        self.append(х)

    def pop(self):
        if not self.isEmpty():
            p = self[-1]
            self.__delitem__(-1)
        return p

    def peek(self):
        if not self.isEmpty():
            return self[-1]

    def size(self):
        return len(self)

# Задача 2

def check_bracket(date):
    stack = Stack()
    for meaning in date:
        if meaning in bracket_dictionaty:
            stack.push(meaning)
        elif meaning == bracket_dictionaty.get(stack.peek()):
            stack.pop()
        else:
            return False
    return stack.isEmpty()

if __name__ == '__main__':
    for y in bracket_1 + bracket_2:
        print(f'{check_bracket(y)}')



