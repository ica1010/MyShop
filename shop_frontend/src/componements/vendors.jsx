import React from 'react'
import VendorCart from './vendorCart'

const Vendors = (props) => {
  return (
    <section className="vendor-section">
    <h2 className="title product-title">Vendors List</h2>
    <div className="vendor-box">
  {props.vendors.map((vendor) => (
          <VendorCart key={vendor.vendor} vendor={vendor} />
))}
    </div>
  </section>

  )
}


export default Vendors