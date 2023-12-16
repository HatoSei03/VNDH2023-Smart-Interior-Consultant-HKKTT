const productList = [
  {
    link: "www.ikea.com",
    image: "magic.png",
    price: "$19.99",
  },
  {
    link: "www.ikea.com",
    image: "magic.png",
    price: "$24.99",
  },
  {
    link: "www.ikea.com",
    image: "magic.png",
    price: "$14.99",
  },
  {
    link: "www.ikea.com",
    image: "magic.png",
    price: "$19.99",
  },
  {
    link: "www.ikea.com",
    image: "magic.png",
    price: "$24.99",
  },
  {
    link: "www.ikea.com",
    image: "magic.png",
    price: "$14.99",
  },
  {
    link: "www.ikea.com",
    image: "magic.png",
    price: "$19.99",
  },
  {
    link: "www.ikea.com",
    image: "magic.png",
    price: "$24.99",
  },
  {
    link: "www.ikea.com",
    image: "magic.png",
    price: "$14.99",
  },
  {
    link: "www.ikea.com",
    image: "magic.png",
    price: "$19.99",
  },
  {
    link: "www.ikea.com",
    image: "magic.png",
    price: "$24.99",
  },
  {
    link: "www.ikea.com",
    image: "magic.png",
    price: "$14.99",
  },
  {
    link: "www.ikea.com",
    image: "magic.png",
    price: "$19.99",
  },
  {
    link: "www.ikea.com",
    image: "magic.png",
    price: "$24.99",
  },
  {
    link: "www.ikea.com",
    image: "magic.png",
    price: "$14.99",
  },
  // Add more products to the list as needed
];

const productListContainer = document.getElementById("productList");

const productRow = document.createElement("div");
productRow.classList.add("product-row");
productList.forEach((product) => {
  const productCard = document.createElement("a");
  productCard.href = product.link;
  productCard.classList.add("product-card");

  const productImage = document.createElement("img");
  productImage.src = product.image;
  productImage.alt = "Product Image";
  productImage.classList.add("product-image");

  const productPrice = document.createElement("p");
  productPrice.textContent = product.price;
  productPrice.classList.add("product-price");

  productCard.appendChild(productImage);
  productCard.appendChild(productPrice);
  productRow.appendChild(productCard);
});
productListContainer.appendChild(productRow);
