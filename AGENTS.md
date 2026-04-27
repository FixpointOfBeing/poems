# AGENTS.md

## Project Overview

This is a personal collection of original Chinese poetry (现代诗) by **maerd-zinbieL**. Each file is a single poem or a pair of poems (original + ChatGPT revision). There is no code, no build system, no test framework, and no linter configuration.

---

## Build / Lint / Test Commands

There are **no** build, lint, or test commands. This is a plain-text poetry repository. To validate changes, do the following manually:

- **File naming check**: Ensure filenames follow `{poem_title}_{YYYY-M-D}.txt`. The date separator is `-` (hyphen), not `/` or `_`.
- **UTF-8 encoding**: All files must be UTF-8 encoded Chinese text.
- **No trailing whitespace**: Trailing whitespace should be removed from all lines.
- **End files with exactly one newline**: Each `.txt` file must end with a single trailing newline.
- **No BOM**: Files must not contain a UTF-8 BOM (byte order mark).
- **No empty files**: Poem files should not be empty unless intentionally a stub. Stubs should be noted in git commit messages.

---

## Commit Conventions

Commits follow **Conventional Commits** with emoji prefixes:

```
<emoji> <type>(<scope>): <description>
```

Examples from history:
- `✨ feat(poetry): add new collection of poems`
- `✨ feat(poetry): add new poem "xxx"`
- `📝 docs(poetry): add new poem file with original and revised versions`

Types: `feat` (new poem), `fix` (correction to a poem), `docs` (documentation/poem text), `refactor` (restructuring), `style` (formatting).

Emoji should be appropriate: `✨` for new poems, `📝` for text/docs, `🎨` for style, `♻️` for refactoring, `🔧` for config.

---

## File Naming Conventions

- Format: `{poem_title}_{YYYY-M-D}.txt`
- The title is in Chinese characters (no pinyin).
- Date uses hyphens: `YYYY-M-D` (e.g., `2026-1-22`, not `2026-01-22`).
- No spaces in filenames.
- Punctuation within poem titles (like `，`) is preserved in filenames.

---

## File Content Conventions

- Poems are written in **modern free-verse Chinese poetry (现代诗)**.
- Stanzas are separated by a blank line.
- Lines within a stanza are single-spaced.
- No stanza numbering.
- For poems that include a ChatGPT revision, separate with a line of 22 hyphens: `----------------------` followed by a header line `chatgpt改：`.
- The poem title is not repeated inside the file (the filename serves as the title).
- No front matter, no metadata headers.
- Plain text only — no markdown formatting within poem files.

---

## Git Workflow

- Author name: `maerd-zinbieL`
- Author email: `db1345569965@gmail.com`
- Commits are made directly to `main` (single author, personal project).
- No pull requests, no branching.

---

## Language & Typography

- Primary language: **Chinese (Simplified)**.
- Use **Chinese punctuation** throughout: `，` `。` `、` `“”` `——` `……` etc.
- Lines should not exceed a reasonable length for readability (typically under 30 Chinese characters per line).
- No English unless intentional for poetic effect.
- No pinyin annotations.

---

## Error Handling & Review Guide

Since there are no automated checks, review changes by:
1. Read the poem aloud (mentally) to check rhythm and line breaks.
2. Verify that the filename date matches the poem's creation/completion date.
3. Ensure no duplicate filenames exist (the same title with different dates is allowed — e.g., `我是_2025-12-17.txt` and `我是_2026-1-1.txt`).
4. For revised versions, ensure the `----------------------` separator and `chatgpt改：` header are consistently formatted.
5. Confirm the `.txt` extension is lowercase.
