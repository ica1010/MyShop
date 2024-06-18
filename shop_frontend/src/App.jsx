import { BrowserRouter, Routes, Route } from "react-router-dom";
import { Home } from "./pages/homePage";
import CartPage from "./pages/cartPage";
import './style/style.css'
import CategoryPage from "./pages/categoryPage";
import StorePage from "./pages/storePage";
import NoPage from "./pages/404Page";


function App() {

  return (
    <main>
        <BrowserRouter>
      <Routes>
        <Route>
          <Route index element={<Home />} />
          <Route path="cart" element={<CartPage/>} />
          <Route path="store" element={<StorePage/>} />
          <Route path="category" element={<CategoryPage/>} />
          <Route path="*" element={<NoPage/>} />
        </Route>
      </Routes>
    </BrowserRouter>      
    </main>
  )
}

export default App
