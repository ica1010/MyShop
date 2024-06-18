import CategoryCard from "./categoryCard";
const Category = ({categories}) => {
console.log('category:'+categories);
console.log(categories);
  return (
    <section className="category product-title">
      <h2 className="title">Category</h2>
      <div className="category-box">
      {categories.map((cat) => (
    <CategoryCard key={cat.cid} cat={cat} />
  ))}
      </div>
    </section>

  );
}

export default Category;
