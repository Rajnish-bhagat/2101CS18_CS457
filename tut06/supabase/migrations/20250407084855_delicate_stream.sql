/*
  # Fix authentication policies

  1. Changes
    - Simplify profile policies
    - Ensure proper access control
    - Fix profile creation during registration

  2. Security
    - Maintains RLS
    - Allows authenticated users to create their profile
    - Preserves admin access control
*/

-- Drop existing policies
DROP POLICY IF EXISTS "Allow profile creation during signup" ON profiles;
DROP POLICY IF EXISTS "Users can read own profile" ON profiles;
DROP POLICY IF EXISTS "Admins have full access" ON profiles;

-- Create new policies
CREATE POLICY "Enable read access to own profile"
ON profiles FOR SELECT
TO authenticated
USING (auth.uid() = id);

CREATE POLICY "Enable insert for authenticated users"
ON profiles FOR INSERT
TO authenticated
WITH CHECK (auth.uid() = id);

CREATE POLICY "Enable update for users"
ON profiles FOR UPDATE
TO authenticated
USING (auth.uid() = id)
WITH CHECK (
  CASE 
    WHEN auth.uid() = id THEN 
      CASE 
        WHEN role = 'admin' THEN 
          EXISTS (SELECT 1 FROM profiles WHERE id = auth.uid() AND role = 'admin')
        ELSE true
      END
    ELSE false
  END
);