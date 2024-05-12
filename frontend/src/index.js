import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.scss';
//import App from './App';
import reportWebVitals from './reportWebVitals';

import { createBrowserRouter , RouterProvider} from 'react-router-dom';
import { QueryClient, QueryClientProvider } from 'react-query';
import { ProtectedRoute } from './components/ProtectedRoute';
import { AuthProvider } from './hooks/useAuth';
import AppLayout from './layouts/app'
import Home from './pages';
import SignUp from './pages/signup';
import Login from './pages/login';
import Dashboard from './pages/dashboard';


const queryClient = new QueryClient()
const router = createBrowserRouter([
  {
    path : '/',
    id : 'root',
    element: <AuthProvider/>,
    children : [
      {
        path : '/signup',
        element : <SignUp/>
      },
      {
        path : '/login',
        element : <Login/>
      },
      {
        path: '/dashboard',
        element: 
        <ProtectedRoute>
          <AppLayout>
            <Dashboard/>
          </AppLayout>
        </ProtectedRoute>
      }

    ]
  },
])

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <QueryClientProvider client={queryClient}>
      <RouterProvider router={router}/>
    </QueryClientProvider>
      
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
