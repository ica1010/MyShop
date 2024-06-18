const CategoryCard = ({cat}) => {

  return (
    <div className="category" key={cat.cid}>
    <img src={'http://127.0.0.1:8000'+cat.image} alt={cat.title} />
    <h2 className="title-2">{cat.title} </h2>
    <input type="hidden" value="" />
  </div>
  );
}
export default CategoryCard;
