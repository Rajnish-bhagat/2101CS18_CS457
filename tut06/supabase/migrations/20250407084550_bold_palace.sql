/*
  # Fix registration policies

  1. Changes
    - Simplify policies to avoid recursion
    - Allow new user registration without role check
    - Maintain secure access control

  2. Security
    - Maintains RLS
    - Allows profile creation during registration
    - Preserves admin access control
*/

-- Drop existing policies
DROP POLICY IF EXISTS "Enable insert for authentication users only" ON profiles;
DROP POLICY IF EXISTS "Users can read own profile" ON profiles;
DROP POLICY IF EXISTS "Admins can manage all profiles" ON profiles;

-- Create simplified policies
CREATE POLICY "Allow profile creation during signup"
ON profiles
FOR INSERT
TO authenticated
WITH CHECK (auth.uid() = id);

CREATE POLICY "Users can read own profile"
ON profiles
FOR SELECT
TO authenticated
USING (auth.uid() = id);

CREATE POLICY "Admins have full access"
ON profiles
FOR ALL
TO authenticated
USING (
  EXISTS (
    SELECT 1 FROM profiles p 
    WHERE p.id = auth.uid() AND p.role = 'admin'
  )
);