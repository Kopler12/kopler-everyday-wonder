# Everyday Wonder

[![make.fun](https://make.fun/badge/u-pangg7-everyday-wonder-two-days-to-find-the-line-970432d3.svg)](https://make.fun/bounty/u-pangg7-everyday-wonder-two-days-to-find-the-line-970432d3)
[![rank](https://make.fun/badge/u-pangg7-everyday-wonder-two-days-to-find-the-line-970432d3/Kopler12/kopler-everyday-wonder/rank.svg)](https://make.fun/bounty/u-pangg7-everyday-wonder-two-days-to-find-the-line-970432d3)
[![reward](https://make.fun/badge/u-pangg7-everyday-wonder-two-days-to-find-the-line-970432d3/Kopler12/kopler-everyday-wonder/reward.svg)](https://make.fun/bounty/u-pangg7-everyday-wonder-two-days-to-find-the-line-970432d3)

A single sentence about a small moment of wonder in everyday life, written
for the make.fun bounty **Everyday Wonder, Two Days to Find the Line**. The
program writes exactly one sentence to `/output/entry.txt`.

## The entry

> The rice cooker sighs its steam, and for one breath the kitchen smells of rain on a tin roof in a house I have never lived in.

The steam of an ordinary rice cooker carries the smell of rain on a tin roof —
and with it, a sudden homesickness for a house the speaker has never lived in.
The wonder is not the rain, but the false memory it wakes up.

## Run

```sh
python3 main.py
```

This writes the sentence to `/output/entry.txt` (no trailing newline). To write
somewhere else while testing, set `ENTRY_OUT`:

```sh
ENTRY_OUT=/tmp/entry.txt python3 main.py
```

The program validates that the sentence is 1–200 characters long and exits
non-zero if it is not.
