(function(){
  "use strict";

  var state = document.getElementById('s-state');
  var btnEstimate = document.getElementById('btn-estimate');

  document.addEventListener('DOMContentLoaded', function(){

    btnEstimate.disabled = true;
    document.getElementById('cart-hplus').addEventListener('submit', estimateTotal);

    state.addEventListener('change', function(){
      btnEstimate.disabled = (state.value === '');
    });
  });

  function estimateTotal(event){
    event.preventDefault();

    if (state.value === ''){
      alert('Please choose your shipping state');

      state.focus();
    }
    var itemBball = parseInt(document.getElementById('txt-q-bball').value, 10) || 0;
    var itemJersey = parseInt(document.getElementById('txt-q-jersey').value, 10) || 0;
    var itemPower = parseInt(document.getElementById('txt-q-power').value, 10) || 0;
    var shippingState = state.value;

    var shippingMethod = document.querySelector('[name = r_method]:checked').value || "";


    var totalQty = itemBball + itemJersey + itemPower,
        shippingCostPer,
        shippingCost,
        taxFactor = 1,
        estimate,
        priceEstimate;

    if(shippingState === 'CA'){
      taxFactor = 1.075;
    }

    switch(shippingMethod){
      default: shippingCostPer = 0;
        break;
      case 'ups':
        shippingCostPer = 3;
        break;
      case 'usps':
        shippingCostPer =  2;
        break;
    }

        shippingCost = shippingCostPer * totalQty;

        priceEstimate = (90 * itemBball) + (25 * itemJersey) + (30 * itemPower);
        estimate = '$' + ((priceEstimate * taxFactor) + shippingCost).toFixed(2);
        document.getElementById('txt-estimate').value = estimate;

        var results = document.getElementById('results');
        results.innerHTML = 'Total items: '+ totalQty + '<br>';
        results.innerHTML += 'Total Shipping: $'+ shippingCost.toFixed(2) + '<br>';
        results.innerHTML += 'Tax: '+ ((taxFactor -1)*100).toFixed(2)+'% ('+shippingState+')';

  }

})();
