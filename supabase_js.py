"""
supabase_js.py
Supabase auth + data layer injected into the generated HTML.
"""

SUPABASE_JS = """
// ── Supabase ──────────────────────────────────────────────────────────────────
const _sb = supabase.createClient(
  'https://jruosffpgqksubufwxgi.supabase.co',
  'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImpydW9zZmZwZ3Frc3VidWZ3eGdpIiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODA3NjgyOTYsImV4cCI6MjA5NjM0NDI5Nn0.pMMikPA3-rx87NikYbOt4ig_P6JUuNWFE4lr3aVrlN8'
);
let _user = null;

function _weekMonday() {
  const d = new Date(), day = d.getDay();
  const diff = d.getDate() - day + (day === 0 ? -6 : 1);
  return new Date(new Date(d).setDate(diff)).toISOString().slice(0, 10);
}

// ── Auth ──────────────────────────────────────────────────────────────────────
async function initAuth() {
  const { data: { session } } = await _sb.auth.getSession();
  if (session) { _user = session.user; await _loadUserData(); _showApp(); }
  else { _showAuthScreen(); }

  _sb.auth.onAuthStateChange(async (event, session) => {
    if (event === 'SIGNED_IN') {
      _user = session.user; await _loadUserData(); _showApp();
    } else if (event === 'SIGNED_OUT') {
      _user = null;
      stockStatus = {}; mealPlan = []; mealPlan2D = null;
      userSettings = null; userTargets = null; customRecipes = [];
      _showAuthScreen();
    }
  });
}

function _showApp() {
  document.getElementById('auth-screen').style.display = 'none';
  document.getElementById('app-container').style.display = '';
  initExtras();
}
function _showAuthScreen() {
  document.getElementById('auth-screen').style.display = '';
  document.getElementById('app-container').style.display = 'none';
}

let _authMode = 'signin';
function toggleAuthMode() {
  _authMode = _authMode === 'signin' ? 'signup' : 'signin';
  document.getElementById('auth-submit').textContent = _authMode === 'signin' ? 'Sign In' : 'Create Account';
  document.getElementById('auth-toggle').textContent = _authMode === 'signin' ? "Don't have an account? Sign up" : 'Already have an account? Sign in';
  document.getElementById('auth-title').textContent  = _authMode === 'signin' ? 'Sign in to your cookbook' : 'Create your cookbook';
}

document.getElementById('auth-form').addEventListener('submit', async e => {
  e.preventDefault();
  const email = document.getElementById('auth-email').value.trim();
  const pwd   = document.getElementById('auth-password').value;
  const msgEl = document.getElementById('auth-message');
  msgEl.textContent = '';
  let error;
  if (_authMode === 'signin') {
    ({ error } = await _sb.auth.signInWithPassword({ email, password: pwd }));
  } else {
    ({ error } = await _sb.auth.signUp({ email, password: pwd }));
    if (!error) { msgEl.textContent = '✉️ Check your email to confirm your account.'; return; }
  }
  if (error) msgEl.textContent = error.message;
});

async function sendMagicLink() {
  const email = document.getElementById('auth-email').value.trim();
  if (!email) { document.getElementById('auth-message').textContent = 'Enter your email first.'; return; }
  const { error } = await _sb.auth.signInWithOtp({ email });
  document.getElementById('auth-message').textContent = error ? error.message : '✉️ Magic link sent — check your email.';
}

async function signOut() { await _sb.auth.signOut(); }

// ── Data load ─────────────────────────────────────────────────────────────────
async function _loadUserData() {
  if (!_user) return;
  const uid = _user.id, weekOf = _weekMonday();

  // Cart: items checked off this week in the store
  const { data: cartData } = await _sb.from('cart')
    .select('item_name,checked').eq('user_id', uid).eq('week_of', weekOf);
  stockStatus = {};
  (cartData || []).forEach(r => { if (r.checked) stockStatus[r.item_name] = 'in'; });

  // Meal plan 2D grid for this week
  const { data: planData } = await _sb.from('meal_plans')
    .select('plan_grid').eq('user_id', uid).eq('week_of', weekOf).maybeSingle();
  mealPlan2D = planData?.plan_grid || null;
  if (mealPlan2D) {
    const ids = new Set();
    mealPlan2D.forEach(s => s && s.forEach(r => r && ids.add(r)));
    mealPlan = [...ids];
  }

  // User profile & targets
  const { data: pd } = await _sb.from('user_profiles')
    .select('settings_json,targets_json').eq('user_id', uid).maybeSingle();
  userSettings = pd?.settings_json || null;
  userTargets  = pd?.targets_json  || null;

  // Custom recipes
  const { data: rData } = await _sb.from('recipes').select('*').eq('user_id', uid);
  customRecipes = (rData || []).map(r => ({
    id: r.id, name: r.name, tier: r.tier, tier_label: r.tier_label,
    chef: r.chef, description: r.description, time: r.time_label,
    servings: r.servings, ingredients: r.ingredients, steps: r.steps,
    macros: r.macros, perf_tip: r.perf_tip, custom: true
  }));
}

// ── Data save ─────────────────────────────────────────────────────────────────
function db_saveCartItem(itemName, checked) {
  if (!_user) return;
  _sb.from('cart').upsert(
    { user_id: _user.id, item_name: itemName, checked, week_of: _weekMonday(), updated_at: new Date().toISOString() },
    { onConflict: 'user_id,item_name,week_of' }
  ).then(({ error }) => { if (error) console.error('cart save:', error); });
}

function db_saveMealPlan2D() {
  if (!_user) return;
  _sb.from('meal_plans').upsert(
    { user_id: _user.id, week_of: _weekMonday(), plan_grid: mealPlan2D },
    { onConflict: 'user_id,week_of' }
  ).then(({ error }) => { if (error) console.error('plan save:', error); });
}

function saveUserProfile() {
  if (!_user || !userTargets) return;
  _sb.from('user_profiles').upsert({
    user_id: _user.id, settings_json: userSettings, targets_json: userTargets,
    daily_kcal_target: userTargets.targetKcal, protein_target_g: userTargets.proteinG,
    carbs_target_g: userTargets.carbG, fat_target_g: userTargets.fatG,
    updated_at: new Date().toISOString()
  }, { onConflict: 'user_id' }).then(({ error }) => { if (error) console.error('profile save:', error); });
}

async function db_saveCustomRecipe(recipe) {
  if (!_user) return;
  const { error } = await _sb.from('recipes').insert({
    id: recipe.id, user_id: _user.id, name: recipe.name, tier: recipe.tier,
    tier_label: recipe.tier_label, chef: recipe.chef || 'Custom',
    description: recipe.description, time_label: recipe.time,
    servings: recipe.servings, ingredients: recipe.ingredients,
    steps: recipe.steps, macros: recipe.macros, perf_tip: recipe.perf_tip
  });
  if (error) console.error('recipe insert:', error);
}
"""
