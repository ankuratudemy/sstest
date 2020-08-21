import sys

from st2common.runners.base_action import Action

class multiplyAction(Action):
    def run(self, operand1,operand2):
        print(operand1)
        print(operand2)

        if operand1 and operand2:
            return (True, operand1 * operand2)
        return (False, 0)