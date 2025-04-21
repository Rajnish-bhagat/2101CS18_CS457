/*
  # Fix recursive policies on profiles table

  1. Changes
    - Remove recursive admin policy that was causing infinite recursion
    - Add new admin policy using auth.jwt() to check role directly
    - Keep existing user policy for reading own profile

  2. Security
    - Maintains row level security
    - Ensures admins can still read all profiles
    - Users can still read their own profile
*/

-- Drop existing policies
DROP POLICY IF EXISTS "Admins can read all profiles" ON profiles;
DROP POLICY IF EXISTS "Users can read own profile" ON profiles;

-- Create new policies that avoid recursion
CREATE POLICY "Users can read own profile"
ON profiles
FOR SELECT
TO authenticated
USING (auth.uid() = id);

CREATE POLICY "Admins can read all profiles"
ON profiles
FOR ALL 
TO authenticated
USING (
  (auth.jwt() ->> 'role')::text = 'admin'
);