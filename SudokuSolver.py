<html>
<head>
  <title>Sodoku Solver</title>
  <script type="text/javascript" src="http://underscorejs.org/underscore-min.js"></script>
  <script type="text/javascript">

    // Initialize some state
    var myApp = {};

    myApp.data = [[],[],[],[],[],[],[],[],[]];
    myApp.data[3][0] = 6;

    //Wait till the page is loaded to mess with the html
    document.addEventListener('DOMContentLoaded', function(){
      var myGameDiv = document.getElementById("game");
      myGameDiv.innerHTML = '';
      for (var i = 0; i < 9; i++) {
        var myBox = document.createElement("div");
        myBox.className = "box box" + i;
        for (var n = 0; n < 9; n++) {
          var myInput = document.createElement("input");
          var myCol = ((i % 3 * 3) + (n % 3));
          var myRow = ((Math.floor(n / 3)) + (Math.floor(i / 3) * 3));
          myInput.type = "text";
          myInput.maxLength = 1;
          myInput.id = "inp"+myCol+"x"+myRow;
          myInput.className = "col" + myCol;
          myInput.className += " row" + myRow;
          myInput.className += " box" + i;
          myInput.addEventListener("change", puzzleChanged);
          myBox.appendChild(myInput);
        };
        myGameDiv.appendChild(myBox);
      };
    });
    function puzzleChanged (event) {
      // console.log(event);
      // console.log(event.srcElement.id);
      var myCoords = event.srcElement.id.replace("inp","").split("x");
      // console.log(myCoords);
      var myVal = parseInt(event.srcElement.value);
      if (myVal) {
        myApp.data[myCoords[0],myCoords[1]] = myVal;
      }else{
        event.srcElement.value = "";
      };
    }
    function puzzleCheck (event) {
      console.log(event);
      // Now you just need to validate the myApp.data array
      // And show a message accordingly
    }

  </script>
  <style type="text/css">
    div.game {
      width: 228px;
      text-align: center;
      float: left;
    }
    div.box {
      width: 74px;
      border: 1px solid black;
      text-align: center;
      float: left;
    }
    div.box input {
      width: 20px;
      margin: 2px;
      text-align: center;
      float: left;
    }
  </style>
</head>
<body>
<div class="">
  <h2>Interesting Links:</h2>
  <a href="http://youmightnotneedjquery.com/">http://youmightnotneedjquery.com/</a><br>
  <a href="http://underscorejs.org/">http://underscorejs.org/</a><br>
</div>
<h2>The Game:</h2>
<div id="game" class="game"></div>
</body>
</html>