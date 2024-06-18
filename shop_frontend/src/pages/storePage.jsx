// import React from "react";
import Navbar from "../componements/navbar";
import Product from "../componements/product";
import axios from "axios";
import { useEffect, useState } from "react";
const StorePage = () => {
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
  
    const [vendorList, setVendorList] = useState([]);
    useEffect(() => {
      axios
        .get("http://127.0.0.1:8000/user/vendor/")
        .then((res) => setVendorList(res.data));
    }, []);
  
  return (
   <main>
      <Navbar categories={Categories} ProductList={ProductList}></Navbar>
      <Product
        Categories={Categories}
        ProductList={ProductList}
        vendorList={vendorList}
      ></Product>
   </main>
  )
}

export default StorePage