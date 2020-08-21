import sys

from st2common.runners.base_action import Action

class multiplyAction(Action):
    def run(self, operand1,operand2):
        print(operand1)
        print(operand2)

        if operand1 and operand2:
            self.logger.info('Add action successfully completed with operand1 = %s and operand2= %s') % (operand1,operand2))
            return (True, operand1 * operand2)
        else:
            self.logger.error('Add action failed with operand1 = %s and operand2= %s') % (operand1,operand2))
            return (False, 0)