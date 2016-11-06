//Google Maps
  var GMapApiKey = 'AIzaSyCBtxBDjh_mDGNVazSW3XA70ePp52-_-rk';
  var map;
  laContent1 = "H+Sport HeadQuarters"
  laContent2 = "Our new location"
      function initMap() {
        map = new google.maps.Map(document.getElementById('hplus-map'), {
          center: {lat: 34.102, lng: -118.326},
          zoom: 12
        });
        var infowindow1 = new google.maps.InfoWindow({
          content: laContent1
        });
        var infowindow2 = new google.maps.InfoWindow({
          content: laContent2
        });
        var marker1 = new google.maps.Marker({
          position : {lat: 34.102, lng: -118.326},
          map: map,
          title: 'H+ Sport'
        });
        var marker2 = new google.maps.Marker({
          position: {lat: 34.0724, lng:-118.2479},
          map: map,
          title: 'New location'
        });
        marker1.addListener('click', function(){
          infowindow1.open(map, marker1);
        });
        marker2.addListener('click', function(){
          infowindow2.open(map, marker2)
        });
      }


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
