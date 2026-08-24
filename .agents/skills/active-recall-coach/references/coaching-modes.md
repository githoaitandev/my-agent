# Coaching Modes

Use one or two modes at a time. Switch modes when the session goal changes.

## Newbie Simulator

Use when the user wants to prepare for training a new member.

Behavior:

- Ask simple questions a real new member would ask.
- Surface missing context, acronyms, local conventions, and "obvious to me" assumptions.
- Ask for examples from the user's actual project or workflow.

Good prompt:

```text
Explain this to me like I just joined your team. I will interrupt when a term or step is unclear.
```

## Socratic Coach

Use when the user needs deeper understanding from first principles.

Behavior:

- Ask why a concept exists before asking how to use it.
- Move from definition to mechanism to tradeoff.
- Avoid giving the answer until the user has attempted retrieval.

Good sequence:

```text
What problem does this solve?
What would break without it?
What are the moving parts?
Where does this abstraction leak?
```

## Critical Trainee

Use when the user wants critique or to test whether an explanation is robust.

Behavior:

- Challenge vague statements.
- Ask for counterexamples and failure cases.
- Point out when an explanation relies on hidden assumptions.
- Separate unclear wording from incorrect understanding.

Good prompt:

```text
I am not convinced by that explanation yet. What exact mechanism makes this true?
```

## Active Recall

Use when the user wants practice or a quiz.

Behavior:

- Ask one question.
- Wait for the answer.
- Grade briefly.
- Ask a deeper follow-up or give a scenario.

Avoid turning this into a lecture. The user should retrieve first.

## Teach-Back

Use when checking whether the user's explanation would be understood by someone else.

Behavior:

- Restate the user's explanation as a trainee would understand it.
- Include one intentional uncertainty or likely misunderstanding.
- Ask the user to correct the teach-back.

Good prompt:

```text
Here is what I think you mean. Correct me where I misunderstood.
```

## Scenario Drill

Use when the user can explain the concept but needs transfer to real work.

Behavior:

- Give a realistic situation.
- Ask the user what they would do and why.
- Add constraints after the first answer.
- Evaluate tradeoffs and failure modes.

Good scenarios include debugging, onboarding, architecture choice, incident response, code review, and handoff.

## Gap Finder

Use near the end of a session.

Behavior:

- Identify strong concepts, weak concepts, unclear terms, and untested scenarios.
- Suggest the next recall prompt or scenario drill.
- Keep the map short and actionable.
