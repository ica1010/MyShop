import ProductCard from "./productCard";

const Product = (props) => {
console.log('Product:'+props.ProductList);
console.log('Product:'+props.Categories);
console.log(props);
  return (
    <section className="category product">
      <h2 className="title product-title">Ours products</h2>
      <div className="category-box">
    {props.ProductList.map((product) => (
            <ProductCard categories={props.Categories} product={product} vendors={props.vendorList} key={product.pid}></ProductCard>
  ))}
      </div>
    </section>

  );
}

export default Product;
