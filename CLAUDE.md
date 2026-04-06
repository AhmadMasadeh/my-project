# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

A single-file Tic Tac Toe web game (`tictactoe.html`) with two modes: 2-player and vs Computer. No build tools, dependencies, or tests — just open the HTML file in a browser.

## Running

```
open tictactoe.html
```

## Architecture

Everything lives in `tictactoe.html`: markup, CSS, and JavaScript in a single file. The game logic uses a flat array of 9 cells and checks win conditions against `LINES` (the 8 possible three-in-a-row combinations). The AI opponent uses a priority-based heuristic (win > block > center > corners > edges), not minimax.

Note: There is an unused `WINS` array on line 38 that appears to be a buggy duplicate of `LINES` (contains `[0,2,4,6]` which is a 4-element array, not a valid win line). Only `LINES` is used for game logic.
