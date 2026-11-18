# How to use the AIR Brain - step by step

## 1. Install (pick one)
**A. Project-level (recommended).** In the project you work in:
1. Copy `air-brain/skills/*` into that project's `.claude/skills/`  (each folder must contain `SKILL.md`).
2. Copy the rules from `air-brain/CLAUDE.md` into the project's own `CLAUDE.md`, changing paths to `.claude/skills/...`.
3. Restart Claude Code (or start a new session) so skills are re-discovered.

**B. Personal.** Copy the same folders into `~/.claude/skills/` to use them in every project.

## 2. Check it loaded
Ask: "What skills do you have for pricing and cold email?" Claude should name `ch-pricing` and `ch-cold-email`. If not, confirm the folder layout `.claude/skills/<name>/SKILL.md` and restart.

## 3. Use it - ask in plain language
Claude loads a skill when your request matches its description. To force one, name it.

| You say | Skill used |
|---|---|
| "Review my landing page for conversion" | ch-cro |
| "Rewrite the homepage headline and CTA" | ch-copywriting |
| "Write a 4-step cold email sequence for roofing contractors" | ch-cold-email |
| "Give me a lead magnet idea for storm-damage homeowners" | ch-lead-magnets |
| "Is my plan page priced right?" | ch-pricing |
| "Design an A/B test for the signup form" | ch-ab-testing |
| "Set up a measurement plan" | ch-analytics |
| "Write TikTok and Meta ad concepts with hooks" | ch-ad-creative |
| "Make interview questions for 5 customers" | ch-customer-research |
| "Define our ideal customer" | tr-icp-research |
| "How do we show up in AI answers?" | rs-seo-aeo-geo |
| "Plan a CapCut edit for a 30s Reel, export for TikTok and Instagram" | video-shortform-editing |

## 4. Give them context (better results)
Most `ch-` skills look for `.agents/product-marketing.md` first. Create it once: product, audience, offer, differentiators, tone. Add `.agents/brand.md` for colors and voice.

## 5. A typical workflow
1. `tr-icp-research` -> who you target
2. `ch-customer-research` -> what they say
3. `ch-copywriting` + `ch-lead-magnets` -> message and offer
4. `ch-cro` + `ch-ab-testing` -> page and tests
5. `ch-ad-creative` + `video-shortform-editing` -> ads and short video
6. `ch-analytics` -> measure it

## 6. Video: CapCut / TikTok / Instagram Edits / 4K
1. Ask: "Plan a short video for [topic], platforms: TikTok + Reels."
2. Claude returns a beat sheet, editor steps, export table and posting copy.
3. Edit in CapCut or Instagram Edits. Export one high-quality master (4K if your source is 4K), then a 1080x1920 file per platform.
4. Anything marked VERIFY (app limits, upload caps): check the app or help page first.

## 7. Safety and upkeep
- Compliance: see `CLAUDE.md`. Cold outreach needs consent/opt-out handling.
- Never paste passwords or API keys into skills or pages.
- Updating: see `sources.md`. Review upstream changes before importing.
- Remove a skill by deleting its folder.
