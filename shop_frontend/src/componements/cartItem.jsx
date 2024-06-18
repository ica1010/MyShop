const CartItem = (props) => {
  return (
    <div className="category cart-item product">
    <img src={"vite.svg"} />
    <div className="desc-section">
      <h2 className="title-2">Product</h2>
      <h2 className="title-3 vendor">
        <span className="by"> by </span> Hello
      </h2>
      <h2 className="title-3">category</h2>
    </div>
    <div className="desc-section">
      <h2 className="title-2">Price</h2>
      <input
        disabled
        type="number"
        name=""
        value={2000}
        id=""
        style={{ width: "fit-content" }}
      />
    </div>
    <div className="desc-section">
      <h2 className="title-2">Quantity</h2>
      <button>-</button>
      <input
        disabled
        type="number"
        name=""
        value={12}
        id=""
        style={{ width: "fit-content" }}
      />
      <button>+</button>
    </div>
    <div className="desc-section">
      <h2 className="title-2">Delete ?</h2>
      <button>DELETE</button>
    </div>
  </div>
  );
};
export default CartItem;
