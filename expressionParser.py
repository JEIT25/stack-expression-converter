# Made by Jerold Amora
class Stack:
    expression = []
    stack = []
    temp = []
    operators = ['^','*','/','+','-']



    #push element
    def add(self,dataval):
        self.stack.append(dataval)

    #pop element
    def remove(self):
        if len(self.stack) <= 0:
            return("No Element in the Stack")
        else:
            return self.stack.pop()

    #see peak element
    def peak(self):
        return self.stack[-1]


    # precedence checker, returns precedence value of an operator
    def precedCheck(self, operator):
        precedValue = 0
        match operator:
            case '^':
                precedValue = 3
                return precedValue
            case '*':
                precedValue = 2
                return precedValue
            case '/':
                precedValue = 2
                return precedValue
            case '-':
                precedValue = 1
                return precedValue
            case '+':
                precedValue = 1
                return precedValue
            case _: #default
                precedValue = 0
                return precedValue



    # method that identifies and returns type of element
    def elementIdentifier(self,element):
        if element.isdigit():
            return 'number'
        else: #loops and check if element is operator if not then return operand type
            index = 0
            while index < len(self.operators):
                if element == self.operators[index] or (element == ')' or element == '('):
                    return 'operator'
                index += 1
            return 'operand'



    # expression converter
    def expressionParser(self,resultType):
        if resultType == "prefix":
            # scanning of expression using len() and index decreament
            index = len(self.expression) - 1
            while index >= 0:
                element = self.expression[index]
                if self.elementIdentifier(element) == 'operand':
                    self.temp.append(element)
                elif self.elementIdentifier(element) == 'operator':
                    if element == ')': #append closing parenthesis
                        self.stack.append(element)
                    elif element == '(': #if opening parethesis is found
                        elementt = self.remove()
                        while elementt != ')':  #then pop until closing parethensis is found
                            self.temp.append(elementt) #add popped elements to temp
                            elementt = self.remove() #remove elementt in between closing and open parenthesis
                    else:
                        if len(self.stack) == 0:
                            self.add(element)
                        elif self.precedCheck(element) == self.precedCheck(self.peak()):
                            poppedElem = self.remove()
                            self.temp.append(poppedElem)
                            self.add(element)
                        else:
                            self.add(element)
                else:
                    self.temp.append(element)
                index -= 1




        elif resultType== 'postfix':
            return
        else:
            return #infix

Astack = Stack()
Astack.expression = '(a+b)+(b+c)-5e'
Astack.expressionParser('prefix')
print(Astack.stack)
print(Astack.temp)


