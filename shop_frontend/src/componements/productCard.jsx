import { FaHeart,FaRegHeart, FaShoppingBag ,FaEuroSign} from 'react-icons/fa';
const ProductCard = (props) => {
console.log(props.categories);

    return (
      <div className="category product" key={props.product.id}>
      <img src={props.product.image} alt={props.product.title} />
      <h2 className="title-2">{props.product.title} </h2>
      <input type="hidden" value="" /> 
      {props.vendors.map((vendor) => (
    <div key={vendor.cid} >
        <h2 className="title-3 vendor"><span className="by">{props.product.vendor == vendor.id ? 'by' : "" }</span> {props.product.vendor == vendor.id ? vendor.vendor : "" } </h2>
    </div>
  ))}
      {props.categories.map((cat) => (
      <h2 className="title-3 " key={cat.cid}>{props.product.category == cat.cid ? cat.title : '' } </h2>
  ))}
<div className="price-box">
  <div className="price">{props.product.price}</div>
  <div className="promo-price">{props.product.promo_price ? props.product.promo_price : ''}</div>
  <div className="device">Francs cfa </div>
</div>
      <div className="action-section"style={{justifyContent:'center',alignContent:'center', display:'flex'}}>
      <button className="wishlist"><FaRegHeart  className="wished unwished" ></FaRegHeart></button>
      <button className="cart"><FaShoppingBag></FaShoppingBag> Add to cart</button></div>
      </div> 
    );
  }
  export default ProductCard;
  