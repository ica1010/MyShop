// import React from "react";
import Navbar from "../componements/navbar";
import Cart from "../componements/cart";
import axios from "axios";
import { useEffect, useState } from "react";
export const CartPage = () => {
  const [Categories, setCategories] = useState([]);
  useEffect(() => {
    axios
      .get("http://127.0.0.1:8000/category/")
      .then((res) => setCategories(res.data));
  }, []); 

  const [ProductList, setProductList] = useState([]);
  useEffect(() => {
    axios
      .get("http://127.0.0.1:8000/product/")
      .then((res) => setProductList(res.data));
  }, []); 

  return (
    <>
      <Navbar categories={Categories} ProductList={ProductList} ></Navbar>
      <Cart />
    </>
  );
};

export default CartPage;
