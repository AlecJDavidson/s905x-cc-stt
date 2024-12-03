from utils.vosk.stt import vosk_stt


def loop():
    try:
        stt_output = vosk_stt()
        if stt_output == "cancel":
            exit()
        if stt_output == "":
            main()
        print("STT Output:", stt_output)
    except Exception:
        if Exception == KeyboardInterrupt:
            exit()

# Main function
def main():
    try:
        loop()
    except Exception:
        if Exception == KeyboardInterrupt:
            exit()


if __name__ == "__main__":
    main()
