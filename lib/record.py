#!/usr/bin/env python3

import os
import shutil
import tempfile
import wave

import pyaudio

# Set parameters
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
CHUNK = 1024
RECORD_SETTINGS = 5


class Recorder:
    """Class to manage audio recordings."""

    def __init__(self) -> None:
        """Initialize the recorder."""
        self._dir = tempfile.mkdtemp()

    def record_n_seconds(self, num_seconds: int = 10) -> str:
        """Record a few seconds of audio, and save it to a file."""
        output_file, output_filename = tempfile.mkstemp(suffix=".wav", dir=self._dir)
        audio = pyaudio.PyAudio()
        stream = audio.open(
            format=FORMAT,
            channels=CHANNELS,
            rate=RATE,
            input=True,
            frames_per_buffer=CHUNK,
        )

        # Record audio
        print("Recording...")
        frames = []
        for i in range(0, int(RATE / CHUNK * num_seconds)):
            data = stream.read(CHUNK)
            frames.append(data)
        print("Finished recording.")

        # Stop the stream and terminate PyAudio
        stream.stop_stream()
        stream.close()
        audio.terminate()

        # Save the recorded audio as a .wav file
        wf = wave.open(output_filename, "wb")
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(audio.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b"".join(frames))
        wf.close()

        return output_filename

    def __del__(self) -> None:
        """Cleanup time."""
        if os.path.exists(self._dir):
            shutil.rmtree(self._dir)
