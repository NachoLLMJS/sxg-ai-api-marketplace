const links=[...document.querySelectorAll('#toc a')];
const byId=new Map(links.map(link=>[link.getAttribute('href').slice(1),link]));
const seen=new IntersectionObserver(entries=>{
  for(const entry of entries){
    if(!entry.isIntersecting) continue;
    links.forEach(link=>link.classList.remove('on'));
    byId.get(entry.target.id)?.classList.add('on');
  }
},{rootMargin:'-20% 0px -70% 0px'});
document.querySelectorAll('main section').forEach(section=>seen.observe(section));
