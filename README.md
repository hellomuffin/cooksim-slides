# CookSim presentation clips

Browsable page: <https://hellomuffin.github.io/cooksim-slides/>

Every clip is a side-by-side composite - **top-down pane left, first-person pane right** - rendered from one simulation state per tick, so the two panes cannot drift apart.

## Groups

- **`gt_completion`** (1 clip) - 1 - Cheeseburger completion (ground truth). A clean, successful run of the common cheeseburger recipe on the medium map, filmed end to end. The cook executes the stored ground-truth plan with no injected error, no assistant and no dialogue. Top-down left, first-person right, both rendered from a single state per tick so the two panes cannot drift.

- **`action_mistake`** (4 clips) - 2 - Action mistake (error period only). The cook performs a WRONG action. Each clip is cut to the window around the error itself - a few seconds of run-up so the mistake is legible, the deviation, the supervisor's flag, and a short tail - rather than the whole episode.

- **`plan_intention`** (9 clips) - 3 - Plan intention (error period only, with dialog). The cook announces a LEGITIMATE change of plan and carries it out - this is not a mistake, even though a supervisor often flags it as one. The cook's spoken line is drawn as a dialog bubble anchored above its head in the top-down pane, shown for the ticks it was actually spoken over.

## Downloading the videos

`manifest.json` at the repo root lists every clip. No HTML scraping is needed.

Each entry carries a ready-to-use `download_url`:

```bash
curl -sL https://raw.githubusercontent.com/hellomuffin/cooksim-slides/main/manifest.json -o manifest.json

# every clip
jq -r '.clips[].download_url' manifest.json | xargs -n1 -P4 curl -sLO

# just one group
jq -r '.clips[] | select(.group=="plan_intention") | .download_url' manifest.json \
  | xargs -n1 -P4 curl -sLO
```

The URL pattern is `https://raw.githubusercontent.com/hellomuffin/cooksim-slides/main/videos/<filename>`, and `.clips[].filename` is the path relative to the repo root.

## Manifest fields

| field | meaning |
| --- | --- |
| `id` | stable clip identifier (also the file stem) |
| `filename` | path within the repo, e.g. `videos/<id>.mp4` |
| `url` | GitHub Pages URL (inline playback) |
| `download_url` | raw.githubusercontent URL (direct `curl`) |
| `group` | `gt_completion`, `action_mistake` or `plan_intention` |
| `source_episode` | the episode JSON the clip was cut from |
| `tick_range` | tick window in the SOURCE episode's own numbering |
| `duration_seconds`, `resolution`, `width`, `height`, `bytes` | probed with ffprobe |
| `has_audio` | true when the clip carries the narration track |

Durations and resolutions are probed from the finished files, not predicted.
