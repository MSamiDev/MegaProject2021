



/*
if (localStorage.getItem("cart") == null) {
  var cart = {};
} else {
  cart = JSON.parse(localStorage.getItem("cart"));
//  document.getElementById('cart').innerHTML = Object.keys(cart).length;
  updateCart(cart);

}
$(".cart").click(function () {
  var idstr = this.id.toString();
  if (cart[idstr] != undefined) {
    cart[idstr] = cart[idstr] + 1;
  } else {
    cart[idstr] = 1;
  }
  updateCart(cart);
 // localStorage.setItem("cart", JSON.stringify(cart));

});


function updateCart(cart) {
  for (var item in cart) {
      document.getElementById('div' + item).innerHTML = "<button id='minus" + item + "' class='btn btn-primary minus'>-</button> <span id='val" + item + "''>" + cart[item] + "</span> <button id='plus" + item + "' class='btn btn-primary plus'> + </button>";
  }
  localStorage.setItem('cart', JSON.stringify(cart));
  //document.getElementById('cart').innerHTML = Object.keys(cart).length;
}

// minu plus btn click
$('.divpr').on("click", "button.minus", function() {
  a = this.id.slice(7, );
  cart['pr' + a] = cart['pr' + a] - 1;
  cart['pr' + a] = Math.max(0, cart['pr' + a]);
  document.getElementById('valpr' + a).innerHTML = cart['pr' + a];
  updateCart(cart);
});
$('.divpr').on("click", "button.plus", function() {
  a = this.id.slice(6, );
  cart['pr' + a] = cart['pr' + a] + 1;
  document.getElementById('valpr' + a).innerHTML = cart['pr' + a];
  updateCart(cart);
});
*/









/*
var updateBtns = document.getElementsByClassName('update-cart')

for (i = 0; i < updateBtns.length; i++) {
	updateBtns[i].addEventListener('click', function(){
		var productId = this.dataset.product
		var action = this.dataset.action
		console.log('productId:', productId, 'Action:', action)
		console.log('USER:', user)

		if (user == 'AnonymousUser'){
			addCookieItem(productId, action)
		}else{
			updateUserOrder(productId, action)
		}
	})
}

function updateUserOrder(productId, action){
	console.log('User is authenticated, sending data...')

		var url = '/t-kart/update_item/'

		fetch(url, {
			method:'POST',
			headers:{
				'Content-Type':'application/json',
				'X-CSRFToken':csrftoken,
			}, 
			body:JSON.stringify({'productId':productId, 'action':action})
		})
		.then((response) => {
		   return response.json();
		})
		.then((data) => {
		    location.reload()
		});
}

function addCookieItem(productId, action){
	console.log('User is not authenticated')

	if (action == 'add'){
		if (cart[productId] == undefined){
		cart[productId] = {'quantity':1}

		}else{
			cart[productId]['quantity'] += 1
		}
	}

	if (action == 'remove'){
		cart[productId]['quantity'] -= 1

		if (cart[productId]['quantity'] <= 0){
			console.log('Item should be deleted')
			delete cart[productId];
		}
	}
	console.log('CART:', cart)
	document.cookie ='cart=' + JSON.stringify(cart) + ";domain=;path=/"
	
	location.reload()
}

*/