import { useState } from 'react'
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom'
import Login from './pages/Login'

import Register from './pages/Register'
import Home from './pages/Home'
import NotFound from './pages/NotFound'
import ProtectedRoute from './components/ProtectedRoutes'
import './App.css'

function Logout() {
  localStorage.clear(); // clear our refresh token and access token
  return <Navigate to="/login" />
}

function RegisterAndLogOut() {
  localStorage.clear();
  return <Register />
}



function App() {
  const [username, setUsername] = useState<string>("")

  return (
    <BrowserRouter>
      <Routes>
        <Route
          path="/"
          element={
            <ProtectedRoute>
              <Home />
              {/* cannot access home component unless you have the access token */}
            </ProtectedRoute>
          }
        />
        <Route path="/login" element={<Login />} />
        <Route path="/logout" element={<Logout />} />
        <Route path="/register" element={<RegisterAndLogOut />} />
        <Route path="*" element={<NotFound />}> </Route>




      </Routes>

    </BrowserRouter>
  )
}

export default App
