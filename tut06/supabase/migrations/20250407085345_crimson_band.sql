/*
  # Implement JWT-based authentication

  1. Changes
    - Create trigger to sync auth.users with profiles
    - Update policies to use JWT claims
    - Simplify access control

  2. Security
    - Maintains RLS
    - Uses JWT for role-based access
    - Automatic profile creation
*/

-- Enable realtime
ALTER PUBLICATION supabase_realtime ADD TABLE profiles;

-- Create function to handle user creation
CREATE OR REPLACE FUNCTION public.handle_new_user()
RETURNS TRIGGER AS $$
BEGIN
  INSERT INTO public.profiles (id, role)
  VALUES (NEW.id, COALESCE((NEW.raw_user_meta_data->>'role')::text, 'user'));
  RETURN NEW;
END;
$$ LANGUAGE plpgsql SECURITY DEFINER;

-- Create trigger for new user creation
DROP TRIGGER IF EXISTS on_auth_user_created ON auth.users;
CREATE TRIGGER on_auth_user_created
  AFTER INSERT ON auth.users
  FOR EACH ROW EXECUTE FUNCTION public.handle_new_user();

-- Drop existing policies
DROP POLICY IF EXISTS "Enable read access to own profile" ON profiles;
DROP POLICY IF EXISTS "Enable insert for authenticated users" ON profiles;
DROP POLICY IF EXISTS "Enable update for users" ON profiles;

-- Create new JWT-based policies
CREATE POLICY "Users can view own profile"
ON profiles FOR SELECT
TO authenticated
USING (auth.uid() = id);

CREATE POLICY "Users can update own profile"
ON profiles FOR UPDATE
TO authenticated
USING (auth.uid() = id)
WITH CHECK (
  CASE
    WHEN NEW.role = 'admin' THEN 
      (SELECT role FROM profiles WHERE id = auth.uid()) = 'admin'
    ELSE 
      auth.uid() = id
  END
);