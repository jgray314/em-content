# Jessica Gray — Engineering Leadership Writing

A collection of essays on engineering leadership, organizational design, scaling teams, and building with AI. Originally written for LinkedIn; migrated here for a more durable, versioned home. Structured so it can be pushed to a Ghost blog or static site later with minimal changes.

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

Generated from each post's frontmatter by `scripts/build_index.py`. Edit the frontmatter, not this table.

<!-- posts:start -->
| Date | Title | Tags |
|---|---|---|
| 2026-10-13 | [Same Test Cases, Different Scores](./posts/2026-10-13-same-test-cases-different-scores.md) | ai, engineering-leadership, evaluation, verification |
| 2026-09-29 | [New Manager Traps](./posts/2026-09-29-new-manager-traps.md) | management, engineering-leadership, new-managers, career-development |
| 2026-09-22 | [The Role of Technical Depth](./posts/2026-09-22-the-role-of-technical-depth.md) | management, ai, project-oxygen, decision-making |
| 2026-09-15 | [Getting Things Done](./posts/2026-09-15-getting-things-done.md) | management, ai, project-oxygen, productivity |
| 2026-09-08 | [A Manager's Most Important Work](./posts/2026-09-08-a-managers-most-important-work.md) | management, ai, project-oxygen, psychological-safety |
| 2026-09-01 | [Research Driven Management](./posts/2026-09-01-research-driven-management.md) | management, ai, project-oxygen |
| 2026-08-25 | [When Candidates Ask About Tech Debt](./posts/2026-08-25-when-candidates-ask-about-tech-debt.md) | hiring, engineering-leadership, recruiting, technical-debt |
| 2026-08-18 | [Applying the Hiring Funnel](./posts/2026-08-18-applying-the-hiring-funnel.md) | hiring, recruiting |
| 2026-07-29 | [Empathy and the Hiring Process](./posts/2026-07-29-empathy-and-the-hiring-process.md) | hiring, ai, recruiting |
| 2026-04-07 | [Dunbar Numbers and the Shape of Scaling Organizations](./posts/2026-04-07-dunbar-numbers-and-scaling-organizations.md) | organizational-design, ai, scaling, dunbar-number |
| 2025-03-18 | [How Organizations Sabotage Themselves](./posts/2025-03-18-how-organizations-sabotage-themselves.md) | organizational-design, management |
| 2025-03-11 | [Lessons from Sabotage](./posts/2025-03-11-lessons-from-sabotage.md) | organizational-design, management |
<!-- posts:end -->

## Structure

```
/posts/                  articles (Markdown with YAML frontmatter) and their images
/scripts/build_index.py  regenerates the Posts table above from frontmatter
/style.css               optional lightweight stylesheet for static-site rendering
LICENSE                  CC BY-NC 4.0
README.md                this index
```

Frontmatter is the source of truth for each post's title, date, and tags. The fields are deliberately compatible with common static-site generators (Jekyll, Hugo, Eleventy) and with Ghost's Markdown/import tooling, so the posts should port with minimal rework whenever they move off GitHub.

## Adding a new post

1. Drop a `.md` file into `/posts/` named `YYYY-MM-DD-slug.md`, using the date it is published on LinkedIn.
2. Add frontmatter, in this order:
   ```yaml
   ---
   title: "Post Title"
   date: YYYY-MM-DD
   tags: [core-tag, specific-tag]
   author: Jessica Gray
   series: "Series Name"   # only if part of a multi-part series
   series_part: 1          # only with series
   ---
   ```
3. Tags: one or two core tags (`engineering-leadership`, `management`, `hiring`, `organizational-design`, `ai`), plus up to two specific ones (e.g. `project-oxygen`, `evaluation`). Reuse an existing specific tag before inventing a new one.
4. Start the body with a `# Title` heading; use `##` for sections.
5. Put images in `/posts/` next to the post, link them relatively (`./ImageName.png`), and give them alt text that states what the image shows.
6. Run `python scripts/build_index.py` to refresh the Posts table. If the post is part of a multi-part series, add it to the Series list by hand.

## License

Text and images are © Jessica Gray, licensed under [CC BY-NC 4.0](./LICENSE): share and adapt with attribution, not for commercial use.
