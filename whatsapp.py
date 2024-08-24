import requests
import base64
from io import BytesIO
from PIL import ImageGrab
from pynput import keyboard
import threading

def take_screenshot():
    screenshot = ImageGrab.grab()
    buffered = BytesIO()
    screenshot.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue())

def upload_to_imgbb(image_base64):
    url = "https://api.imgbb.com/1/upload"
    payload = {
        'key': '5b5f2087a76922dd298c1ad2feb3b7f4',
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

def send_to_whatsapp(response):
    url = "https://api.ultramsg.com/instance69649/messages/chat"
    payload = "token=en6d5fzd8ph8crwm&to=+918189851258&body=Answer: {}".format(response)
    payload = payload.encode('utf8').decode('iso-8859-1')
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.request("POST", url, data=payload, headers=headers)
    if response.status_code != 200:
        raise Exception("Failed to send message via WhatsApp")

def on_press(key):
    if key == keyboard.KeyCode(char='a'):
        try:
            screenshot_base64 = take_screenshot()
            screenshot_url = upload_to_imgbb(screenshot_base64)
            response = send_to_local_server(screenshot_url)
            send_to_whatsapp(response)
        except Exception as e:
            print(f"An error occurred: {e}")

def start_keyboard_listener():
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    listener_thread = threading.Thread(target=start_keyboard_listener)
    listener_thread.daemon = True
    listener_thread.start()

    while True:
        pass  # Keeps the script running
