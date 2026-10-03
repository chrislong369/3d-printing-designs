/* Only Final_Products data is used by the customer-facing catalog. */
async function loadProducts() {
  const response = await fetch('./data/site-products.json');
  if (!response.ok) throw new Error('Catalog request failed: ' + response.status);
  const products = await response.json();
  const grid = document.getElementById('catalog-grid');
  const category = document.getElementById('category-filter');
  for (const value of [...new Set(products.map(p => p.category))].sort()) category.add(new Option(value, value));
  document.getElementById('stat-total').textContent = products.length;
  document.getElementById('stat-categories').textContent = category.options.length - 1;
  for (const extension of ['stl', '3mf']) {
    document.getElementById('stat-' + extension).textContent = products.filter(p => p.extension === '.' + extension).length;
  }
  function render() {
    const query = document.getElementById('search-input').value.toLowerCase();
    const extension = document.getElementById('extension-filter').value;
    const sort = document.getElementById('sort-filter').value;
    const filtered = products.filter(p =>
      (p.name + ' ' + p.file).toLowerCase().includes(query) &&
      (category.value === 'all' || category.value === p.category) &&
      (extension === 'all' || extension === p.extension));
    filtered.sort((a, b) => sort === 'size-desc' ? b.size_mb - a.size_mb :
      sort === 'size-asc' ? a.size_mb - b.size_mb :
      sort === 'name-desc' ? b.name.localeCompare(a.name) : a.name.localeCompare(b.name));
    grid.replaceChildren();
    for (const product of filtered) {
      const card = document.createElement('article');
      card.className = 'product-card';
      const heading = document.createElement('h3');
      heading.textContent = product.name;
      const detail = document.createElement('p');
      detail.textContent = product.category + ' · ' + product.extension.slice(1).toUpperCase();
      card.append(heading, detail);
      grid.append(card);
    }
    document.getElementById('results-count').textContent = filtered.length + ' products';
    document.getElementById('empty-state').classList.toggle('hidden', filtered.length > 0);
  }
  for (const id of ['search-input', 'category-filter', 'extension-filter', 'sort-filter'])
    document.getElementById(id).addEventListener('input', render);
  render();
}
loadProducts().catch(error => {
  console.error(error);
  document.getElementById('results-count').textContent = 'Catalog unavailable. Please try again later.';
});
