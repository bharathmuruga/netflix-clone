import speech_recognition as sr

# Initialize recognizer
recognizer = sr.Recognizer()

def listen():
  """Captures user speech input and returns recognized text."""
  with sr.Microphone() as source:
    print("Listening...")
    audio = recognizer.listen(source)
  try:
    text = recognizer.recognize_google(audio)
    print("You said: " + text)
    return text.lower()  # Convert to lowercase for easier comparison
  except sr.UnknownValueError:
    print("Sorry, I could not understand audio")
    return None
  except sr.RequestError as e:
    print(f"Request error: {e}")
    return None

def respond(text):
  """Responds to the user based on their input."""
  if "hello" in text:
    print("Hi there! How can I help you today?")
  else:
    print("Sorry, I can't assist you with that yet.")

# Main loop (listening and responding)
while True:
  user_input = listen()
  if user_input:
    respond(user_input)
