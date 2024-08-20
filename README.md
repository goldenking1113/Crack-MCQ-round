# Crack-your-MCQ-round

**Crack-your-MCQ-round** is a tool designed to help you effortlessly clear the first round of multiple-choice questions (MCQs) during online assessments. It captures your screen and provides answers in real-time, making the process smooth and efficient. Whether you're working in full-screen mode or need to quickly navigate through questions, this tool has got you covered.

### Advantages:
1. This is the most useful tool to clear your 1st round of MCQ.
2. It works fine in full-screen mode as well.
3. This tool does not affect full-screen mode.
4. Until you close the **Crack-your-MCQ-round** pop-up window, it will work when you click `A`..

### Disadvantages:
1. If you click the **Crack-your-MCQ-round** pop-up window, it will notify your test platform that you navigated to another window.  
   **Solution:** Do not click the **Crack-your-MCQ-round** pop-up window.
   
2. If screen sharing is enabled on your test platform, they may see that you are using this tool.  
   **Solution:** If you are asked for permission to share your screen, do not use this tool. I am working on a solution to this issue.

###How do use it
To get started with this process you have to get API in [https://aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey).

After getting the API, you update it in `API.txt`.
Like below
```bash
API_KEY="your_API"
```

To run the server, run the following commands:

Install Node packages
```bash
npm install
```
Start server
```bash
node index.js
```

Create a virtual environment named .venv
```bash
python -m venv .venv
```
Activate the virtual environment
```bash
.\.venv\Scripts\Activate
```
Install the required packages from requirements.txt
```bash
pip install -r requirements.txt
```

Run the main Python script
```bash
python main.py
```

After running this, you will get a Crack-your-MCQ-round pop-up window on your screen that asks you to press 'A' to capture.

To get started, press `A`. It will capture the current screen and answer your MCQ questions like a boss. It also shows the current status of execution.

**Main points to note:**

1. To capture the current screen, press `A`.
2. It will give you the answer.
3. Again, press `A` to capture the screen.
4. This capture process repeats until you close the pop-up window.


**Note:**  I did this just for my learning purpose. I will not be responsible for anything. Clearing aptitude rounds is difficult and not related to technical skills, which is why I made it. But this is at your own risk.