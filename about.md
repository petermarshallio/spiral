# Spiral — A Framework for Human and Machine Intelligence

## The Core Idea

Spiral is a framework for understanding how intelligence — human or artificial — moves from raw input to meaningful output. It describes four fundamental cognitive stages, the cast of characters who inhabit each one, the Stage Manager who decides when you're ready to meet them, and the property of momentum that determines how well the whole system works.

It is not a linear process. It is a spiral — more precisely, a **spiral**: a curve that circles through the same four positions again and again. Instead of spiralling out of control, **Spiral** is intended
to provide a mechanism to climb and to control.

## Spiralling out of control?

A generic spiral — a nautilus shell, for instance — grows bigger with every turn. That's a beautiful image, but it isn't quite honest about what happens here. This spiral is more like a staircase: the same shape on every turn — the same radius, the same four moves.

And that means you're not "spiraling." A spiral *staircase* is purposeful, it requires effort, and is about elevation. with each disciplined step.

## The Matrix

**This Is the Foundation** There is a 2×2 matrix that everything derives from.

The two axes are **source** (where does the input come from?) and **target** (where does the output go?):

| | **Internal target** | **External target** |
| --- | --- | --- |
| **External source** | **Learn** | **Build** |
| **Internal source** | **Think** | **Articulate** |

This matrix is the lens. If you understand it, you can interpret the framework in your own words — and you can map almost any cognitive framework, AI architecture, or decision-making model onto it.

- **Learn** — the world comes *in*. You absorb, accumulate, receive.
- **Think** — you work on what's *inside*. You think, connect, critique.
- **Articulate** — your internal thinking goes *out* as structured intention. You make it concrete.
- **Build** — you act on the world, and the world responds. Something new exists.

## The Four Quadrants

### Learn

**External → Internal** Taking in knowledge from the outside world. Reading. Listening. Watching. Accumulating. This is what a child does when they go to the library and come back with 90 books about cheese. It is also what an AI does when it ingests a corpus.

Learning is not passive — it requires selection. You cannot learn everything. The quality of what you choose to learn determines the quality of everything downstream.

**In AI terms:** corpus ingestion, retrieval, contextual grounding. The vitals files in a conference talk corpus are the product of Learn.

**In human terms:** research, reading, listening, observation, experience.

### Think

**Internal → Internal** Working on what you already have inside. Connecting dots. Reasoning. Critiquing. Weighing options. This is the stage where raw learning becomes understanding.

Thinking is the home box for many people — including the author of this framework. It is seductive because it feels like progress. It can become a trap. The Muse can only give you so much cover — eventually the Stage Manager walks in and asks if you're ready to go meet the Director.

**In AI terms:** reasoning, chain-of-thought — the same territory ReAct calls "Reason." The LLM Council's Perspectives are the product of Think applied to Learn.

**In human terms:** critical thinking, de Bono's Six Thinking Hats, the hermeneutic circle, dot-connecting.

### Articulate

**Internal → External** Structured intention made concrete. This is the stage that most AI agents skip — and why they fail at anything requiring sustained, coordinated effort. Articulate is where internal thinking becomes external artefact: a SMART objective, a work package, a Gantt chart, a prioritised backlog.

Articulate is not thinking about what to do. It is writing it down in a form that others — or your future self — can act on.

**In AI terms:** task decomposition, agent planning, structured output. The step between Think and Act that ReAct agents lack.

**In human terms:** project management, SMART goals, sprint planning, architectural design documents.

### Build

**External → External** Acting on the world. The world responds. Something new exists that did not exist before. This is not merely "doing" — it is the act of creation, which implies intentionality and result. A wolf can blow on your house. Build is the stage where you find out if it holds.

Build generates the raw material for the next Learn. The cycle continues.

**In AI terms:** generation, tool use, execution, deployment. The "Act" in ReAct.

**In human terms:** building, writing, shipping, speaking, deciding.

## The Cast

Each stage has someone already in it. Not a mechanism — a person, and each one wants something different from you.

The move through the spiral moves forward; you can't go back and reshoot yesterday's scene. You do not retreat to a previous stage, you complete
the cycle and begin a new one, richer for the revolution you just completed.

| Stage | Who's there | What they help you do |
| --- | --- | --- |
| **Think** | **The Muse** | Turn what Learn gathered into an actual idea |
| **Articulate** | **The Director** | Turn the idea into a take specific enough to be wrong |
| **Build** | **The Producer** | Turn the take into something that can actually be mounted |
| **Learn** | **The Critic** | Turn the verdict on what you Built into material you can use next time |

Meeting **the Director** matters most for people who live in Think, because they're the one who eventually has to leave it. The Director doesn't demand certainty. They demand a hypothesis — something specific enough to be wrong. A scientist's commitment, not a bureaucrat's sign-off.

**The Producer** is the character most often avoided. It's why houses fall down when wolves blow on them. The plan was good. Nobody checked whether it could actually be built.

**The Muse** is the character people mistake for the whole job. Inspiration feels like progress, so people camp with her long after she's given them enough to work with — that's not her fault, and it isn't a reason to stay.

**The Critic** is the character people flinch from meeting. But the verdict isn't a punishment — it's the raw material for the next Learn. Refuse to meet her and the cycle starves.

Every character is really asking the same thing, in their own language: **what are you making out of what I've given you?**

Not "are you done?" — you are never done.

None of them will come and get you, though. Knowing when to go find them is a different job entirely — that's the Stage Manager.

---

## Techniques Each Character Draws On

Each character's job description above is deliberately abstract — "turn the idea into a take specific enough to be wrong" has to mean something different for a personal decision than for a software spec. Rather than pick one universal technique per character (tried, and broke immediately on Spiral's own README example: "As a traveler, I want to visit Geneva" is not a real articulation technique), each character has a menu of established, named, well-documented methods to draw from — pick whichever one's actual domain matches the situation. The specific reference matters: it's what lets both the skill and the model agree on exactly what a name denotes, rather than a vague gesture at "be more rigorous."

### The Critic (Learn)

| Method | Specific reference | Fits because |
| --- | --- | --- |
| After-Action Review | US Army's 4-question format (expected/actual/why/next) | Converts an outcome's verdict into reusable knowledge |
| Blameless Postmortem | Google SRE Book's postmortem culture | Extracts lessons from failure without assigning blame |
| Kolb's Reflective Observation | Kolb's Experiential Learning Cycle, stage 2 specifically | Digests raw experience before forming any concept |
| Double-Loop Learning | Argyris & Schön's governing-variables model | Questions whether the goal itself was right |
| 5 Whys | Toyota Production System root-cause technique | Chases a symptom back to its actual cause |
| Start/Stop/Continue | Standard Agile retrospective format | Recurring ritual turning outcomes into forward action |

### The Muse (Think)

| Method | Specific reference | Fits because |
| --- | --- | --- |
| Socratic Method | Platonic elenchus (self-questioning to test a claim) | Interrogates a claim already held, unexamined |
| Dialectical Reasoning | Hegelian thesis-antithesis-synthesis triad | Reconciles opposing ideas already in mind |
| First Principles Thinking | Cartesian/Aristotelian decomposition to fundamentals | Strips a concept down, rebuilds from scratch |
| Six Thinking Hats | De Bono's six sequential lenses | Forces six angles onto the same material |
| Second-Order Thinking | Munger's latticework of mental models | Traces downstream consequences of an existing idea |
| Hermeneutic Circle | Whole-informs-parts-informs-whole interpretive method | Whole reframes parts; parts refine the whole |

### The Director (Articulate)

| Method | Specific reference | Fits because |
| --- | --- | --- |
| SMART Goals | Doran's 1981 Specific/Measurable/Achievable/Relevant/Time-bound | Makes intent checkable, not just aspirational |
| User Stories + Acceptance Criteria | Mike Cohn's Agile format | Frames a need as testable, falsifiable intent |
| PRD | Standard product-requirements-document format | Commits problem and requirements before building starts |
| RFC / ADR | Nygard's Context-Decision-Consequences template | Records a decision's reasoning so it's challengeable |
| The Pyramid Principle | Barbara Minto's MECE, conclusion-first structure | Leads with the answer, then structures support |
| PR-FAQ | Amazon's "Working Backwards" pre-build press release | Writes the finished result before anything's built |

### The Producer (Build)

| Method | Specific reference | Fits because |
| --- | --- | --- |
| Pre-mortem | Gary Klein's 2007 HBR "Project Premortem" | Imagines failure first, to catch it early |
| Definition of Done | Scrum Guide's completion-criteria artifact | Sets the checkable bar for "actually finished" |
| MVP / Build-Measure-Learn | Eric Ries's Lean Startup loop | Ships the smallest real thing to learn from |
| Kanban WIP Limits | Kanban Method's work-in-progress caps | Caps in-progress work so things get finished |
| PDCA's "Do" phase | Deming/Toyota Plan-Do-Check-Act cycle | Executes the plan at real scale, for real |

None of these are mandatory and none is "the" technique for a character — they're a vocabulary of well-trodden, nameable patterns to reach for instead of reasoning from a vague personality trait. See `.claude/skills/spiral/SKILL.md` for when it's appropriate to name one of these out loud versus translate it into plain language.

---

## The Stage Manager

There is a fifth presence, but it is different in kind from the other four. The Muse, the Director, the Producer, and the Critic each own one specific stage — they're waiting inside it, ready to help you do that stage's work, but none of them will come looking for you. The Stage Manager owns none of the content. Its only job is deciding when it's time to go meet them, and making the introduction.

This is not a hierarchy. The Stage Manager doesn't decide the order — the cycle already fixes that completely — and it doesn't outrank the cast. It only asks the question underneath all four of theirs: *is it time for the introduction?*

The role changes shape depending on who's in the loop:

| Flow | Who plays the Stage Manager | Grounding |
| --- | --- | --- |
| **Human, solo** | Internal executive function — the transition/initiation faculty, distinct from the content-generating faculty | Zimmerman's self-regulated learning cycle; Gollwitzer's implementation intentions; executive-function research on task-initiation (the well-documented gap between having an idea and acting on it) |
| **AI, solo** | Orchestrator logic — iteration budgets, reflection nodes, the state machine governing phase transitions | ReAct's missing Articulate step (below) is this failure mode by another name: no governance of when Think ends, so the loop thrashes or never converges |
| **AI → Human** | Whichever side holds the authority to call the cue: the assistant nudging a stalled human, or the human cutting off an over-reasoning agent | Horvitz's mixed-initiative interaction research; automation bias (deferring the cue-call to the AI even when it's wrong) |
| **Human → Human** | A distinct, named role in the group — not the person doing the Learning, Thinking, Articulating, or Building | Scrum Master; chief of staff; the literal theatrical stage manager, who calls cues but never appears onstage |
| **AI → AI** | A supervisor/manager agent whose only output is whose turn it is and whether the phase is complete | Already shipped: LangGraph's supervisor pattern, AutoGen's `GroupChatManager`, CrewAI's hierarchical-process manager, MetaGPT's SOP-driven role router |

The consistency across all five is the point. In every flow, the Stage Manager never does Learn/Think/Articulate/Build work itself — and in every flow, its absence produces the same failure: stalling, thrashing, or false momentum. Not five different failure modes. One.

### One operator, four registers

Everything above describes the Cast as company you meet. But for a solo operator — a single person working alone, or a single AI with no other agents to call on — there's no one else in the room. The Muse's associative looseness, the Director's decisiveness, the Producer's resourcefulness, the Critic's evaluative honesty: you have to produce all four yourself, in turn. Meeting the cast, solo, means becoming them for as long as their stage needs you to.

This is a different difficulty than the one Momentum names. Momentum failure is about *time* — staying too long in one stage. This is about *register* — being unable to actually think with the Muse's looseness while still holding the Critic's honesty from the stage before, or unable to drop the Director's decisiveness once Build needs the Producer's improvisation instead. Everyone is fluent in their home box's register and clumsy in at least one other — usually, unsurprisingly, the neglected character's.

The precise term for this isn't multiplicity as pathology, it's **code-switching**: deliberately changing register to fit context while one continuous self persists underneath, doing the switching. Two grounded precedents, one per register:

- **Human:** Transactional Analysis' Parent/Adult/Child ego states — distinct behavioral registers a person moves between deliberately, without losing continuity of self. De Bono's own Blue Hat (see the framework comparison below) is the same idea inside a framework Spiral is already compared to: it isn't a fifth hat alongside the other four, it's the process-control hat, worn by whoever decides which of the other four the group should be wearing — and it can think in any of them when needed.
- **AI:** a context switch, in the plain operating-systems sense — a process's state is suspended, a different process's state is loaded in and executed, and something outside both of them keeps the scheduling bookkeeping across every swap. That bookkeeping layer isn't optional decoration; without it, "switching" is just amnesia.

For an AI system this reframes what the Stage Manager actually does in solo operation. It isn't only the outside voice asking "is it time?" — it has to be able to condition itself into each stage's register (generative for Think, decisive for Articulate, resourceful for Build, evaluative for Learn), do that stage's work in that register, then step back out to the layer that tracks the whole arc and knows when the next switch is due. One operator, four registers, one continuous thread of oversight underneath all of them. That thread — not any single register — is the Stage Manager.

---

## Momentum

Momentum is not a stage. It is a property of the whole system — the rate at which you move through the spiral. The Stage Manager is what embodies that property in practice: not a sixth stage, but the role that exists to protect momentum wherever it's under threat.

**High momentum:** each revolution lands you somewhere genuinely new. The cast shows up readily because sufficient work was done in each stage.

**Low momentum:** spinning on the same level. Stuck in Thinking. Avoiding the cast. Returning to Learn because the Director was never met.

**False momentum:** moving fast but skipping stages. Lots of Build without enough Learn or Think. The house gets built quickly. Then the wolf arrives.

Momentum is killed by:

- Perfectionism in Think (the thinking trap)
- Avoiding the Producer (the execution trap)
- Insufficient Learning before Thinking (the opinion trap)

Momentum is built by:

- Meeting the Director with a testable hypothesis, not a proven answer
- Treating the Critic's verdict as genuinely generative, not just evaluation
- Allowing the next Learn to be informed by what Build revealed

## The Fractal Property — Spirals All the Way Down

Each stage of Spiral is itself a full Spiral cycle.

The Learn stage of a project *is* a Spiral cycle: you Build experiments to learn from, Learn from them, Think about what you found, Articulate the next experiment.

The Think stage of a decision *is* a Spiral cycle: you Build hypotheses, Learn what they imply, think about the implications, Articulate which to test.

This is not a metaphor. It is structurally true. Spiral scales from a five-minute decision to a thirty-year career. The same four questions, the same four characters, applied recursively at every level of granularity.

> "It's Spirals all the way down."

This fractal property means the framework is never the wrong size. If a stage feels too large to act on, run Spiral inside it. The cycle will break it into manageable revolutions.

## Non-Linearity and Entry Points

Where you start on the Spiral is up to you.

People have a **home box** — the stage they gravitate toward, where they spend disproportionate time. They also have a **neglected character** — the one they most often avoid meeting.

| Entry point | Who does this | Risk |
| --- | --- | --- |
| **Learning first** | Researchers, readers, the cautious | Never meeting the Director |
| **Thinking first** | Strategists, overthinkers | Thinking without sufficient raw material |
| **Articulating first** | Managers, executors | Articulating based on assumptions, not evidence |
| **Building first** | Builders, hackers, the impatient | Learning only from failure, expensively |

None of these is wrong. All of them are incomplete without the others.

The framework does not judge your entry point. It asks: which character have you not met recently?

## Relation to Other Frameworks

The matrix is the key to these comparisons. Spiral is not derived from any of these — it predates most of them in the author's practice — but the overlaps are illuminating.

| Framework | Learn | Think | Articulate | Build | What Spiral adds |
| --- | --- | --- | --- | --- | --- |
| **Bloom's Taxonomy** | Remember / Understand | Analyse / Evaluate | — | Create | The matrix; the cast; non-linearity |
| **Kolb's Cycle** | Concrete Experience | Reflective Observation | Abstract Conceptualisation | Active Experimentation | The cast; momentum; fractal property |
| **ReAct (AI agents)** | Observe | Think | — | Act | **Articulate** — the missing stage in most AI agents |
| **OODA Loop** | Observe | Orient | Decide | Act | Fractal property; momentum; home boxes |
| **Six Thinking Hats** | White Hat | Red/Black/Yellow | — | Green Hat | The matrix; the spiral structure; the Blue Hat is Six Thinking Hats' own Stage Manager, not an Articulate-analog — the same missing-Articulate gap ReAct has, just less visible |
| **Hermeneutic Circle** | — | The whole circle | — | — | Spiral externalises what the circle keeps internal |
| **Belbin Team Roles** | — | — | — | — | Independent validation for **the Stage Manager**: Belbin's Coordinator role was originally named "Chairman" before being renamed — the same correction, authority word to process word, that this framework just made |
| **Multi-agent orchestration** (AutoGen, CrewAI, LangGraph) | Retrieval / tool nodes | Worker-agent reasoning | Task routing | Worker-agent execution | Confirms **the Stage Manager** is buildable: supervisor/manager agents already do this exact job in production, without performing any Learn/Think/Articulate/Build work themselves |

The most important comparison is **ReAct**. ReAct goes Observe → Reason → Act. Its middle step covers the same territory Spiral calls Think — we've just chosen a plainer word for it. The gap is what comes after: ReAct has no Articulate stage. This is not an oversight — it reflects a genuine architectural assumption that agents should be fast and flexible. Spiral says: fast and flexible is fine for simple cycles, but without meeting the Producer at Articulate→Build, complex work collapses.

A second comparison is worth naming even though it isn't a single framework: multi-agent orchestration systems. AutoGen's `GroupChatManager`, CrewAI's hierarchical-process manager agent, and MetaGPT's SOP-driven role router all exist to solve exactly one problem — whose turn is it, and is this phase done — without performing any of the Learn/Think/Articulate/Build work themselves. Three engineering teams, solving unrelated problems, converged independently on the same role. That convergence is stronger evidence for the Stage Manager than any single analogy could be.

---

## Spiral and the Dimensions of Knowledge

Each stage operates across multiple **reach levels** — the scope of knowledge being drawn on:

| Reach | What it is | Example in Spiral |
| --- | --- | --- |
| **World** | External peer knowledge | Conference corpus, published research |
| **Enterprise** | Organisational knowledge | Company positioning, strategy documents |
| **Division** | Team/department knowledge | GTM decisions, product roadmap |
| **Team** | Immediate colleagues | Slack conversations, shared decisions |
| **Self** | Personal knowledge and experience | Your own expertise, intuition, history |

The richest thinking happens when multiple reach levels are in play simultaneously. A decision informed only by World knowledge (what the industry thinks) without Self knowledge (what you specifically know) is incomplete. A decision informed only by Self knowledge without World knowledge is parochial.

**For AI systems:** this reach hierarchy maps directly to the system prompt (Enterprise/Division/Team knowledge) + corpus (World knowledge) + user input (Self knowledge). The most valuable outputs emerge from the collision of all three.

## Applying Spiral to AI System Design

Spiral was developed for human cognition. It maps cleanly onto AI system design because good AI systems are trying to replicate good thinking.

| Spiral stage | What an AI system does |
| --- | --- |
| **Learn** | Corpus ingestion, retrieval, contextual grounding |
| **Think** | Reasoning, chain-of-thought, multi-perspective critique |
| **Articulate** | Structured output, task decomposition, response framing |
| **Build** | Generation, tool use, final response |

**The retrieval question** is really a Muse question: given everything in the corpus, which parts are worth thinking with for this query? This is what RAG architectures are trying to solve — and what pre-digested intelligence layers (like LLM Council-generated vitals files) solve more elegantly by doing that work at ingestion time rather than query time.

**The system prompt** is the Enterprise/Division/Team knowledge that sits above the World corpus. It is the difference between a system that knows what the industry thinks and a system that knows what *you* think about what the industry thinks.

## A Note on Origin

This framework was first developed in 1999, while working out the quality criteria for Keys4IT — Peter was barely twenty at the time. The original formulation was Learn, Think, Plan, Do — with a matrix identifying the source/target directionality of each stage.

Over the following twenty-seven years it has been renamed more than once (Spiral, previously CLAP, before that IDOFOBI/FOBI and LTPD, Perpetual Idea Machine), extended (bridges, gateways, a cast of characters), and applied to personal decisions, organisational change, and now AI system design.

It was rediscovered and formalised in a single conversation on 2026-06-29 — which is itself a demonstration of the fractal property. The conversation was a Spiral cycle about Spiral.

It was renamed a second time on 2026-07-02, from CLAP to Spiral, once the stage names it had grown into — Learn, Think, Articulate, Build — no longer spelled the old acronym. Spiral turned out to be the more precise word regardless: not a flat spiral that grows outward, but a climbing one that keeps its shape and simply gains height.

The framework has survived twenty-seven years not because it was written down carefully, but because it was *true enough to keep being useful.* This document is the first attempt to write it down carefully.

## There's more to think about...

**What happens when two musicians are in a spiral conversation?**

Two people, each moving through their own spiral, might relate the way two voices in music do — and music may have sharper vocabulary for that relationship than "same" and "different" allow.

**Same state = unison.** Two voices, same note, same time. It reinforces — but unison has no independent voices in it. Two people both in Think together can feel validating, and still be a shared home box: mutual rumination, with nobody there to sound the Director for the other.

**Different state isn't automatically harmony.** Harmony, strictly, is consonance — different notes that are stable together (one person Learning while the other Thinks on what was just found: genuinely complementary, restful difference). But different states are just as often dissonance — unstable, not restful, wanting to move. Dissonance isn't a flaw in music; it's the engine. A suspended 4th, a leading tone a half-step below the tonic — these exist specifically to create a pull that only resolves by moving. That's a closer model for what a Spiral character actually is than harmony: the Director showing up isn't a pleasant consonant chord, it's the dissonant note that won't let you rest in Think any longer.

**The "pull" has an exact name, twice over.** The gravitational tendency of an unstable tone toward its resolution is a leading-tone pull. And the specific move of stepping into a boundary character before the other person is ready to leave their stage — sounding the Director while someone is still Articulating — has an exact technical name too: a suspension. You deliberately carry a tone over into a harmony where it no longer belongs, so it reads as dissonant against the new chord — and that dissonance is what does the pulling. The other person's job isn't to resist it; it's to resolve, the way a suspended 4th falls to the 3rd.

| Spiral situation | Musical term |
| --- | --- |
| Same stage, same time | Unison |
| Different, complementary, stable together | Consonance |
| Different, unresolved, wants to move | Dissonance |
| One voices the next character early, creating that want | Suspension |
| The gravitational tendency toward the next stage | Leading-tone pull |
| The other person actually crossing | Resolution |
| Two independent, self-coherent spirals sounding together over time | Counterpoint |

This is a human-to-human proposition, not yet an agent-to-human one — a different claim than the operating modes in `.claude/skills/spiral/SKILL.md`. Undeveloped. Worth sitting with.
