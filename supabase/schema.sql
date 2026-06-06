-- ── Tables ───────────────────────────────────────────────────────────────────

create table public.recipes (
  id           text primary key,
  user_id      uuid references auth.users(id) on delete cascade,
  name         text not null,
  tier         text not null check (tier in ('grab','easy','moderate','batch','snack')),
  tier_label   text not null,
  chef         text,
  description  text,
  time_label   text,
  servings     text,
  ingredients  jsonb not null default '[]',
  steps        jsonb not null default '[]',
  macros       jsonb not null default '{}',
  perf_tip     text,
  created_at   timestamptz default now()
);
-- user_id NULL = built-in recipe shared across all users
-- user_id set  = custom recipe owned by that user

create table public.user_profiles (
  user_id            uuid primary key references auth.users(id) on delete cascade,
  weight_kg          numeric,
  height_cm          numeric,
  age                integer,
  sex                text,
  activity_level     text,
  goal               text check (goal in ('muscle_gain','fat_loss','endurance','general')),
  daily_kcal_target  integer,
  protein_target_g   integer,
  carbs_target_g     integer,
  fat_target_g       integer,
  updated_at         timestamptz default now()
);

create table public.meal_plans (
  id         uuid default gen_random_uuid() primary key,
  user_id    uuid not null references auth.users(id) on delete cascade,
  week_of    date not null,
  recipe_ids text[] not null default '{}',
  created_at timestamptz default now(),
  unique (user_id, week_of)
);

create table public.pantry (
  user_id    uuid not null references auth.users(id) on delete cascade,
  item_name  text not null,
  in_stock   boolean not null default true,
  updated_at timestamptz default now(),
  primary key (user_id, item_name)
);

create table public.cart (
  user_id    uuid not null references auth.users(id) on delete cascade,
  item_name  text not null,
  checked    boolean not null default false,
  week_of    date not null,
  updated_at timestamptz default now(),
  primary key (user_id, item_name, week_of)
);

-- ── Row Level Security ────────────────────────────────────────────────────────

alter table public.recipes       enable row level security;
alter table public.user_profiles enable row level security;
alter table public.meal_plans    enable row level security;
alter table public.pantry        enable row level security;
alter table public.cart          enable row level security;

-- recipes: authenticated users can read all built-in recipes (user_id is null)
--          and can fully manage their own custom recipes
create policy "Read built-in and own recipes" on public.recipes
  for select using (user_id is null or auth.uid() = user_id);

create policy "Manage own custom recipes" on public.recipes
  for all using (auth.uid() = user_id)
  with check (auth.uid() = user_id);

-- all other tables: each user sees and touches only their own rows
create policy "Own profile"    on public.user_profiles for all using (auth.uid() = user_id) with check (auth.uid() = user_id);
create policy "Own meal plans" on public.meal_plans    for all using (auth.uid() = user_id) with check (auth.uid() = user_id);
create policy "Own pantry"     on public.pantry        for all using (auth.uid() = user_id) with check (auth.uid() = user_id);
create policy "Own cart"       on public.cart          for all using (auth.uid() = user_id) with check (auth.uid() = user_id);
