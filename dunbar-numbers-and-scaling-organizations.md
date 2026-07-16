---
title: "Dunbar Numbers and the Shape of Scaling Organizations"
date: YYYY-MM-DD
tags: [organizational-design, leadership, scaling, dunbar-number]
author: Jessica Gray
---

# Dunbar Numbers and the Shape of Scaling Organizations

Why do organizations suddenly feel "different" after they cross a certain size? A recent post from Adam Sah got me thinking again about Dunbar numbers — rough estimates of the size of stable human social groupings of differing closeness.

The most well-known is ~150: the point where groups stop functioning on shared norms alone and start needing formal structure. But there are smaller layers inside that too: ~5 for deep collaboration, ~15 for strong team trust, ~50 where everyone still knows everyone.

These patterns show up almost everywhere we build organizations, and I keep coming back to the same question: can tools or technology increase these limits? My experience is that they help individuals — but not organizations. The rest of this piece works through why.

## The Layers, and Why They Persist

If Dunbar limits are real, they should show up in how successful organizations are structured. The exact numbers matter less than the underlying pattern: **organizations scale in predictable layers, and each layer requires a different structure.**

One of the clearest examples is the military. The exact numbers vary by branch and era, but the pattern is consistent — each unit of scale is typically 3–5x the previous one (squad, platoon, company, battalion...). These layers mark natural transition points, where structure, coordination, and leadership all need to evolve.

The same layering shows up in companies, at roughly these scales:

- **~3–5 people** — a support group in network-theory terms. Deep shared context, high-trust, high-frequency contact. This is the scale of a swarm on a hard problem, and it maps onto why small agile teams work so well: communication paths grow combinatorially with group size, so a group this small can stay in constant, low-friction sync. Adding one more person to a team this size is far cheaper than adding one to a large team — a cost that only grows from here.

- **~10–15 people** — the "two-pizza team," or sympathy group. This is roughly the ceiling for deep trust that still enables rapid, efficient communication without formal bureaucracy. People at this scale see each other regularly and share real context. It's the scale of a typical product or feature team — recognizable to both the individual contributors and the managers who deal with its day-to-day pain points.

- **~50 people** — the "active network" scale, and the first real discontinuity. Below this, an organization can still function on a personal level: everyone knows everyone else's skills and role. Above it, that stops being reliably true.

- **~150 people** — the "Rule of 150." Beyond this point, organizations lose the ability to manage through social norms alone and require formal management structures. This is where many companies feel a real shift: communication stops being effortless, alignment stops being implicit, and culture stops being self-reinforcing. What used to just work, suddenly doesn't.

Dunbar's own research says little about groups larger than 150, but the discontinuities keep reappearing at bigger scales — in the military and in companies alike. Roughly every 3–5x increase in scale seems to demand a new layer to manage communication complexity, adding bureaucracy in service of alignment. And within those larger structures, the smaller numbers (5, 15, 50) keep reappearing as the effective unit sizes inside each layer.

## What This Means for Organizational Design

These layers aren't just descriptive — they're a useful guardrail for org design.

The most commonly discussed failure mode is the overly vertical, hierarchical organization: slow decision-making, slow communication, low empowerment, operational silos, and general inefficiency. This is the natural direction of unplanned organic growth, absent outside pressure to counteract it. The less commonly discussed failure mode runs the other way — too few layers, which shows up as low oversight and accountability, poor mapping from goals to execution, and leadership burnout. This tends to hit fast-growing companies, or ones that push efficiency further than is sustainable.

Dunbar-informed research suggests useful, predictable ranges for span of control:

| Layer | Typical span |
|---|---|
| Manager | ~8–12 |
| Director | ~30–60 |
| Org leader | ~100–200 |

Where an organization should land within these ranges — and how much they can stretch — depends on context. A more experienced, high-autonomy workforce supports a wider span at each layer. So do lower turnover, strong mission alignment, and decentralized decision-making. Conversely, an organization that needs to provide more of its own training and development, or that operates under strict accountability requirements (say, due to regulation), needs a narrower span at each layer.

Most org design problems I've seen trace back to violating these constraints in one direction or the other: too many layers produces something slow and rigid; too few produces something chaotic and exhausting. Dunbar numbers don't give exact answers, but they give guardrails — and those are valuable.

## Why Tools Scale Individuals, Not Groups

There have been many attempts over the years to expand the effective Dunbar number, generally through technology. What I've observed is that tooling helps *individuals* expand their networks, but doesn't solve the underlying problem for *groups*: relationships don't scale linearly, they multiply. Signaling and regular interaction are what maintain in-group status, and that cost grows combinatorially with group size regardless of what tools are available.

Some individuals can maintain contact with a thousand-plus people. But that doesn't translate into a self-sustaining group. Social media has increased the raw number of contacts people track, but those relationships tend to be casual — they lack the sense of obligation and reciprocity that comes from real ongoing interaction. Maintaining relationships outside of family still generally requires some minimum of continued contact. Tooling and intention can help an individual manage a larger personal network, but the effort of fanning that out across a whole group appears to make it infeasible at the group level.

Put simply: tools can scale awareness. They don't scale mutual connection and obligation. And mutual connection and obligation are what actually hold a group together.

## The Core Takeaway

Scaling an organization isn't continuous — it's stepwise. At fairly predictable points (~15, ~50, ~150, ~500, and beyond) something breaks: communication stops scaling, alignment gets harder, culture weakens. And the system needs to change in response.

In practice:

- Small teams thrive on trust and shared context.
- Mid-size organizations rely on structure and clear ownership.
- Larger organizations require layers, abstraction, and deliberate communication.

Most of the pain I've seen comes from fighting this rather than working with it — staying "flat" too long produces chaos and burnout, while adding structure too early produces bureaucracy and drag.

Dunbar numbers aren't hard limits. They're signals — signals that it's time to evolve how an organization works, not just add more people to it. We've spent decades building tools to scale communication. The open question is whether we can actually scale trust, shared context, and mutual accountability, or whether those remain fundamentally human constraints that no amount of tooling removes.

## Postscript: AI and the Shape of Structure

Shortly after I started thinking through this series, Jack Dorsey and Roelof Botha published ["From Hierarchy to Intelligence"](#), which touches on many of the same ideas — why management structures exist in the first place, and how AI might change or replace parts of them, reframing companies as "intelligence systems."

There's a lot in that piece I agree with. A large part of what an organization does is solve information problems: aggregating context, routing decisions, maintaining alignment. But is that *all* organizational structure solves? AI can meaningfully change how we coordinate work and share information, but it doesn't remove every constraint that drove organizational structure to exist in the first place. Not all of those constraints are purely informational — long-term accountability comes to mind first, as does the need to build relationships that go beyond transactions to create trust, shared context, and speed.

Around the same time, I came across Grady Booch's framing of a ["third golden age" of software](#) — another useful lens for where AI fits into software engineering. He frames the current moment as a new abstraction layer, shifting engineers from execution toward system-level design. Extending that idea further: AI isn't just changing tools, it's shifting the level of abstraction across entire categories of work. As with past shifts — digital computing replacing manual calculation, for instance — some execution work disappears, but new problems emerge one layer up. What exactly gets abstracted away is still very much an open question.

If you've worked in a highly data-driven or AI-heavy organization: did it reduce the need for structure? Or did structure just reappear in a different form? We're at the beginning of a real shift here — but not a simple or predictable one.
