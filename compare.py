class Compare:

    def __init__(self, user_sentence):
        self.OG_sentence = "And this is the testimony that God has given us eternal life," \
        " and this life is in His Son. He who has the Son has life; " \
        "he who does not have the Son of God does not have life."
        self.user_sentence = user_sentence
    
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