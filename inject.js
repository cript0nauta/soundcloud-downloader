// Código a inyectar en el navegador para deslizarse continuamente
f = function(){
	e = $('#sm2-container')[0];
	e.scrollIntoView();
	if(x){setTimeout(f,1000)}; // Me vuelvo a ejecutar dentro de un segundo
}
x=1; f();






// Ejecutar cuando se haya bajado hasta el final
x = 0;
links = $('.soundTitle__title');
for(i=0; i<links.length; i++)
{
	console.log(links[i].href);
}
