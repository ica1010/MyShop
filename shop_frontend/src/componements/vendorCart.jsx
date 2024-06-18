import React from "react";
import { FaCheckCircle, FaArrowRight } from "react-icons/fa";
import Container from "react-bootstrap/Container";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import Card  from "react-bootstrap/Card"
import Button from "react-bootstrap/Button"
const VendorCart = (props) => {
  return (
    <Card style={{ width: '18rem' }} className="h-cart " >
    <Card.Img variant="top"  src={"http://127.0.0.1:8000" + props.vendor.image} />
    <Card.Body>
      <Card.Title>{props.vendor.vendor} <div className="verified">
          <FaCheckCircle></FaCheckCircle> verified
        </div> </Card.Title>
      <Card.Text>
        Some quick example text to build on the card title and make up the
        bulk of the cards content.
      </Card.Text>
      <Button variant="primary">Go somewhere</Button>
    </Card.Body>
  </Card>
  );
};

export default VendorCart;
