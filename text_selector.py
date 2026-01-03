class SelectText:

    def __init__(self):
        self._base_string = ""

    @property
    def base_string(self):
        return self._base_string

    def select_text(self):
        while True:
            user_input = int(input("Type\n1 - To choose a string to practice\n2 - To input a string to practice\n"))
            if user_input == 1:
                print("feature not yet implemented")  #TODO ADD THIS
                continue
            elif user_input == 2:
                self.input_string()
                break
            else:
                print("Invalid input")
                continue
    
    def input_string(self):
        self._base_string = input("Input String:")