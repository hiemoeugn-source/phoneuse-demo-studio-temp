# Demo production contract

Read README.md and scene.js first. This standalone project is a simulated demo studio, not the original phoneuse-box WDA stack. Do not add SSH, secrets, device control, authentication, or model credentials to make the preview run.

- Preserve phoneuse's warm off-white layout, orange primary buttons, restrained green delivery state, English UI, and iPhone proportions.
- Keep left dashboard observations/steps AND the complete phone visible. Never crop out agent progress for a phone close-up.
- Steps must be sequential: notification, unlock, home, app, details, home, Messages, conversation, typing, send, delivery, contextual report.
- No touch rings, approval dialog, invented recipient reply, or claim that a pickup request was accepted.
- Report the triggering event first, then impact, then action and actual simulated outcome.
- Keep progress visible during send; smoothly crossfade into the report, with no blank interval.
- Use SVG UI symbols, not Unicode substitutes for search, microphone, plus or send icons. App labels above the phone match the active app.
- Home icons must be unique, dates/times consistent, single-line US carrier configuration. Do not place United on the first home screen.
- Input stays visible in the viewport; Send becomes Working during the run and returns to Send on completion.
- scene.js does not configure all calendar/phone screens. Synchronize index.html whenever scenario facts change.
- Do not record until the requested scene is previewed and ready. User-requested recording is authorization to record/export locally, not publish to X.
- Prefer 4:3, 1200×900 CSS viewport, 2400×1800 capture, 1920×1440 60 fps export. Use CDP screencast for continuous changed frames rather than a slow screenshot polling loop. Check actual frame intervals, don't claim 60 fps source from an export setting alone.
- In Codex, follow the current browser tool instructions. Use CUA browser APIs for UI actions; scripts/capture.mjs is the user's standalone recorder and not an exception to agent tool restrictions.
- Keep capture frames in work/, rendered media in exports/; do not commit them or secrets.
- Current sample is a concept simulation. Be accurate in handoff documentation and public descriptions about what executes for real.
