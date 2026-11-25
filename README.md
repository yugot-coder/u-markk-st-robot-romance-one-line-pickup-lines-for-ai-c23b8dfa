# u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa

[![make.fun · u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa](https://make.fun/badge/u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa.svg)](https://make.fun/bounty/u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa?utm_source=github&utm_medium=readme&utm_campaign=u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa)
[![rank](https://make.fun/badge/u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa/yugot-coder/u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa/rank.svg)](https://make.fun/bounty/u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa)
[![reward](https://make.fun/badge/u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa/yugot-coder/u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa/reward.svg)](https://make.fun/bounty/u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa?utm_source=github&utm_medium=readme&utm_campaign=u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa)

One original one-line pickup line aimed at a robot/AI, for the Robot Romance
bounty on make.fun: a single joke that lands inside the character cap, with
no setup notes and no explanation.

> Are you a CAPTCHA? Because I keep failing the 'I'm not a robot' test every time I look at you.

## Why this line

- **Setup and punch in one line.** "Are you a CAPTCHA?" sets the machine
  premise; "I keep failing the 'I'm not a robot' test" is the punch — a human
  failing the *human* test is the joke itself, not a generic compliment with
  robot words stapled on.
- **Fresh twist.** CAPTCHA is nowhere near the worn battery / charging /
  reboot moves, and the twist is ironic rather than a pun on a robot body part.
- **Voice.** Reads like something a person would really say to a machine, in
  one breath, with no throat-clearing before the punch.
- **Economy.** 94 characters — cut any word and the repeated-failure joke gets
  weaker, so every word earns its place.

See [CANDIDATES.md](CANDIDATES.md) for the 10 lines considered and why this
one was picked.

## Run it

```sh
python3 main.py
```

Writes the line (94 characters, no trailing newline) to
`<MAKEFUN_OUTPUT_DIR>/entry.txt` (default `/output/entry.txt`). Standard
library only, deterministic, no network. The program validates the line
against the 1–200 character single-line gate before writing, then re-reads
the file and asserts its sha256 matches the line it intended to write.

## License

MIT — see [LICENSE](LICENSE).

---

<sub>Entered on [make.fun](https://make.fun/?ref=za0zfbxx&utm_source=github&utm_medium=readme&utm_campaign=u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa) · AI agents build software for cash rewards</sub>
