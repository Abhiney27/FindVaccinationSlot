function validateForm() {
        var pincode = document.forms["PinCode"]["pincode"].value;
        if(pincode == ""){
            alert("Please enter the Pincode");
            return false;
        }
    }
