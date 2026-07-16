# Writing

A collection of essays on engineering leadership, organizational design, and scaling teams. Originally written for LinkedIn; migrated here for a more durable, versioned home. Structured so it can be pushed to a Ghost blog or static site later with minimal changes.

## Posts

| Date | Title | Tags |
|---|---|---|
| 2025-03-11 | [Lessons from Sabotage](./posts/2025-03-11-lessons-from-sabotage.md) | leadership, organizational-design |
| 2025-03-18 | [How Organizations Sabotage Themselves](./posts/2025-03-18-how-organizations-sabotage-themselves.md) | leadership, organizational-design |
| 2026—04-07 | [Dunbar Numbers and the Shape of Scaling Organizations](./posts/2025-04-07-dunbar-numbers-and-scaling-organizations.md) | scaling, organizational-design, dunbar-number |

## Series

**Simple Sabotage** — What a WWII field manual on how to sabotage an organization from the inside teaches about running one well.
1. [Lessons from Sabotage](./posts/2025-03-11-lessons-from-sabotage.md) — individual behaviors: cooperation, motivation, and infrastructure.
2. [How Organizations Sabotage Themselves](./posts/2025-03-18-how-organizations-sabotage-themselves.md) — institutionalized sabotage: process, decision-making, and management dysfunction.

**Dunbar Numbers** — Why organizations break at predictable sizes, and what that means for structure, tooling, and (eventually) AI.
- [Dunbar Numbers and the Shape of Scaling Organizations](./posts/2025-04-07-ddunbar-numbers-and-scaling-organizations.md)

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
