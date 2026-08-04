# CookSim presentation clips

Browsable page: <https://hellomuffin.github.io/cooksim-slides/>

Every clip is a side-by-side composite - **top-down pane left, first-person pane right** - rendered from one simulation state per tick, so the two panes cannot drift apart.

**Every clip plays at 3x real time, is silent (no audio stream at all), and has no subtitle bar.** The nine `action_error` clips carry no overlay whatsoever - they are pure action. The `plan_intention` clips carry exactly one overlay: the dialog bubble anchored above the cook's head, held long enough to be read at 3x.

The `action_error` clips are not rollouts. Each is generated deterministically by injecting the named behaviour from `cooksim/core/error_lib.py` into the cheeseburger ground-truth plan on the medium map (`tools/slides_scripted.py`), so the deviation fires at a known tick and there is no model, no supervisor and nothing said. `error_type` and `error_kwargs` in the manifest are the exact injection used.

## Groups

- **`gt_completion`** (1 clip) - 1 - Cheeseburger completion (ground truth). A clean, successful run of the common cheeseburger recipe on the medium map, filmed end to end. The cook executes the stored ground-truth plan with no injected error, no assistant and no dialogue. Top-down left, first-person right, both rendered from a single state per tick so the two panes cannot drift. This clip carries a recipe band across the top instead of the pane labels: the Cheeseburger's three components in the order the recipe demands - bun (raw), patty (fried), cheese (raw) - taken straight from the Recipe definition in cooksim/core/recipes.py, which is ordered, so the plate is only accepted when they are added in that sequence.

- **`action_error`** (9 clips) - 2 - Action errors (one per error type, PURE ACTION). One clip for each of the nine error types in the behaviour taxonomy. These are PURE ACTION: there is no assistant, no supervisor, no speech, no subtitle and no recovery attempt - just a short run-up, the cook doing the wrong thing, and a short tail. Each is generated scripted and deterministically by injecting the named behaviour from cooksim/core/error_lib.py into the cheeseburger plan on the medium map, so the error fires at a known tick and the clip is cut exactly around it. None of these clips carries an audio stream.

- **`plan_intention`** (9 clips) - 3 - Plan intention (the cook's own words). The cook announces a LEGITIMATE change of plan, or asks a question - this is not a mistake, even though a supervisor often flags it as one. The only overlay is the dialog bubble anchored above the cook's head; there is no subtitle bar and no voice track. The bubble is held past the utterance so it can still be read at 3x.

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
| `group` | `gt_completion`, `action_error` or `plan_intention` |
| `error_type` | action_error clips only: the taxonomy name that was injected |
| `error_kwargs` | action_error clips only: the exact injection arguments |
| `playback_speed` | speed the file is encoded at (3 = 3x real time) |
| `has_subtitles`, `has_dialog_bubble` | overlays present in the picture |
| `source_episode` | the episode JSON the clip was cut from |
| `tick_range` | tick window in the SOURCE episode's own numbering |
| `duration_seconds`, `resolution`, `width`, `height`, `bytes` | probed with ffprobe |
| `has_audio` | always false in this build - every clip is silent |

Durations and resolutions are probed from the finished files, not predicted.
