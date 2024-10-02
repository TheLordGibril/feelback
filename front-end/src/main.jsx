import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client' 
import {
  createBrowserRouter,
  RouterProvider,
} from "react-router-dom";
import './index.css'

import Dashboard from "./routes/dashboard"
import Form from "./routes/form"
import Home from "./routes/home"

const router = createBrowserRouter([
  {
    path: "/",
    element: <Home/>,
  },  
  {
    path: "/form",
    element: <Form/>,
  },  
  {
    path: "/dashboard",
    element: <Dashboard/>,
  },
]);


createRoot(document.getElementById('root')).render(
  <StrictMode>
    <RouterProvider router={router} />
  </StrictMode>,
)
