"""
_new_tabs.py
New tab HTML, extra CSS, and extra JS for: Dashboard, Meal Plan, Settings.
Imported by build_cookbook.py.
"""
import json

# ── SLOT / RECIPE MAPPINGS ─────────────────────────────────────────────────
SLOT_RECIPE_MAP = {
    "breakfast": ["berry-chia-pudding","yogurt-parfait","avocado-egg-toast",
                  "tofu-scramble","shakshuka","date-energy-bites","chickpea-wrap"],
    "lunch":     ["quinoa-bowl","bean-tacos","fried-rice","chickpea-salad",
                  "lentil-soup","caprese-toast","miso-noodles","zucchini-fritters",
                  "stuffed-peppers","buddha-bowl"],
    "dinner":    ["enchiladas","mushroom-risotto","tikka-masala","thai-curry",
                  "stuffed-shells","saag-paneer","red-lentil-dal","moroccan-stew",
                  "veg-chili","minestrone","tomato-bean-soup","veg-biryani","shakshuka"],
    "snack":     ["roasted-chickpeas","rice-cakes-hummus","trail-mix",
                  "apple-almond-butter","hard-boiled-eggs","edamame-salt",
                  "cheese-crackers","banana-pb"],
}
BATCH_IDS = ["red-lentil-dal","moroccan-stew","veg-chili","minestrone",
             "tomato-bean-soup","veg-biryani","kale-salad"]

# ── EXTRA CSS ──────────────────────────────────────────────────────────────
EXTRA_CSS = """
/* ── SIDEBAR LAYOUT (replaces top tabs) ── */
.tabs { display: none !important; }
.app-body { display: flex; min-height: 100vh; }

.sidebar {
  width: 214px; flex-shrink: 0;
  background: #fff; border-right: 1px solid var(--border);
  padding: 0 0 12px; position: sticky; top: 0;
  height: 100vh; overflow-y: auto; z-index: 150;
}
.sidebar-brand {
  padding: 22px 20px 16px;
  border-bottom: 1px solid var(--border);
  margin-bottom: 10px;
}
.sidebar-brand-title {
  font-family: 'Open Sans', sans-serif; font-size: 1.05rem; font-weight: 700;
  color: var(--green); line-height: 1.2;
}
.sidebar-section-label {
  font-family: sans-serif; font-size: .7rem; font-weight: 700;
  color: var(--muted); text-transform: uppercase; letter-spacing: .06em;
  padding: 14px 18px 4px;
}
.nav-item {
  display: flex; align-items: center; gap: 10px;
  padding: 11px 16px; margin: 2px 8px;
  font-family: 'Open Sans', sans-serif; font-size: .9rem; font-weight: 600;
  color: #4b5563; cursor: pointer; border-radius: 8px; transition: all .15s;
  text-decoration: none;
}
.nav-item:hover { background: var(--green-pale); color: var(--green); }
.nav-item.active { background: var(--green-pale); color: var(--green); }
.nav-icon { font-size: 1rem; width: 22px; text-align: center; flex-shrink: 0; }
.nav-badge {
  margin-left: auto; background: var(--red); color: #fff;
  font-size: .68rem; padding: 1px 6px; border-radius: 10px; font-weight: 700;
}
.main-area { flex: 1; min-width: 0; overflow-x: hidden; }

/* ── SETUP BANNER ── */
.setup-banner {
  background: #fff7ed; border-left: 4px solid var(--amber);
  margin: 16px 20px 0; padding: 10px 16px; border-radius: 0 8px 8px 0;
  font-family: sans-serif; font-size: .84rem; color: #92400e;
  display: flex; align-items: center; justify-content: space-between; gap: 12px;
}
.setup-banner a { color: var(--amber); font-weight: 700; cursor: pointer; text-decoration: underline; }

/* ── DASHBOARD ── */
#tab-dashboard { padding: 36px 32px; max-width: 1100px; margin: 0 auto; }
.dash-greeting { font-size: 1.65rem; font-weight: 700; margin-bottom: 6px; }
.dash-sub { font-family: 'Open Sans', sans-serif; font-size: .95rem; color: var(--muted); margin-bottom: 32px; }
.dash-grid { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 20px; margin-bottom: 32px; }
.dash-card {
  background: #fff; border: 1px solid var(--border); border-radius: 14px;
  padding: 24px; transition: box-shadow .15s;
}
.dash-card:hover { box-shadow: 0 4px 16px rgba(0,0,0,.07); }
.dash-card-label {
  font-family: 'Open Sans', sans-serif; font-size: .8rem; font-weight: 700;
  color: var(--muted); text-transform: uppercase; letter-spacing: .05em; margin-bottom: 14px;
}
.dash-card-big { font-size: 2.2rem; font-weight: 700; color: var(--green); font-family: 'Open Sans', sans-serif; }
.dash-card-unit { font-size: .88rem; color: var(--muted); font-family: 'Open Sans', sans-serif; }

/* today's meals on dashboard */
.today-meals { background: #fff; border: 1px solid var(--border); border-radius: 14px; padding: 24px; margin-bottom: 24px; }
.today-meals h3 { font-size: 1.05rem; color: var(--green); margin-bottom: 18px; font-family: 'Open Sans', sans-serif; font-weight: 700; }
.today-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 12px; }
.today-slot { background: var(--bg); border-radius: 10px; padding: 16px; }
.today-slot-label { font-family: 'Open Sans', sans-serif; font-size: .75rem; font-weight: 700; color: var(--muted); text-transform: uppercase; letter-spacing: .04em; margin-bottom: 8px; }
.today-slot-name { font-family: 'Open Sans', sans-serif; font-size: .9rem; font-weight: 600; color: var(--text); line-height: 1.4; }
.today-slot-kcal { font-family: 'Open Sans', sans-serif; font-size: .8rem; color: var(--muted); margin-top: 6px; }
.today-empty { color: var(--muted); font-style: italic; font-size: .85rem; }

/* macro progress bars on dashboard */
.macro-progress { background: #fff; border: 1px solid var(--border); border-radius: 14px; padding: 24px; margin-bottom: 24px; }
.macro-progress h3 { font-size: 1.05rem; color: var(--green); margin-bottom: 18px; font-family: 'Open Sans', sans-serif; font-weight: 700; }
.mp-prog-row { display: flex; align-items: center; gap: 14px; margin-bottom: 12px; font-family: 'Open Sans', sans-serif; font-size: .88rem; }
.mp-prog-label { width: 70px; font-weight: 600; color: #374151; }
.mp-prog-bar-wrap { flex: 1; background: var(--border); border-radius: 20px; height: 10px; overflow: hidden; }
.mp-prog-bar-fill { height: 100%; border-radius: 20px; transition: width .5s ease; }
.mp-prog-bar-fill.protein { background: #3b82f6; }
.mp-prog-bar-fill.carbs   { background: var(--green-l); }
.mp-prog-bar-fill.fat     { background: var(--amber); }
.mp-prog-val { width: 90px; text-align: right; color: var(--muted); font-size: .78rem; }

/* quick actions */
.quick-actions { display: grid; grid-template-columns: repeat(3, 1fr); gap: 12px; margin-bottom: 20px; }
.qa-btn {
  background: #fff; border: 1.5px solid var(--border); border-radius: 12px;
  padding: 16px; cursor: pointer; transition: all .15s;
  text-align: left; font-family: sans-serif;
}
.qa-btn:hover { border-color: var(--green-l); background: var(--green-pale); }
.qa-icon { font-size: 1.4rem; margin-bottom: 8px; display: block; }
.qa-title { font-weight: 700; font-size: .9rem; color: var(--text); display: block; margin-bottom: 2px; }
.qa-desc  { font-size: .78rem; color: var(--muted); display: block; }

/* ── SETTINGS TAB ── */
#tab-settings { padding: 36px 32px; max-width: 960px; margin: 0 auto; }
#tab-settings h2 { font-size: 1.5rem; color: var(--green); margin-bottom: 8px; font-weight: 700; }
#tab-settings .tab-desc { font-family: 'Open Sans', sans-serif; font-size: .95rem; color: var(--muted); margin-bottom: 28px; line-height: 1.6; }
.settings-layout { display: grid; grid-template-columns: 1fr 1fr; gap: 24px; }
.settings-card {
  background: #fff; border: 1px solid var(--border); border-radius: 14px; padding: 28px;
}
.settings-card h3 { color: var(--green); margin-bottom: 16px; font-size: .95rem; font-family: sans-serif; font-weight: 700; }
.settings-form { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; }
.setting-group { display: flex; flex-direction: column; gap: 5px; }
.setting-group label { font-family: sans-serif; font-size: .8rem; font-weight: 600; color: var(--muted); }
.setting-group input, .setting-group select {
  border: 2px solid var(--border); border-radius: 8px; padding: 8px 11px;
  font-family: sans-serif; font-size: .87rem; outline: none; transition: border .15s;
  background: #fff;
}
.setting-group input:focus, .setting-group select:focus { border-color: var(--green-l); }
.height-inputs { display: flex; gap: 8px; }
.height-inputs input { flex: 1; }
.height-inputs .ht-label { font-family: sans-serif; font-size: .75rem; color: var(--muted); margin-top: 4px; text-align: center; }
.calc-btn {
  background: var(--green); color: #fff; border: none;
  padding: 11px 20px; border-radius: 8px; cursor: pointer;
  font-family: sans-serif; font-weight: 700; font-size: .9rem;
  margin-top: 16px; width: 100%; transition: background .15s; letter-spacing: .02em;
}
.calc-btn:hover { background: #1b4332; }
.settings-results {
  grid-column: 1 / -1;
  background: var(--green-pale); border: 1px solid var(--green-l);
  border-radius: 12px; padding: 22px;
}
.results-empty {
  font-family: sans-serif; font-size: .9rem; color: var(--green);
  text-align: center; padding: 16px 0; opacity: .7;
}
.results-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 12px; margin-bottom: 16px; }
.result-card {
  background: #fff; border-radius: 10px; padding: 14px;
  text-align: center; box-shadow: 0 1px 4px rgba(0,0,0,.05);
}
.result-big { font-size: 1.5rem; font-weight: 700; color: var(--green); font-family: sans-serif; line-height: 1; }
.result-unit { font-size: .72rem; color: var(--muted); font-family: sans-serif; margin-top: 2px; }
.result-lbl  { font-size: .8rem; color: #374151; font-family: sans-serif; margin-top: 4px; }
.macro-target-row { display: grid; grid-template-columns: repeat(3,1fr); gap: 12px; margin-bottom: 14px; }
.macro-target-card { background: #fff; border-radius: 10px; padding: 14px; text-align: center; }
.macro-target-card .mt-v { font-size: 1.4rem; font-weight: 700; font-family: sans-serif; line-height: 1; }
.macro-target-card .mt-l { font-size: .78rem; color: var(--muted); font-family: sans-serif; margin-top: 4px; }
.protein-card .mt-v { color: #3b82f6; }
.carbs-card   .mt-v { color: var(--green); }
.fat-card     .mt-v { color: var(--amber); }
.calc-breakdown {
  background: #fff; border-radius: 8px; padding: 12px 16px;
  font-family: sans-serif; font-size: .82rem; color: #374151; line-height: 1.85;
}
.calc-breakdown strong { color: var(--green); }

/* ── MEAL PLAN TAB ── */
#tab-mealplan { padding: 24px 20px; max-width: 1200px; margin: 0 auto; }
.mp-header-row {
  display: flex; align-items: center; flex-wrap: wrap; gap: 12px; margin-bottom: 22px;
}
.mp-header-row h2 { font-size: 1.25rem; color: var(--green); flex: 1; }
.mp-btns { display: flex; gap: 8px; flex-wrap: wrap; }
.mp-btn { font-family:sans-serif; font-size:.84rem; font-weight:700; padding:9px 18px; border-radius:8px; cursor:pointer; transition:all .15s; }
.mp-btn-primary { background:var(--green); color:#fff; border:none; }
.mp-btn-primary:hover { background:#1b4332; }
.mp-btn-ghost { background:#fff; color:var(--green); border:2px solid var(--green-l); }
.mp-btn-ghost:hover { background:var(--green-pale); }
.mp-btn-muted { background:#fff; color:var(--muted); border:2px solid var(--border); }
.mp-btn-muted:hover { border-color:var(--muted); }

/* empty state */
.mp-empty-state {
  text-align: center; padding: 60px 20px;
  background: #fff; border: 2px dashed var(--border); border-radius: 16px; margin-bottom: 24px;
}
.mp-empty-icon { font-size: 3rem; margin-bottom: 12px; }
.mp-empty-title { font-size: 1.1rem; font-weight: 700; color: var(--text); margin-bottom: 6px; }
.mp-empty-desc { font-family: sans-serif; font-size: .88rem; color: var(--muted); margin-bottom: 20px; }
.mp-gen-big-btn {
  background: var(--green); color: #fff; border: none;
  padding: 13px 32px; border-radius: 10px; cursor: pointer;
  font-family: sans-serif; font-weight: 700; font-size: 1rem; transition: background .15s;
}
.mp-gen-big-btn:hover { background: #1b4332; }

/* grid */
.mp-grid-scroll { overflow-x: auto; margin-bottom: 28px; }
.mp-grid {
  display: grid; grid-template-columns: 90px repeat(7, minmax(110px,1fr));
  gap: 6px; min-width: 860px;
}
.mp-corner { }
.mp-day-hdr {
  font-family: sans-serif; font-size: .8rem; font-weight: 700; color: var(--green);
  text-align: center; padding: 8px 4px; background: var(--green-pale); border-radius: 6px;
}
.mp-slot-lbl {
  font-family: sans-serif; font-size: .8rem; font-weight: 700; color: var(--muted);
  display: flex; align-items: center; justify-content: flex-end;
  padding-right: 6px; text-align: right;
}
.mp-cell {
  background: #fff; border: 1.5px solid var(--border); border-radius: 8px;
  min-height: 72px; padding: 8px; cursor: pointer; transition: all .15s; position: relative;
}
.mp-cell:hover { border-color: var(--green-l); background: #f0fdf4; }
.mp-cell.empty { border-style: dashed; background: #fafafa; }
.mp-cell.empty:hover { background: var(--green-pale); }
.mp-chip-name { font-family:sans-serif; font-size:.78rem; font-weight:700; color:var(--text); line-height:1.3; margin-bottom:3px; }
.mp-chip-cals { font-family:sans-serif; font-size:.7rem; color:var(--muted); }
.mp-chip-macros { font-family:sans-serif; font-size:.68rem; color:var(--muted); }
.mp-total-lbl {
  font-family:sans-serif; font-size:.78rem; font-weight:700; color:var(--green);
  display:flex; align-items:center; justify-content:flex-end; padding-right:6px;
}
.mp-total-cell {
  background: var(--green-pale); border: 1px solid var(--green-l);
  border-radius: 8px; padding: 8px; cursor: default;
}
.mp-total-kcal { font-family:sans-serif; font-size:.8rem; font-weight:700; color:var(--green); }
.mp-total-macros { font-family:sans-serif; font-size:.7rem; color:var(--muted); }

/* picker dropdown */
.mp-picker {
  position: absolute; top: calc(100% + 4px); left: 0; z-index: 300;
  background: #fff; border: 1px solid var(--border); border-radius: 10px;
  box-shadow: 0 6px 20px rgba(0,0,0,.12); width: 230px; max-height: 260px; overflow-y: auto;
}
.mp-picker-item {
  padding: 8px 14px; cursor: pointer; font-family:sans-serif; font-size:.82rem;
  border-bottom: 1px solid #f3f4f6; transition: background .1s;
}
.mp-picker-item:hover { background: var(--green-pale); }
.mp-picker-item:last-child { border-bottom: none; }
.mp-picker-item .pi-tier { font-size:.7rem; color:var(--muted); }
.mp-picker-remove { color:var(--red); font-style:italic; }

/* macros chart */
.mp-chart-card { background:#fff; border:1px solid var(--border); border-radius:12px; padding:22px; margin-bottom:16px; }
.mp-chart-card h3 { color:var(--green); font-size:.95rem; margin-bottom:18px; font-family:sans-serif; }
.bar-chart-area { display:flex; align-items:flex-end; gap:10px; height:160px; padding-bottom:28px; position:relative; }
.bar-col { display:flex; flex-direction:column; align-items:center; flex:1; height:100%; justify-content:flex-end; }
.bar-kcal-label { font-family:sans-serif; font-size:.7rem; font-weight:700; color:var(--text); margin-bottom:3px; }
.bar-stack { width:80%; border-radius:4px 4px 0 0; overflow:hidden; transition:height .4s ease; display:flex; flex-direction:column; }
.bar-seg-fat     { background:var(--amber); }
.bar-seg-carbs   { background:var(--green-l); }
.bar-seg-protein { background:#3b82f6; }
.bar-day-label { font-family:sans-serif; font-size:.72rem; color:var(--muted); margin-top:6px; }
.bar-target-line { position:absolute; left:0; right:0; border-top:2.5px dashed var(--amber); pointer-events:none; }
.bar-target-lbl { position:absolute; right:4px; top:-18px; font-family:sans-serif; font-size:.7rem; color:var(--amber); font-weight:700; background:#fff; padding:1px 4px; border-radius:4px; }
.chart-legend { display:flex; gap:16px; margin-top:10px; font-family:sans-serif; font-size:.78rem; color:var(--muted); flex-wrap:wrap; }
.legend-swatch { width:12px; height:12px; border-radius:3px; display:inline-block; margin-right:4px; vertical-align:middle; }

/* summary table */
.mp-summary-wrap { overflow-x:auto; }
table.mp-table { width:100%; border-collapse:collapse; font-family:sans-serif; font-size:.84rem; }
table.mp-table th { background:var(--green-pale); color:var(--green); padding:9px 12px; text-align:left; font-weight:700; }
table.mp-table td { padding:9px 12px; border-bottom:1px solid var(--border); }
table.mp-table tr.row-avg td { font-weight:700; background:#f0fdf4; color:var(--green); }
table.mp-table tr.row-target td { background:#fff7ed; color:var(--amber); font-weight:700; }
.vs-good { color:var(--green); font-weight:600; }
.vs-bad  { color:var(--red); font-weight:600; }

@media(max-width:960px){
  .app-body { flex-direction:column; }
  .sidebar { width:100%; height:auto; position:static; display:flex; flex-wrap:wrap; padding:6px 8px; border-right:none; border-bottom:1px solid var(--border); }
  .sidebar-section-label { display:none; }
  .nav-item { padding:7px 10px; margin:2px 2px; font-size:.8rem; }
  .dash-grid { grid-template-columns:1fr 1fr; }
  .today-grid { grid-template-columns:1fr 1fr; }
  .quick-actions { grid-template-columns:1fr 1fr; }
  .settings-layout { grid-template-columns:1fr; }
  .results-grid { grid-template-columns:1fr 1fr; }
  .mp-grid { min-width:700px; }
}
@media(max-width:600px){
  .dash-grid { grid-template-columns:1fr; }
  .quick-actions { grid-template-columns:1fr; }
  .macro-target-row { grid-template-columns:1fr 1fr; }
}

/* ── ONBOARDING MODAL ── */
.onboarding-modal { max-width: 500px; }
.ob-progress {
  display: flex; align-items: center; justify-content: center;
  gap: 0; margin-bottom: 28px;
}
.ob-step-dot {
  width: 10px; height: 10px; border-radius: 50%;
  background: var(--border); transition: background .3s;
}
.ob-step-dot.active { background: var(--green); }
.ob-step-dot.done   { background: var(--green-l); }
.ob-step-line { width: 44px; height: 2px; background: var(--border); }
.ob-step h2  { font-size: 1.2rem; color: var(--green); margin-bottom: 8px; }
.ob-desc     { font-family: sans-serif; font-size: .88rem; color: var(--muted); margin-bottom: 22px; }
.ob-actions  { display: flex; align-items: center; justify-content: space-between; margin-top: 24px; }
.ob-skip-btn { background: none; border: none; color: var(--muted); font-family: sans-serif;
  font-size: .82rem; cursor: pointer; text-decoration: underline; padding: 0; }
.ob-skip-btn:hover { color: var(--text); }
.ob-back-btn { background: none; border: 1px solid var(--border); color: var(--muted);
  font-family: sans-serif; font-size: .88rem; padding: 9px 18px; border-radius: 8px; cursor: pointer; }
.ob-next-btn { background: var(--green); color: #fff; border: none; font-family: sans-serif;
  font-size: .88rem; padding: 9px 22px; border-radius: 8px; cursor: pointer; font-weight: 700; }
.ob-next-btn:hover { background: #1b4332; }
.ob-results  { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin-top: 4px; }
.ob-result-card { background: var(--green-pale); border-radius: 10px; padding: 16px; text-align: center; }
.ob-r-val { font-size: 1.7rem; font-weight: 700; color: var(--green); font-family: sans-serif; }
.ob-r-lbl { font-family: sans-serif; font-size: .78rem; color: var(--muted); margin-top: 4px; }
.ob-results-note { font-family:sans-serif; font-size:.82rem; color:var(--muted);
  text-align:center; margin-top:14px; font-style:italic; }

/* grocery no-plan placeholder */
#grocery-no-plan {
  text-align: center; padding: 48px 24px;
  font-family: sans-serif; font-size: .9rem; color: var(--muted);
}
#grocery-no-plan a { color: var(--green); font-weight: 700; cursor: pointer; }
"""

# ── HTML FUNCTIONS ─────────────────────────────────────────────────────────

def sidebar_html():
    return """
<div class="app-body">
  <nav class="sidebar" id="sidebar">
    <div class="sidebar-brand">
      <div class="sidebar-brand-title">🌿 Vidya's Cookbook</div>
    </div>
    <div class="sidebar-section-label">Overview</div>
    <div class="nav-item active" data-tab="dashboard" onclick="switchTab('dashboard')">
      <span class="nav-icon">🏠</span> Dashboard
    </div>
    <div class="sidebar-section-label">Plan</div>
    <div class="nav-item" data-tab="mealplan" onclick="switchTab('mealplan')">
      <span class="nav-icon">🗓</span> Meal Plan
    </div>
    <div class="nav-item" data-tab="grocery" onclick="switchTab('grocery')">
      <span class="nav-icon">🛒</span> Grocery &amp; Pantry
      <span class="nav-badge hidden" id="oos-badge">0</span>
    </div>
    <div class="sidebar-section-label">Cook</div>
    <div class="nav-item" data-tab="recipes" onclick="switchTab('recipes')">
      <span class="nav-icon">📖</span> Recipes
    </div>
    <div class="sidebar-section-label">Profile</div>
    <div class="nav-item" data-tab="settings" onclick="switchTab('settings')">
      <span class="nav-icon">⚙️</span> Settings
    </div>
    <div class="nav-item" onclick="signOut()" style="color:var(--muted);margin-top:8px;">
      <span class="nav-icon">↩</span> Sign Out
    </div>
  </nav>
  <div class="main-area">
"""

def dashboard_tab_html():
    return """
<div id="tab-dashboard" class="tab-content active">
  <div id="tab-dashboard-inner">
    <div class="dash-greeting" id="dash-greeting">Good morning, Vidya 👋</div>
    <div class="dash-sub" id="dash-sub">Here's your overview for today.</div>

    <div id="setup-prompt" class="setup-banner hidden">
      <span>⚡ Set your weight &amp; training goals to unlock personalised macro targets.</span>
      <a onclick="switchTab('settings')">Go to Settings →</a>
    </div>

    <!-- Quick actions -->
    <div class="quick-actions">
      <button class="qa-btn" onclick="switchTab('mealplan');generateMealPlan()">
        <span class="qa-icon">🎲</span>
        <span class="qa-title">Generate Week</span>
        <span class="qa-desc">Auto-fill your 7-day meal plan</span>
      </button>
      <button class="qa-btn" onclick="switchTab('grocery')">
        <span class="qa-icon">🛒</span>
        <span class="qa-title">Shopping List</span>
        <span class="qa-desc">View ingredients &amp; pantry</span>
      </button>
      <button class="qa-btn" onclick="openAddModal()">
        <span class="qa-icon">➕</span>
        <span class="qa-title">Add a Recipe</span>
        <span class="qa-desc">Save a new recipe to your book</span>
      </button>
    </div>

    <!-- Today's meals -->
    <div class="today-meals">
      <h3>📅 Today's Meals</h3>
      <div class="today-grid" id="today-meals-grid">
        <div class="today-slot"><div class="today-slot-label">Breakfast</div><div class="today-empty">No plan yet</div></div>
        <div class="today-slot"><div class="today-slot-label">Lunch</div><div class="today-empty">No plan yet</div></div>
        <div class="today-slot"><div class="today-slot-label">Dinner</div><div class="today-empty">No plan yet</div></div>
        <div class="today-slot"><div class="today-slot-label">Snack</div><div class="today-empty">No plan yet</div></div>
      </div>
      <div style="margin-top:12px;font-family:sans-serif;font-size:.8rem;color:var(--muted)">
        No meal plan yet? <a style="color:var(--green);cursor:pointer;font-weight:600" onclick="switchTab('mealplan');generateMealPlan()">Generate this week →</a>
      </div>
    </div>

    <!-- Macro progress -->
    <div class="macro-progress" id="dash-macro-section">
      <h3>📊 Today's Macros</h3>
      <div id="dash-macro-content">
        <div style="font-family:sans-serif;font-size:.85rem;color:var(--muted);font-style:italic">
          Complete Settings to see macro progress vs your targets.
          <a style="color:var(--green);cursor:pointer;font-weight:600" onclick="switchTab('settings')">Set up now →</a>
        </div>
      </div>
    </div>

    <!-- Stats row -->
    <div class="dash-grid">
      <div class="dash-card">
        <div class="dash-card-label">Recipes Logged This Week</div>
        <div class="dash-card-big" id="dash-logged-count">0</div>
        <div class="dash-card-unit">recipes made</div>
      </div>
      <div class="dash-card">
        <div class="dash-card-label">Total Recipes Available</div>
        <div class="dash-card-big" id="dash-total-recipes">38</div>
        <div class="dash-card-unit">in your cookbook</div>
      </div>
      <div class="dash-card">
        <div class="dash-card-label">Pantry Items Out of Stock</div>
        <div class="dash-card-big" id="dash-oos-count" style="color:var(--red)">0</div>
        <div class="dash-card-unit">need restocking</div>
      </div>
    </div>
  </div>
</div>
"""

def settings_tab_html():
    return """
<div id="tab-settings" class="tab-content">
  <h2>⚙️ Settings</h2>
  <p class="tab-desc">Enter your stats and training goals — your weekly macro targets will be calculated automatically and applied to your Meal Plan.</p>
  <div class="settings-layout">

    <!-- Personal Stats -->
    <div class="settings-card">
      <h3>👤 Personal Stats</h3>
      <div class="settings-form">
        <div class="setting-group">
          <label>Weight (lbs)</label>
          <input type="number" id="s-weight" min="80" max="400" step="0.5" placeholder="e.g. 140">
        </div>
        <div class="setting-group">
          <label>Age</label>
          <input type="number" id="s-age" min="16" max="80" placeholder="e.g. 30">
        </div>
        <div class="setting-group" style="grid-column:1/-1">
          <label>Height</label>
          <div class="height-inputs">
            <div>
              <input type="number" id="s-ft" min="4" max="7" placeholder="ft" style="width:100%">
              <div class="ht-label">feet</div>
            </div>
            <div>
              <input type="number" id="s-in" min="0" max="11" placeholder="in" style="width:100%">
              <div class="ht-label">inches</div>
            </div>
          </div>
        </div>
        <div class="setting-group" style="grid-column:1/-1">
          <label>Sex (used for BMR formula)</label>
          <select id="s-sex">
            <option value="female">Female</option>
            <option value="male">Male</option>
          </select>
        </div>
      </div>
    </div>

    <!-- Training Profile -->
    <div class="settings-card">
      <h3>🏋️ Training Profile</h3>
      <div class="settings-form">
        <div class="setting-group" style="grid-column:1/-1">
          <label>Primary Goal</label>
          <select id="s-goal">
            <option value="endurance">Endurance Performance</option>
            <option value="muscle">Muscle Gain</option>
            <option value="fatloss">Fat Loss + Muscle Retention</option>
            <option value="general">General Health &amp; Strength</option>
          </select>
        </div>
        <div class="setting-group">
          <label>Training Days / Week</label>
          <select id="s-days">
            <option value="1">1 day / week</option>
            <option value="2">2 days / week</option>
            <option value="3">3 days / week</option>
            <option value="4" selected>4 days / week</option>
            <option value="5">5 days / week</option>
            <option value="6">6 days / week</option>
            <option value="7">7 days / week</option>
          </select>
        </div>
        <div class="setting-group">
          <label>Avg Session Length</label>
          <select id="s-duration">
            <option value="30">30 min</option>
            <option value="45">45 min</option>
            <option value="60" selected>60 min</option>
            <option value="90">90 min</option>
            <option value="120">2+ hours</option>
          </select>
        </div>
        <div class="setting-group" style="grid-column:1/-1">
          <label>How do you distribute meals?</label>
          <select id="s-meal-style">
            <option value="light-b-big-l">Light breakfast, big lunch, smaller dinner</option>
            <option value="even">Even across all meals</option>
            <option value="big-b">Big breakfast, moderate lunch &amp; dinner</option>
            <option value="no-b">Skip breakfast (brunch/lunch focused)</option>
          </select>
        </div>
      </div>
      <button class="calc-btn" onclick="saveAndCalculate()">Calculate My Targets →</button>
    </div>

    <!-- Results -->
    <div class="settings-results">
      <div class="results-empty" id="settings-empty">
        Enter your stats above and click <strong>Calculate My Targets</strong> to see your personalised daily macros.
      </div>
      <div id="settings-output" class="hidden">
        <h3 style="color:var(--green);margin-bottom:14px;font-family:sans-serif;">📊 Your Daily Targets</h3>
        <div class="results-grid">
          <div class="result-card">
            <div class="result-big" id="r-bmr">—</div>
            <div class="result-unit">kcal / day</div>
            <div class="result-lbl">BMR (at rest)</div>
          </div>
          <div class="result-card">
            <div class="result-big" id="r-tdee">—</div>
            <div class="result-unit">kcal / day</div>
            <div class="result-lbl">TDEE (with activity)</div>
          </div>
          <div class="result-card">
            <div class="result-big" id="r-target">—</div>
            <div class="result-unit">kcal / day</div>
            <div class="result-lbl">Daily Target</div>
          </div>
          <div class="result-card">
            <div class="result-big" id="r-adjust" style="color:var(--amber)">—</div>
            <div class="result-unit">&nbsp;</div>
            <div class="result-lbl">Goal Adjustment</div>
          </div>
        </div>
        <div class="macro-target-row">
          <div class="macro-target-card protein-card">
            <div class="mt-v" id="r-protein">—</div>
            <div class="mt-l">Protein (g / day)</div>
          </div>
          <div class="macro-target-card carbs-card">
            <div class="mt-v" id="r-carbs">—</div>
            <div class="mt-l">Carbs (g / day)</div>
          </div>
          <div class="macro-target-card fat-card">
            <div class="mt-v" id="r-fat">—</div>
            <div class="mt-l">Fat (g / day)</div>
          </div>
        </div>
        <div class="calc-breakdown" id="r-breakdown"></div>
      </div>
    </div>

  </div>
</div>
"""

def mealplan_tab_html():
    return """
<div id="tab-mealplan" class="tab-content">
  <div class="mp-header-row">
    <h2>🗓 Weekly Meal Plan</h2>
    <div class="mp-btns">
      <button class="mp-btn mp-btn-primary" onclick="generateMealPlan()">🎲 Generate Week</button>
      <button class="mp-btn mp-btn-ghost"   onclick="syncMealPlanToGrocery()">🛒 Sync to This Week</button>
      <button class="mp-btn mp-btn-muted"   onclick="clearMealPlan()">✕ Clear</button>
    </div>
  </div>

  <!-- Empty state (shown when no plan exists) -->
  <div class="mp-empty-state" id="mp-empty-state">
    <div class="mp-empty-icon">🗓</div>
    <div class="mp-empty-title">No meal plan yet</div>
    <div class="mp-empty-desc">Generate a smart 7-day plan based on your recipe book, or build it manually by clicking each cell.</div>
    <button class="mp-gen-big-btn" onclick="generateMealPlan()">🎲 Generate This Week</button>
  </div>

  <!-- Grid (shown when plan exists) -->
  <div id="mp-plan-content" class="hidden">
    <div class="mp-grid-scroll">
      <div class="mp-grid" id="mp-grid"></div>
    </div>
    <div class="mp-chart-card">
      <h3>📊 Weekly Macros vs Your Targets</h3>
      <div class="bar-chart-area" id="mp-bar-chart"></div>
      <div class="chart-legend">
        <span><span class="legend-swatch" style="background:#3b82f6"></span>Protein</span>
        <span><span class="legend-swatch" style="background:#52b788"></span>Carbs</span>
        <span><span class="legend-swatch" style="background:#e76f51"></span>Fat</span>
        <span><span class="legend-swatch" style="border:2px dashed #e76f51;background:none;height:0;border-radius:0;width:14px;display:inline-block;vertical-align:middle"></span>Calorie target</span>
      </div>
    </div>
    <div class="mp-summary-wrap">
      <table class="mp-table">
        <thead><tr><th>Day</th><th>kcal</th><th>Protein</th><th>Carbs</th><th>Fat</th><th>vs Target</th></tr></thead>
        <tbody id="mp-summary-body"></tbody>
      </table>
    </div>
  </div>
</div>
"""

def onboarding_modal_html():
    return """
<div class="modal-overlay" id="onboarding-modal">
  <div class="modal onboarding-modal">

    <div class="ob-progress">
      <div class="ob-step-dot active" id="ob-dot-0"></div>
      <div class="ob-step-line"></div>
      <div class="ob-step-dot" id="ob-dot-1"></div>
      <div class="ob-step-line"></div>
      <div class="ob-step-dot" id="ob-dot-2"></div>
    </div>

    <!-- Step 0: Personal Stats -->
    <div class="ob-step" id="ob-step-0">
      <h2>Welcome to your cookbook 🌿</h2>
      <p class="ob-desc">Let's set up your profile to calculate daily macro targets and build your first meal plan. Takes 30 seconds.</p>
      <div class="form-grid">
        <div class="form-group">
          <label>Weight (lbs)</label>
          <input type="number" id="ob-weight" min="80" max="400" step="0.5" placeholder="e.g. 140">
        </div>
        <div class="form-group">
          <label>Age</label>
          <input type="number" id="ob-age" min="16" max="80" placeholder="e.g. 30">
        </div>
        <div class="form-group form-full">
          <label>Height</label>
          <div class="height-inputs">
            <div>
              <input type="number" id="ob-ft" min="4" max="7" placeholder="ft" style="width:100%">
              <div class="ht-label">feet</div>
            </div>
            <div>
              <input type="number" id="ob-in" min="0" max="11" placeholder="in" style="width:100%">
              <div class="ht-label">inches</div>
            </div>
          </div>
        </div>
        <div class="form-group form-full">
          <label>Sex (used for BMR formula)</label>
          <select id="ob-sex">
            <option value="female">Female</option>
            <option value="male">Male</option>
          </select>
        </div>
      </div>
    </div>

    <!-- Step 1: Training Profile -->
    <div class="ob-step hidden" id="ob-step-1">
      <h2>Your training profile 🏋️</h2>
      <p class="ob-desc">Tell us how you train so we can set the right calorie and protein targets for your goals.</p>
      <div class="form-grid">
        <div class="form-group form-full">
          <label>Primary Goal</label>
          <select id="ob-goal">
            <option value="endurance">Endurance Performance</option>
            <option value="muscle">Muscle Gain</option>
            <option value="fatloss">Fat Loss + Muscle Retention</option>
            <option value="general">General Health &amp; Strength</option>
          </select>
        </div>
        <div class="form-group">
          <label>Training days / week</label>
          <select id="ob-days">
            <option value="1">1 day</option>
            <option value="2">2 days</option>
            <option value="3" selected>3 days</option>
            <option value="4">4 days</option>
            <option value="5">5 days</option>
            <option value="6">6 days</option>
            <option value="7">7 days</option>
          </select>
        </div>
        <div class="form-group">
          <label>Avg session length (min)</label>
          <input type="number" id="ob-session" min="15" max="180" step="5" placeholder="e.g. 60">
        </div>
        <div class="form-group form-full">
          <label>How do you typically eat?</label>
          <select id="ob-meal-style">
            <option value="light-b-big-l">Light breakfast, big lunch, smaller dinner</option>
            <option value="even">Even across all meals</option>
            <option value="big-b">Big breakfast, moderate lunch &amp; dinner</option>
            <option value="no-b">Skip breakfast (brunch/lunch focused)</option>
          </select>
        </div>
      </div>
    </div>

    <!-- Step 2: Calculated Targets -->
    <div class="ob-step hidden" id="ob-step-2">
      <h2>Your daily targets 📊</h2>
      <p class="ob-desc">Here's what your body needs each day to support your goal. Hit the button below to generate your first meal plan.</p>
      <div class="ob-results" id="ob-results"></div>
      <p class="ob-results-note" id="ob-results-note"></p>
    </div>

    <div class="ob-actions">
      <button class="ob-skip-btn" onclick="skipOnboarding()">Skip for now</button>
      <div style="display:flex;gap:10px;align-items:center">
        <button class="ob-back-btn hidden" id="ob-back-btn" onclick="obBack()">← Back</button>
        <button class="ob-next-btn" id="ob-next-btn" onclick="obNext()">Next →</button>
      </div>
    </div>

  </div>
</div>
"""

# ── EXTRA JS ───────────────────────────────────────────────────────────────
def extra_js(recipe_data_json, slot_map_json, batch_ids_json):
    return f"""
// ── Injected data ──────────────────────────────────────────────────────────
const RECIPE_DATA   = {recipe_data_json};
const SLOT_RECIPES  = {slot_map_json};
const BATCH_IDS_SET = new Set({batch_ids_json});
const DAYS_SHORT    = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun'];
const SLOT_NAMES    = ['Breakfast','Lunch','Dinner','Snack'];
const SLOT_KEYS     = ['breakfast','lunch','dinner','snack'];
const GOAL_LABELS   = {{ endurance:'Endurance Performance', muscle:'Muscle Gain', fatloss:'Fat Loss + Muscle Retention', general:'General Health & Strength' }};
const GOAL_ADJ      = {{ endurance:100, muscle:250, fatloss:-400, general:0 }};
const GOAL_PROT_KG  = {{ endurance:1.6, muscle:2.0, fatloss:2.2, general:1.6 }};
const ACT_MULT      = {{ 1:1.375,2:1.375,3:1.55,4:1.55,5:1.725,6:1.725,7:1.9 }};
// Calorie split per meal slot based on eating style
const MEAL_STYLE_SPLITS = {{
  'light-b-big-l': {{ breakfast:0.15, lunch:0.40, snack:0.15, dinner:0.30 }},
  'even':          {{ breakfast:0.25, lunch:0.30, snack:0.10, dinner:0.35 }},
  'big-b':         {{ breakfast:0.35, lunch:0.25, snack:0.10, dinner:0.30 }},
  'no-b':          {{ breakfast:0.05, lunch:0.45, snack:0.15, dinner:0.35 }},
}};
const MEAL_STYLE_LABELS = {{
  'light-b-big-l': 'Light breakfast, big lunch, smaller dinner',
  'even':          'Even across all meals',
  'big-b':         'Big breakfast, moderate lunch & dinner',
  'no-b':          'Skip breakfast (brunch/lunch focused)',
}};

// ── Persisted state ────────────────────────────────────────────────────────
let userSettings = null;
let userTargets  = null;
let mealPlan2D   = null;

// ── Sidebar tab switching ──────────────────────────────────────────────────
// (overrides old switchTab — same fn name, updated for sidebar)
function switchTab(id) {{
  document.querySelectorAll('.nav-item').forEach(b => b.classList.toggle('active', b.dataset.tab===id));
  document.querySelectorAll('.tab-content').forEach(c => c.classList.toggle('active', c.id==='tab-'+id));
  if (id==='dashboard') refreshDashboard();
  if (id==='mealplan')  {{ renderMealPlanGrid(); renderMacrosChart(); renderMacrosSummary(); }}
  if (id==='settings')  restoreSettings();
}}

// ── Dashboard ─────────────────────────────────────────────────────────────
function refreshDashboard() {{
  // greeting
  const h = new Date().getHours();
  const el = document.getElementById('dash-greeting');
  if (el) el.textContent = (h<12?'Good morning':h<17?'Good afternoon':'Good evening') + ', Vidya 👋';

  // setup prompt
  const sp = document.getElementById('setup-prompt');
  if (sp) sp.classList.toggle('hidden', !!userTargets);

  // out of stock — update sidebar badge + dashboard stat card only
  const oosItems = Object.entries(stockStatus).filter(([,v])=>v==='out').map(([k])=>k);
  const oosBadge = document.getElementById('oos-badge');
  const oosCount = document.getElementById('dash-oos-count');
  if (oosBadge) {{ oosBadge.textContent=oosItems.length; oosBadge.classList.toggle('hidden',oosItems.length===0); }}
  if (oosCount) oosCount.textContent = oosItems.length;

  // week log count
  const lc = document.getElementById('dash-logged-count');
  if (lc) lc.textContent = weekLog.length;

  // total recipes
  const tr = document.getElementById('dash-total-recipes');
  if (tr) tr.textContent = document.querySelectorAll('.recipe-row').length;

  // today's meals
  renderTodayMeals();
  // macro progress
  renderDashMacros();
}}

function renderTodayMeals() {{
  const grid = document.getElementById('today-meals-grid');
  if (!grid || !mealPlan2D) return;
  const day = (new Date().getDay()+6)%7; // 0=Mon
  const slotNames = ['Breakfast','Lunch','Dinner','Snack'];
  grid.innerHTML = slotNames.map((sn, si) => {{
    const rid = mealPlan2D[si] && mealPlan2D[si][day];
    const r   = rid ? RECIPE_DATA[rid] : null;
    return `<div class="today-slot">
      <div class="today-slot-label">${{sn}}</div>
      ${{r
        ? `<div class="today-slot-name">${{r.name}}</div><div class="today-slot-kcal">${{r.macros.kcal}} kcal</div>`
        : '<div class="today-empty">Not planned</div>'
      }}
    </div>`;
  }}).join('');
}}

function renderDashMacros() {{
  const el = document.getElementById('dash-macro-content');
  if (!el) return;
  if (!userTargets) {{
    el.innerHTML = '<div style="font-family:sans-serif;font-size:.85rem;color:var(--muted);font-style:italic">Complete Settings to see macro progress vs your targets. <a style="color:var(--green);cursor:pointer;font-weight:600" onclick="switchTab(\\'settings\\')">Set up now →</a></div>';
    return;
  }}
  const day = (new Date().getDay()+6)%7;
  let tot = {{kcal:0,protein:0,carbs:0,fat:0}};
  if (mealPlan2D) {{
    for (let si=0;si<4;si++) {{
      const rid = mealPlan2D[si] && mealPlan2D[si][day];
      const r = rid ? RECIPE_DATA[rid] : null;
      if (r) {{ tot.kcal+=r.macros.kcal; tot.protein+=r.macros.protein; tot.carbs+=r.macros.carbs; tot.fat+=r.macros.fat; }}
    }}
  }}
  const t = userTargets;
  const macros = [
    {{name:'Protein', val:tot.protein, target:t.proteinG, cls:'protein'}},
    {{name:'Carbs',   val:tot.carbs,   target:t.carbG,    cls:'carbs'}},
    {{name:'Fat',     val:tot.fat,     target:t.fatG,     cls:'fat'}},
  ];
  el.innerHTML = `
    <div style="font-family:sans-serif;font-size:.82rem;color:var(--muted);margin-bottom:10px">${{tot.kcal}} / ${{t.targetKcal}} kcal today</div>
    ${{macros.map(m=>{{
      const pct = Math.min(100, Math.round((m.val/Math.max(m.target,1))*100));
      return `<div class="mp-prog-row">
        <div class="mp-prog-label">${{m.name}}</div>
        <div class="mp-prog-bar-wrap"><div class="mp-prog-bar-fill ${{m.cls}}" style="width:${{pct}}%"></div></div>
        <div class="mp-prog-val">${{m.val}}g / ${{m.target}}g</div>
      </div>`;
    }}).join('')}}
  `;
}}

// ── Settings ───────────────────────────────────────────────────────────────
function saveAndCalculate() {{
  const wt        = parseFloat(document.getElementById('s-weight').value);
  const age       = parseInt(document.getElementById('s-age').value);
  const ft        = parseInt(document.getElementById('s-ft').value) || 0;
  const inn       = parseInt(document.getElementById('s-in').value) || 0;
  const sex       = document.getElementById('s-sex').value;
  const goal      = document.getElementById('s-goal').value;
  const days      = parseInt(document.getElementById('s-days').value);
  const dur       = parseInt(document.getElementById('s-duration').value);
  const mealStyle = document.getElementById('s-meal-style')?.value || 'even';
  if (!wt || !age || (!ft && !inn)) {{ showToast('Please fill in weight, height, and age'); return; }}

  const totalIn  = ft*12 + inn;
  const wt_kg    = wt / 2.205;
  let bmr = sex==='female'
    ? (4.536*wt) + (12.7*totalIn) - (5*age) - 161
    : (4.536*wt) + (12.7*totalIn) - (5*age) + 5;
  bmr = Math.round(bmr);

  let mult = ACT_MULT[Math.min(days,7)] || 1.55;
  if (dur>=90)  mult += 0.05;
  if (dur>=120) mult += 0.05;
  const tdee       = Math.round(bmr * mult);
  const adj        = GOAL_ADJ[goal];
  const targetKcal = tdee + adj;
  const protG      = Math.round(GOAL_PROT_KG[goal] * wt_kg);
  const fatG       = Math.round(targetKcal * 0.25 / 9);
  const carbG      = Math.round((targetKcal - protG*4 - fatG*9) / 4);

  userSettings = {{ wt, age, ft, inn, sex, goal, days, dur, mealStyle }};
  userTargets  = {{ bmr, tdee, targetKcal, proteinG:protG, carbG, fatG, adj, goal, wt_kg }};
  saveUserProfile();
  displaySettings();
  renderMacrosChart(); renderMacrosSummary();
  showToast('✅ Targets saved and applied to your Meal Plan!');
}}

function displaySettings() {{
  if (!userTargets) return;
  document.getElementById('settings-empty')?.classList.add('hidden');
  document.getElementById('settings-output')?.classList.remove('hidden');
  const {{bmr,tdee,targetKcal,proteinG,carbG,fatG,adj,goal,wt_kg}} = userTargets;
  const set = (id,v) => {{ const e=document.getElementById(id); if(e) e.textContent=v; }};
  set('r-bmr',    bmr.toLocaleString());
  set('r-tdee',   tdee.toLocaleString());
  set('r-target', targetKcal.toLocaleString());
  set('r-adjust', (adj>=0?'+':'')+adj+' kcal');
  set('r-protein', proteinG+'g');
  set('r-carbs',   carbG+'g');
  set('r-fat',     fatG+'g');
  const actLabels = ['','Light','Light','Moderate','Moderate','Active','Active','Very Active'];
  const adjLabel  = adj>0?`+${{adj}} kcal surplus`:adj<0?`${{adj}} kcal deficit`:'Maintenance';
  const bd = document.getElementById('r-breakdown');
  if (bd) bd.innerHTML = `
    <strong>Calculation breakdown</strong><br>
    BMR (Mifflin-St Jeor, imperial) → <strong>${{bmr.toLocaleString()}} kcal</strong> at complete rest<br>
    × ${{actLabels[userSettings?.days||4]}} activity multiplier → TDEE <strong>${{tdee.toLocaleString()}} kcal</strong><br>
    ${{adjLabel}} for ${{GOAL_LABELS[goal]}} → Daily Target <strong>${{targetKcal.toLocaleString()}} kcal</strong><br>
    Protein <strong>${{GOAL_PROT_KG[goal]}}g/kg</strong> × ${{wt_kg.toFixed(1)}}kg = <strong>${{proteinG}}g</strong> · Fat 25% cals = <strong>${{fatG}}g</strong> · Carbs remainder = <strong>${{carbG}}g</strong>
  `;
}}

function restoreSettings() {{
  if (!userSettings) return;
  const s = userSettings;
  const sv = (id,v) => {{ const e=document.getElementById(id); if(e&&v!==undefined) e.value=v; }};
  sv('s-weight',s.wt); sv('s-age',s.age); sv('s-ft',s.ft); sv('s-in',s.inn);
  sv('s-sex',s.sex); sv('s-goal',s.goal); sv('s-days',s.days); sv('s-duration',s.dur);
  sv('s-meal-style', s.mealStyle || 'even');
  displaySettings();
}}

// ── Meal Plan ─────────────────────────────────────────────────────────────
function saveMealPlan2D() {{ db_saveMealPlan2D(); }}

// Score a recipe candidate by pantry stock overlap + calorie proximity.
// weekIngs = Set of ingredient names already committed for the week.
function smartPick(cands, targetKcal, weekIngs) {{
  if (!cands.length) return null;
  const scored = cands.map(id => {{
    const r    = RECIPE_DATA[id];
    const ings = RECIPE_INGREDIENTS[id] || [];
    // In-stock pantry items score 3× vs week-pool overlap (use what you have)
    const inStockHits = ings.filter(i => stockStatus[i] === 'in').length;
    const weekHits    = ings.filter(i => weekIngs.has(i)).length;
    const denom = Math.max(ings.length * 4, 1);
    const overlapScore = ((inStockHits * 3 + weekHits) / denom) * 10;
    // Calorie proximity: 0–10, degrades as % deviation from slot target grows
    let calScore = 5;  // neutral when no target set
    if (targetKcal && r.macros.kcal > 0) {{
      const pct = Math.abs(r.macros.kcal - targetKcal) / Math.max(targetKcal, 50);
      calScore = Math.max(0, 10 * (1 - pct * 1.5));
    }}
    const noise = Math.random() * 2;  // prevent identical plans on re-gen
    return {{ id, score: overlapScore * 0.6 + calScore * 0.4 + noise }};
  }});
  scored.sort((a, b) => b.score - a.score);
  // Pick from top 3 to maintain variety while still being smart
  const topN = scored.slice(0, Math.min(3, scored.length));
  return topN[Math.floor(Math.random() * topN.length)].id;
}}

function generateMealPlan() {{
  mealPlan2D = [[],[],[],[]];
  const tKcal  = userTargets?.targetKcal || null;
  const style  = userSettings?.mealStyle || 'even';
  const splits = MEAL_STYLE_SPLITS[style] || MEAL_STYLE_SPLITS['even'];
  // weekIngs accumulates as we pick — later picks reuse earlier ingredients
  const weekIngs     = new Set();
  const usedPerSlot  = [new Set(), new Set(), new Set(), new Set()];

  // Day-first so each day's calorie budget is respected across all slots
  for (let d = 0; d < 7; d++) {{
    for (let s = 0; s < 4; s++) {{
      const pool  = (SLOT_RECIPES[SLOT_KEYS[s]] || []).filter(id => RECIPE_DATA[id]);
      let cands   = pool.filter(id => BATCH_IDS_SET.has(id) || !usedPerSlot[s].has(id));
      if (!cands.length) cands = [...pool];
      const slotTarget = tKcal ? tKcal * splits[SLOT_KEYS[s]] : null;
      const pick = smartPick(cands, slotTarget, weekIngs);
      if (!mealPlan2D[s]) mealPlan2D[s] = [];
      mealPlan2D[s][d] = pick || null;
      if (pick) {{
        if (!BATCH_IDS_SET.has(pick)) usedPerSlot[s].add(pick);
        (RECIPE_INGREDIENTS[pick] || []).forEach(i => weekIngs.add(i));
      }}
    }}
  }}
  saveMealPlan2D();
  showMealPlanContent();
  renderMealPlanGrid(); renderMacrosChart(); renderMacrosSummary();
  const msg = tKcal
    ? `🗓 Plan built around your ${{tKcal}} kcal target & pantry stock!`
    : `🗓 Week generated! Set your targets in Settings for calorie-aware planning.`;
  showToast(msg);
}}

function clearMealPlan() {{
  mealPlan2D = [[],[],[],[]];
  saveMealPlan2D();
  document.getElementById('mp-empty-state')?.classList.remove('hidden');
  document.getElementById('mp-plan-content')?.classList.add('hidden');
  renderMacrosChart(); renderMacrosSummary();
}}

function showMealPlanContent() {{
  document.getElementById('mp-empty-state')?.classList.add('hidden');
  document.getElementById('mp-plan-content')?.classList.remove('hidden');
}}

function renderMealPlanGrid() {{
  const grid = document.getElementById('mp-grid');
  if (!grid) return;
  if (!mealPlan2D || mealPlan2D.every(s=>!s||s.every(r=>!r))) return;
  showMealPlanContent();
  let html = '<div class="mp-corner"></div>';
  DAYS_SHORT.forEach(d => html+=`<div class="mp-day-hdr">${{d}}</div>`);
  SLOT_NAMES.forEach((sn,si) => {{
    html += `<div class="mp-slot-lbl">${{sn}}</div>`;
    for (let di=0;di<7;di++) {{
      const rid = mealPlan2D[si]&&mealPlan2D[si][di];
      const r   = rid?RECIPE_DATA[rid]:null;
      html += r
        ? `<div class="mp-cell" onclick="openPicker(${{si}},${{di}},this)">
            <div class="mp-chip-name">${{r.name}}</div>
            <div class="mp-chip-cals">${{r.macros.kcal}} kcal</div>
            <div class="mp-chip-macros">P${{r.macros.protein}} C${{r.macros.carbs}} F${{r.macros.fat}}</div>
           </div>`
        : `<div class="mp-cell empty" onclick="openPicker(${{si}},${{di}},this)"><span style="font-size:.75rem;color:var(--muted);font-family:sans-serif">+ add</span></div>`;
    }}
  }});
  html += '<div class="mp-total-lbl">Daily Total</div>';
  for (let di=0;di<7;di++) {{
    const t=getDayTotals(di);
    html+=`<div class="mp-total-cell"><div class="mp-total-kcal">${{t.kcal}} kcal</div><div class="mp-total-macros">P${{t.protein}}g C${{t.carbs}}g F${{t.fat}}g</div></div>`;
  }}
  grid.innerHTML = html;
}}

function getDayTotals(di) {{
  let kcal=0,protein=0,carbs=0,fat=0;
  for (let si=0;si<4;si++) {{
    const rid=mealPlan2D&&mealPlan2D[si]&&mealPlan2D[si][di];
    const r=rid?RECIPE_DATA[rid]:null;
    if(r){{kcal+=r.macros.kcal;protein+=r.macros.protein;carbs+=r.macros.carbs;fat+=r.macros.fat;}}
  }}
  return {{kcal,protein,carbs,fat}};
}}

// picker
let _pickerState=null;
function openPicker(si,di,cell) {{
  document.querySelectorAll('.mp-picker').forEach(p=>p.remove());
  if(_pickerState&&_pickerState.si===si&&_pickerState.di===di){{_pickerState=null;return;}}
  _pickerState={{si,di}};
  const pool=(SLOT_RECIPES[SLOT_KEYS[si]]||[]).filter(id=>RECIPE_DATA[id]);
  let html=`<div class="mp-picker-item mp-picker-remove" onclick="setCellRecipe(${{si}},${{di}},null)">— Remove —</div>`;
  pool.forEach(id=>{{
    const r=RECIPE_DATA[id];
    html+=`<div class="mp-picker-item" onclick="setCellRecipe(${{si}},${{di}},'${{id}}')">
      ${{r.name}}<div class="pi-tier">${{r.tier_label}} · ${{r.macros.kcal}}kcal</div>
    </div>`;
  }});
  const p=document.createElement('div'); p.className='mp-picker'; p.innerHTML=html;
  cell.style.position='relative'; cell.appendChild(p);
  setTimeout(()=>document.addEventListener('click',_closePickerOutside,{{once:true}}),10);
}}
function _closePickerOutside(e){{if(!e.target.closest('.mp-picker'))document.querySelectorAll('.mp-picker').forEach(p=>p.remove());}}
function setCellRecipe(si,di,rid){{
  if(!mealPlan2D)mealPlan2D=[[],[],[],[]];
  if(!mealPlan2D[si])mealPlan2D[si]=[];
  mealPlan2D[si][di]=rid;
  document.querySelectorAll('.mp-picker').forEach(p=>p.remove());
  _pickerState=null;
  saveMealPlan2D(); renderMealPlanGrid(); renderMacrosChart(); renderMacrosSummary();
}}

function renderMacrosChart() {{
  const chart=document.getElementById('mp-bar-chart');
  if(!chart||!mealPlan2D)return;
  const days=DAYS_SHORT.map((_,di)=>getDayTotals(di));
  const tKcal=userTargets?.targetKcal||null;
  const maxK=Math.max(...days.map(d=>d.kcal),tKcal||0,1);
  const maxH=130;
  let html='';
  days.forEach((d,di)=>{{
    const bH=d.kcal>0?Math.max(4,(d.kcal/maxK)*maxH):0;
    const pH=d.kcal>0?bH*(d.protein*4/(d.kcal)):0;
    const cH=d.kcal>0?bH*(d.carbs*4/(d.kcal)):0;
    const fH=d.kcal>0?bH*(d.fat*9/(d.kcal)):0;
    html+=`<div class="bar-col">
      <div class="bar-kcal-label">${{d.kcal||'—'}}</div>
      <div class="bar-stack" style="height:${{bH}}px">
        <div class="bar-seg-fat"     style="height:${{fH}}px"></div>
        <div class="bar-seg-carbs"   style="height:${{cH}}px"></div>
        <div class="bar-seg-protein" style="height:${{pH}}px"></div>
      </div>
      <div class="bar-day-label">${{DAYS_SHORT[di]}}</div>
    </div>`;
  }});
  if(tKcal){{
    const tH=(tKcal/maxK)*maxH;
    html+=`<div class="bar-target-line" style="bottom:${{tH+28}}px"><span class="bar-target-lbl">${{tKcal}} kcal</span></div>`;
  }}
  chart.innerHTML=html;
}}

function renderMacrosSummary(){{
  const tbody=document.getElementById('mp-summary-body');
  if(!tbody||!mealPlan2D)return;
  let tot={{kcal:0,protein:0,carbs:0,fat:0}};
  let rows='';
  const tgt=userTargets;
  DAYS_SHORT.forEach((day,di)=>{{
    const d=getDayTotals(di);
    tot.kcal+=d.kcal;tot.protein+=d.protein;tot.carbs+=d.carbs;tot.fat+=d.fat;
    const diff=tgt&&d.kcal>0?d.kcal-tgt.targetKcal:null;
    const vs=diff!==null?`<span class="${{Math.abs(diff)<200?'vs-good':'vs-bad'}}">${{diff>0?'+':''}}${{diff}}</span>`:'—';
    rows+=`<tr><td>${{day}}</td><td>${{d.kcal||'—'}}</td><td>${{d.protein||'—'}}g</td><td>${{d.carbs||'—'}}g</td><td>${{d.fat||'—'}}g</td><td>${{vs}}</td></tr>`;
  }});
  const avg={{kcal:Math.round(tot.kcal/7),protein:Math.round(tot.protein/7),carbs:Math.round(tot.carbs/7),fat:Math.round(tot.fat/7)}};
  rows+=`<tr class="row-avg"><td>Avg / day</td><td>${{avg.kcal}}</td><td>${{avg.protein}}g</td><td>${{avg.carbs}}g</td><td>${{avg.fat}}g</td><td>—</td></tr>`;
  if(tgt) rows+=`<tr class="row-target"><td>Your Target</td><td>${{tgt.targetKcal}}</td><td>${{tgt.proteinG}}g</td><td>${{tgt.carbG}}g</td><td>${{tgt.fatG}}g</td><td>—</td></tr>`;
  tbody.innerHTML=rows;
}}

function syncMealPlanToGrocery(){{
  if(!mealPlan2D){{showToast('Generate a meal plan first!');return;}}
  const ids=new Set();
  mealPlan2D.forEach(s=>s&&s.forEach(r=>r&&ids.add(r)));
  mealPlan=[ ...ids ];
  document.querySelectorAll('.planner-check').forEach(cb=>{{cb.checked=ids.has(cb.value);}});
  refreshGroceryForPlan(); refreshShoppingSummary();
  switchTab('grocery');
  showToast(`🛒 Synced ${{ids.size}} recipes to "This Week"!`);
}}

// ── ONBOARDING ─────────────────────────────────────────────────────────────
let obStep = 0;

function showOnboarding() {{
  if (userTargets) return;  // already completed, skip
  const modal = document.getElementById('onboarding-modal');
  if (modal) {{ modal.classList.add('open'); obStep = 0; renderObStep(); }}
}}

function skipOnboarding() {{
  document.getElementById('onboarding-modal').classList.remove('open');
}}

function obNext() {{
  if (obStep === 0) {{
    const w  = parseFloat(document.getElementById('ob-weight')?.value);
    const a  = parseInt(document.getElementById('ob-age')?.value);
    const ft = parseInt(document.getElementById('ob-ft')?.value);
    if (!w || !a || !ft) {{ showToast('Please fill in weight, age and height'); return; }}
    obStep = 1;
  }} else if (obStep === 1) {{
    const sess = parseInt(document.getElementById('ob-session')?.value);
    if (!sess) {{ showToast('Please enter your average session length'); return; }}
    obCalculate();
    obStep = 2;
  }} else if (obStep === 2) {{
    obFinish();
    return;
  }}
  renderObStep();
}}

function obBack() {{
  if (obStep > 0) {{ obStep--; renderObStep(); }}
}}

function renderObStep() {{
  document.querySelectorAll('.ob-step').forEach((el, i) => el.classList.toggle('hidden', i !== obStep));
  document.querySelectorAll('.ob-step-dot').forEach((d, i) => {{
    d.classList.toggle('active', i === obStep);
    d.classList.toggle('done', i < obStep);
  }});
  const backBtn = document.getElementById('ob-back-btn');
  const nextBtn = document.getElementById('ob-next-btn');
  if (backBtn) backBtn.classList.toggle('hidden', obStep === 0);
  if (nextBtn) nextBtn.textContent = obStep === 2 ? '🎲 Generate My Plan' : 'Next →';
}}

function obCalculate() {{
  const w    = parseFloat(document.getElementById('ob-weight')?.value) || 0;
  const a    = parseInt(document.getElementById('ob-age')?.value) || 0;
  const ft   = parseInt(document.getElementById('ob-ft')?.value) || 0;
  const inch = parseInt(document.getElementById('ob-in')?.value) || 0;
  const sex  = document.getElementById('ob-sex')?.value || 'female';
  const goal = document.getElementById('ob-goal')?.value || 'endurance';
  const days = parseInt(document.getElementById('ob-days')?.value) || 3;
  const sess = parseInt(document.getElementById('ob-session')?.value) || 60;
  const wKg  = w * 0.453592;
  const hCm  = (ft * 12 + inch) * 2.54;
  const bmr  = sex === 'male' ? 10*wKg + 6.25*hCm - 5*a + 5 : 10*wKg + 6.25*hCm - 5*a - 161;
  const mult = ACT_MULT[days] || 1.55;
  const sessBonus = sess >= 90 ? 100 : sess >= 60 ? 50 : 0;
  const tdee  = Math.round(bmr * mult + sessBonus);
  const adj   = GOAL_ADJ[goal] || 0;
  const tKcal = tdee + adj;
  const protG = Math.round((GOAL_PROT_KG[goal] || 1.6) * wKg);
  const fatG  = Math.round(tKcal * 0.25 / 9);
  const carbG = Math.round((tKcal - protG*4 - fatG*9) / 4);
  const res = document.getElementById('ob-results');
  if (res) res.innerHTML = `
    <div class="ob-result-card"><div class="ob-r-val">${{tKcal}}</div><div class="ob-r-lbl">kcal / day</div></div>
    <div class="ob-result-card"><div class="ob-r-val">${{protG}}g</div><div class="ob-r-lbl">Protein / day</div></div>
    <div class="ob-result-card"><div class="ob-r-val">${{carbG}}g</div><div class="ob-r-lbl">Carbs / day</div></div>
    <div class="ob-result-card"><div class="ob-r-val">${{fatG}}g</div><div class="ob-r-lbl">Fat / day</div></div>
  `;
  const note = document.getElementById('ob-results-note');
  if (note) note.textContent = `BMR ${{Math.round(bmr)}} · TDEE ${{tdee}} · Goal: ${{GOAL_LABELS[goal] || goal}}`;
  const mealStyle = document.getElementById('ob-meal-style')?.value || 'even';
  window._obCalc = {{ w, a, ft, inch, sex, goal, days, sess, tKcal, protG, carbG, fatG,
    bmr: Math.round(bmr), tdee, wKg, adj, mealStyle }};
}}

function obFinish() {{
  const c = window._obCalc;
  if (!c) {{ showToast('Please complete all steps first'); return; }}
  // Use exact same key names as saveAndCalculate() so restoreSettings() works
  userSettings = {{ wt:c.w, age:c.a, ft:c.ft, inn:c.inch,
    sex:c.sex, goal:c.goal, days:c.days, dur:c.sess, mealStyle:c.mealStyle }};
  userTargets  = {{ bmr:c.bmr, tdee:c.tdee, targetKcal:c.tKcal,
    proteinG:c.protG, carbG:c.carbG, fatG:c.fatG,
    adj:c.adj, goal:c.goal, wt_kg:c.wKg }};
  saveUserProfile();
  // Pre-fill Settings tab fields
  restoreSettings();
  // Close modal, generate plan, go to dashboard
  document.getElementById('onboarding-modal').classList.remove('open');
  generateMealPlan();
  refreshDashboard();
  showToast('🎉 Setup complete! Your first meal plan is ready.');
}}

// ── INIT ────────────────────────────────────────────────────────────────────
function initExtras() {{
  customRecipes.forEach(r => injectCustomRecipe(r));
  applyStockToUI();
  restoreMealPlan();
  restoreLog();
  if (mealPlan2D && mealPlan2D.some(s => s && s.some(r => r))) {{
    showMealPlanContent();
    renderMealPlanGrid(); renderMacrosChart(); renderMacrosSummary();
  }}
  restoreSettings();
  refreshDashboard();
  showOnboarding();
}}
"""
