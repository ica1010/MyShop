import CartItem from "./cartItem";

const Cart = (props) => {
  return (
    <section className="category Cart">
      <h2 className="title product-title">your Cart</h2>
      <div className="category-box">
      <div className="main">
      <div className="item-col">
      <CartItem></CartItem>
      <CartItem></CartItem>
      </div>
      <div className="chip-col">
        <div className="category total product" >
          <div className="desc-section">
            <h2 className="title-2">Total</h2>
            <h2 className="title-3 price">
              5000
            </h2>
            <h2 className="title-2">Frais de livraison</h2>
            <h2 className="title-3 price">
              1000
            </h2>
            <h2 className="title-2 price-title ">Grand Total</h2>
            <h2 className="title-3 price-total">
              6000
            </h2>
           <button className="ship-btn">Shiping now</button>
          </div>
        </div>
      </div>
    </div>
      </div>
    </section>
  );
}

export default Cart;
