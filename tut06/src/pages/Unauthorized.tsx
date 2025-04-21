import { Link } from 'react-router-dom';
import { ShieldX } from 'lucide-react';

export function Unauthorized() {
  return (
    <div className="min-h-screen bg-gray-100 flex items-center justify-center">
      <div className="max-w-md w-full bg-white rounded-lg shadow-md p-8 text-center">
        <div className="flex justify-center mb-6">
          <ShieldX className="h-16 w-16 text-red-600" />
        </div>
        <h2 className="text-2xl font-bold text-gray-900 mb-4">
          Access Denied
        </h2>
        <p className="text-gray-600 mb-6">
          You are not authorized to access this page. This area is restricted to administrators only.
        </p>
        <Link
          to="/dashboard"
          className="inline-flex items-center justify-center px-4 py-2 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
        >
          Return to Dashboard
        </Link>
      </div>
    </div>
  );
}