import vosk
import pyaudio
import json

# Set the model path
model_path = "models/vosk-model-small-en-us-0.15"  # Update this as needed
model = vosk.Model(model_path)

# Create a recognizer
rec = vosk.KaldiRecognizer(model, 16000)

# Need to specify the sound device

USB_MIC_DEVICE_INDEX = 0

def vosk_stt():
    # Open PyAudio stream
    p = pyaudio.PyAudio()
    try:
        # Configure the microphone stream
        stream = p.open(
            format=pyaudio.paInt16,
            channels=1,
            rate=48000,  # Use the default sample rate of your USB mic
            input=True,
            frames_per_buffer=8192,
            input_device_index=USB_MIC_DEVICE_INDEX,  # Use the USB mic
        )

        # Open a text file in write mode using a 'with' block
        print("Listening for speech, say something!...")
        # Start streaming and recognize speech
        while True:
            data = stream.read(4096, exception_on_overflow=False)
            if rec.AcceptWaveform(data):
                result = json.loads(rec.Result())
                recognized_text = result.get("text", "")
                # print("Recognized Text:", recognized_text)
                return recognized_text
    except Exception as e:
        print(f"Error: {e}")

    finally:
        stream.stop_stream()
        stream.close()
        p.terminate()
