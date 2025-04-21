/*
  # Fix registration flow and profile policies

  1. Changes
    - Add policy to allow new users to create their profile
    - Update admin policy to use proper role check
    - Ensure users can read their own profile

  2. Security
    - Maintains row level security
    - Allows new user registration
    - Preserves admin access
*/

-- Drop existing policies
DROP POLICY IF EXISTS "Admins can read all profiles" ON profiles;
DROP POLICY IF EXISTS "Users can read own profile" ON profiles;

-- Create new policies
CREATE POLICY "Enable insert for authentication users only"
ON profiles
FOR INSERT
TO authenticated
WITH CHECK (auth.uid() = id);

CREATE POLICY "Users can read own profile"
ON profiles
FOR SELECT
TO authenticated
USING (auth.uid() = id);

CREATE POLICY "Admins can manage all profiles"
ON profiles
FOR ALL 
TO authenticated
USING (
  coalesce(
    (SELECT role FROM profiles WHERE id = auth.uid()) = 'admin',
    false
  )
);