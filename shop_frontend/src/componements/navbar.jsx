import { FaBars, FaHeart, FaHome, FaRegUserCircle, FaSearch, FaShoppingBag } from 'react-icons/fa';
import { Link } from "react-router-dom";

function Navbar({ categories }) {
  return (
    <>
      <header className="navbar">
        <Link to="/"><div className="logo">
          <h1>Market .</h1>
        </div></Link>
        <ul>
          <Link to={'/'} className="navlinks"><li className="navlinks ">Home</li></Link>
          <div className="dropdown">
          <Link to={'/category'} className="navlinks"><li className="navlinks ">Category</li></Link>

            <div className="dropdown-content">
              {categories.map((cat) => (
                <a href="#" key={cat.cid}>
                  {cat.title}
                </a>
              ))}
            </div>
          </div>
          <Link to={'/store'} className="navlinks" ><li >Store</li></Link>
          <li className="navlinks">Vendors</li>
          <li className="navlinks">about</li>
          <li className="navlinks">Contact us</li>
        </ul>
        <ul>
          <Link to={'/cart'} className="navlinks"><li className="navlinks "><FaShoppingBag style={{fontSize:'1.4rem'}} ></FaShoppingBag> <sup>0</sup></li></Link>
          <Link to={'/cart'}  className="navlinks "><FaHeart style={{fontSize:'1.4rem'}} ></FaHeart><sup>0</sup></Link>
          <li className="navlinks mobile-navlinks"> <FaSearch style={{fontSize:'1.3rem', margin:'0px 15px'}} ></FaSearch></li>
          <li className=" mobile-navlinks" style={{fontSize:'1.4rem'}}><FaBars></FaBars></li>

          {/* <li className="navlinks mobile-navlinks">Sign in</li> */}
        </ul>
      </header>
      <div className="mobile-menu">
        <ul className="bottom-navbar" style={{justifyContent:'space-around', padding:'15px 0px'}}>
          <Link className="navlinks mobile-navlinks" to={'/'}><FaHome style={{fontSize:'1.4rem'}} ></FaHome></Link>
          <Link className="navlinks mobile-navlinks" to={'/cart'}><FaShoppingBag style={{fontSize:'1.4rem'}}></FaShoppingBag><sup>0</sup></Link>
          <li className="navlinks mobile-navlinks"><FaHeart style={{fontSize:'1.4rem'}}></FaHeart><sup>0</sup></li>
          <li className="navlinks mobile-navlinks"><FaRegUserCircle style={{fontSize:'1.4rem'}}></FaRegUserCircle></li>
        </ul>
      </div>
    </>
  );
}

export default Navbar;
