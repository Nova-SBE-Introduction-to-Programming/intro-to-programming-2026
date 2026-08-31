---
title: Setup
---

# Setup

Everything you need installed before Class 1. Budget about 30 minutes. If something does not work, bring your laptop to the first class — we fix setups there.

You will install four things: **Python** (the language), **VS Code** (the editor), **GitHub Copilot** (the AI that writes with you) and a **GitHub account** (where your code lives). Then you run one app to prove it all works.

## 1. Install Python 3.12

Go to [python.org/downloads](https://www.python.org/downloads/) and download **Python 3.12** for your system. Any 3.12.x is fine.

**Windows**

- Run the installer. On the very first screen, **tick "Add python.exe to PATH"** before clicking *Install Now*. This is the step people miss.
- When it finishes, open *Terminal* (search for it in the Start menu) and type:

```
python --version
```

You should see `Python 3.12.x`.

**macOS**

- Run the `.pkg` installer and click through.
- Open *Terminal* (Cmd + Space, type "Terminal") and type:

```
python3 --version
```

You should see `Python 3.12.x`. On macOS the command is `python3`, not `python`. Everywhere this guide says `python`, type `python3`.

## 2. Install VS Code

Download from [code.visualstudio.com](https://code.visualstudio.com/) and install it like any app.

**Windows:** in the installer, tick *"Add 'Open with Code' action"* and *"Add to PATH"* — both are handy.

**macOS:** drag *Visual Studio Code* into your Applications folder. The first time you open it, macOS asks if you are sure — you are.

## 3. Install the extensions

Open VS Code. On the left edge there is a column of icons; click the one that looks like four squares (**Extensions**), or press `Ctrl+Shift+X` (Windows) / `Cmd+Shift+X` (macOS). Search and install:

- **Python** (by Microsoft) — lets VS Code understand and run Python.
- **GitHub Copilot** (by GitHub) — the AI pair programmer. It will ask you to sign in; do that in the next step.

You do **not** need Jupyter or any notebook extension for this course.

## 4. Sign in to GitHub

1. If you do not have a GitHub account, create one at [github.com](https://github.com/) using your **university email**.
2. Get **Copilot for free** as a student: go to [education.github.com/pack](https://education.github.com/pack), click *Sign up for Student Developer Pack*, and verify with your student email or card. Approval takes a few minutes to a few days. Until it is approved, the free Copilot tier still works for the first weeks.
3. Back in VS Code, click the **Accounts** icon (a person silhouette, bottom-left corner) → **Sign in with GitHub**. Your browser opens; authorise it. Copilot switches on automatically once you are signed in.

## 5. Clone your first repository

"Cloning" means downloading a copy of a project from GitHub to your computer, in a way that stays connected to the original. You will do this a lot. In this course you never type Git commands — VS Code does it through buttons.

1. Open VS Code. If you see the **Welcome** screen, click **Clone Git Repository…**. (If you do not see it: *File → New Window*, or press `Ctrl+Shift+P` / `Cmd+Shift+P`, type `Git: Clone` and press Enter.)
2. Paste the repository URL you were given in class (it looks like `https://github.com/.../splitit`) and press Enter.
3. Pick a folder on your computer for course work — for example a `nova` folder in your Documents. VS Code downloads the project there.
4. When asked *"Would you like to open the cloned repository?"*, click **Open**. If a "Do you trust the authors?" box appears, click **Yes**.

**Windows note:** if VS Code says Git is not installed, download it from [git-scm.com](https://git-scm.com/download/win), install with all the defaults, then restart VS Code. macOS usually has Git already; if it asks to install *Command Line Developer Tools*, say yes and wait.

## 6. Run a Streamlit app

Every project in this course is a small web app built with **Streamlit**. Here is how you run one.

1. In VS Code, open a terminal inside the project: menu **Terminal → New Terminal**. A panel opens at the bottom, already sitting in the project folder.
2. Install the project's dependencies (the libraries it needs). Type and press Enter:

```
pip install -r requirements.txt
```

On macOS use `pip3` if `pip` is not found. This downloads for a minute the first time; a wall of text is normal.

3. Start the app:

```
streamlit run app.py
```

4. Your browser opens at `http://localhost:8501` with the app running. Click around. That is your company's software, running on your machine.
5. To stop the app, click in the terminal and press `Ctrl+C` (also `Ctrl+C` on macOS, not Cmd).

If `streamlit` is "not recognised" or "not found", close the terminal, open a new one, and try again — the installation was fine, the terminal just needs a fresh start. If it still fails, try `python -m streamlit run app.py` (`python3` on macOS).

## You are done when…

- `python --version` says 3.12
- VS Code opens with the Python and Copilot extensions installed and you are signed in to GitHub
- A Streamlit app runs in your browser from a project you cloned

Anything stuck? Bring it to Class 1. Nobody is behind on day one.
