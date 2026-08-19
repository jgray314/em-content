---
title: "When Candidates Ask About Tech Debt"
date: 2026-08-25
tags: [recruiting, engineering-leadership, technical-debt, hiring, tech-recruiting]
author: Jessica Gray
---

*Recruiters increasingly get asked about tech debt in candidate screens. Most don't know how to answer.*

Recently I had a check-in call with a recruiter I used to work with, Ximena. She had a question for me: "when engineers ask about technical debt, what do they want to know about?". She was getting that question, but wasn't sure how to respond to candidates about the state of technical debt for the role or even what to ask the hiring manager to address the question. It is a great, and surprisingly challenging question to answer, so I decided to write up a bit of my thoughts for other recruiters facing similar candidate questions.

## What we're actually talking about

Technical debt is a financial metaphor for engineering tradeoffs for speed and simplicity: take a shortcut now, pay "interest" on it later. It's a useful starting point, but like most metaphors, not accurate in the details. It is also a phrase that can refer to many things.

When engineers ask about technical debt, they may be asking about technical operations health, or the engineering team's control of their own roadmap, or the expected pace of feature development, or if the team uses modern tools and technologies, or a number of other things.

For someone who doesn't come from a technical background, that's really non-obvious.

## Why it can actually be good

No system that's live is perfect. Technical debt can and should be an intentional set of trade-offs. Being able to complete work and validate ideas quickly, rather than trying to waterfall it all out and have everything pre-planned to some idealized form. Idealized forms have a bad habit of not being particularly useful in the real world anyway.

So the presence of technical debt isn't itself the problem. The real question is whether it's being handled deliberately and if engineering has a voice in the conversation.

The key is discussing it, and being very explicit about it. What are you using to maintain observability about technical debt? What are the dimensions you're thinking about it through: operational health processes, dashboards, system health, norms around deliverability? Those are all different tools you can use. But the key is really: how are you linking the architecture and investment in it back to the business case? Is that connection even currently there?

## When it's a red flag

Severe technical debt is a business risk. Full stop.

When candidates ask about it, they're usually asking about a suite of underlying concerns. Concerns about their day-to-day workplace quality-of-life and about the effectiveness of the company as a whole. Not just technical dysfunction, but business dysfunction. Any major problem with tech debt is at its heart a business problem in that it took a while to get to that stage and it's staying there for an extended period.

Three common failure modes are worth naming.

1. **Architectural Overhead:** Are your existing tools and services helping you build or slowing you down?
2. **Operational Nightmare:** Are you finding out about problems yourself or do customers have to report them to you? Do you know the size of impact problems caused to your customers and business?
3. **Feature Factory:** Can engineers advocate for investment when it competes with new features? Can a problem be big enough to be prioritized over feature work?

## The part engineers often get wrong

Engineers talk about technical debt as a trade-off against other potential investments like new features and they often skip the step of connecting it back to business requirements. How does this increase speed of execution? How does paying it down lower the operational risk of launching a new feature?

Engineers aren't necessarily used to framing it that way, and then they're surprised they have such a hard time getting buy-in for the investment. Realistically, that's an expectation for every role when they're requesting investment. Engineering isn't exempt just because the details happen to be technical.

Is that translation happening somehow and is that being weighed in the business prioritization process? That's really the underlying question engineers are getting at, even if what's immediately in their mind is a pager going off at 3am.

## A playbook for the conversation

Here are a few suggestions for any recruiter fielding questions around technical debt:

First, step back and figure out what a candidate's real concern actually is. Is it architectural overhead? Is it the feature-factory problem? Is it an operational nightmare where on-call is brutal? Understanding the underlying concern is necessary to actually address what they are worried about.

- What aspect of technical debt are you most concerned with: operations, business priorities, or something else?
- Do you have specific concerns or situations you are trying to avoid?
- Can you give an example you've seen that reflects excellent management of tech debt?

Then, be ready with a framework for how your company or team actually thinks about and addresses it.

You should know going in that there isn't one universal right answer. This can have a very different answer for a role focused mostly on greenfield development versus a role stewarding more mature systems. What's "right" looks different in each case across the different failure modes encompassed by technical debt. Your hiring manager can help you out, and your company or organization may be addressing the space systemically.

- Does the team have an on-call rotation, and if so how is it structured and how busy is it?
- Do we have incident response processes?
- How does team planning and prioritization work generally, especially with regards to product work versus other investments?

You are likely to get some questions about how the company and team uses AI here since it is rapidly changing the space and tradeoffs for teams. Some questions to have at the ready:

- How does your team use AI in development today?
- What are you working towards next in using AI in development?

## Closing thought

At the end of the day, a conversation about technical debt is rarely really about code. It's a business and communication conversation. Once you know that, it gets a lot easier to have.