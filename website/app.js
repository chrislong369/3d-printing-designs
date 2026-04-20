async function loadCatalog(){
  try{
    const res=await fetch('./3d-catalog.json');
    if(!res.ok) throw new Error('No catalog yet');
    const data=await res.json();
    initUI(data);
  }catch(e){
    document.getElementById('results-count').textContent='Catalog not built yet. Push files to trigger it.';
  }
}

function initUI(data){
  const grid=document.getElementById('catalog-grid');
  const count=document.getElementById('results-count');
  const search=document.getElementById('search-input');
  const catFilter=document.getElementById('category-filter');
  const extFilter=document.getElementById('extension-filter');

  const categories=[...new Set(data.map(d=>d.category))];
  categories.forEach(c=>{
    const opt=document.createElement('option');
    opt.value=c;opt.textContent=c;catFilter.appendChild(opt);
  });

  function render(){
    const s=search.value.toLowerCase();
    const cat=catFilter.value;
    const ext=extFilter.value;

    const filtered=data.filter(d=>{
      return (cat==='all'||d.category===cat)
        &&(ext==='all'||d.extension===ext)
        &&(d.name.toLowerCase().includes(s)||d.path.toLowerCase().includes(s));
    });

    grid.innerHTML='';
    filtered.forEach(d=>{
      const card=document.createElement('div');
      card.className='product-card';
      card.innerHTML=`<div><span class="badge">${d.category}</span><span class="badge">${d.extension}</span></div><h3>${d.name}</h3><p class="product-path">${d.path}</p><small>${d.size_mb} MB</small>`;
      grid.appendChild(card);
    });

    count.textContent=`${filtered.length} results`;
  }

  search.addEventListener('input',render);
  catFilter.addEventListener('change',render);
  extFilter.addEventListener('change',render);

  document.getElementById('stat-total').textContent=data.length;
  document.getElementById('stat-categories').textContent=categories.length;
  document.getElementById('stat-3mf').textContent=data.filter(d=>d.extension==='.3mf').length;
  document.getElementById('stat-stl').textContent=data.filter(d=>d.extension==='.stl').length;

  render();
}

loadCatalog();