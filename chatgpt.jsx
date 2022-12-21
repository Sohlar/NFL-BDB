import React from 'react';

const ComplexReactFunction = props => {
  const { products, cart, handleAddToCart, handleRemoveFromCart } = props;

  const renderProductCards = () => {
    return products.map(product => (
      <ProductCard
        key={product.id}
        name={product.name}
        price={product.price}
        imageUrl={product.imageUrl}
        handleAddToCart={handleAddToCart}
      />
    ));
  };

  const renderCartItems = () => {
    return cart.map(item => (
      <CartItem
        key={item.id}
        name={item.name}
        price={item.price}
        quantity={item.quantity}
        handleRemoveFromCart={handleRemoveFromCart}
      />
    ));
  };

  const renderTotal = () => {
    let total = 0;
    cart.forEach(item => {
      total += item.price * item.quantity;
    });
    return total;
  };

  return (
    <div className="complex-react-function">
      <h1>Ecommerce Website</h1>
      <div className="products-container">
        {renderProductCards()}
      </div>
      <div className="cart-container">
        <h2>Cart</h2>
        {renderCartItems()}
        <p>Total: ${renderTotal()}</p>
      </div>
    </div>
  );
};

export default ComplexReactFunction;
