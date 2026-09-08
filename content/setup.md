---
title: Setup
---

# Setup

Everything you need installed before Class 2. Budget about 20 minutes. If something does not work, bring your laptop to class — we fix setups there.

You will install two things: **Python** (the language) and the **ChatGPT desktop app**, which contains **Codex** (the AI that reads and writes code with you). Then you run one app to prove it all works. (GitHub, where your code will live, comes in Class 3 — nothing to do about it now.)

## 1. Install Python 3.12

Go to [python.org/downloads](https://www.python.org/downloads/) and download **Python 3.12** for your system. Any 3.12.x is fine.

**Windows**

- Run the installer. On the very first screen, **tick "Add python.exe to PATH"** before clicking *Install Now*. This is the step people miss.
- When it finishes, open *Terminal* (search for it in the Start menu) and type:

```
python --version
```

You should see `Python 3.12.x`. If it opens the Microsoft Store instead, Python was installed without PATH — run the installer again and tick the box.

**macOS**

- Run the `.pkg` installer and click through.
- Open *Terminal* (Cmd + Space, type "Terminal") and type:

```
python3 --version
```

You should see `Python 3.12.x`. On macOS the command is `python3`, not `python`. Everywhere this guide says `python`, type `python3`; everywhere it says `pip`, type `pip3`.

## 2. Install the ChatGPT desktop app (Codex)

Codex is the coding side of ChatGPT. It lives inside the **ChatGPT desktop app** — the app you install, not the website. It is free.

1. Download the app from [openai.com/chatgpt/download](https://openai.com/chatgpt/download/) for macOS or Windows.
    - **macOS:** open the `.dmg` and drag *ChatGPT* into Applications. The first time you open it, macOS asks if you are sure — you are.
    - **Windows:** run the installer (or install *ChatGPT* from the Microsoft Store — same thing).
2. Open it and **sign in**. No account? Click *Sign up* and create a free one, with your university email.
3. In the **top-left corner**, open the menu and choose **Codex**. *Chat* is for talking; *Codex* is for code. You will spend the course in Codex.

You do **not** need ChatGPT Plus. The free plan includes Codex, with a cap on how much you can ask in any five-hour window — enough for a class, not enough to let it run unattended. If you hit the cap, it resets on its own; go for a coffee.

## 3. Folder, project, repository — three words for one thing

You will hear three words for what is, most of the time, the same thing on your disk. Get them straight now and half of the confusion in this course disappears.

| Word | Whose word | What it means |
|---|---|---|
| **Folder** | Your computer (Finder, File Explorer) | A directory with files in it. What you get when you unzip a download. |
| **Project** | Codex | A folder that Codex has opened. Codex remembers your conversations (*threads*) per project. Same folder, plus memory of what you asked. |
| **Repository** (*repo*) | Git and GitHub | A folder whose **history** is tracked: every change is recorded and can be undone, and the folder can be copied to and from GitHub. A folder with a memory. Yours becomes one in Class 3. |

Two ways to get a repository from GitHub onto your computer: **download a ZIP** (a plain copy — a folder, no history) or **clone** it (a copy that stays connected to GitHub — a repository). Today you download; from Class 3 you clone.

The rule that keeps everything working: **one app, one folder, one project, one repository.** Do not rename it, move it, or put it inside another project. `Documents/nova/splitit` is a good address. `Desktop/New folder (3)/splitit copy` is not.

## 4. Get a project onto your computer

1. Go to [Week 2](weeks/week-02/index.html) and download the ZIP for your group's app: `splitit.zip` or `tiny-crm.zip`.
2. Unzip it into a `nova` folder in your Documents. **Windows:** right-click the ZIP → *Extract All…* **macOS:** double-click it. You get a folder called `splitit` (or `tiny-crm`) with `app.py` inside it.
3. In Codex, choose **Open folder** (or *+* → *Open local folder*) and pick that folder — the one that contains `app.py`, not the folder above it. Codex now calls it a project.
4. Ask Codex your first question: *"What does this app do? Answer in one sentence and name the file you read."* It should answer and name `app.py` or `README.md`. If it does, everything is wired up.

## 5. Run the app

Every project in this course is a small web app built with **Streamlit**. To run it you type two commands in a *terminal* that is standing inside the project folder.

**Open a terminal in the folder**

- **Windows:** open the project folder in File Explorer, right-click on empty space, choose **Open in Terminal**.
- **macOS:** open *Terminal*, type `cd ` (with a space after it), drag the project folder from Finder into the Terminal window, press Enter.

**Then type, one at a time:**

```
pip install -r requirements.txt
streamlit run app.py
```

The first downloads the libraries the app needs — a minute of scrolling text the first time is normal. The second starts the app; your browser opens at `http://localhost:8501`. Click around. That is your company's software, running on your machine.

To stop the app, click in the terminal and press `Ctrl+C` (also `Ctrl+C` on macOS, not Cmd).

If `streamlit` is "not recognised" or "not found", close the terminal, open a new one and try again — the install was fine, the terminal just needs a fresh start. If it still fails, try `python -m streamlit run app.py`.

**The other way:** ask Codex — *"Install the requirements and run the app."* It will ask permission to run the same two commands; read them, approve them. Nice when it works, but the terminal is the way that always works, and you will need it anyway.

## 6. Working with Codex — three habits

- **Ask in plain language, name files when you can.** *"In `logic.py`, what does `add_expense` check before saving?"* beats *"is there validation?"*
- **Read before you approve.** Codex asks before it runs a command or edits a file. That prompt is not a formality: if you cannot say what the command does, click *No* and ask it to explain first.
- **Verify.** Whatever Codex claims, open the file and line it names and look. The one rule of the course: *AI is allowed everywhere; you cannot ship what you cannot explain.*

**Writing in a file** works the same way: tell Codex what to write and where — *"Under question 4 in `ONBOARDING.md`, write: …"* — then read the change it shows you before you accept it. That is how you answer the question sheet.

One more: a **thread** is one conversation. Start a new thread for a new task — long threads make Codex slower and vaguer.

## You are done when…

- `python --version` says 3.12
- The ChatGPT app opens on **Codex**, your project folder is open in it, and it answers a question about the code
- The Streamlit app runs in your browser from that folder

Anything stuck? Bring it to class. Nobody is behind on day one.
