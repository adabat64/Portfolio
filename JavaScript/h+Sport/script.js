(function(){
  "use strict";


  var state = document.getElementById('s-state');
  var btnEstimate = document.getElementById('btn-estimate');

//On initial DOM Load
  document.addEventListener('DOMContentLoaded', function(){

    // Disable the Estimate button
    btnEstimate.disabled = true;
    //Attach Estimate btn to function
    document.getElementById('cart-hplus').addEventListener('submit', estimateTotal);

    //change the state of the btn when the State selector is changed --> when empty keep on disabled
    state.addEventListener('change', function(){
      btnEstimate.disabled = (state.value === '');
    });
  });

//Function attached to Estimate btn
  function estimateTotal(event){
    event.preventDefault();

    //alert if no state has been added + focus on the State selector
    if (state.value === ''){
      alert('Please choose your shipping state');
      state.focus();
    }

    //create variables from element HTML IDs -->parsed to ints, base 10, default to 0
    var itemBball = parseInt(document.getElementById('txt-q-bball').value, 10) || 0;
    var itemJersey = parseInt(document.getElementById('txt-q-jersey').value, 10) || 0;
    var itemPower = parseInt(document.getElementById('txt-q-power').value, 10) || 0;
    var itemWater = parseInt(document.getElementById('txt-q-water').value, 10) || 0;

    var shippingState = state.value;

    //get radio btn value from CSS[], default to empty string
    var shippingMethod = document.querySelector('[name = r_method]:checked').value || "";

    //create vars for calculation
    var totalQty = itemBball + itemJersey + itemPower + itemWater,
        shippingCostPer,
        shippingCost,
        taxFactor = 1,
        estimate,
        priceEstimate;

    //taking tax into account
    if(shippingState === 'CA'){
      taxFactor = 1.075;
    } else if (shippingState === 'WA') {
      taxFactor = 1.065;
    }

    //taking shipping costs into account
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

        //Calculations
        shippingCost = shippingCostPer * totalQty;

        priceEstimate = (90 * itemBball) + (25 * itemJersey) + (30 * itemPower)+ (4 * itemWater);
        estimate = '$' + ((priceEstimate * taxFactor) + shippingCost).toFixed(2);
        document.getElementById('txt-estimate').value = estimate;


        //Creating innerHTML as summary elements
        var results = document.getElementById('results');
        results.innerHTML = 'Total items: '+ totalQty + '<br>';
        results.innerHTML += 'Total Shipping: $'+ shippingCost.toFixed(2) + '<br>';
        results.innerHTML += 'Tax: '+ ((taxFactor -1)*100).toFixed(2)+'% ('+shippingState+')';

  }

})();
