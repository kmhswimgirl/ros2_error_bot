import random

class ROSErrors:
    def get_error_msg():
        try:
            with open('error_msgs.txt', 'r') as f:
                lines = f.readlines()
                num_lines = len(lines)
                roll = random.randint(0, num_lines-1)
                return lines[roll] # return random msg
        except: FileNotFoundError
            