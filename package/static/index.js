$(function() { 
    var count = 0;
    $("#addMore").click(function(e) { 
     count = count +1;
      e.preventDefault();
      $("#fieldList").append("<li>&nbsp;</li>");
      $("#fieldList").append("<li>Vehicle #"+(count+1)+"</li>"); 
      $("#fieldList").append("<li>Please Enter the License Plate Number for All Vehicles Your Household Uses: <input type='text' class='form-control' id='license' name='license' style=border:2pxsolidwhite;background:transparent placeholder=' ' autocomplete='off' /></li>");
      $("#fieldList").append("<li>Please Enter How Many Miles You Drive This Vehicle Per Week:<input type='text' class='form-control' id='mpw' name='mpw' style=border:2pxsolidwhite;background:transparent placeholder=' ' autocomplete='off' /></li>");
      $("#fieldList").append("<li>Please Enter the Gas Mileage for This Vehicle In Miles Per Gallon: <input type='text' class='form-control' id='mpg' name='mpg' style=border:2pxsolidwhite;background:transparent placeholder=' ' autocomplete='off' /></li>");
    });
  });