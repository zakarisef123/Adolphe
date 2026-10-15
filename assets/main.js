(function(){
  var $=function(id){return document.getElementById(id)};

  // Header shadow on scroll
  var header=$('header');
  if(header){
    var onScroll=function(){header.classList.toggle('scrolled',window.scrollY>10)};
    window.addEventListener('scroll',onScroll,{passive:true});onScroll();
  }

  // Mobile menu
  var burger=$('burger'),mnav=$('mobileNav');
  if(burger&&mnav){
    var setMenu=function(open){
      mnav.classList.toggle('open',open);
      burger.setAttribute('aria-expanded',open);
      burger.innerHTML='<svg><use href="#i-'+(open?'x':'menu')+'"/></svg>';
    };
    burger.addEventListener('click',function(){setMenu(!mnav.classList.contains('open'))});
    mnav.querySelectorAll('a').forEach(function(a){a.addEventListener('click',function(){setMenu(false)})});
  }

  // Services dropdown (keyboard / touch)
  document.querySelectorAll('.dd > button').forEach(function(btn){
    btn.addEventListener('click',function(e){
      e.stopPropagation();
      var dd=btn.parentNode,open=!dd.classList.contains('open');
      document.querySelectorAll('.dd.open').forEach(function(d){d.classList.remove('open')});
      dd.classList.toggle('open',open);btn.setAttribute('aria-expanded',open);
    });
  });
  document.addEventListener('click',function(){document.querySelectorAll('.dd.open').forEach(function(d){d.classList.remove('open')})});

  // Tabs (home page)
  var tabs=document.querySelectorAll('.tab');
  function selectTab(id){
    tabs.forEach(function(t){
      var on=t.getAttribute('aria-controls')==='panel-'+id;
      t.setAttribute('aria-selected',on);
      $(t.getAttribute('aria-controls')).hidden=!on;
    });
  }
  tabs.forEach(function(t){t.addEventListener('click',function(){selectTab(t.id.replace('tab-',''))})});
  if(tabs.length&&location.hash==='#toiture')selectTab('toit');

  // Service CTA -> prefill form
  var select=$('f-type');
  function setService(service){
    if(!select||!service)return;
    for(var i=0;i<select.options.length;i++){if(select.options[i].text===service){select.selectedIndex=i;break;}}
  }
  function goQuote(service){
    setService(service);
    var c=$('contact');if(!c)return;
    c.scrollIntoView({behavior:'smooth'});
    setTimeout(function(){var n=$('f-name');if(n)n.focus({preventScroll:true})},700);
  }
  document.querySelectorAll('[data-service]').forEach(function(b){b.addEventListener('click',function(){goQuote(b.getAttribute('data-service'))})});
  document.querySelectorAll('[data-service-link]').forEach(function(a){a.addEventListener('click',function(e){e.preventDefault();goQuote(a.getAttribute('data-service-link'))})});

  // Form -> mailto
  var form=$('quoteForm'),ok=$('formOk');
  if(form){
    setService(form.getAttribute('data-default-service'));
    form.addEventListener('submit',function(e){
      e.preventDefault();
      var req=form.querySelectorAll('[required]'),bad=null;
      req.forEach(function(f){var empty=!f.value.trim();f.style.borderColor=empty?'#d64545':'';if(empty&&!bad)bad=f;});
      if(bad){bad.focus();ok.textContent='Merci de remplir les champs obligatoires (*).';ok.style.background='#fdecec';ok.style.color='#a12a2a';ok.classList.add('show');return;}
      var d=new FormData(form);
      var body='Nom : '+d.get('nom')+'\nTéléphone : '+d.get('telephone')+'\nEmail : '+(d.get('email')||'-')+'\nVille : '+d.get('ville')+'\nTravaux : '+d.get('type')+'\n\n'+(d.get('message')||'');
      var subject='Demande de devis – '+d.get('type')+' – '+d.get('ville');
      if(window.gtag){gtag('event','generate_lead',{service:d.get('type')});gtag('event','conversion',{'send_to':'AW-17854390149/ghi2CKGo6o8cEIW_0cFC'});}
      window.location.href='mailto:barryadolphe9@gmail.com?subject='+encodeURIComponent(subject)+'&body='+encodeURIComponent(body);
      ok.style.background='';ok.style.color='';
      ok.innerHTML='Merci ! Votre messagerie va s\'ouvrir avec votre demande. Pour une réponse immédiate, appelez le <a href="tel:+33759781806" style="text-decoration:underline">07 59 78 18 06</a>.';
      ok.classList.add('show');
    });
  }

  // Track call / WhatsApp clicks
  document.querySelectorAll('a[href^="tel:"],a[href*="wa.me"]').forEach(function(a){a.addEventListener('click',function(){if(window.gtag)gtag('event',a.href.indexOf('tel:')===0?'click_call':'click_whatsapp');})});

  // Gallery lightbox
  var lb=$('lightbox');
  if(lb){
    var items=[].slice.call(document.querySelectorAll('.gallery button')),lbImg=$('lbImg'),lbCap=$('lbCap'),idx=0;
    var show=function(i){idx=(i+items.length)%items.length;var im=items[idx].querySelector('img');lbImg.src=im.src;lbImg.alt=im.alt;lbCap.textContent=im.alt;};
    var close=function(){lb.classList.remove('open');document.body.style.overflow='';};
    items.forEach(function(b,i){b.addEventListener('click',function(){show(i);lb.classList.add('open');document.body.style.overflow='hidden';})});
    $('lbClose').addEventListener('click',close);
    $('lbPrev').addEventListener('click',function(){show(idx-1)});
    $('lbNext').addEventListener('click',function(){show(idx+1)});
    lb.addEventListener('click',function(e){if(e.target===lb)close();});
    document.addEventListener('keydown',function(e){if(!lb.classList.contains('open'))return;if(e.key==='Escape')close();if(e.key==='ArrowLeft')show(idx-1);if(e.key==='ArrowRight')show(idx+1);});
  }

  // Reviews carousel
  var track=$('revTrack');
  if(track&&$('revPrev')){
    var step=function(){var c=track.querySelector('.rev');return c?c.offsetWidth+20:320;};
    $('revPrev').addEventListener('click',function(){track.scrollBy({left:-step(),behavior:'smooth'})});
    $('revNext').addEventListener('click',function(){track.scrollBy({left:step(),behavior:'smooth'})});
  }

  // Reveal on scroll
  var els=document.querySelectorAll('.reveal');
  if('IntersectionObserver' in window){
    var io=new IntersectionObserver(function(entries){entries.forEach(function(en){if(en.isIntersecting){en.target.classList.add('in');io.unobserve(en.target);}})},{threshold:.12,rootMargin:'0px 0px -40px 0px'});
    els.forEach(function(el){io.observe(el)});
  } else { els.forEach(function(el){el.classList.add('in')}); }

  var y=$('year');if(y)y.textContent=new Date().getFullYear();
})();
