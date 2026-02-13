-- ==============================================================================
-- Engelsiz Alışveriş - Supabase Database Schema
-- ==============================================================================

-- 1. Profiles Table (Extends auth.users)
-- This table is automatically populated via a trigger when a new user signs up.
create table public.profiles (
  id uuid references auth.users not null primary key,
  updated_at timestamp with time zone,
  full_name text,
  avatar_url text,
  is_staff boolean default false, -- Determines if the user is a staff member
  disability_type text check (disability_type in ('none', 'visual', 'hearing', 'physical', 'other')) default 'none'
);

-- Turn on Row Level Security
alter table public.profiles enable row level security;

-- Policies for Profiles
create policy "Public profiles are viewable by everyone."
  on profiles for select
  using ( true );

create policy "Users can insert their own profile."
  on profiles for insert
  with check ( auth.uid() = id );

create policy "Users can update own profile."
  on profiles for update
  using ( auth.uid() = id );

-- 2. Products Table
create table public.products (
  id uuid default uuid_generate_v4() primary key,
  created_at timestamp with time zone default timezone('utc'::text, now()) not null,
  name text not null,
  barcode text unique,
  price numeric,
  image_url text,
  description text
);

-- Turn on Row Level Security
alter table public.products enable row level security;

-- Policies for Products
create policy "Products are viewable by everyone."
  on products for select
  using ( true );

create policy "Only staff can insert products."
  on products for insert
  with check ( exists ( select 1 from profiles where id = auth.uid() and is_staff = true ) );

create policy "Only staff can update products."
  on products for update
  using ( exists ( select 1 from profiles where id = auth.uid() and is_staff = true ) );


-- 3. Help Requests Table
create table public.help_requests (
  id uuid default uuid_generate_v4() primary key,
  created_at timestamp with time zone default timezone('utc'::text, now()) not null,
  user_id uuid references public.profiles(id) not null,
  status text check (status in ('pending', 'in_progress', 'completed', 'cancelled')) default 'pending',
  latitude float,
  longitude float,
  staff_id uuid references public.profiles(id), -- The staff member who accepted the request
  notes text
);

-- Turn on Row Level Security
alter table public.help_requests enable row level security;

-- Policies for Help Requests
-- Users can see their own requests. Staff can see all requests.
create policy "Users can view own requests. Staff can view all."
  on help_requests for select
  using ( 
    auth.uid() = user_id 
    or 
    exists ( select 1 from profiles where id = auth.uid() and is_staff = true ) 
  );

-- Users can create help requests.
create policy "Users can create help requests."
  on help_requests for insert
  with check ( auth.uid() = user_id );

-- Users can cancel their own requests.
create policy "Users can update own requests."
  on help_requests for update
  using ( auth.uid() = user_id );

-- Staff can update requests (to accept or complete them).
create policy "Staff can update requests."
  on help_requests for update
  using ( exists ( select 1 from profiles where id = auth.uid() and is_staff = true ) );


-- ==============================================================================
-- Triggers and Functions
-- ==============================================================================

-- Function to handle new user signup
create or replace function public.handle_new_user() 
returns trigger as $$
begin
  insert into public.profiles (id, full_name, avatar_url, disability_type)
  values (new.id, new.raw_user_meta_data->>'full_name', new.raw_user_meta_data->>'avatar_url', COALESCE(new.raw_user_meta_data->>'disability_type', 'none'));
  return new;
end;
$$ language plpgsql security definer;

-- Trigger to call the function on signup
create trigger on_auth_user_created
  after insert on auth.users
  for each row execute procedure public.handle_new_user();

-- Helper function to generate dummy product data (Optional, for testing)
create or replace function insert_dummy_products()
returns void as $$
begin
  insert into public.products (name, barcode, price, description) values
    ('Süt (1L)', '86900001', 25.50, 'Tam yağlı süt'),
    ('Ekmek', '86900002', 10.00, 'Odun ekmeği'),
    ('Çikolata', '86900003', 15.00, 'Fındıklı çikolata');
end;
$$ language plpgsql;
