(function(){
  'use strict';

  document.addEventListener('DOMContentLoaded', function(){
    var time = document.getElementById('current-time');
    var date = document.getElementById('current-date')

    //Time funtion
    setInterval(updateTime, 1000);
    function updateTime() {
      var d = new Date();

      //Create vars
      var minutes = d.getMinutes(),
          day = d.getDay().toString(),
          daynumber = d.getDate().toString(),
          month = formatMonth(d.getMonth());

      //Adds padding to the minutes such that 15:5 becomes 15:05
      if (minutes <10){
        minutes = '0' + minutes;
      }

      //Changes the separator's CSS class to make in transparent every other second
      var sepClass = '';
      if(d.getSeconds() %2 ===1 ){
        sepClass = 'trans';
      }
      var sep = '<span class ="'+sepClass +'">:</span>';

      //Date formatting
      switch (day){
        case '1':
          day = 'Monday';
          break;
        case '2':
          day = 'Tuesday';
          break;
        case '3':
          day = 'Wednesday';
          break;
        case '4':
          day = 'Thursday';
          break;
        case '5':
          day = 'Friday';
          break;
        case '6':
          day = 'Saturday';
          break;
        case '0':
          day = 'Sunday';
          break;
      }

      function formatMonth(m){
        var months = ['January', 'February', 'March', 'April', 'May', 'June', 'July','August', 'September', 'October', 'November', 'December'];
        return months[m];
      }

      //Actual Date and Time writing
      time.innerHTML = d.getHours() + sep + minutes;
      date.innerHTML = day + ', ' +  month + ' ' +daynumber;

    }

  });
})();
