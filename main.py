from record_audio import RecordAudio
from transcribe import TranscribeAudio
from compare import Compare

def run():
    ra = RecordAudio()
    recording = ra.record()
    ra.write_file(recording)

    ta = TranscribeAudio()
    text_path = ta.transcribe()

    with open(text_path, "r", encoding="utf-8") as text_file:
        user_sentence = text_file.read()

    c = Compare(user_sentence)
    output_string = c.compare_sentences()
    print(output_string)

if __name__ == "__main__":
    run()