# 🌿 Vidya's Vegetarian Performance Cookbook

A personal web app for calorie-aware vegetarian meal planning, pantry-first grocery lists, and chef-recommended recipes optimised for weight training.

## Features

- **Smart meal planning** — generates a 7-day plan targeting your daily calorie & macro goals, split by your eating style (light breakfast / big lunch / etc.)
- **Pantry-first ingredient scoring** — prioritises recipes that use what you already have to minimise waste and grocery spend
- **Calorie & macro tracking** — Mifflin-St Jeor BMR + TDEE calculator, goal-based macro splits (muscle gain, fat loss, endurance, general health)
- **38 chef-inspired vegetarian recipes** across grab-and-go, easy, moderate, batch, and snack tiers
- **Grocery list** — plan-driven, showing only ingredients for your selected week; marks what you have in stock
- **Onboarding wizard** — multi-step setup (stats → training profile → calculated targets → first meal plan)
- **Single-file output** — everything runs in the browser via `localStorage`, no backend needed

## Stack

Pure HTML/CSS/JS, generated from Python source files. No frameworks, no server.

## Usage

```bash
python3 build_cookbook.py
# → outputs mnt/Grocery List/recipe-book.html
```

Open `recipe-book.html` in any browser.

## Files

| File | Purpose |
|------|---------|
| `build_cookbook.py` | Main generator — assembles HTML from data + templates |
| `_new_tabs.py` | Dashboard, Meal Plan, Settings tabs; extra CSS & JS |
| `recipe_data.py` | All 38 recipes with macros, ingredients, steps, chef credits |
| `grocery_data.py` | Grocery categories, ingredient→recipe mappings, pantry staples |
| `weekly_agent.py` | (WIP) scheduled weekly meal plan refresh agent |
