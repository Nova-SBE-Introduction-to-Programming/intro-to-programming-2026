---
title: Solo project exam question template
---

# Solo project exam question template

The project part of the exam accounts for **30% of the course grade**. It asks about your own Block 2 app. The separate general code-reading part accounts for another 30%; the team presentation accounts for 40%.

Use these question forms while building. The final exam may adapt or combine them and supply a particular input, bug, or requested change. This template does not set question counts or marks per question.

## 1. Explain one workflow

Choose a user action in your app. Explain what the user enters, which rule is checked, what the program changes, and what the user sees. Use a concrete example.

## 2. Explain the state and stored data

Identify the information your app needs to carry out that workflow. Distinguish fixed content from user progress. Explain where data is stored and what is loaded after a restart.

## 3. Predict the outcome

Given a starting state and an action, predict the resulting state. Explain why the action is accepted or rejected. State what remains unchanged if it is rejected.

Examples: use a route without its required item; try to sell more stock than exists; add an overlapping performance on the same stage.

## 4. Locate and explain a bug

Given a symptom in your app, identify the relevant function or part of the program and explain what you would inspect. Trace the connection between the screen, the rule, and stored data. Explain how you would reproduce the symptom.

## 5. Show how you verified a rule

Describe one test or manual check, including the starting state, action, and expected result. Explain which mistake it would catch and what it does not prove. Include an edge case or restart check where relevant.

## 6. Reason about a change

Explain how a new requirement would affect the workflow, rules, and stored data. Identify an existing behaviour that must keep working and a check you would add.

Examples: make an item consumable; introduce a daily operating cost; require a setup interval between performances.

## What makes an answer convincing

Tie the explanation to the app you actually built. Name the relevant data and code, use specific values, and explain cause and effect. A generic description of what the app ought to do is not evidence that you understand its implementation. Exact line numbers are not required by this template.

AI may help you build the app. You must understand the result well enough to explain it yourself. The exam permits an A4 cheat sheet, as described on the [evaluation page](../../evaluation.html).
