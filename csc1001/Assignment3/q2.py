class Polynomial(object):
    
    def __init__(self, original = '', variable = '', derivative = ''):
        self.original = original
        self.variable = variable
        self.derivative = derivative
    
    def reset_original(self):
        self.original = input('Please enter the original polynomial\n> ').replace(' ', '').replace('-', '+-')
        character = {'*' : 1, '^' : 1, '+' : 1, '-' : 1, '.' : 1}
        for i in range(len(self.original)):
            if not character.get(self.original[i], 0) and not self.original[i].isdigit():
                self.variable = self.original[i]
                break
        self.original = self.original.replace(self.variable, '1*' + self.variable + '^1').replace('*1', '').replace('1^', '')
        list = self.original.split('+')
        for i in range(len(list)):
            list[i] = list[i].split('*' + self.variable + '^')
            if len(list[i]) == 2:
                self.derivative += str(eval(list[i][0] + '*' + list[i][1])) + '*' + self.variable + '^' + str(eval(list[i][1] + '-1')) + '+'
        self.derivative = self.derivative.replace('*' + self.variable + '^0', '').replace('+-', '-').replace('1*', '').replace('^1', '')

    def print(self):
        print('The derivative of the polynomial is\n>', self.derivative[:-1])

polynomial = Polynomial()