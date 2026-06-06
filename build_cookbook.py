"""
build_cookbook.py
Generates recipe-book.html from recipe_data.py and grocery_data.py.
Run: python3 build_cookbook.py
"""
import json, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from recipe_data import RECIPES
from grocery_data import GROCERY_CATEGORIES, GENERAL_PANTRY, RECIPE_NAMES
from supabase_js import SUPABASE_JS
from _new_tabs import (EXTRA_CSS, SLOT_RECIPE_MAP, BATCH_IDS,
                       sidebar_html, dashboard_tab_html, settings_tab_html,
                       mealplan_tab_html, onboarding_modal_html, extra_js)

OUT = os.path.join(os.path.dirname(__file__), "cookbook", "index.html")

# ── helpers ────────────────────────────────────────────────────────────────

TIER_META = {
  "grab":     {"label": "Grab & Go",    "badge": "badge-grab",     "color": "#065f46"},
  "easy":     {"label": "Easy Everyday","badge": "badge-easy",     "color": "#1e40af"},
  "moderate": {"label": "Moderate",     "badge": "badge-moderate", "color": "#9a3412"},
  "batch":    {"label": "Batch Meal",   "badge": "badge-batch",    "color": "#5b21b6"},
  "snack":    {"label": "Snack",        "badge": "badge-snack",    "color": "#6b7280"},
}

def esc(s):
    return str(s).replace("&","&amp;").replace("<","&lt;").replace(">","&gt;").replace('"',"&quot;")

def recipe_row(r):
    tm = TIER_META[r["tier"]]
    ing_list = "".join(f"<li>{esc(i)}</li>" for i in r["ingredients"])
    step_list = "".join(f"<li>{esc(s)}</li>" for s in r["steps"])
    recipe_tags = json.dumps([r["id"]])  # for out-of-stock JS lookup
    return f"""
<tr class="recipe-row" data-tier="{r['tier']}" data-id="{r['id']}"
    data-name="{esc(r['name'].lower())}" data-chef="{esc(r['chef'].lower())}"
    data-ingredients="{esc(' '.join(r['ingredients']).lower())}"
    data-recipe-ids='{recipe_tags}'>
  <td><span class="tier-badge {tm['badge']}">{esc(tm['label'])}</span></td>
  <td class="recipe-name-cell">
    <span class="recipe-name">{esc(r['name'])}</span>
    <span class="stock-warn hidden" title="Some ingredients out of stock">⚠️</span>
  </td>
  <td class="hide-sm">{esc(r['chef'])}</td>
  <td class="hide-sm">{esc(r['time'])}</td>
  <td class="hide-sm">{esc(r['servings'])}</td>
  <td class="macro-cell">{r['macros']['kcal']}</td>
  <td class="macro-cell hide-md">{r['macros']['protein']}g</td>
  <td class="macro-cell hide-md">{r['macros']['carbs']}g</td>
  <td class="macro-cell hide-md">{r['macros']['fat']}g</td>
  <td><button class="expand-btn" onclick="toggleRow(this)" aria-label="Expand">▶</button></td>
</tr>
<tr class="detail-row hidden" data-detail-for="{r['id']}">
  <td colspan="10">
    <div class="detail-inner">
      <div class="detail-desc">{esc(r['description'])}</div>
      <div class="detail-cols">
        <div>
          <h4>Ingredients</h4>
          <ul class="ing-list">{ing_list}</ul>
        </div>
        <div>
          <h4>Method</h4>
          <ol class="step-list">{step_list}</ol>
        </div>
      </div>
      <div class="perf-tip-box">⚡ <strong>Performance Edge:</strong> {esc(r['perf_tip'])}</div>
      <div class="detail-actions">
        <button class="log-made-btn" onclick="logMade('{r['id']}', '{esc(r['name'])}')">✅ Mark as Made This Week</button>
      </div>
    </div>
  </td>
</tr>"""

def grocery_section(cat):
    items_js = json.dumps([{"name": i["name"], "recipes": i["recipes"]} for i in cat["items"]])
    rows = ""
    for item in cat["items"]:
        recipe_tags = "".join(
            f'<span class="recipe-tag" data-recipe="{rid}">{esc(RECIPE_NAMES.get(rid, rid))}</span>'
            for rid in item["recipes"]
        )
        rows += f"""
<tr class="grocery-row" data-item="{esc(item['name'].lower())}"
    data-recipes="{esc(' '.join(item['recipes']))}"
    data-cat="{cat['id']}">
  <td class="check-cell">
    <input type="checkbox" class="stock-check" data-item="{esc(item['name'])}"
      onchange="updateStock(this)" />
  </td>
  <td class="item-name">{esc(item['name'])}</td>
  <td class="recipe-tags-cell">{recipe_tags}</td>
  <td>
    <button class="out-btn" onclick="toggleOut(this, '{esc(item['name'])}')" title="Remove 'have it' mark">↩</button>
  </td>
</tr>"""
    return f"""
<div class="grocery-cat" id="cat-{cat['id']}">
  <div class="cat-header" onclick="toggleCat(this)">
    <span>{esc(cat['label'])}</span>
    <span class="cat-toggle">▾</span>
    <span class="cat-out-badge hidden">0 out of stock</span>
  </div>
  <div class="cat-body">
    <table class="grocery-table"><tbody>{rows}</tbody></table>
  </div>
</div>"""

def general_pantry_section():
    by_cat = {}
    for item in GENERAL_PANTRY:
        by_cat.setdefault(item["category"], []).append(item["name"])
    rows = ""
    for cat, items in by_cat.items():
        rows += f'<tr class="general-cat-header"><td colspan="3">{esc(cat)}</td></tr>'
        for name in items:
            rows += f"""
<tr class="grocery-row general-item" data-item="{esc(name.lower())}" data-cat="general">
  <td class="check-cell">
    <input type="checkbox" class="stock-check" data-item="{esc(name)}" onchange="updateStock(this)" />
  </td>
  <td class="item-name">{esc(name)}</td>
  <td>
    <button class="out-btn" onclick="toggleOut(this, '{esc(name)}')" title="Remove 'have it' mark">↩</button>
  </td>
</tr>"""
    return f"""
<div class="grocery-cat" id="cat-general">
  <div class="cat-header" onclick="toggleCat(this)">
    <span>🏠 General Pantry Staples</span>
    <span class="cat-toggle">▾</span>
    <span class="cat-out-badge hidden">0 out of stock</span>
  </div>
  <div class="cat-body">
    <table class="grocery-table general-table"><tbody>{rows}</tbody></table>
    <button class="add-general-btn" onclick="addGeneralItem()">＋ Add pantry item</button>
  </div>
</div>"""

def meal_planner_section():
    checkboxes = ""
    tiers_seen = []
    for r in RECIPES:
        if r["tier"] not in tiers_seen:
            tiers_seen.append(r["tier"])
            checkboxes += f'<div class="planner-tier-label">{TIER_META[r["tier"]]["label"]}</div>'
        checkboxes += f"""
<label class="planner-label" data-recipe-id="{r['id']}">
  <input type="checkbox" class="planner-check" value="{r['id']}"
    data-name="{esc(r['name'])}" onchange="updateMealPlan()">
  {esc(r['name'])}
</label>"""
    return f"""
<div id="meal-planner-panel">
  <div class="planner-intro">
    Tick what you're cooking this week. The shopping list below will update automatically.
  </div>
  <div id="planner-checkboxes">{checkboxes}</div>
  <div class="planner-actions">
    <button onclick="selectAll()">Select All</button>
    <button onclick="clearPlan()">Clear</button>
    <button onclick="syncMealPlanToGrocery()">🔄 Sync from Meal Plan</button>
    <button class="primary-btn" onclick="exportLog()">📤 Log Week &amp; Save</button>
  </div>
</div>"""

# ── JS data injected into page ─────────────────────────────────────────────

def js_data():
    # Build map: recipe_id -> list of ingredient names
    recipe_ingredients = {}
    for cat in GROCERY_CATEGORIES:
        for item in cat["items"]:
            for rid in item["recipes"]:
                recipe_ingredients.setdefault(rid, []).append(item["name"])
    return f"""
const RECIPE_NAMES = {json.dumps(RECIPE_NAMES)};
const RECIPE_INGREDIENTS = {json.dumps(recipe_ingredients)};
const ALL_RECIPE_IDS = {json.dumps([r['id'] for r in RECIPES])};
"""

# ── CSS ────────────────────────────────────────────────────────────────────

CSS = """
:root {
  --green:#2d6a4f; --green-l:#52b788; --green-pale:#d8f3dc;
  --amber:#e76f51; --blue:#457b9d; --purple:#5b21b6;
  --bg:#fafaf8; --card:#fff; --text:#1a1a2e; --muted:#6b7280;
  --border:#e5e7eb; --red:#dc2626; --red-pale:#fee2e2;
}
*{box-sizing:border-box;margin:0;padding:0;}
body{font-family:'Open Sans',sans-serif;background:var(--bg);color:var(--text);font-size:16px;line-height:1.6;}
a{color:var(--green);}

/* HEADER */
header{background:linear-gradient(135deg,var(--green),#40916c);color:#fff;padding:36px 24px 28px;text-align:center;}
header h1{font-size:2.1rem;margin-bottom:6px;}
header p{font-size:1rem;opacity:.88;font-family:sans-serif;max-width:540px;margin:0 auto;}

/* TABS */
.tabs{background:#fff;border-bottom:2px solid var(--border);display:flex;gap:0;position:sticky;top:0;z-index:200;}
.tab-btn{flex:1;padding:14px 10px;font-family:sans-serif;font-size:.9rem;font-weight:700;
  border:none;background:none;cursor:pointer;color:var(--muted);border-bottom:3px solid transparent;
  transition:all .15s;max-width:200px;}
.tab-btn.active{color:var(--green);border-bottom-color:var(--green);}
.tab-content{display:none;} .tab-content.active{display:block;}

/* CONTROLS */
.controls{background:#fff;border-bottom:1px solid var(--border);padding:16px 24px;
  display:flex;flex-wrap:wrap;gap:10px;align-items:center;justify-content:space-between;}
.filters{display:flex;flex-wrap:wrap;gap:8px;}
.filter-btn{border:2px solid var(--border);background:#fff;padding:7px 16px;border-radius:20px;
  cursor:pointer;font-family:'Open Sans',sans-serif;font-size:.84rem;font-weight:600;color:var(--muted);transition:all .15s;}
.filter-btn:hover{border-color:var(--green-l);color:var(--green);}
.filter-btn.active{color:#fff;}
.filter-btn[data-filter="all"].active{background:var(--green);border-color:var(--green);}
.filter-btn[data-filter="grab"].active{background:var(--green-l);border-color:var(--green-l);}
.filter-btn[data-filter="easy"].active{background:var(--blue);border-color:var(--blue);}
.filter-btn[data-filter="moderate"].active{background:var(--amber);border-color:var(--amber);}
.filter-btn[data-filter="batch"].active{background:#6d4c41;border-color:#6d4c41;}
.filter-btn[data-filter="snack"].active{background:var(--muted);border-color:var(--muted);}
#search{border:2px solid var(--border);padding:6px 14px;border-radius:20px;
  font-family:sans-serif;font-size:.82rem;outline:none;width:180px;transition:border .15s;}
#search:focus{border-color:var(--green-l);}
.add-recipe-btn{background:var(--green);color:#fff;border:none;padding:7px 16px;
  border-radius:20px;cursor:pointer;font-family:sans-serif;font-size:.82rem;font-weight:700;transition:background .15s;}
.add-recipe-btn:hover{background:#1b4332;}

/* RECIPE TABLE */
main{max-width:1300px;margin:0 auto;padding:32px 28px;}
.recipe-table-wrap{overflow-x:auto;}
table.recipe-table{width:100%;border-collapse:collapse;font-family:'Open Sans',sans-serif;font-size:.9rem;}
table.recipe-table th{background:var(--green-pale);color:var(--green);padding:13px 16px;
  text-align:left;font-weight:700;white-space:nowrap;cursor:pointer;user-select:none;}
table.recipe-table th:hover{background:#b7e4c7;}
.recipe-row td{padding:13px 16px;border-bottom:1px solid var(--border);vertical-align:middle;}
.recipe-row:hover td{background:#f0fdf4;}
.recipe-name-cell{min-width:200px;}
.recipe-name{font-weight:600;}
.stock-warn{font-size:.85rem;margin-left:6px;cursor:help;}
.macro-cell{text-align:right;color:var(--green);font-weight:700;}

/* TIER BADGES */
.tier-badge{font-size:.72rem;font-family:sans-serif;font-weight:700;padding:3px 9px;border-radius:10px;white-space:nowrap;}
.badge-grab{background:#d1fae5;color:#065f46;}
.badge-easy{background:#dbeafe;color:#1e40af;}
.badge-moderate{background:#fed7aa;color:#9a3412;}
.badge-batch{background:#f3e8ff;color:#5b21b6;}
.badge-snack{background:#f1f5f9;color:#475569;}

/* EXPAND BUTTON */
.expand-btn{background:none;border:1px solid var(--border);padding:3px 8px;border-radius:6px;
  cursor:pointer;font-size:.75rem;color:var(--muted);transition:all .15s;}
.expand-btn:hover{background:var(--green-pale);color:var(--green);}
.expand-btn.open{color:var(--green);border-color:var(--green);}

/* DETAIL ROW */
.detail-row td{padding:0;background:#f8fffe;border-bottom:2px solid var(--green-pale);}
.detail-inner{padding:28px 32px;}
.detail-desc{font-size:.95rem;color:#374151;margin-bottom:18px;font-style:italic;line-height:1.7;}
.detail-cols{display:grid;grid-template-columns:1fr 1fr;gap:28px;margin-bottom:18px;}
.detail-cols h4{color:var(--green);font-size:.9rem;margin-bottom:10px;font-family:'Open Sans',sans-serif;font-weight:700;}
.ing-list,.step-list{margin-left:20px;font-family:'Open Sans',sans-serif;font-size:.9rem;color:#374151;line-height:2;}
.perf-tip-box{background:var(--green-pale);border-left:3px solid var(--green-l);
  padding:10px 14px;border-radius:0 6px 6px 0;font-family:sans-serif;font-size:.83rem;color:var(--green);margin-bottom:12px;}
.detail-actions{display:flex;gap:10px;}
.log-made-btn{background:var(--green-pale);color:var(--green);border:1px solid var(--green-l);
  padding:7px 16px;border-radius:8px;cursor:pointer;font-family:sans-serif;font-size:.82rem;font-weight:600;transition:all .15s;}
.log-made-btn:hover{background:var(--green);color:#fff;}
.log-made-btn.done{background:var(--green);color:#fff;}

/* WEEK LOG BAR */
#log-bar{background:#1b4332;color:#fff;padding:10px 20px;font-family:sans-serif;font-size:.84rem;
  display:none;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:8px;}
#log-bar.visible{display:flex;}
#log-count{font-weight:700;}
#clear-log-btn{background:none;border:1px solid rgba(255,255,255,.4);color:#fff;
  padding:4px 12px;border-radius:6px;cursor:pointer;font-size:.8rem;}

/* NO RESULTS */
.no-results{text-align:center;padding:50px;color:var(--muted);font-family:sans-serif;}

/* ── GROCERY TAB ── */
#tab-grocery{max-width:1300px;margin:0 auto;padding:32px 28px;}
.grocery-layout{display:grid;grid-template-columns:320px 1fr;gap:24px;align-items:start;}

/* MEAL PLANNER PANEL */
#meal-planner-panel{background:#fff;border:1px solid var(--border);border-radius:12px;padding:20px;position:sticky;top:60px;}
#meal-planner-panel h3{color:var(--green);margin-bottom:10px;font-size:1rem;}
.planner-intro{font-family:sans-serif;font-size:.82rem;color:var(--muted);margin-bottom:14px;}
.planner-tier-label{font-family:sans-serif;font-size:.75rem;font-weight:700;color:var(--muted);
  text-transform:uppercase;letter-spacing:.05em;margin:12px 0 6px;padding-top:8px;border-top:1px solid var(--border);}
.planner-tier-label:first-child{border-top:none;margin-top:0;padding-top:0;}
.planner-label{display:flex;align-items:center;gap:8px;font-family:sans-serif;font-size:.83rem;
  color:#374151;padding:4px 0;cursor:pointer;}
.planner-label:hover{color:var(--green);}
.planner-label input{accent-color:var(--green);cursor:pointer;}
.planner-actions{margin-top:14px;display:flex;gap:8px;flex-wrap:wrap;}
.planner-actions button{font-family:sans-serif;font-size:.8rem;padding:7px 14px;border-radius:8px;
  cursor:pointer;border:1px solid var(--border);background:#fff;color:var(--muted);font-weight:600;transition:all .15s;}
.planner-actions button:hover{border-color:var(--green);color:var(--green);}
.primary-btn{background:var(--green)!important;color:#fff!important;border-color:var(--green)!important;}
.primary-btn:hover{background:#1b4332!important;}

/* GROCERY LIST RIGHT PANEL */
.grocery-right h3{color:var(--green);margin-bottom:4px;}
.grocery-filters{display:flex;gap:6px;flex-wrap:wrap;margin-bottom:16px;font-family:sans-serif;}
.gfilter-btn{border:2px solid var(--border);background:#fff;padding:4px 12px;border-radius:16px;
  cursor:pointer;font-size:.78rem;font-weight:600;color:var(--muted);transition:all .15s;}
.gfilter-btn.active,.gfilter-btn:hover{border-color:var(--green);color:var(--green);}
.gfilter-btn.active{background:var(--green-pale);}
#grocery-search{border:2px solid var(--border);padding:6px 14px;border-radius:20px;
  font-family:sans-serif;font-size:.82rem;outline:none;width:200px;margin-bottom:12px;transition:border .15s;}
#grocery-search:focus{border-color:var(--green-l);}
.grocery-header-row{display:flex;align-items:center;justify-content:space-between;margin-bottom:12px;}
.grocery-header-row h3{margin:0;}

/* GROCERY CATEGORY */
.grocery-cat{background:#fff;border:1px solid var(--border);border-radius:10px;margin-bottom:10px;overflow:hidden;}
.cat-header{background:var(--green-pale);padding:11px 16px;cursor:pointer;display:flex;
  align-items:center;gap:10px;font-family:sans-serif;font-size:.9rem;font-weight:700;color:var(--green);}
.cat-header:hover{background:#b7e4c7;}
.cat-toggle{margin-left:auto;transition:transform .2s;font-size:.8rem;}
.cat-header.collapsed .cat-toggle{transform:rotate(-90deg);}
.cat-body{transition:max-height .3s;}
.cat-out-badge{background:var(--red);color:#fff;font-size:.72rem;padding:2px 8px;border-radius:10px;margin-left:auto;}

/* GROCERY TABLE */
table.grocery-table{width:100%;border-collapse:collapse;font-family:'Open Sans',sans-serif;font-size:.9rem;}
.grocery-row td{padding:11px 16px;border-bottom:1px solid #f3f4f6;vertical-align:middle;}
.grocery-row:last-child td{border-bottom:none;}
.grocery-row:hover td{background:#f9fafb;}
.grocery-row.in-stock .item-name{text-decoration:line-through;color:var(--muted);}
.check-cell{width:30px;} .check-cell input{accent-color:var(--green);width:16px;height:16px;cursor:pointer;}
.item-name{font-weight:500;color:#374151;}
.recipe-tags-cell{width:50%;}
.recipe-tag{background:#f3f4f6;color:var(--muted);font-size:.72rem;padding:2px 7px;border-radius:10px;
  margin:2px;display:inline-block;cursor:pointer;transition:all .15s;}
.recipe-tag:hover{background:var(--green-pale);color:var(--green);}
.out-btn{background:none;border:none;cursor:pointer;font-size:1rem;padding:2px 4px;
  border-radius:4px;transition:opacity .15s;opacity:.6;}
.out-btn:hover{opacity:1;}
.out-btn.active{opacity:1;}

/* SHOPPING LIST SUMMARY */
#shopping-summary{background:#fff;border:1px solid var(--border);border-radius:10px;
  padding:16px;margin-bottom:16px;font-family:sans-serif;font-size:.84rem;}
#shopping-summary h4{color:var(--green);margin-bottom:10px;}
#shopping-summary-list{color:#374151;line-height:1.9;}
#shopping-summary-list .sum-item{display:flex;align-items:baseline;gap:6px;}
#shopping-summary-list .sum-item::before{content:'•';color:var(--green);}
.summary-empty{color:var(--muted);font-style:italic;}
.print-btn{background:var(--green-pale);color:var(--green);border:1px solid var(--green-l);
  padding:7px 16px;border-radius:8px;cursor:pointer;font-family:sans-serif;font-size:.82rem;font-weight:600;transition:all .15s;margin-top:10px;}
.print-btn:hover{background:var(--green);color:#fff;}

/* ADD ITEM */
.add-general-btn{background:none;border:1px dashed var(--border);width:100%;padding:8px;
  font-family:sans-serif;font-size:.82rem;color:var(--muted);cursor:pointer;transition:all .15s;margin:4px 0;}
.add-general-btn:hover{border-color:var(--green);color:var(--green);}

/* GENERAL TABLE */
table.general-table .general-cat-header td{background:var(--green-pale);color:var(--green);
  font-weight:700;font-size:.78rem;padding:6px 14px;text-transform:uppercase;letter-spacing:.04em;}

/* MODAL */
.modal-overlay{position:fixed;inset:0;background:rgba(0,0,0,.5);z-index:1000;
  display:none;align-items:center;justify-content:center;}
.modal-overlay.open{display:flex;}
.modal{background:#fff;border-radius:16px;padding:28px;width:min(700px,95vw);
  max-height:90vh;overflow-y:auto;position:relative;}
.modal h2{color:var(--green);margin-bottom:20px;font-size:1.3rem;}
.modal-close{position:absolute;top:16px;right:16px;background:none;border:none;
  font-size:1.4rem;cursor:pointer;color:var(--muted);}
.modal-close:hover{color:var(--text);}
.form-grid{display:grid;grid-template-columns:1fr 1fr;gap:14px;}
.form-full{grid-column:1/-1;}
.form-group{display:flex;flex-direction:column;gap:5px;}
.form-group label{font-family:sans-serif;font-size:.82rem;font-weight:600;color:var(--muted);}
.form-group input,.form-group select,.form-group textarea{
  border:2px solid var(--border);border-radius:8px;padding:8px 12px;
  font-family:sans-serif;font-size:.85rem;outline:none;transition:border .15s;}
.form-group input:focus,.form-group select:focus,.form-group textarea:focus{border-color:var(--green-l);}
.form-group textarea{resize:vertical;min-height:90px;}
.macro-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:10px;}
.modal-actions{display:flex;gap:10px;justify-content:flex-end;margin-top:20px;}
.modal-actions button{font-family:sans-serif;font-size:.85rem;padding:9px 20px;border-radius:8px;cursor:pointer;font-weight:600;}
.btn-cancel{border:1px solid var(--border);background:#fff;color:var(--muted);}
.btn-save{background:var(--green);color:#fff;border:none;}
.btn-save:hover{background:#1b4332;}

/* TOAST */
.toast{position:fixed;bottom:24px;right:24px;background:#1b4332;color:#fff;
  padding:12px 20px;border-radius:10px;font-family:sans-serif;font-size:.87rem;
  z-index:2000;opacity:0;transform:translateY(10px);transition:all .3s;pointer-events:none;}
.toast.show{opacity:1;transform:translateY(0);}

/* HIDE HELPERS */
.hidden{display:none!important;}
@media(max-width:900px){
  .hide-md{display:none;}
  .grocery-layout{grid-template-columns:1fr;}
  #meal-planner-panel{position:static;}
  .detail-cols{grid-template-columns:1fr;}
}
@media(max-width:600px){
  .hide-sm{display:none;}
  header h1{font-size:1.5rem;}
  .form-grid{grid-template-columns:1fr;}
}
"""
CSS += EXTRA_CSS

# ── JS ─────────────────────────────────────────────────────────────────────

JS = """
// ── Data from Python ──────────────────────────────────────────────────────
"""
# JS continued as a separate multi-line string to keep build.py under token limit
JS2 = r"""
// ── State ─────────────────────────────────────────────────────────────────
let stockStatus   = {};
let mealPlan      = [];
let weekLog       = JSON.parse(localStorage.getItem('vidya_log') || '[]');
let customRecipes = [];
let gFilter        = 'all';
let rFilter        = 'all';
let rSearch        = '';
let gSearch        = '';

// ── Tabs ──────────────────────────────────────────────────────────────────
function switchTab(id) {
  document.querySelectorAll('.tab-btn').forEach(b => b.classList.toggle('active', b.dataset.tab===id));
  document.querySelectorAll('.tab-content').forEach(c => c.classList.toggle('active', c.id==='tab-'+id));
}

// ── Recipe table ──────────────────────────────────────────────────────────
function toggleRow(btn) {
  const row = btn.closest('tr');
  const id  = row.dataset.id;
  const det = document.querySelector(`tr[data-detail-for="${id}"]`);
  const open = !det.classList.contains('hidden');
  // close all
  document.querySelectorAll('.detail-row').forEach(r => r.classList.add('hidden'));
  document.querySelectorAll('.expand-btn').forEach(b => { b.textContent='▶'; b.classList.remove('open'); });
  if (!open) {
    det.classList.remove('hidden');
    btn.textContent = '▼';
    btn.classList.add('open');
  }
}

function filterRecipes() {
  const rows = document.querySelectorAll('.recipe-row');
  let visible = 0;
  rows.forEach(row => {
    const tier = row.dataset.tier;
    const name = row.dataset.name || '';
    const chef = row.dataset.chef || '';
    const ing  = row.dataset.ingredients || '';
    const matchTier   = rFilter === 'all' || tier === rFilter;
    const matchSearch = !rSearch || name.includes(rSearch) || chef.includes(rSearch) || ing.includes(rSearch);
    const show = matchTier && matchSearch;
    row.classList.toggle('hidden', !show);
    const det = document.querySelector(`tr[data-detail-for="${row.dataset.id}"]`);
    if (det) det.classList.toggle('hidden', !show || det.classList.contains('hidden'));
    if (show) visible++;
  });
  document.getElementById('no-results').classList.toggle('hidden', visible > 0);
}

document.querySelectorAll('.filter-btn').forEach(btn => {
  btn.addEventListener('click', () => {
    document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    rFilter = btn.dataset.filter;
    filterRecipes();
  });
});
document.getElementById('search').addEventListener('input', e => {
  rSearch = e.target.value.toLowerCase().trim();
  filterRecipes();
});

// ── Stock management ──────────────────────────────────────────────────────
function saveStock() {}

// Reset button — removes "have it" status, item returns to "need to buy"
function toggleOut(btn, itemName) {
  const row = btn.closest('tr');
  delete stockStatus[itemName];
  row.classList.remove('in-stock');
  const cb = row.querySelector('.stock-check');
  if (cb) cb.checked = false;
  db_saveCartItem(itemName, false);
  refreshShoppingSummary();
}

function updateStock(cb) {
  const itemName = cb.dataset.item;
  const row = cb.closest('tr');
  const checked = cb.checked;
  if (checked) {
    stockStatus[itemName] = 'in';
    row.classList.add('in-stock');
  } else {
    delete stockStatus[itemName];
    row.classList.remove('in-stock');
  }
  db_saveCartItem(itemName, checked);
  refreshShoppingSummary();
}

function applyStockToUI() {
  // Restore "have it" checkmarks from saved state
  document.querySelectorAll('.grocery-row').forEach(row => {
    const nameEl = row.querySelector('.item-name');
    if (!nameEl) return;
    const name = nameEl.textContent.trim();
    if (stockStatus[name] === 'in') {
      row.classList.add('in-stock');
      const cb = row.querySelector('.stock-check');
      if (cb) cb.checked = true;
    }
  });
}

// ── Category collapse ─────────────────────────────────────────────────────
function toggleCat(header) {
  header.classList.toggle('collapsed');
  const body = header.nextElementSibling;
  body.style.display = header.classList.contains('collapsed') ? 'none' : '';
}

// ── Meal planner ──────────────────────────────────────────────────────────
function updateMealPlan() {
  mealPlan = [];
  document.querySelectorAll('.planner-check:checked').forEach(cb => mealPlan.push(cb.value));
  refreshGroceryForPlan();
  refreshShoppingSummary();
}

function refreshGroceryForPlan() {
  filterGrocery(); // grocery visibility is now fully controlled by filterGrocery
}

function refreshShoppingSummary() {
  const planSet = new Set(mealPlan);
  const summaryEl = document.getElementById('shopping-summary-list');
  if (!summaryEl) return;
  if (mealPlan.length === 0) {
    summaryEl.innerHTML = '<span class="summary-empty">Select recipes in the meal planner to generate your shopping list.</span>';
    return;
  }
  // Collect all needed ingredients not in stock
  const needed = new Set();
  mealPlan.forEach(rid => {
    const ings = RECIPE_INGREDIENTS[rid] || [];
    ings.forEach(ing => {
      if (stockStatus[ing] !== 'in') needed.add(ing);
    });
  });
  if (needed.size === 0) {
    summaryEl.innerHTML = '<span class="summary-empty">🎉 You have everything you need!</span>';
    return;
  }
  summaryEl.innerHTML = [...needed].sort()
    .map(i => `<div class="sum-item">${i}</div>`)
    .join('');
}

function selectAll() {
  document.querySelectorAll('.planner-check').forEach(cb => { cb.checked = true; });
  updateMealPlan();
}
function clearPlan() {
  document.querySelectorAll('.planner-check').forEach(cb => { cb.checked = false; });
  mealPlan = [];
  refreshGroceryForPlan();
  refreshShoppingSummary();
}

function restoreMealPlan() {
  const planSet = new Set(mealPlan);
  document.querySelectorAll('.planner-check').forEach(cb => {
    cb.checked = planSet.has(cb.value);
  });
  refreshGroceryForPlan();
  refreshShoppingSummary();
}

// ── Grocery filter ────────────────────────────────────────────────────────
function setGFilter(f) {
  gFilter = f;
  document.querySelectorAll('.gfilter-btn').forEach(b => b.classList.toggle('active', b.dataset.gfilter===f));
  filterGrocery();
}

function filterGrocery() {
  const q = gSearch.toLowerCase();
  const planSet = new Set(mealPlan);
  const hasPlan = mealPlan.length > 0;
  // Show/hide the no-plan placeholder
  const noplan = document.getElementById('grocery-no-plan');
  if (noplan) noplan.classList.toggle('hidden', hasPlan);
  document.querySelectorAll('.grocery-cat').forEach(catEl => {
    const catId    = catEl.id.replace('cat-','');
    const isGeneral = catId === 'general';
    // General pantry is always visible
    if (isGeneral) { catEl.classList.remove('hidden'); return; }
    // Recipe categories only shown when there's a plan
    if (!hasPlan) { catEl.classList.add('hidden'); return; }
    // Category-level tab filter
    const catMatch = gFilter === 'all' || gFilter !== 'general';
    if (!catMatch) { catEl.classList.add('hidden'); return; }
    let anyVisible = false;
    catEl.querySelectorAll('.grocery-row').forEach(row => {
      const name    = row.dataset.item || '';
      const recipes = (row.dataset.recipes || '').split(' ').filter(Boolean);
      const inPlan  = recipes.some(r => planSet.has(r));
      const matchQ  = !q || name.includes(q);
      const matchF  = gFilter === 'all' || recipes.includes(gFilter);
      const show = inPlan && matchQ && matchF;
      row.classList.toggle('hidden', !show);
      if (show) anyVisible = true;
    });
    catEl.classList.toggle('hidden', !anyVisible);
  });
}

document.getElementById('grocery-search').addEventListener('input', e => {
  gSearch = e.target.value.toLowerCase().trim();
  filterGrocery();
});

// ── Week log ──────────────────────────────────────────────────────────────
function logMade(id, name) {
  const btn = document.querySelector(`tr[data-detail-for="${id}"] .log-made-btn`);
  if (!weekLog.find(e => e.id === id)) {
    weekLog.push({ id, name, date: new Date().toISOString().slice(0,10) });
    localStorage.setItem('vidya_log', JSON.stringify(weekLog));
    showToast(`✅ "${name}" added to this week's log`);
  }
  if (btn) btn.classList.add('done');
  refreshLogBar();
}

function refreshLogBar() {
  const bar = document.getElementById('log-bar');
  const cnt = document.getElementById('log-count');
  if (weekLog.length === 0) { bar.classList.remove('visible'); return; }
  bar.classList.add('visible');
  cnt.textContent = `${weekLog.length} recipe${weekLog.length>1?'s':''} logged this week`;
}

function exportLog() {
  if (weekLog.length === 0) { showToast('No recipes logged yet — mark some as made first!'); return; }
  const blob = new Blob([JSON.stringify({
    week_of: new Date().toISOString().slice(0,10),
    recipes_made: weekLog
  }, null, 2)], { type: 'application/json' });
  const a = document.createElement('a');
  a.href = URL.createObjectURL(blob);
  a.download = `cooking_log_${new Date().toISOString().slice(0,10)}.json`;
  a.click();
  showToast('📥 cooking_log saved — the weekly agent will pick it up!');
}

document.getElementById('clear-log-btn').addEventListener('click', () => {
  weekLog = [];
  localStorage.setItem('vidya_log', JSON.stringify(weekLog));
  document.querySelectorAll('.log-made-btn').forEach(b => b.classList.remove('done'));
  refreshLogBar();
  showToast('Week log cleared');
});

function restoreLog() {
  weekLog.forEach(e => {
    const btn = document.querySelector(`tr[data-detail-for="${e.id}"] .log-made-btn`);
    if (btn) btn.classList.add('done');
  });
  refreshLogBar();
}

// ── Add Custom Recipe ─────────────────────────────────────────────────────
function openAddModal() { document.getElementById('add-modal').classList.add('open'); }
function closeAddModal() {
  document.getElementById('add-modal').classList.remove('open');
  document.getElementById('recipe-form').reset();
}
document.getElementById('add-modal').addEventListener('click', e => {
  if (e.target === document.getElementById('add-modal')) closeAddModal();
});

document.getElementById('recipe-form').addEventListener('submit', e => {
  e.preventDefault();
  const f = e.target;
  const newRecipe = {
    id: 'custom-' + Date.now(),
    name: f.rname.value.trim(),
    tier: f.rtier.value,
    tier_label: f.rtier.options[f.rtier.selectedIndex].text,
    chef: f.rchef.value.trim() || 'Custom',
    description: f.rdesc.value.trim(),
    time: f.rtime.value.trim(),
    servings: f.rservings.value.trim(),
    ingredients: f.ring.value.split('\n').map(s=>s.trim()).filter(Boolean),
    steps: f.rsteps.value.split('\n').map(s=>s.trim()).filter(Boolean),
    macros: {
      kcal: parseInt(f.rkcal.value)||0,
      protein: parseInt(f.rprotein.value)||0,
      carbs: parseInt(f.rcarbs.value)||0,
      fat: parseInt(f.rfat.value)||0,
    },
    perf_tip: f.rtip.value.trim(),
    custom: true,
  };
  customRecipes.push(newRecipe);
  db_saveCustomRecipe(newRecipe);
  injectCustomRecipe(newRecipe);
  closeAddModal();
  showToast(`🌿 "${newRecipe.name}" added to your cookbook!`);
});

function injectCustomRecipe(r) {
  const TIER_BADGES = {
    grab:'badge-grab',easy:'badge-easy',moderate:'badge-moderate',batch:'badge-batch',snack:'badge-snack'
  };
  const badge = TIER_BADGES[r.tier] || 'badge-snack';
  const ingHTML = r.ingredients.map(i=>`<li>${i}</li>`).join('');
  const stepHTML = r.steps.map(s=>`<li>${s}</li>`).join('');
  const tbody = document.querySelector('table.recipe-table tbody');
  const rowHTML = `
<tr class="recipe-row" data-tier="${r.tier}" data-id="${r.id}"
    data-name="${r.name.toLowerCase()}" data-chef="${r.chef.toLowerCase()}"
    data-ingredients="${r.ingredients.join(' ').toLowerCase()}">
  <td><span class="tier-badge ${badge}">${r.tier_label}</span></td>
  <td class="recipe-name-cell"><span class="recipe-name">${r.name}</span> <span class="recipe-tag" style="background:#fef9c3;color:#713f12;font-size:.7rem">Custom</span><span class="stock-warn hidden">⚠️</span></td>
  <td class="hide-sm">${r.chef}</td>
  <td class="hide-sm">${r.time}</td>
  <td class="hide-sm">${r.servings}</td>
  <td class="macro-cell">${r.macros.kcal}</td>
  <td class="macro-cell hide-md">${r.macros.protein}g</td>
  <td class="macro-cell hide-md">${r.macros.carbs}g</td>
  <td class="macro-cell hide-md">${r.macros.fat}g</td>
  <td><button class="expand-btn" onclick="toggleRow(this)">▶</button></td>
</tr>
<tr class="detail-row hidden" data-detail-for="${r.id}">
  <td colspan="10"><div class="detail-inner">
    <div class="detail-desc">${r.description}</div>
    <div class="detail-cols">
      <div><h4>Ingredients</h4><ul class="ing-list">${ingHTML}</ul></div>
      <div><h4>Method</h4><ol class="step-list">${stepHTML}</ol></div>
    </div>
    ${r.perf_tip ? `<div class="perf-tip-box">⚡ <strong>Performance Edge:</strong> ${r.perf_tip}</div>` : ''}
    <div class="detail-actions">
      <button class="log-made-btn" onclick="logMade('${r.id}','${r.name.replace(/'/g,"\\'")}')">✅ Mark as Made This Week</button>
    </div>
  </div></td>
</tr>`;
  tbody.insertAdjacentHTML('beforeend', rowHTML);
  // Add to planner
  const plannerEl = document.getElementById('planner-checkboxes');
  plannerEl.insertAdjacentHTML('beforeend', `
<label class="planner-label">
  <input type="checkbox" class="planner-check" value="${r.id}"
    data-name="${r.name}" onchange="updateMealPlan()"> ${r.name} <span style="font-size:.72rem;color:var(--muted)">(custom)</span>
</label>`);
}

// ── Add General Pantry Item ───────────────────────────────────────────────
function addGeneralItem() {
  const name = prompt('Enter pantry item name:');
  if (!name || !name.trim()) return;
  const cleanName = name.trim();
  const tbody = document.querySelector('#cat-general .general-table tbody');
  tbody.insertAdjacentHTML('beforeend', `
<tr class="grocery-row general-item" data-item="${cleanName.toLowerCase()}" data-cat="general">
  <td class="check-cell"><input type="checkbox" class="stock-check" data-item="${cleanName}" onchange="updateStock(this)" /></td>
  <td class="item-name">${cleanName}</td>
  <td><button class="out-btn" onclick="toggleOut(this,'${cleanName.replace(/'/g,"\\'")}')">🔴</button></td>
</tr>`);
  showToast(`Added "${cleanName}" to general pantry`);
}

// ── Grocery filter buttons ────────────────────────────────────────────────
function buildGroceryFilterBtns() {
  // Dynamically build per-recipe filter buttons from all recipe IDs
  // (already rendered as static All / General buttons — recipe tags are clickable)
}

// Recipe tag click → filter grocery to that recipe
document.addEventListener('click', e => {
  if (e.target.classList.contains('recipe-tag') && e.target.dataset.recipe) {
    const rid = e.target.dataset.recipe;
    switchTab('grocery');
    gFilter = rid;
    document.querySelectorAll('.gfilter-btn').forEach(b => b.classList.remove('active'));
    filterGrocery();
    showToast(`Showing ingredients for: ${RECIPE_NAMES[rid] || rid}`);
  }
});

// ── Toast ─────────────────────────────────────────────────────────────────
function showToast(msg) {
  const t = document.getElementById('toast');
  t.textContent = msg;
  t.classList.add('show');
  setTimeout(() => t.classList.remove('show'), 2800);
}

// ── Table sort ────────────────────────────────────────────────────────────
let sortCol = -1, sortAsc = true;
document.querySelectorAll('table.recipe-table th').forEach((th, i) => {
  th.addEventListener('click', () => {
    if (sortCol === i) sortAsc = !sortAsc; else { sortCol = i; sortAsc = true; }
    const tbody = document.querySelector('table.recipe-table tbody');
    // collect only recipe-rows (not detail rows)
    const pairs = [];
    document.querySelectorAll('.recipe-row').forEach(row => {
      const det = document.querySelector(`tr[data-detail-for="${row.dataset.id}"]`);
      pairs.push([row, det]);
    });
    pairs.sort((a, b) => {
      const at = a[0].cells[i]?.textContent.trim() || '';
      const bt = b[0].cells[i]?.textContent.trim() || '';
      const an = parseFloat(at), bn = parseFloat(bt);
      if (!isNaN(an) && !isNaN(bn)) return sortAsc ? an-bn : bn-an;
      return sortAsc ? at.localeCompare(bt) : bt.localeCompare(at);
    });
    pairs.forEach(([row, det]) => { tbody.appendChild(row); if(det) tbody.appendChild(det); });
  });
});

// ── Init ──────────────────────────────────────────────────────────────────
document.addEventListener('DOMContentLoaded', () => {
  initAuth();
});
"""

# ── BUILD HTML ─────────────────────────────────────────────────────────────

def build():
    # Recipe rows
    recipe_rows = "".join(recipe_row(r) for r in RECIPES)

    # Grocery sections
    grocery_sections = "".join(grocery_section(c) for c in GROCERY_CATEGORIES)
    grocery_sections += general_pantry_section()

    # Grocery filter buttons (one per recipe)
    gfilter_btns = '\n'.join(
        f'<button class="gfilter-btn" data-gfilter="{rid}" onclick="setGFilter(\'{rid}\')">{esc(name)}</button>'
        for rid, name in RECIPE_NAMES.items()
    )

    # Extra JS for new tabs (dashboard, meal plan, settings)
    recipe_data_js = {r['id']: {
        'name': r['name'], 'tier': r['tier'],
        'tier_label': r['tier_label'], 'macros': r['macros']
    } for r in RECIPES}
    extra_js_code = extra_js(
        json.dumps(recipe_data_js),
        json.dumps(SLOT_RECIPE_MAP),
        json.dumps(BATCH_IDS)
    )

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Vidya's Vegetarian Performance Cookbook</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
<script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2"></script>
<style>{CSS}</style>
</head>
<body>

<div id="auth-screen" style="min-height:100vh;display:flex;align-items:center;justify-content:center;background:var(--bg);">
  <div style="background:#fff;border:1px solid var(--border);border-radius:16px;padding:40px 36px;width:min(420px,92vw);box-shadow:0 4px 24px rgba(0,0,0,.08);">
    <div style="text-align:center;margin-bottom:28px;">
      <div style="font-size:2.5rem;margin-bottom:10px;">🌿</div>
      <h1 id="auth-title" style="font-size:1.3rem;color:var(--green);font-family:'Open Sans',sans-serif;font-weight:700;margin:0 0 6px;">Sign in to your cookbook</h1>
      <p style="font-family:sans-serif;font-size:.88rem;color:var(--muted);margin:0;">Meal planning built for your training goals</p>
    </div>
    <form id="auth-form" autocomplete="on">
      <div style="margin-bottom:12px;">
        <input type="email" id="auth-email" placeholder="Email address" autocomplete="email"
          style="width:100%;border:2px solid var(--border);border-radius:8px;padding:11px 14px;font-family:sans-serif;font-size:.92rem;outline:none;box-sizing:border-box;">
      </div>
      <div style="margin-bottom:20px;">
        <input type="password" id="auth-password" placeholder="Password" autocomplete="current-password"
          style="width:100%;border:2px solid var(--border);border-radius:8px;padding:11px 14px;font-family:sans-serif;font-size:.92rem;outline:none;box-sizing:border-box;">
      </div>
      <button type="submit" id="auth-submit"
        style="width:100%;background:var(--green);color:#fff;border:none;border-radius:8px;padding:13px;font-family:sans-serif;font-weight:700;font-size:.95rem;cursor:pointer;">Sign In</button>
    </form>
    <div style="text-align:center;margin-top:14px;">
      <button onclick="sendMagicLink()" style="background:none;border:none;color:var(--green);font-family:sans-serif;font-size:.84rem;cursor:pointer;text-decoration:underline;padding:0;">Send magic link instead</button>
    </div>
    <div style="text-align:center;margin-top:8px;">
      <button id="auth-toggle" onclick="toggleAuthMode()" style="background:none;border:none;color:var(--muted);font-family:sans-serif;font-size:.82rem;cursor:pointer;padding:0;">Don't have an account? Sign up</button>
    </div>
    <div id="auth-message" style="margin-top:14px;text-align:center;font-family:sans-serif;font-size:.84rem;color:var(--red);min-height:18px;"></div>
  </div>
</div>

<div id="app-container" style="display:none">

<div id="log-bar">
  <span>📋 Week Log: <span id="log-count"></span></span>
  <div style="display:flex;gap:8px;align-items:center">
    <span style="font-size:.8rem;opacity:.7">Log Week in Meal Planner tab to export</span>
    <button id="clear-log-btn">Clear Log</button>
  </div>
</div>

<nav class="tabs">
  <button class="tab-btn" data-tab="recipes" onclick="switchTab('recipes')">📖 Recipes</button>
  <button class="tab-btn" data-tab="grocery" onclick="switchTab('grocery')">🛒 Grocery &amp; Pantry</button>
</nav>

{sidebar_html()}

<!-- ═══════════════════ DASHBOARD TAB ═══════════════════ -->
{dashboard_tab_html()}

<!-- ═══════════════════ MEAL PLAN TAB ═══════════════════ -->
{mealplan_tab_html()}

<!-- ═══════════════════ GROCERY TAB ═══════════════════ -->
<div id="tab-grocery" class="tab-content">
  <div class="grocery-layout">

    <!-- LEFT: This Week -->
    <div>
      <h3 style="color:var(--green);margin-bottom:12px;font-family:sans-serif;">📅 This Week</h3>
      {meal_planner_section()}
    </div>

    <!-- RIGHT: Grocery List -->
    <div class="grocery-right">
      <div class="grocery-header-row">
        <h3 style="font-family:sans-serif;">🛒 Ingredients &amp; Pantry</h3>
      </div>

      <!-- Shopping summary -->
      <div id="shopping-summary">
        <h4>This Week's Shopping List</h4>
        <div id="shopping-summary-list"><span class="summary-empty">Select recipes in This Week to generate your shopping list.</span></div>
        <button class="print-btn" onclick="window.print()">🖨 Print / Save List</button>
      </div>

      <!-- Grocery filters -->
      <div style="margin-bottom:10px;">
        <input type="text" id="grocery-search" placeholder="Search ingredients…">
      </div>
      <div class="grocery-filters">
        <button class="gfilter-btn active" data-gfilter="all" onclick="setGFilter('all')">All</button>
        <button class="gfilter-btn" data-gfilter="general" onclick="setGFilter('general')">🏠 General</button>
        {gfilter_btns}
      </div>

      <!-- No-plan placeholder -->
      <div id="grocery-no-plan">
        🗓 Select recipes in <strong>This Week</strong> to build your grocery list.
        <br><br><a onclick="syncMealPlanToGrocery ? switchTab('grocery') : null; switchTab('mealplan'); generateMealPlan()">Generate a meal plan →</a>
      </div>

      <!-- Category sections -->
      {grocery_sections}
    </div>
  </div>
</div>

<!-- ═══════════════════ RECIPES TAB ═══════════════════ -->
<div id="tab-recipes" class="tab-content">
  <div class="controls">
    <div class="filters">
      <button class="filter-btn active" data-filter="all">All</button>
      <button class="filter-btn" data-filter="grab">⚡ Grab &amp; Go</button>
      <button class="filter-btn" data-filter="easy">🥗 Easy</button>
      <button class="filter-btn" data-filter="moderate">🍳 Moderate</button>
      <button class="filter-btn" data-filter="batch">🥘 Batch</button>
      <button class="filter-btn" data-filter="snack">🍎 Snacks</button>
    </div>
    <div style="display:flex;gap:8px;align-items:center">
      <input type="text" id="search" placeholder="Search recipes…">
      <button class="add-recipe-btn" onclick="openAddModal()">＋ Add Recipe</button>
    </div>
  </div>
  <main>
    <div class="recipe-table-wrap">
      <table class="recipe-table">
        <thead>
          <tr>
            <th>Tier</th><th>Recipe</th><th class="hide-sm">Chef</th>
            <th class="hide-sm">Time</th><th class="hide-sm">Serves</th>
            <th>kcal</th><th class="hide-md">Protein</th>
            <th class="hide-md">Carbs</th><th class="hide-md">Fat</th><th></th>
          </tr>
        </thead>
        <tbody>
{recipe_rows}
        </tbody>
      </table>
    </div>
    <div class="no-results hidden" id="no-results">No recipes match your search.</div>
  </main>
</div>

<!-- ═══════════════════ SETTINGS TAB ═══════════════════ -->
{settings_tab_html()}

</div><!-- /main-area -->
</div><!-- /app-body -->

<!-- ═══════════════════ ONBOARDING MODAL ═══════════════════ -->
{onboarding_modal_html()}

<!-- ═══════════════════ ADD RECIPE MODAL ═══════════════════ -->
<div class="modal-overlay" id="add-modal">
  <div class="modal">
    <button class="modal-close" onclick="closeAddModal()">✕</button>
    <h2>🌿 Add a New Recipe</h2>
    <form id="recipe-form">
      <div class="form-grid">
        <div class="form-group form-full">
          <label>Recipe Name *</label>
          <input type="text" name="rname" required placeholder="e.g. Miso Glazed Aubergine">
        </div>
        <div class="form-group">
          <label>Tier *</label>
          <select name="rtier" required>
            <option value="grab">Grab &amp; Go</option>
            <option value="easy">Easy Everyday</option>
            <option value="moderate">Moderate</option>
            <option value="batch">Batch Meal</option>
            <option value="snack">Snack</option>
          </select>
        </div>
        <div class="form-group">
          <label>Chef Inspiration</label>
          <input type="text" name="rchef" placeholder="e.g. Yotam Ottolenghi">
        </div>
        <div class="form-group">
          <label>Time</label>
          <input type="text" name="rtime" placeholder="e.g. 25 min">
        </div>
        <div class="form-group">
          <label>Servings</label>
          <input type="text" name="rservings" placeholder="e.g. 2">
        </div>
        <div class="form-group form-full">
          <label>Description</label>
          <input type="text" name="rdesc" placeholder="Short description of the dish">
        </div>
        <div class="form-group form-full">
          <label>Ingredients (one per line) *</label>
          <textarea name="ring" required placeholder="400g firm tofu, pressed&#10;2 tbsp soy sauce&#10;1 tsp sesame oil"></textarea>
        </div>
        <div class="form-group form-full">
          <label>Steps (one per line) *</label>
          <textarea name="rsteps" required placeholder="Step 1: Press the tofu for 20 minutes.&#10;Step 2: ..."></textarea>
        </div>
        <div class="form-group form-full">
          <label>Macros (per serving)</label>
          <div class="macro-grid">
            <div class="form-group"><label>kcal</label><input type="number" name="rkcal" placeholder="400"></div>
            <div class="form-group"><label>Protein (g)</label><input type="number" name="rprotein" placeholder="18"></div>
            <div class="form-group"><label>Carbs (g)</label><input type="number" name="rcarbs" placeholder="50"></div>
            <div class="form-group"><label>Fat (g)</label><input type="number" name="rfat" placeholder="14"></div>
          </div>
        </div>
        <div class="form-group form-full">
          <label>Performance Tip (optional)</label>
          <textarea name="rtip" placeholder="e.g. Eat this post-workout for..."></textarea>
        </div>
      </div>
      <div class="modal-actions">
        <button type="button" class="btn-cancel" onclick="closeAddModal()">Cancel</button>
        <button type="submit" class="btn-save">Save Recipe</button>
      </div>
    </form>
  </div>
</div>

<div class="toast" id="toast"></div>

</div><!-- /app-container -->

<script>
{SUPABASE_JS}
{JS}
{js_data()}
{JS2}
{extra_js_code}
</script>
</body>
</html>"""
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"✅  Built: {OUT}")
    print(f"   Recipes: {len(RECIPES)}")
    print(f"   Grocery categories: {len(GROCERY_CATEGORIES)}")
    print(f"   General pantry items: {len(GENERAL_PANTRY)}")

if __name__ == "__main__":
    build()
