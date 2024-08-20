import requests
import base64
from io import BytesIO
from PIL import ImageGrab
import tkinter as tk
from pynput import keyboard
import threading

window_open = True

def take_screenshot():
    screenshot = ImageGrab.grab()
    buffered = BytesIO()
    screenshot.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue())

def upload_to_imgbb(image_base64):
    url = "https://api.imgbb.com/1/upload"
    payload = {
        'key': 'aea1014911ef618a11a303bcebf25ca7',
        'image': image_base64
    }
    response = requests.post(url, data=payload)
    if response.status_code == 200:
        json_response = response.json()
        return json_response['data']['url']
    else:
        raise Exception("Failed to upload image")

def send_to_local_server(screenshot_url):
    url = "http://localhost:3000/generate"
    payload = {
        "url": screenshot_url
    }
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        json_response = response.json()
        return json_response['response']
    else:
        raise Exception("Failed to send URL to local server")

def display_response(response, status_label):
    status_label.config(text=f"Response: {response}")

def on_press(key, status_label):
    if key == keyboard.KeyCode(char='a'):
        try:
            status_label.config(text="Taking screenshot...")
            screenshot_base64 = take_screenshot()
            status_label.config(text="Uploading screenshot to imgbb...")
            screenshot_url = upload_to_imgbb(screenshot_base64)
            status_label.config(text="Sending URL to local server...")
            response = send_to_local_server(screenshot_url)
            display_response(response, status_label)
        except Exception as e:
            status_label.config(text=f"An error occurred: {e}")

def start_keyboard_listener(status_label):
    with keyboard.Listener(on_press=lambda key: on_press(key, status_label)) as listener:
        listener.join()

def close_window():
    global window_open
    window_open = False
    root.destroy()

def main():
    global root
    root = tk.Tk()
    root.title("Crack-your-MCQ-round")
    
    root.attributes("-topmost", True)
    
    status_label = tk.Label(root, text="Press 'A' to take a screenshot...", font=("Arial", 12))
    status_label.pack(padx=20, pady=20)
    
    close_button = tk.Button(root, text="Close", command=close_window)
    close_button.pack(pady=10)

    listener_thread = threading.Thread(target=start_keyboard_listener, args=(status_label,))
    listener_thread.daemon = True
    listener_thread.start()

    root.mainloop()

if __name__ == "__main__":
    main()
