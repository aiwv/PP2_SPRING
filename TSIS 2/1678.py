class Solution:
    def interpret(self, command):
        return command.replace("(al)", "al").replace("()", "o")