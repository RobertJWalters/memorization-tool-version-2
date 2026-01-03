import re

class Compare:

    def __init__(self, user_sentence, OG_sentence):
        self._user_sentence = self.clean(user_sentence)
        self._OG_sentence = self.clean(OG_sentence)

    @property
    def user_sentence(self):
        return self._user_sentence
    
    @property
    def OG_sentence(self):
        return self._OG_sentence
    
    def clean(self, string):
        arr = self.convert_string_to_array(string)
        return " ".join(arr)

    
    def convert_string_to_array(self, string):
        return re.findall(r'\b\w+\b', string.lower())
    
    def compare_sentences(self):
        RED_TEXT = '\033[91m'
        RESET = '\033[0m'
             
        output_string = ""
        for OG_c, usr_c in zip(self.OG_sentence, self.user_sentence):
            if OG_c == usr_c:
                output_string += OG_c
            else:
                output_string += f"{RED_TEXT}{OG_c}{RESET}"

        output_string += f"{RED_TEXT}{self.OG_sentence[len(self.user_sentence):]}{RESET}"
        return output_string