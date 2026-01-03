from record_audio import RecordAudio
from transcribe import TranscribeAudio
from text_selector import SelectText
from compare import Compare

def run():
    print("Welcome to Memorization Tool V2.0\n")
    st = SelectText()
    st.select_text()
    OG_string = st.base_string

    # Record and transcribe user input
    record()
    text_path = transcribe()
    # Open text file
    with open(text_path, "r", encoding="utf-8") as text_file:
        user_sentence = text_file.read()

    # Compare sentences
    c = Compare(user_sentence, OG_string)
    output_string = c.compare_sentences()
    print(output_string)

def record():
    ra = RecordAudio()
    recording = ra.record()
    ra.write_file(recording)

def transcribe():
    ta = TranscribeAudio()
    return ta.transcribe()


if __name__ == "__main__":
    run()