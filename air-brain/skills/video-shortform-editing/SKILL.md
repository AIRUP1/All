---
name: video-shortform-editing
description: "Plan, edit and export short-form vertical video in CapCut, Instagram Edits, TikTok and Instagram Reels, including 4K masters and per-platform delivery. Use when the user asks for a CapCut edit, TikTok or Reels workflow, Instagram Edits app steps, 4K export settings, captions, safe zones, or repurposing one video across platforms. Complements ch-video (AI/code video) and ch-social (strategy)."
metadata:
  version: 0.1.0
  status: draft
  sources: ch-video, ch-social, ch-ad-creative (short-form-video-specs.md)
---

# Short-Form Video Editing: CapCut / TikTok / Instagram (Edits) / 4K

Hands-on editing and export workflow. For hooks, scripts and strategy, use `ch-social` (references/short-form-video.md). For AI-generated or code-rendered video, use `ch-video` / `tr-remotion-video`. For ad-specific specs, use `ch-ad-creative`.

## Verify before you promise
App features, export caps and upload limits change often. Anything marked VERIFY below must be confirmed in the current app or the platform's help page before you state it to the user as fact. Never invent a limit.

## Step 0 - Ask
1. Platform(s): TikTok, Reels, Shorts, all?
2. Source: phone footage, screen recording, AI clips, existing long video?
3. Goal and length. Organic or paid?
4. Which editor is available: CapCut (phone/desktop), Instagram Edits, other?
5. Does the user need a 4K master (archive, repurposing, client delivery) or just a post-ready file?

## Step 1 - Pick the editor
| Need | Use |
|---|---|
| Fast captions, templates, effects, desktop + mobile | CapCut |
| Reels-first, quick cuts, then post straight to Instagram | Instagram Edits (VERIFY current feature set and export options) |
| Trending sounds and native effects | Edit in-app in TikTok or Instagram, or attach the sound at posting |
| Repeatable product films | `ch-video` / Remotion |

## Step 2 - Shoot/ingest
- Shoot vertical 9:16. Shoot at the highest quality the device offers (4K if storage allows) so you can crop/reframe.
- Keep key action inside the safe band (see references/specs-and-safe-zones.md).

## Step 3 - Edit (platform-agnostic beat sheet)
1. **Hook in 0-3s**: visual + on-screen text. Use hook patterns from `ch-social`.
2. **Cut tempo**: new visual or text every 1-3s. Remove dead air.
3. **Captions**: burn in, high contrast, inside the safe band. Check auto-caption accuracy line by line.
4. **Audio**: voice clear first, music low under it. For organic posts, consider attaching trending audio in-app instead of baking it in.
5. **Payoff and CTA** in the last 2-4s; avoid a dead-end outro.
6. **Loop**: for short clips, end so the last frame flows into the first.

## Step 4 - Export (master, then deliver)
Recommended pipeline:
1. **Master**: export once at the highest quality you have (4K if the source is 4K; VERIFY the editor's export options and any paywall on 4K/60fps).
2. **Deliverables**: one file per platform at 1080x1920, 9:16, MP4 (H.264), 30fps (or match source). The platforms recompress on upload, so upload the cleanest file you can and do not re-export a re-export.
3. Name files `YYYYMMDD_topic_platform_vN.mp4`.
4. Platforms may cap or downscale resolution on upload (VERIFY TikTok and Reels current upload limits and max resolution before promising "4K on TikTok/Instagram").

Details and checklist: references/export-checklist.md.

## Step 5 - Platform publish notes
- **TikTok**: native text/captions, sound from the library, cover frame, hashtags and keywords in caption. Check watermark-free export if cross-posting.
- **Instagram Reels / Edits**: cover image, caption + keywords, collab/tag. If cross-posting from TikTok, use a file without the TikTok watermark.
- **Both**: do not reuse a watermarked clip from the other platform.

## Step 6 - Review
Play the final on a phone, sound off then sound on. Check: hook readable in 1s, captions inside safe band, no clipped text, audio levels, last frame.

## Output format
Give the user: (a) beat sheet, (b) editor-specific click path (marked VERIFY where unsure), (c) export settings table, (d) per-platform posting copy.
