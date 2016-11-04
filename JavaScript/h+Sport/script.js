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
  }

})();
