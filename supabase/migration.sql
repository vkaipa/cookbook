-- Run this in Supabase SQL Editor after schema.sql

-- meal_plans: swap text[] for jsonb to store the 4×7 slot grid
alter table public.meal_plans drop column if exists recipe_ids;
alter table public.meal_plans add column if not exists plan_grid jsonb;

-- user_profiles: add columns to store the settings and calculated targets as JSON blobs
alter table public.user_profiles add column if not exists settings_json jsonb;
alter table public.user_profiles add column if not exists targets_json  jsonb;
