import { Link } from "react-router-dom";
const NoPage = () => {
    return <center>
         <h1 className="title-404 title">404 Error</h1>
         <p className="text-404">Page not found</p>
         <p className="text-404">Go <Link to={'/'}>Home</Link></p>
    </center>;
  };
  
  export default NoPage;