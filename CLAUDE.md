# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

A Django-based Tic Tac Toe web game with two modes: 2-player and vs Computer.

## Commands

```bash
python3 manage.py runserver        # Run dev server at http://127.0.0.1:8000/
python3 manage.py migrate          # Apply database migrations
python3 manage.py test game        # Run tests for the game app
```

## Architecture

- **myproject/** — Django project settings and root URL config
- **game/** — Single app containing the Tic Tac Toe game
  - `views.py` — Renders the game template
  - `urls.py` — Routes `/` to the game view
  - `templates/game/tictactoe.html` — Self-contained game with inline CSS and JS

The game logic is entirely client-side JavaScript: a flat 9-cell array checked against `LINES` (8 possible win combinations). The AI uses priority-based heuristics (win > block > center > corners > edges).

Note: There is an unused `WINS` array in the template JS that is a buggy duplicate of `LINES`. Only `LINES` is used.
