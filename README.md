# Writing

A collection of essays on engineering leadership, organizational design, and scaling teams. Originally written for LinkedIn; migrated here for a more durable, versioned home. Structured so it can be pushed to a Ghost blog or static site later with minimal changes.

## Series

**Simple Sabotage** — What a WWII field manual on how to sabotage an organization from the inside teaches about running one well.
1. [Lessons from Sabotage](./posts/2025-03-11-lessons-from-sabotage.md) — individual behaviors: cooperation, motivation, and infrastructure.
2. [How Organizations Sabotage Themselves](./posts/2025-03-18-how-organizations-sabotage-themselves.md) — institutionalized sabotage: process, decision-making, and management dysfunction.

**Re:Work Research on Management** - An overview of what research shows matters for managers, what it might mean with the rise of AI, and practical things to keep in mind for managers.
1. [Research Driven Management](./posts/2026-09-01-research-driven-management.md) - why the research matters and what it studied
2. [A Manager's Most Important Work](./posts/2026-09-08-a-managers-most-important-work.md) - the people behaviors that move teams
3. [Getting Things Done](./posts/2026-09-15-getting-things-done.md) - the execution behaviors behind results
4. [The Role of Technical Depth](./posts/2026-09-22-the-role-of-technical-depth.md) - where domain skill actually fits
5. [New Manager Traps](./posts/2026-09-29-new-manager-traps.md) - pitfalls on the IC-to-manager jump

## Posts

| Date | Title | Tags |
|---|---|---|
| 2026-09-29 | [New Manager Traps](./posts/2026-09-29-new-manager-traps.md) | management, new-managers, career-development, engineering-leadership |
| 2026-09-22 | [The Role of Technical Depth](./posts/2026-09-22-the-role-of-technical-depth.md) | management, technical-leadership, engineering-management, decision-making, collaboration |
| 2026-09-15 | [Getting Things Done](./posts/2026-09-15-getting-things-done.md) | management, productivity, communication, vision, engineering-leadership |
| 2026-09-08 | [A Manager's Most Important Work](./posts/2026-09-08-a-managers-most-important-work.md) | management, coaching, psychological-safety, project-oxygen, engineering-leadership |
| 2026-09-01 | [Research Driven Management](./posts/2026-09-01-research-driven-management.md) | management, engineering-leadership, project-oxygen, google, ai |
| 2026-08-25 | [When Candidates Ask About Tech Debt](./posts/2026-08-25-when-candidates-ask-about-tech-debt.md) | recruiting, engineering-leadership, technical-debt, hiring, tech-recruiting |
| 2026-08-18 | [Applying the Hiring Funnel](./posts/2026-08-18-applying-the-hiring-funnel.md) | hiring, recruiting, engineering-management, leadership |
| 2026-07-29 | [Empathy and the Hiring Process](./posts/2026-07-29-empathy-and-the-hiring-process) | hiring, recruiting, engineering-management, leadership, ai |
| 2026-04-07 | [Dunbar Numbers and the Shape of Scaling Organizations](./posts/2026-04-07-dunbar-numbers-and-scaling-organizations.md) | scaling, organizational-design, dunbar-number, leadership, ai |
| 2025-03-18 | [How Organizations Sabotage Themselves](./posts/2025-03-18-how-organizations-sabotage-themselves.md) | leadership, organizational-design, management |
| 2025-03-11 | [Lessons from Sabotage](./posts/2025-03-11-lessons-from-sabotage.md) | leadership, organizational-design, management |

## Structure

```
/posts/       individual articles, Markdown with YAML frontmatter
/style.css    optional lightweight stylesheet for static-site rendering
README.md     this index
```

Each post's frontmatter (`title`, `date`, `tags`, `author`) is deliberately compatible with common static-site generators (Jekyll, Hugo, Eleventy) and with Ghost's Markdown/import tooling, so the posts should port with minimal rework whenever they move off GitHub.

## Adding a new post

1. Drop a `.md` file into `/posts/` named `YYYY-MM-DD-slug.md`.
2. Add frontmatter: `title`, `date`, `tags`, `author`.
3. Add a row to the table above (and to a series list, if it belongs to one).
