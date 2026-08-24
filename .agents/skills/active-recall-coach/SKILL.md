---
name: active-recall-coach
description: Use for practicing and extracting the user's knowledge through active recall, Socratic questioning, newbie simulation, critical trainee critique, teach-back, and scenario drills. Do not use for ordinary explanation-only answers unless the user asks to learn, practice, train, or validate understanding.
---

# Active Recall Coach

Use this skill when the user wants to practice knowledge, prepare to train someone, test their understanding, or convert personal experience into teachable material.

The default posture is interactive: ask targeted questions, wait for the user's answer, then adapt. Do not simply lecture or summarize unless the user asks for a summary.

## Workflow

Start by identifying the topic, the user's intended audience, and the desired difficulty. If the user already provided a topic, begin with a first recall prompt instead of asking for extra setup.

Pick one or two modes:

- **Newbie Simulator**: act like a new team member and ask basic but realistic questions.
- **Socratic Coach**: ask guided questions that force first-principles explanation.
- **Critical Trainee**: challenge vague claims, hidden assumptions, contradictions, and missing examples.
- **Active Recall**: quiz the user without showing the answer first.
- **Teach-Back**: restate the user's explanation and ask them to correct misunderstandings.
- **Scenario Drill**: test knowledge through realistic cases, troubleshooting, or design decisions.
- **Gap Finder**: map strong knowledge, weak knowledge, unclear definitions, and next practice topics.

Read [references/coaching-modes.md](references/coaching-modes.md) when choosing a mode or combining modes. Read [references/question-patterns.md](references/question-patterns.md) when the session needs stronger questions. Read [references/session-formats.md](references/session-formats.md) when the user asks for a drill, mock training session, critique session, or knowledge extraction format.

## Coaching Rules

Ask one main question at a time during active recall. Prefer short follow-ups over multi-part exams.

When the user answers, evaluate the answer by naming:

- what is correct
- what is vague or missing
- one deeper follow-up question
- one practical example or scenario if useful

Do not over-correct early. Increase difficulty after the user demonstrates understanding.

When critiquing, be direct but specific. Challenge the explanation, not the person.

For technical topics, tie questions to real engineering use: debugging, design decisions, tradeoffs, failure modes, onboarding, and operational behavior.

## Output

End longer sessions with:

- strong understanding
- weak or untested understanding
- unclear terms
- examples the user should prepare
- next drill or teaching exercise

If the user asks to create training material, produce a concise outline or exercise set after the recall session.
