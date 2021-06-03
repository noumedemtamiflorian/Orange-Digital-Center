class Message:

    def __init__(self,message):
        self.message = message
      
    
    def  warning(self):
        return "\033[93m{}\033[0m".format(self.message)
    def  success(self):
        return "\033[92m{}\033[0m".format(self.message)
    def  danger(self):
        return "\033[91m{}\033[0m".format(self.message)
    def info(self):
        return "\033[94m{}\033[0m".format(self.message)  
    def magenta(self):
        return "\033[95m{}\033[0m".format(self.message)
