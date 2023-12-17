fetch("products.json")
  .then((response) => response.json())
  .then((data) => {
    const productListContainer = document.getElementById("productList");
    const productRow = document.createElement("div");
    productRow.classList.add("product-row");

    data.forEach((product) => {
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
  })
  .catch((error) => {
    console.error("Error:", error);
  });
