# Eastern ideas of good design, value, and reducing complexity

Research for [issue #13](https://github.com/austinbreunig/skills/issues/13). Feeds [#4, how mindful works](https://github.com/austinbreunig/skills/issues/4).

## The answer

Eastern traditions agree on one core idea: **good work goes with the grain of the problem, and value often lives in what you leave out.**

That gives `/mindful` a way of thinking, not just a checklist:

1. **Don't force it (wu wei).** If an agent is fighting the code, the tools, or the problem, that's a signal. Stop and find the natural seam.
2. **Subtract, then subtract again.** Learning adds every day. The Way takes away every day (Tao Te Ching ch. 48).
3. **Empty space is useful.** A cup works because it is hollow (ch. 11). Leave room: in interfaces, in plans, in scope.
4. **Keep the block uncarved.** Don't cut raw material into a fixed shape (an abstraction, a framework) before you need that shape (ch. 28, 32).
5. **Act small and early.** Hard things start out easy. Big things start out small (ch. 63, 64).
6. **Have a beginner's mind.** Experts see few options. Beginners see many (Suzuki).
7. **Accept "unfinished" and "temporary" (wabi-sabi).** Don't polish what will change. Leave space for the next person.
8. **Cut waste, unevenness, and overload (muda, mura, muri).** When something breaks, stop the line and find the root cause (Toyota).

Each idea below has: the source, what it means in plain words, what it means for code, and **questions mindful can ask** while it watches another agent work.

A warning up front: these ideas are a *lens*, not a rulebook. Wu wei does not mean "do nothing." Simple does not mean "fewest lines." See [Cautions](#cautions).

---

## Part 1: High-level patterns

### 1. Wu wei: act without forcing

**Source.**
- "The Tao in its regular course does nothing (for the sake of doing it), and so there is nothing which it does not do." (Tao Te Ching ch. 37, Legge)
- "The sage manages affairs without doing anything." (ch. 2, Legge)
- Scholarship: "*Wuwei* does not mean total inaction." It is "a contrast against any form of action driven by self-serving desire." (SEP, "Laozi")

**Plain words.** Wu wei is not laziness. It means doing the work without strain, without showing off, without pushing against how things want to go. Edward Slingerland's study calls it "effortless action."

**For code.** When an agent writes wrappers to work around a library, fights the type checker, or adds config to bend a tool into a shape it wasn't built for, it is forcing. Forcing is a sign the design is off.

**Mindful asks:**
- Is this agent fighting something? A tool, a framework, a test, the data shape?
- Is there a way to do this that the language or library already supports?
- Is this work for the problem, or for the agent to look thorough?

### 2. Follow the grain (Cook Ding)

**Source.** Zhuangzi ch. 3, Giles translation. Prince Hui's cook has used one knife for nineteen years and it is still sharp.
- "A good cook changes his chopper once a year,--because he cuts. An ordinary cook, once a month,--because he hacks."
- "I follow such openings or cavities as there may be, according to the natural constitution of the animal. I do not attempt to cut through joints: still less through large bones."
- At a hard spot: "I am all caution. I fix my eye on it. I stay my hand, and gently apply my blade."

**Plain words.** The master doesn't cut harder. He finds the gaps that are already there. When he hits something tough, he slows down and looks closely.

**For code.** Every problem has natural joints: where the data changes shape, where a team boundary is, where a thing changes at a different speed. Splitting code there is easy and lasts. Splitting through the middle of something ("cutting through bone") wears down the codebase.

**Mindful asks:**
- Where are the natural seams in this problem? Is the code split along them?
- Is this agent "hacking" (many tries, many reverts) instead of "cutting" (one clean pass)?
- At the hard part, did the agent slow down and look closely, or push harder?

### 3. Subtract, then subtract again

**Source.**
- "He who devotes himself to learning (seeks) from day to day to increase (his knowledge); he who devotes himself to the Tao (seeks) from day to day to diminish (his doing). He diminishes it and again diminishes it, till he arrives at doing nothing (on purpose)." (ch. 48, Legge)
- The tea room is "devoid of ornamentation except for what may be placed in it to satisfy some aesthetic need of the moment." (Okakura, *The Book of Tea*, ch. 4)

**Plain words.** Getting better at something often means doing less of it. The tea room holds one scroll and one flower, chosen for today. Everything else is put away.

**For code.** Agents tend to add: one more option, one more layer, one more helper. Mindful pushes the other way. The question isn't "what else should this have?" It's "what can it lose and still do its job?"

**Mindful asks:**
- What can be deleted and the thing still works?
- Is each part here for a need *right now*, or "just in case"?
- If we removed this feature, who would notice?

### 4. Emptiness is useful

**Source.**
- "The thirty spokes unite in the one nave; but it is on the empty space (for the axle), that the use of the wheel depends. Clay is fashioned into vessels; but it is on their empty hollowness, that their use depends." (ch. 11, Legge)
- "The reality of a room, for instance, was to be found in the vacant space enclosed by the roof and the walls, not in the roof and walls themselves." (Okakura, ch. 3)
- The Japanese idea of *ma* (the interval, the gap between things) was shown to the West in Arata Isozaki's 1978 exhibition *Ma: Space-Time in Japan*.

**Plain words.** The useful part of a cup is the empty part. A room is useful because of the space inside.

**For code.** A good interface is mostly empty: few parameters, little to learn, room for callers to bring their own needs. A good plan leaves slack. A good page has white space. Filling every gap makes things rigid.

**Mindful asks:**
- Does this interface leave room for the caller, or does it decide everything for them?
- Is there slack in this plan, or is every hour booked?
- Is the agent filling space because space feels wrong?

### 5. The uncarved block (pu)

**Source.**
- "The unwrought material, when divided and distributed, forms vessels." (ch. 28, Legge)
- "Simplicity without a name / Is free from all external aim." (ch. 37, Legge)
- Scholarship: *pu* is "the utterly simple, unaffected, and seemingly valueless *pu*, a plain uncarved block of wood." (SEP, "Laozi")

**Plain words.** Raw wood can become anything. Once you carve it into a bowl, it can only be a bowl. The plain block looks worthless, but it holds every option.

**For code.** A plain function is an uncarved block. A class hierarchy, a plugin system, or a framework is a carved block. Carve too early and you lock in a shape before you know the real need. This is the deep reason behind YAGNI.

**Mindful asks:**
- Is this abstraction carving a shape we don't know we need yet?
- Could this stay a plain function (or plain data) a while longer?
- What options does this design close off?

### 6. Act small and early

**Source.**
- "(The master of it) anticipates things that are difficult while they are easy, and does things that would become great while they are small. All difficult things in the world are sure to arise from a previous state in which they were easy." (ch. 63, Legge)
- "Order should be secured before disorder has begun. The tree which fills the arms grew from the tiniest sprout... the journey of a thousand li commenced with a single step." (ch. 64, Legge)
- "Governing a great state is like cooking small fish." (ch. 60, Legge). Commentators read this as: don't keep poking it, or it falls apart.

**Plain words.** Fix the small crack before it's a big crack. Take one step at a time. Don't keep stirring.

**For code.** Name the confusing thing now, while it's one file. Write the test while the function is small. Make small commits. Don't refactor a working system over and over.

**Mindful asks:**
- What small problem here will be a big problem in a month?
- Is this change one step, or many steps bundled together?
- Is the agent stirring the pot (churning working code) without a reason?

### 7. Soft beats hard

**Source.**
- "Man at his birth is supple and weak; at his death, firm and strong... firmness and strength are the concomitants of death; softness and weakness, the concomitants of life." (ch. 76, Legge)
- "There is nothing in the world more soft and weak than water, and yet for attacking things that are firm and strong there is nothing that can take precedence of it." (ch. 78, Legge)
- "The highest excellence is like (that of) water... occupying, without striving (to the contrary), the low place which all men dislike." (ch. 8, Legge)

**Plain words.** Living things bend. Dead things are stiff. Water is soft but wears down stone.

**For code.** Rigid designs break when needs change. Easy-to-change designs survive. A decision you can undo beats a "perfect" decision you can't. Like water taking the low place, good code does the humble job well (clear errors, plain names) and doesn't need to be clever.

**Mindful asks:**
- If this need changes next month, how hard is it to change this code?
- Is this decision easy to undo? If not, does it need to be made now?
- Is there a humble, boring way to do this?

### 8. Don't overfill, don't overreach

**Source.**
- "It is better to leave a vessel unfilled, than to attempt to carry it when it is full." (ch. 9, Legge)
- "He who stands on his tiptoes does not stand firm; he who stretches his legs does not walk (easily)." (ch. 24, Legge)
- "He whose (desires) are few gets them; he whose (desires) are many goes astray." (ch. 22, Legge)

**Plain words.** A full cup spills. Standing on tiptoe makes you wobble. Want fewer things and you'll get them.

**For code.** A ticket that tries to do everything spills. A design that stretches to impress is unstable. Fewer goals, done fully, beat many goals done halfway.

**Mindful asks:**
- Is this change trying to carry too much at once?
- Is any part here to impress rather than to serve?
- What's the one thing this must do? Is that thing done well?

### 9. The "machine heart": cleverness has a cost

**Source.** Zhuangzi ch. 12, Giles translation. A gardener carries water by hand. Zigong suggests a well-sweep (a lever for lifting water). The gardener refuses: "those who have cunning implements are cunning in their dealings, and that those who are cunning in their dealings have cunning in their hearts... It is not that I do not know of these things. I should be ashamed to use them."

**Plain words.** Every clever tool changes how you think. The gardener knows about the tool. He chooses not to use it because of what it does to him.

**For code.** This is not "never automate." It is: count the hidden cost of a clever tool. A code generator, a meta-framework, or a magic decorator saves typing but adds something everyone must now understand. Cleverness spreads.

**Mindful asks:**
- What does this clever tool or trick cost the next reader?
- Is the plain way only a little longer? Then why not use it?
- Does the agent understand the tool it's adding, or is it reaching for it out of habit?

### 10. Don't stretch the duck's legs

**Source.** Zhuangzi ch. 8, Giles: "just as a duck's legs, though short, cannot be lengthened without pain to the duck, and a crane's legs, though long, cannot be shortened without misery to the crane."

**Plain words.** Things have their own nature. Forcing them into a "standard" shape hurts them. Daoists call fitting your own nature *ziran*, "self so" (SEP, "Laozi").

**For code.** Don't force two different things into one shared abstraction just because they look alike. Don't make every module follow the same pattern if they have different jobs. This is the guard against *bad* DRY.

**Mindful asks:**
- Are these two things really the same, or do they just look alike today?
- Is this "shared" code forcing one caller to bend for the other?

### 11. The fish trap: drop the scaffolding

**Source.** Zhuangzi ch. 26, Giles: "The *raison d'être* of a fish-trap is the fish. When the fish is caught, the trap may be ignored... The *raison d'être* of language is an idea to be expressed. When the idea is expressed, the language may be ignored."

**Plain words.** Tools exist for a purpose. Once the purpose is met, you don't need to keep the tool.

**For code.** Debug prints, temporary flags, prototype code, migration shims, planning docs. They did their job. Remove them. Also: a process or checklist is a fish trap. Don't serve the checklist; serve the goal.

**Mindful asks:**
- What here was scaffolding that can now go?
- Is the agent following the process for its own sake, or for the goal?

### 12. Beginner's mind and the empty cup

**Source.**
- "In the beginner's mind there are many possibilities, but in the expert's there are few." (Shunryu Suzuki, *Zen Mind, Beginner's Mind*, 1970, opening lines)
- "A Cup of Tea" in *Zen Flesh, Zen Bones* (Reps and Senzaki, 1957). The master Nan-in pours tea into a visitor's cup until it overflows: "Like this cup, you are full of your own opinions and speculations. How can I show you Zen unless you first empty your cup?"

**Plain words.** If you already "know" the answer, you can't see a better one. Empty your cup first.

**For code.** Agents (and people) jump to the pattern they know best. Beginner's mind means asking "what is this problem, really?" before picking a solution. It also means mindful itself must watch with fresh eyes, not just match against old rules.

**Mindful asks:**
- Did the agent look at the problem, or jump straight to a familiar pattern?
- If someone new saw this, what would they find strange?
- What's a second, totally different way to solve this? Is it simpler?

### 13. Wabi-sabi: imperfect, impermanent, incomplete

**Source.**
- The tea room is "consecrated to the worship of the Imperfect, purposely leaving some thing unfinished for the play of the imagination to complete." "True beauty could be discovered only by one who mentally completed the incomplete." (Okakura, ch. 4)
- Rikyu has his son sweep the garden path until it is spotless. Then Rikyu shakes a tree so leaves fall on it: "What Rikiu demanded was not cleanliness alone, but the beautiful and the natural also." (Okakura, ch. 4)
- Kenkō, *Essays in Idleness* (14th c.): "The most precious thing in life is its uncertainty." He prefers "branches about to blossom or gardens strewn with faded flowers." (quoted in SEP, "Japanese Aesthetics," Keene translation)
- Wabi is "not asceticism but rather moderation." (SEP, "Japanese Aesthetics")
- Leonard Koren's *Wabi-Sabi for Artists, Designers, Poets & Philosophers* (1994) brings these ideas into design practice.

**Plain words.** Nothing lasts. Nothing is finished. Nothing is perfect. Accept that, and you stop wasting effort on fake polish.

**For code.** All code is temporary. Don't gold-plate code that will be rewritten. "Done and clear" beats "perfect." Leave hooks open for the next person to finish. Too-sterile code (every edge case wrapped, every name generic) can be harder to read than plain, slightly rough code.

**Mindful asks:**
- Is the agent polishing something that will change soon?
- Is this "good enough to be clear and correct"? Then stop.
- Is it so "complete" that there's no room for the next person to extend it?

### 14. Value comes from use and real feeling, not display

**Source.**
- "Sincere words are not fine; fine words are not sincere." (ch. 81, Legge)
- Okakura tells of tea master Enshu, who admits Rikyu was greater: "The great Rikiu dared to love only those objects which personally appealed to him, whereas I unconsciously cater to the taste of the majority." (ch. 5)
- Okakura also warns: "Would that we loved the ancients more and copied them less!" (ch. 4)
- The silver pavilion (plain, aged) is held up against the gold pavilion (gold leaf) as the model of sabi. (SEP, "Japanese Aesthetics")

**Plain words.** Something is valuable because it truly serves, not because it looks impressive. Copying a famous style isn't the same as understanding it.

**For code.** A long, fancy-looking design doc isn't more valuable than a short one that's right. Copying a big company's architecture (microservices, event sourcing) without their problem is "copying the ancients."

**Mindful asks:**
- Is this here because it helps, or because it looks serious?
- Is the agent copying a famous pattern without the problem that pattern solves?

### 15. The best leader is barely noticed

**Source.**
- "In the highest antiquity, (the people) did not know that there were (their rulers)... Their work was done and their undertakings were successful, while the people all said, 'We are as we are, of ourselves!'" (ch. 17, Legge)
- "The work is accomplished, and there is no resting in it (as an achievement)." (ch. 2, Legge)

**Plain words.** The best guide works so lightly that people think they did it themselves.

**For mindful itself.** This is how mindful should *behave* toward other agents. Don't lecture. Don't stack up rules. Nudge with one good question at the right moment. The goal is that other agents start working simply on their own.

---

## Part 2: Practices from Japanese manufacturing (Lean)

These come from Toyota, not from philosophy texts, but they are the most proven way Eastern ideas became daily engineering practice.

- **Muda, mura, muri.** Toyota works to eliminate "waste, inconsistencies, and unreasonable requirements." (Toyota, "Toyota Production System")
  - *Muda* (waste): work that adds nothing.
  - *Mura* (unevenness): stop-start, inconsistent work.
  - *Muri* (overload): asking too much of a person or machine.
- **Just-in-time.** "Only make what is needed by the customer, when it is needed, and in the amount needed." (Toyota) This is YAGNI in a factory.
- **Jidoka: stop the line.** When something goes wrong, the operator can stop the line "by pulling the stop cord themselves," and the *andon* board lights up. (Toyota) Fix the cause before you keep going.
- **Kaizen.** "All employees implement daily incremental kaizen." (Toyota) Small, constant improvement, not big rewrites.
- **Ask "why" five times.** Taiichi Ohno's method for finding the root cause, from *Toyota Production System: Beyond Large-Scale Production* (1978; English 1988).
- **The seven wastes of software.** Mary and Tom Poppendieck mapped Toyota's wastes onto software in *Implementing Lean Software Development* (2006): partially done work, extra features, relearning, handoffs, task switching, delays, and defects.

**Mindful asks:**
- Which of the seven wastes is this agent creating? (Extra features? Half-done work? Relearning something it already found?)
- Is the agent moving on past a failing test or a warning? It should "stop the line."
- When a bug is fixed, did the agent ask "why" enough times to find the real cause?
- Is this a big rewrite where a small kaizen step would do?

---

## Part 3: Software writing that draws on these ideas

- **Rich Hickey, "Simple Made Easy" (Strange Loop, 2011).** *Simple* comes from "one fold or one braid." "The meaning of simple means unentangled, not twisted together with something else." *Easy* means "to lie near," that is, familiar. To *complect* is "to braid together," the root of complexity. Key lines: "Simplicity is not about counting," and "simplicity is a choice. It requires constant vigilance." Hickey doesn't cite Daoism, but his idea fits Cook Ding: find where things are already separate, and don't tie them together.
- **The Zen of Python (PEP 20, Tim Peters, 2004).** Openly borrows the Zen frame. "Simple is better than complex." "Flat is better than nested." "Sparse is better than dense." "If the implementation is hard to explain, it's a bad idea." "Now is better than never. Although never is often better than *right* now." That last pair is very close to wu wei: don't rush to act.
- **Poppendieck, *Lean Software Development* (2003) and *Implementing Lean Software Development* (2006).** The main bridge from Toyota to software (see Part 2).
- **Lighter, folk sources.** Geoffrey James's *The Tao of Programming* (1987) is a fun parody in Tao Te Ching style. It shows how common the link is, but it isn't scholarship. Don't build on it.

---

## Part 4: A field guide for mindful

How mindful can use all this while it watches another agent. Grouped by *when* to ask.

**Before the agent starts (empty the cup)**
- What is the problem, in one sentence, before any solution?
- What are its natural joints? (data shape, team, speed of change)
- What's the smallest step that teaches us something?

**While the agent works (don't force)**
- Is it fighting a tool, a test, or the data? → Stop and look for the seam.
- Is it hacking (many retries) instead of cutting (one clean pass)? → Slow down at the hard spot.
- Is it carving an abstraction early? → Keep the block uncarved.
- Is it moving past a failure? → Stop the line.

**After a draft (subtract)**
- What can be deleted and it still works?
- What scaffolding can go now? (fish trap)
- Is anything here to look thorough, not to serve?
- Is it polished past the point of change? (wabi-sabi)
- Which of the seven wastes showed up?

**Learning from what it watched (kaizen)**
- What did the agent force? What would going with the grain have looked like?
- What did it add that it later removed? That's a lesson for next time.
- Record one small lesson, not ten. Keep mindful's own rules few (ch. 48 applies to mindful too).

**How mindful speaks (the quiet ruler)**
- One question at the right moment beats a long list.
- Ask, don't command. Let the agent find the simpler path.
- If mindful's notes grow long, mindful is forcing.

---

## Cautions

- **Wu wei is not "do nothing."** Scholars are clear: "*Wuwei* does not mean total inaction" (SEP, "Laozi"). Cook Ding works hard. He just doesn't strain.
- **Simple is not "fewest lines."** Hickey: "Simplicity is not about counting." More separate parts can be simpler than a few tangled ones.
- **The machine-heart story is not anti-tool.** Use it to weigh a tool's hidden cost, not to refuse tools.
- **Okakura's "fear of repetition" is about art, not code.** He says no design should repeat in a tea room. In code, the matching lesson is the duck's legs (don't force sameness), not "never repeat anything."
- **Translations differ a lot.** Legge (1891) and Giles (1889) are public domain and serious but dated. For quotes in the skill, check a modern translation too (for example Burton Watson's *Zhuangzi*, D. C. Lau's *Tao Te Ching*). The ideas above hold up across translations; exact wording does not.
- **"Eastern" is a very broad label.** Daoism, Zen, Japanese aesthetics, and Toyota are different things from different eras. Okakura (1906) was also writing to sell Japanese culture to Western readers. Use these as practical lenses, not as claims about "the East."

---

## Sources

Primary texts (public domain, checked directly):
- Laozi, *Tao Te Ching*, tr. James Legge (1891). Project Gutenberg #216. https://www.gutenberg.org/ebooks/216 . Chapters used: 2, 8, 9, 11, 17, 22, 24, 28, 37, 48, 60, 63, 64, 76, 78, 81.
- Zhuangzi, *Chuang Tzŭ: Mystic, Moralist, and Social Reformer*, tr. Herbert A. Giles (1889). Project Gutenberg #59709. https://www.gutenberg.org/ebooks/59709 . Stories used: Cook Ding (ch. 3), duck's legs (ch. 8), the gardener and the well-sweep (ch. 12), the fish trap (ch. 26).
- Kakuzo Okakura, *The Book of Tea* (1906). Project Gutenberg #769. https://www.gutenberg.org/ebooks/769 . Chapters 3 (Taoism and Zennism), 4 (The Tea-Room), 5 (Art Appreciation).

Scholarship:
- Stanford Encyclopedia of Philosophy, "Laozi" (Alan Chan; rev. 2025). https://plato.stanford.edu/entries/laozi/ . Wu wei, ziran, pu.
- Stanford Encyclopedia of Philosophy, "Japanese Aesthetics" (Graham Parkes and Adam Loughnane; rev. 2023). https://plato.stanford.edu/entries/japanese-aesthetics/ . Wabi, sabi, yūgen, Kenkō, Rikyu, Tanizaki.
- Edward Slingerland, *Effortless Action: Wu-wei as Conceptual Metaphor and Spiritual Ideal in Early China* (Oxford, 2003). Cited for the "effortless action" reading; not quoted.

Zen and design books (cited; text not checked line by line here):
- Shunryu Suzuki, *Zen Mind, Beginner's Mind* (Weatherhill, 1970).
- Paul Reps and Nyogen Senzaki, *Zen Flesh, Zen Bones* (1957), incl. *101 Zen Stories* (1919), "A Cup of Tea."
- Leonard Koren, *Wabi-Sabi for Artists, Designers, Poets & Philosophers* (1994).
- Arata Isozaki, *Ma: Space-Time in Japan* (exhibition, 1978).

Engineering:
- Toyota Motor Corporation, "Toyota Production System." https://global.toyota/en/company/vision-and-philosophy/production-system/ . Jidoka, andon, kaizen, just-in-time, muda/mura/muri.
- Taiichi Ohno, *Toyota Production System: Beyond Large-Scale Production* (1978; English 1988). Five whys.
- Mary and Tom Poppendieck, *Lean Software Development* (2003) and *Implementing Lean Software Development* (2006).
- Rich Hickey, "Simple Made Easy" (Strange Loop, 2011). Transcript: https://github.com/matthiasn/talk-transcripts/blob/master/Hickey_Rich/SimpleMadeEasy.md
- Tim Peters, "PEP 20 – The Zen of Python" (2004). https://peps.python.org/pep-0020/ (also `python -c "import this"`).
