# Retro

- **What surprised us about the AI?**  
It did so many things automatically in response to fixing import issues.

When it read, "from bowling import BowlingGame  # implement this in `bowling.py`"
it created the entire bowling.py file for us.


- **Which prompt gave best leverage?**
"as per the bowling.md describe the requirements for bowling game, can you design tests to write steps by steps to implement the bowing game"

- **Where did misalignment happen? How did we catch it?**  
We didn't get to adding any lessons in the learn.md file.10th

We attempted to run the first prompt from prompt_cards.md
"""
You are the Historian. Summarize the last 15 minutes into:
1) One‑sentence goal
2) Steps we took
3) One lesson (pattern/anti‑pattern)
4) One reusable prompt (exact)
Return Markdown suitable for `docs/learn.md` (≤120 words).
"""
but it only worked for Tony.


- **Could another team restart from our docs alone? What’s missing?** 
Don't think so.

- **What will we automate next time (hook/script/check)?**
Next, would be getting the Historian prompt above to work in VS code.

Each IDE/AI pair had separate context and so there was very little to summarize with the Historian prompt.
Depends on the interactions of each user with the AI

One repository
git@github.com:barba-rossa/code-retreat.git
many separate IDE and AI interface windows.


## What did you feel?
Confused
After deciding on the Bowling Kata, it was unclear as to what approach we were taking.
We didn't determine the roles 

## 👥 Team composition (3–4 people)

| Role              | Main duty                                           | AI pattern practiced                 |
| ----------------- | --------------------------------------------------- | ------------------------------------ |
| 🧑‍💻 **Driver**  | Types, accepts/rejects AI code                      | *Lazy Coder / Chain of Small Steps*  |
| 🧭 **Navigator**  | States intent, writes tests, asks guiding questions | *Check Alignment / Predictive TDD*   |
| 📚 **Historian**  | Prompts AI for summaries, maintains `learn.md`      | *Extract Knowledge / Knowledge Docs* |
| 🤖 **AI Partner** | Coder + Reviewer + Referee (one chat session)       | *Active Partner / Focused Agent*     |

> With 3 people: rotate Historian every 15 min.
> With 4 people: rotate all 3 human roles; AI is constant.

but Kevin did navigate, Tony did Drive, and Barbosa did try being the Historian by promting the AI with
"""
You are the Historian. Summarize the last 15 minutes into:
1) One‑sentence goal
2) Steps we took
3) One lesson (pattern/anti‑pattern)
4) One reusable prompt (exact)
Return Markdown suitable for `docs/learn.md` (≤120 words).
"""
which did return an accurate summary. So this was also a good prompt.
How did it do this? By looking at the reposiory change?




- Another lesson: The Chat GPT windows doesn't show up on the Web VS code interface.