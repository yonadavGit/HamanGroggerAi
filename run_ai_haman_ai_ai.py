from RealtimeSTT import AudioToTextRecorder
from playsound import playsound
from visuals import grogger_emoji
import re

def play_grogger():
    playsound("grogger.mp3")

def process_haman_text(text):
    patterns = [
        r"""
            [האכע]              
            (?:[אהוי]*[^א-ת]*)* 
            מ                  
            (?:[אהוי]*[^א-ת]*)* 
            [נן]               
        """,
        r"המען",
        r"""
                    את[מם]              
            ([^א-ת]*)* 
            מ[נן]
        """
    ]

    found = False

    def highlight_match(match):
        nonlocal found
        found = True
        return f"\033[91m{match.group(0)}\033[0m"

    for pattern in patterns:
        text = re.sub(pattern, highlight_match, text, flags=re.VERBOSE)

    return text, found

def grog_haman(text):
    if text:
        # print(f"Recognized Text: {text}")
        highlighted_text, is_found = process_haman_text(text)
        print(f"Recognized Text: {highlighted_text}")
        if is_found:
            print("Haman is in the text! Grogger!")
            print(grogger_emoji)
            play_grogger()
        else:
            print("Haman is not in the text.")
    else:
        print("No speech detected.")

if __name__ == '__main__':
    print("Wait until it says 'speak now'")
    recorder = AudioToTextRecorder(language='he', post_speech_silence_duration=0.05)
    while True:
        recorder.text(grog_haman)