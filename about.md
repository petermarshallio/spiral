# Spiral — A Framework for Human and Machine Intelligence

*This is the narrative explanation — what Spiral is and why it works. For strict definitions and lookup tables, see [`reference.md`](./reference.md). For the framework's history, see [`origin.md`](./origin.md).*

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
| **External source** | **Internalising** | **Interacting** |
| **Internal source** | **Examining** | **Externalising** |

This matrix is the lens. If you understand it, you can interpret the framework in your own words — and you can map almost any cognitive framework, AI architecture, or decision-making model onto it.

- **Internalising** — the world comes *in*. You absorb, accumulate, receive.
- **Examining** — you work on what's *inside*. You reason, connect, critique.
- **Externalising** — your internal thinking goes *out* as structured intention. You make it concrete.
- **Interacting** — something already out there meets something else already out there, and the world responds.

**Internal and external are relative to whoever's spiral this is.** Neither term describes a medium or a body part — they describe whose current state is doing the sourcing or receiving, for whichever Actor is the subject of the cycle in question (see `reference.md`'s "Internal / External"). A machine's own memory is genuinely internal to that machine, even though nothing resembling human comprehension occurs there; a sensor reading nobody and nothing ever stores is external on both ends, no matter how it was captured.

## The Four Quadrants

### Internalising

**External → Internal** Taking in knowledge from the outside world. Reading. Listening. Watching. Accumulating. This is what a child does when they go to the library and come back with 90 books about cheese. It is also what an AI does when it ingests a corpus.

Internalising is not passive — it requires selection. You cannot internalise everything. The quality of what you choose to internalise determines the quality of everything downstream.

**In AI terms:** corpus ingestion, retrieval, contextual grounding. The vitals files in a conference talk corpus are the product of Internalising.

**In human terms:** research, reading, listening, observation, experience.

### Examining

**Internal → Internal** Working on what you already have inside. Connecting dots. Reasoning. Critiquing. Weighing options. This is the stage where what's freshly internalised becomes understanding.

Examining is the home box for many people — including the author of this framework. It is seductive because it feels like progress. It can become a trap. The Dramaturg can only give you so much cover — eventually the Stage Manager walks in and asks if you're ready to go meet the Director.

**In AI terms:** reasoning, chain-of-thought — the same territory ReAct calls "Reason." The LLM Council's Perspectives are the product of Examining applied to Internalising.

**In human terms:** critical thinking, de Bono's Six Thinking Hats, the hermeneutic circle, dot-connecting.

### Externalising

**Internal → External** Structured intention made concrete. This is the stage that most AI agents skip — and why they fail at anything requiring sustained, coordinated effort. Externalising is where internal thinking becomes external artefact: a SMART objective, a work package, a Gantt chart, a prioritised backlog.

Externalising is not thinking about what to do. It is writing it down in a form that others — or your future self — can act on.

**In AI terms:** task decomposition, agent planning, structured output, generation. The step between Examining and Act that ReAct agents lack.

**In human terms:** project management, SMART goals, sprint planning, architectural design documents.

### Interacting

**External → External** Something already out in the world meets something else already out in the world, and the world responds. This is not the moment a design or a plan first becomes real — that crossing already happened, at Externalising, regardless of whose hands or tools were involved. Interacting is what happens next: a wolf blows on the house that's already standing. Interacting is the stage where you find out if it holds.

Interacting generates the raw material for the next Internalising. The cycle continues.

**In AI terms:** tool execution, deployment, an agent's action changing a system already in production. The "Act" in ReAct.

**In human terms:** a market reacting to news, a policy being enforced, a rumour spreading, a system failing under load.

## The Cast

Each stage has someone already in it. Not a mechanism — a person, and each one wants something different from you. (The roster — which character owns which stage — is in reference.md; here's who they are.)

Every character named here — plus the Hero and the Stage Manager, met below — is a Role, not a fixed person. Whoever picks one up, human or AI, is the Actor; the same Actor often holds several Roles in turn, sometimes within a single exchange, sometimes within the same handful of lines. (Strict definitions in reference.md.)

The move through the spiral moves forward; you can't go back and reshoot yesterday's scene. You do not retreat to a previous stage, you complete
the cycle and begin a new one, richer for the revolution you just completed.

Meeting **the Director** matters most for people who live in Examining, because they're the one who eventually has to leave it. The Director doesn't demand certainty. They demand a hypothesis — something specific enough to be wrong. A scientist's commitment, not a bureaucrat's sign-off.

**The Witness** is the character most often avoided — not because watching is hard, but because doing nothing while you wait for a real verdict is. It's why houses fall down when wolves blow on them: nobody was willing to let the wind actually test the walls and watch honestly, instead of assuming, or rushing back in with more straw the moment it wobbled. The hard part of Witnessing isn't doing something well — it's tolerating not doing anything yet. Watching well looks like a process blocked on an interrupt: genuinely idle until a real signal arrives, not one burning cycles on anxious polling. Checking the dashboard every ten seconds isn't Witnessing. It's intervention dressed up as patience.

**The Dramaturg** is the character people mistake for the whole job. Interrogating a claim feels like progress — turning it over, testing it from six angles, reconciling the tension in it — so people camp there long after they've got something worth testing, circling a question that's already answered rather than committing to an answer that could be wrong. That's not a flaw in the questioning. It's a reason to eventually stop asking and go meet the Director.

**The Critic** is the character people flinch from meeting. But the verdict isn't a punishment — it's the raw material for the next Internalising. Refuse to meet her and the cycle starves.

Every character but one is really asking the same thing, in their own language: **what are you making out of what I've given you?** The Witness alone asks something different: **what is actually happening, now that it's out of your hands?**

Not "are you done?" — you are never done.

None of them will come and get you, though. Knowing when to go find them is a different job entirely — that's the Stage Manager.

This is the coaching relationship, not the advisory one: each character's job is to draw the next move out of the Hero, not hand it to them — except the Witness, whose job during Interacting is the opposite of drawing a move out: holding the Hero back from making one before the world has actually answered.

Each character also draws on a menu of established, named techniques rather than one universal method per character — SMART goals, PR-FAQs, and pre-mortems for the Director, Socratic questioning and first-principles thinking for the Dramaturg, after-action reviews and blameless postmortems for the Critic, chaos engineering and observability for the Witness. The full library, with specific sources and why each one fits, is in reference.md.

---

## The Stage Manager

There is a fifth presence, but it is different in kind from the other four. The Dramaturg, the Director, the Witness, and the Critic each own one specific stage — they're waiting inside it, ready to help you do that stage's work (for the Witness, that help means holding you back) — but none of them will come looking for you. The Stage Manager owns none of the content. Its only job is flagging when it's time to go meet them — a moment with a name, borrowed from the same theatre this cast came from: **calling the cue**. (See "The Cues" below for what happens at one, and for why flagging it isn't the same as calling it alone.)

This is not a hierarchy. The Stage Manager doesn't decide the order — the cycle already fixes that completely — and it doesn't outrank the cast. It only asks the question underneath all four of theirs: *is it time to call the cue?*

Asking that question is not the same as answering it alone. The answer comes from Notes — a joint check with whoever's playing the Hero, not a call the Stage Manager makes and delivers. This matters most when the Stage Manager is an AI and the Hero is human: neither Actor has complete knowledge of themselves, let alone the other, so the crossing gets worked out between them, not decided by one and handed to the other.

That question isn't only asked passively, waiting for a natural pause between stages. Protecting momentum sometimes means forcing the issue mid-stage — closing down an Examining that's overstaying its welcome, enforcing an end to circular creative options before anyone feels ready — because the Stage Manager's job was never to certify that a stage's content is finished, only that the whole system keeps moving. It shows up wherever momentum is under threat, not only at the four fixed cues.

The role changes shape depending on who's in the loop — a solo human, a solo AI, an AI and a human handing off to each other, a team of people, a team of agents. The full breakdown, with the academic and engineering grounding for each, is in reference.md.

The consistency across all five is the point. In every flow, the Stage Manager never does Internalising/Examining/Externalising/Interacting work itself — and in every flow, its absence produces the same failure: stalling, thrashing, or false momentum. Not five different failure modes. One.

### One operator, four registers

Everything above describes the Cast as company you meet. But for a solo operator — a single person working alone, or a single AI with no other agents to call on — there's no one else in the room. The Dramaturg's interrogative rigour, the Director's decisiveness, the Witness's restraint, the Critic's evaluative honesty: you have to produce all four yourself, in turn. Meeting the cast, solo, means becoming them for as long as their stage needs you to — and for the Witness, "becoming them" means doing the one thing hardest to fake alone: actually stopping.

This is a different difficulty than the one Momentum names. Momentum failure is about *time* — staying too long in one stage. This is about *register* — being unable to actually think with the Dramaturg's interrogative rigour while still holding the Critic's honesty from the stage before, or unable to drop the Director's decisiveness once Interacting needs the Witness's restraint instead. Everyone is fluent in their home box's register and clumsy in at least one other — usually, unsurprisingly, the neglected character's.

The precise term for this isn't multiplicity as pathology, it's **code-switching**: deliberately changing register to fit context while one continuous self persists underneath, doing the switching. Two grounded precedents, one per register:

- **Human:** Transactional Analysis' Parent/Adult/Child ego states — distinct behavioral registers a person moves between deliberately, without losing continuity of self. De Bono's own Blue Hat (see the framework comparison below) is the same idea inside a framework Spiral is already compared to: it isn't a fifth hat alongside the other four, it's the process-control hat, worn by whoever decides which of the other four the group should be wearing — and it can think in any of them when needed.
- **AI:** a context switch, in the plain operating-systems sense — a process's state is suspended, a different process's state is loaded in and executed, and something outside both of them keeps the scheduling bookkeeping across every swap. That bookkeeping layer isn't optional decoration; without it, "switching" is just amnesia.

For an AI system this reframes what the Stage Manager actually does in solo operation. It isn't only the outside voice asking "is it time?" — it has to be able to condition itself into each stage's register (interrogative for Examining, decisive for Externalising, restrained for Interacting, evaluative for Internalising), do that stage's work in that register, then step back out to the layer that tracks the whole arc and knows when the next switch is due. One operator, four registers, one continuous thread of oversight underneath all of them. That thread — not any single register — is the Stage Manager.

### Facilitation can change hands

Everything above assumes one Actor holds the Stage Manager Role for a whole exchange. That's the solo case. In a live conversation between two Actors — a human and an AI, say — it isn't what actually happens: whoever proposes a candidate next step, whoever reflects back what's just been said, whoever asks "is that fair?" is holding the Stage Manager Role for that turn, and it passes back and forth within a single exchange, sometimes more than once in the same handful of lines. This is different from code-switching, which is one Actor moving between all four Cast Roles solo — this is two Actors sharing custody of one Role, the way facilitation visibly shifts in a well-run meeting when someone other than the designated facilitator says "should we park this and move on?" reference.md's table of who plays the Stage Manager per flow type describes who's eligible, not a fixed assignment for the whole exchange.

---

## The Cues

Between every stage and the next there's a fixed point where whoever is doing the work — call them the Hero — crosses from one cast member's territory into another's. Theatre already has a word for that point: a **cue**. It isn't a metaphor reached for after the fact — calling cues is the Stage Manager's literal job, four times around the cycle, not once.

Readers who know Cooper's Stage-Gate process will recognise the shape, but the word is deliberately different: a gate is a pass/fail checkpoint you seek approval to open, while a cue is a signal to enter — a smaller claim, and the one that actually fits a coaching relationship rather than a review board.

A cue is not a formality to wave through. Crossing it means answering something real: given what the last stage actually produced, what happens now? Neither cast member either side of the cue can answer that alone — the one being left knows what just happened, the one about to be met knows what's needed next. What happens at a cue is called **Notes**: a check of what's understood against what's needed, before the Hero is allowed to move.

Most Notes are one clause, wordless, over as soon as they start — the everyday version of "that's enough, go," already described above as the Stage Manager quietly deciding it's time. Some cues earn the full version instead: several cast members speaking in turn before a direction is committed to. That fuller version isn't a new mechanism — it's "Convening the cast for review" (see the skill file), renamed for what it structurally is: a full Notes session, held at a cue, instead of the ordinary quiet one. See reference.md's "Deciding When to Hold Full Notes" for when that expense is worth paying.

Zoom out one level and a full cycle, start to finish, is itself a unit of joint behaviour — architecture frameworks like ArchiMate call this an Interaction, performed by a Collaboration of whichever Actors hold which Roles. A cue's Notes is a smaller Interaction nested inside the larger one, the Fractal Property applied to the cycle itself rather than to a single stage. Informally, call a running Interaction a Ceremony — just remember a Spiral Ceremony convenes when the work is ready, not on Scrum's schedule.

The four cues already have names — recovered rather than invented. In a 2011–2012 version of this framework, when the stages were still Creation, Learning, Analysis, and Planning, the transitions between them were already called **EESS**: Elect, Enable, Sense, Separate — driven by a connecting force called Enertia, which this document now calls Momentum. Mapped onto today's stages, the fit is exact — the mapping table is in reference.md.

Every nested cycle the fractal property opens up has its own four cues, usually quiet ones — see reference.md's "Deciding When to Hold Full Notes" for how to tell the difference.

---

## Momentum

Momentum is not a stage. It is a property of the whole system — the rate at which you move through the spiral. The Stage Manager is what embodies that property in practice: not a sixth stage, but the role that exists to protect momentum wherever it's under threat.

**High momentum:** each revolution lands you somewhere genuinely new. The cast shows up readily because sufficient work was done in each stage.

**Low momentum:** spinning on the same level. Stuck in Examining. Avoiding the cast. Returning to Internalising because the Director was never met.

**False momentum:** moving fast but skipping stages. Lots of Interacting without enough Internalising or Examining. The house gets built quickly. Then the wolf arrives.

Momentum is killed by:

- Perfectionism in Examining (the thinking trap)
- Avoiding the Witness (the control trap) — refusing to let go long enough to see what actually happens
- Insufficient Internalising before Examining (the opinion trap)

Momentum is built by:

- Meeting the Director with a testable hypothesis, not a proven answer
- Treating the Critic's verdict as genuinely generative, not just evaluation
- Allowing the next Internalising to be informed by what Interacting revealed

## The Fractal Property — Spirals All the Way Down

Each stage of Spiral is itself a full Spiral cycle.

The Internalising stage of a project *is* a Spiral cycle: you interact with small experiments to learn from, internalise what they teach you, examine what you found, and externalise the next experiment.

The Examining stage of a decision *is* a Spiral cycle: you interact with hypotheses to see what they imply, internalise what that reveals, think through the implications, and externalise which one to test next.

Lean Startup's Build-Measure-Learn loop is this same property, already named and already in wide use, wearing a three-word label rather than a Spiral one: ship the smallest real thing (Externalising), watch how the market actually responds (Interacting), and internalise what that response taught you (Internalising). It's a full miniature cycle, not a single stage's technique — which is exactly why it doesn't belong on any one character's list in reference.md.

This is not a metaphor. It is structurally true. Spiral scales from a five-minute decision to a thirty-year career. The same four questions, the same four characters, applied recursively at every level of granularity.

> "It's Spirals all the way down."

This fractal property means the framework is never the wrong size. If a stage feels too large to act on, run Spiral inside it. The cycle will break it into manageable revolutions.

## Non-Linearity and Entry Points

Where you start on the Spiral is up to you.

People have a **home box** — the stage they gravitate toward, where they spend disproportionate time. They also have a **neglected character** — the one they most often avoid meeting. Researchers and readers tend to enter through Internalising, and risk never meeting the Director; strategists and overthinkers enter through Examining, and risk thinking without sufficient raw material; managers and executors enter through Externalising, and risk articulating from assumptions rather than evidence; builders and hackers enter through Interacting, and risk learning only from failure, expensively. (The table version is in reference.md.)

None of these is wrong. All of them are incomplete without the others.

The framework does not judge your entry point. It asks: which character have you not met recently?

## Relation to Other Frameworks

The matrix is the key to these comparisons. Spiral is not derived from any of these — it predates most of them in the author's practice — but the overlaps are illuminating. The full comparison table (Bloom's Taxonomy, Kolb's Cycle, ReAct, OODA, Six Thinking Hats, the Hermeneutic Circle, Belbin Team Roles, multi-agent orchestration) is in reference.md.

The most important comparison is **ReAct**. ReAct goes Observe → Reason → Act. Its middle step covers the same territory Spiral calls Examining — we've just chosen a plainer word for it. The gap is what comes after: ReAct has no Externalising stage. This is not an oversight — it reflects a genuine architectural assumption that agents should be fast and flexible. Spiral says: fast and flexible is fine for simple cycles, but without meeting the Witness at Externalising→Interacting, complex work collapses.

A second comparison is worth naming even though it isn't a single framework: multi-agent orchestration systems. AutoGen's `GroupChatManager`, CrewAI's hierarchical-process manager agent, and MetaGPT's SOP-driven role router all exist to solve exactly one problem — whose turn is it, and is this phase done — without performing any of the Internalising/Examining/Externalising/Interacting work themselves. Three engineering teams, solving unrelated problems, converged independently on the same role. That convergence is stronger evidence for the Stage Manager than any single analogy could be.

---

## Spiral and the Dimensions of Knowledge

Each stage operates across multiple **reach levels** — the scope of knowledge being drawn on: World, Enterprise, Division, Team, and Self, each broader or narrower than the last. (The table with examples is in reference.md.)

The richest thinking happens when multiple reach levels are in play simultaneously. A decision informed only by World knowledge (what the industry thinks) without Self knowledge (what you specifically know) is incomplete. A decision informed only by Self knowledge without World knowledge is parochial.

**For AI systems:** this reach hierarchy maps directly to the system prompt (Enterprise/Division/Team knowledge) + corpus (World knowledge) + user input (Self knowledge). The most valuable outputs emerge from the collision of all three.

## Applying Spiral to AI System Design

Spiral was developed for human cognition. It maps cleanly onto AI system design because good AI systems are trying to replicate good thinking — Internalising as corpus ingestion and retrieval, Examining as reasoning and critique, Externalising as structured output and generation, Interacting as tool use and execution against systems already in production. (The table is in reference.md.)

**The retrieval question** is really a Dramaturg question: given everything in the corpus, which parts are worth thinking with for this query? This is what RAG architectures are trying to solve — and what pre-digested intelligence layers (like LLM Council-generated vitals files) solve more elegantly by doing that work at ingestion time rather than query time.

**The system prompt** is the Enterprise/Division/Team knowledge that sits above the World corpus. It is the difference between a system that knows what the industry thinks and a system that knows what *you* think about what the industry thinks.

A full multi-voice Notes session (see "The Cues," above) costs real tokens, latency, and attention, so it shouldn't be the default at every cue — reference.md's "Deciding When to Hold Full Notes" gives the exact signals worth scoring a cue against, framed as literal branching logic a Claude Code implementation can use.

## Origin, briefly

This framework is decades old: first developed in 1999, renamed more than once since, rediscovered and properly written down in 2026. The full history — every name it's worn, including one, "the FOBI controller," that turns out to have been the Stage Manager all along — is in [`origin.md`](./origin.md).

## There's more to think about...

**What happens when two musicians are in a spiral conversation?**

Two people, each moving through their own spiral, might relate the way two voices in music do — and music may have sharper vocabulary for that relationship than "same" and "different" allow.

**Same state = unison.** Two voices, same note, same time. It reinforces — but unison has no independent voices in it. Two people both in Examining together can feel validating, and still be a shared home box: mutual rumination, with nobody there to sound the Director for the other.

**Different state isn't automatically harmony.** Harmony, strictly, is consonance — different notes that are stable together (one person Internalising while the other Examines what was just found: genuinely complementary, restful difference). But different states are just as often dissonance — unstable, not restful, wanting to move. Dissonance isn't a flaw in music; it's the engine. A suspended 4th, a leading tone a half-step below the tonic — these exist specifically to create a pull that only resolves by moving. That's a closer model for what a Spiral character actually is than harmony: the Director showing up isn't a pleasant consonant chord, it's the dissonant note that won't let you rest in Examining any longer.

**The "pull" has an exact name, twice over.** The gravitational tendency of an unstable tone toward its resolution is a leading-tone pull. And the specific move of stepping into a boundary character before the other person is ready to leave their stage — sounding the Director while someone is still Externalising — has an exact technical name too: a suspension. You deliberately carry a tone over into a harmony where it no longer belongs, so it reads as dissonant against the new chord — and that dissonance is what does the pulling. The other person's job isn't to resist it; it's to resolve, the way a suspended 4th falls to the 3rd.

| Spiral situation | Musical term |
| --- | --- |
| Same stage, same time | Unison |
| Different, complementary, stable together | Consonance |
| Different, unresolved, wants to move | Dissonance |
| One voices the next character early, creating that want | Suspension |
| The gravitational tendency toward the next stage | Leading-tone pull |
| The other person actually crossing | Resolution |
| Two independent, self-coherent spirals sounding together over time | Counterpoint |

This started as a human-to-human proposition, but the agent-to-human version turned out to be closer than it looked: the skill file's two operating modes — guiding the user's spiral, and sharing the agent's own — are exactly two Actors' individual spirals, and Notes is the counterpoint between them. What's still undeveloped is whether the musical vocabulary itself survives the move — does an AI declining to advance actually read as a suspension the way it would between two humans, or does that need its own term? Worth sitting with.

**What happens when two separate spirals notice each other?**

Not two voices in one conversation — two entirely different cycles, each with its own full cast, running at once without either one aware of the other by default. A Stage Manager operating at a high enough Reach Level might notice that one cycle's Internalising stage just landed exactly where another cycle's Critic left off, and suggest a route for cooperation between them — something neither cycle's own Hero would think to look for, since neither is watching the other. Different from the Fractal Property, which nests cycles inside each other: this is cycles running alongside each other. A different scale of claim than anything else in this document, and genuinely unresolved — including whether the noticing Stage Manager needs visibility into both cycles itself, or whether it's really two separate Stage Managers signalling to each other.
