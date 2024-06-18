// import React from 'react'
import Category from '../componements/category'
import Navbar from '../componements/navbar';
import axios from "axios";
import { useEffect, useState } from "react";
const CategoryPage = () => {
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
    <main>
        <Navbar categories={Categories} ProductList={ProductList}></Navbar>
        <Category categories={Categories}></Category>
    </main>
  )
}

export default CategoryPage