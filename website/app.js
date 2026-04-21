async function loadProducts(){
  const res = await fetch('./data/site-products.json');
  const data = await res.json();
  return data;
}

function renderProducts(products){
  const grid = document.getElementById('product-grid');
  grid.innerHTML='';

  if(!products.length){
    grid.innerHTML='<div class="empty-state">No products yet. Move approved items into library/public.</div>';
    return;
  }

  products.forEach(p=>{
    const card=document.createElement('div');
    card.className='product-card';
    card.innerHTML=`
      <div class="product-image">
        ${p.image?`<img src="${p.image}" />`:'<div class="product-fallback"></div>'}
        <div class="product-badges">
          <span class="badge">${p.category}</span>
        </div>
      </div>
      <div class="product-copy">
        <h3>${p.name}</h3>
        <p>${p.description||'Clean, optimized 3D printable design.'}</p>
      </div>
    `;
    grid.appendChild(card);
  });
}

loadProducts().then(renderProducts);