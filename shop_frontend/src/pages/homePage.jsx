// import React from "react";
import Navbar from "../componements/navbar";
import Silders from "../componements/sliders";
import Category from "../componements/category";
import Product from "../componements/product";
import Vendors from "../componements/vendors";
import axios from "axios";
import { FaHome } from 'react-icons/fa';
import { useEffect, useState } from "react";

export const Home = () => {
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

  const create = () => {
    const formData = new FormData();
    formData.append("vendor", 2);
    formData.append("title", "sweetLeaf");
    formData.append("category", "Cat-ca13eggcbd3adddc");
    formData.append("descriptions", "");
    formData.append("stock", 50);
    formData.append("price", 854);
    // Ajoutez vos fichiers d'image
    const imageFile = document.querySelector('#imageFile').files[0]; // supposant que vous avez un input type file avec id imageFile
    formData.append("image", imageFile);

    axios.post("http://localhost:8000/product/create/", formData, {
        headers: {
            'Content-Type': 'multipart/form-data'
        }
    })
    .then(response => {
        console.log("Product created successfully:", response.data);
    })
    .catch(error => {
        console.error("There was an error creating the product:", error);
    });
};
  return (
    <div>
      <Navbar categories={Categories} ProductList={ProductList}></Navbar>
      {/* <Silders></Silders> */}
      <Category categories={Categories}></Category>
      <input type="file" name="" id="imageFile" onChange={create} />
      <Product
        Categories={Categories}
        ProductList={ProductList}
        vendorList={vendorList}
      ></Product>
      <Vendors vendors={vendorList} ></Vendors>
    </div>
  )
}
