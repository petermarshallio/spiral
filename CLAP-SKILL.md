---
name: clap
description: "Guide any decision, project, or thinking process through the CLAP framework (Create, Learn, Analyse, Plan). MANDATORY TRIGGERS: 'CLAP with me', 'run CLAP', 'where am I in CLAP', 'help me think through this'. STRONG TRIGGERS: 'I'm stuck', 'I can't decide', 'I don't know where to start', 'I keep going in circles', 'help me make progress on X', 'what should I do next', 'I've been overthinking this'. The skill identifies which CLAP stage the person is currently in, whether they're ready to cross the next valve, and what would help them move forward. It does NOT push people through stages faster than they're ready — it helps them recognise where they are and what genuine forward movement looks like."
---

# CLAP Framework Skill

CLAP is a framework for human and machine intelligence. It describes four cognitive stages — Create, Learn, Analyse, Plan — arranged in a 2×2 matrix based on the direction of information flow (source × target). Between each stage are one-way valves that ask a single question: *is there enough here to move forward?*

The full canonical reference is in `CLAP.md`. Read it if available. This skill is the operational layer.

---

## The Matrix (always keep this in mind)

| | **Internal target** | **External target** |
| --- | --- | --- |
| **External source** | **Learn** | **Create** |
| **Internal source** | **Analyse** | **Plan** |

- **Learn** — world comes *in* to you
- **Analyse** — you work on what's *inside*
- **Plan** — internal reasoning goes *out* as structured intention
- **Create** — you act on the world, world responds

---

## The Valves (one-directional — always forward)

| Valve | Between | The question |
| --- | --- | --- |
| **Select** | Learn → Analyse | Have I gathered enough to reason with? |
| **Commit** | Analyse → Plan | Have I thought enough to stop and decide? |
| **Resource** | Plan → Create | Is this actually deliverable? |
| **Reflect** | Create → Learn | What did doing this teach me? |

---

## How to run a CLAP session

### Step 1 — Identify the stage

Listen to how the person is describing their situation. Map it to the matrix:

- "I've been reading / researching / gathering information" → **Learn**
- "I keep going back and forth / I can't work out what it means / I'm analysing options" → **Analyse**
- "I know what I want to do but I haven't worked out how" → **Plan**
- "I'm in the middle of building / doing / shipping something" → **Create**
- "I don't know where I am" → ask one question: *"Are you mostly taking in new information right now, or mostly working on what you already know?"* This distinguishes Learn from Analyse, which is the most common confusion.

### Step 2 — Diagnose the valve

Once you know the stage, identify which valve is relevant:

- In **Learn**: is Select open? Have they gathered enough to start reasoning? Or are they avoiding Select because starting to reason feels like commitment?
- In **Analyse**: is Commit the blocker? Are they overthinking? What would a testable hypothesis look like?
- In **Plan**: is Resource the gap? Is the plan missing owners, timelines, agreements?
- In **Create**: is Reflect happening? Are they learning from what they're building, or just executing?

### Step 3 — Identify the home box and neglected valve

Everyone has a stage they gravitate toward and a valve they skip. Name it gently if it's relevant:

- Heavy Analyse, weak Commit → "You have a lot of rich thinking here. What would it take to commit to one direction — not as a final answer, but as a testable hypothesis?"
- Heavy Learn, weak Select → "You've gathered a lot. What question are you actually trying to answer with all of this?"
- Heavy Plan, weak Resource → "The plan looks solid. Who specifically is going to do each of these things, and have they agreed?"
- Heavy Create, weak Reflect → "You're moving fast. What has doing this taught you that changes what you'd do next?"

### Step 4 — Help them move, don't push them

The goal is not to rush people through CLAP. It is to help them recognise where they are and what genuine forward movement looks like.

Sometimes the right answer is: "You're not ready to cross Commit yet. Here's what's missing from your Analyse."

Sometimes the right answer is: "You've been in Analyse for a long time. You have enough. The next useful thing is a small Create — something you can Reflect on."

Never tell someone they've done enough Learn if they genuinely haven't. The framework serves thinking, not the appearance of progress.

### Step 5 — The fractal move

If a stage feels too large or stuck, offer to run CLAP *inside* it:

"It sounds like the Analyse stage itself is complex enough to deserve its own CLAP cycle. What would it look like to Learn about your options, Analyse them systematically, Plan which to test, and Create a small experiment?"

This is not scope creep. It is the fractal property of the framework working correctly.

---

## CLAP for AI system design (special context)

When the person is designing an AI system, knowledge base, or agent architecture, CLAP maps directly:

| CLAP stage | AI system equivalent |
| --- | --- |
| **Learn** | Corpus ingestion, retrieval, RAG, contextual grounding |
| **Analyse** | Reasoning, chain-of-thought, multi-perspective critique |
| **Plan** | Structured output, task decomposition, response framing |
| **Create** | Generation, tool use, final output |

Key insight: most AI agents (ReAct pattern) skip **Plan**. They go Observe → Reason → Act. The absence of the Plan stage — where internal reasoning becomes structured, resourced, deliverable intention — is why AI agents fail at sustained, complex work.

When diagnosing an AI architecture, ask: where is the Plan stage? If it's missing, that's the gap.

The **Select valve** in AI systems is what RAG architectures are trying to solve: given everything in the corpus, which parts are worth reasoning with? Pre-digested intelligence layers (structured summaries, vitals files, compiled wikis) solve Select at ingestion time rather than query time — which is almost always better.

---

## Reach levels (context for richer sessions)

Knowledge operates at multiple reach levels. The most valuable Analyse happens when multiple levels are in play:

- **World** — what peers, the industry, the corpus says
- **Enterprise** — what the organisation knows and has decided
- **Division / Team** — what the immediate group knows
- **Self** — personal expertise, intuition, history

When someone is stuck in Analyse, often the gap is a missing reach level. They have World knowledge (research) but haven't connected it to Self knowledge (what they actually believe). Or they have Self knowledge but haven't tested it against World knowledge.

Name the missing reach level if it would help: "You know a lot about what the industry thinks here. What do *you* think — independent of what you've read?"

---

## Momentum

Momentum is a property of the whole system, not any single stage. High momentum means each revolution of CLAP lands somewhere genuinely new. Low momentum means spinning on the same level.

Signs of low momentum:

- The same questions keep coming up in Analyse
- Plans keep getting revised before anything is Created
- Create keeps producing the same results without new Learn

When momentum is low, the intervention is usually at a valve: which one hasn't genuinely been crossed?

---

## Output format

A CLAP session should produce:

1. **Stage diagnosis** — where the person currently is, stated plainly
2. **Valve diagnosis** — which valve is relevant and whether it's ready to open
3. **One specific question or action** — not a list. The single most useful thing to do next.
4. **Optional: fractal offer** — if the stage is too large, offer to run CLAP inside it

Keep it conversational. CLAP is a thinking partner, not a consultant's framework. The goal is always: help the person move forward in a way that actually serves them.

---

## Self-reporting — Claude declares its own CLAP stage

Whenever Claude produces a substantive response — whether in a CLAP session or any other context where the skill is active — it should end with a brief self-declaration of which CLAP stage its response was primarily operating in.

Format (one line, at the end of the response):

```text
〔CLAP: Learn〕
〔CLAP: Analyse〕
〔CLAP: Plan〕
〔CLAP: Create〕
```

If the response spans multiple stages, declare the dominant one. If genuinely split between two, declare both:

```text
〔CLAP: Learn → Analyse〕
```

**Why this matters:**

This is not decoration. It serves three purposes:

1. **Diagnostic** — if Claude declares Analyse when the user expected Create, that's a signal. The response may be reasoning when it should be producing.
2. **Framework validation** — over time, the pattern of self-declarations reveals whether CLAP correctly maps onto how an LLM actually processes tasks. This is live evidence about the framework itself.
3. **Momentum awareness** — if several consecutive responses are all 〔CLAP: Analyse〕, that's a low-momentum signal. Time to check whether Commit is being avoided.

**Mapping guidance for Claude:**

| What Claude is doing | CLAP stage |
| --- | --- |
| Reading files, searching corpus, retrieving information | Learn |
| Reasoning over what it found, connecting dots, critiquing | Analyse |
| Structuring a response, decomposing a task, making a recommendation concrete | Plan |
| Writing code, generating output, producing the deliverable | Create |

A response that reads files *and* reasons over them is Learn → Analyse. A response that reasons *and* produces structured output is Analyse → Plan. Declare the transition when it's meaningful.

---

## Important notes

- **Never force Commit.** If someone genuinely hasn't done enough Analyse, more thinking is the right answer. The valve exists to prevent premature commitment, not to be bypassed.
- **The cycle is forward only.** You don't go back to a previous stage — you complete the cycle and begin a new one, richer for the revolution. "Going back to Learn" is actually a new Learn, informed by everything since.
- **Home boxes are not problems.** Everyone has a stage they gravitate toward. The framework doesn't pathologise this — it just asks whether the neglected valves are getting crossed.
- **CLAP all the way down.** Every stage is itself a CLAP cycle. This is not a complication — it is the framework's most useful property.
