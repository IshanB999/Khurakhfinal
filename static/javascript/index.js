function openDialog() {
    window.location.href = '/login'

}

function openProfileDialog(){
    document.getElementById('dialogOverlay2').classList.add('show');

}


function openMealRegistration(){
  document.getElementById('dialogOverlay3').classList.add('show');

}

function closeDialogRegistration(){
  document.getElementById('dialogOverlay3').classList.remove("show")
}

function closeProfileDialog(){
  document.getElementById('dialogOverlay2').classList.remove('show');

}


function openChangePassword(){
  // document.getElementById('dialogOverlay3').classList.add('show');
  window.location.href = '/profile/change-password'

}
function hideChangePassword(){
  // window.history.back();
  window.location.href = '/profile'

}
function closeDialog() {
    window.history.back();
    // document.getElementById('dialogOverlay').classList.remove('show');
}



if(window.location.pathname.includes("login")){
  document.getElementById('dialogOverlay').classList.add('show');

}

if(window.location.pathname.includes("change-password")){
  document.getElementById('dialogOverlay3').classList.add('show');

}



function calculate_ticker(bmi){

const bmit = bmi; // Example value for bmit

  let targetWidth = 0;

  // Determine the target width based on the bmit value
  if (bmit < 18.5) {
    targetWidth = (bmit / 18.5) * 25; // 0% to 25%
  } else if (bmit >= 18.5 && bmit < 25.0) {
    targetWidth = 25 + ((bmit - 18.5) / (24.9 - 18.5)) * 25; // 25% to 50%
  } else if (bmit >= 25.0 && bmit < 30.0) {
    targetWidth = 50 + ((bmit - 25.0) / (29.0 - 25.0)) * 25; // 50% to 75%
  } else if (bmit >= 30.0 && bmit < 40.0) {
    targetWidth = 75 + ((bmit - 30.0) / (40.0 - 30.0)) * 25; // 75% to 100%
  } else if (bmit >= 40.0) {
    targetWidth = 100; // 100%
  }


  console.log(targetWidth)
  document.getElementById('bmi-ticker').style.left = targetWidth + '%'

}







// dropdown js

function toggleDropdown(event) {
  const dropdown = document.getElementById('dropdownMenu');
  dropdown.style.display = dropdown.style.display === 'block' ? 'none' : 'block';
}



// gender select on bmi calculator

function selectGender(gender) {
  // Remove active class from both labels
  document.getElementById("label-male").classList.remove("active-label");
  document.getElementById("label-female").classList.remove("active-label");
  
  // Add active class to the selected label
  document.getElementById("label-" + gender).classList.add("active-label");
  
  // Set the radio input to checked
  document.getElementById(gender).checked = true;
}



// trigger the ticker of bmi box after form is submitted
document.addEventListener("DOMContentLoaded", function() {
  // Retrieve the BMI value from JSON data
  const bmiValue = parseFloat(document.getElementById("bmi-data").textContent);

  // console.log('bmi value',bmiValue)
  if (!isNaN(bmiValue)) {
      calculate_ticker(bmiValue);
  }
});


// 


class SnackBar{
  constructor() {
    // Create a container for all snackbars if it doesn't exist
    if (!document.querySelector('.snackbar-container')) {
        const container = document.createElement('div');
        container.classList.add('snackbar-container');
        document.body.appendChild(container);
    }
    this.container = document.querySelector('.snackbar-container');
}

showSnack(message, type) {
  // Create a new snackbar element
  const snackbar = document.createElement('div');
  snackbar.classList.add('snackbar');
  if (type) {
      snackbar.classList.add(type); // Add type-specific class (e.g., success, error)
  }
  snackbar.textContent = message;

  // Append snackbar to the container
  this.container.appendChild(snackbar);

  // Trigger fade-in effect
  setTimeout(() => {
      snackbar.classList.add('show');
  }, 10);

  // Automatically hide the snackbar after 3 seconds
  setTimeout(() => {
      this.hide(snackbar);
  }, 3000);
}
  hide(snackbar) {
    // snackbar.classList.remove('show');
    snackbar.classList.add('hide');
    // snackbar.style.display = 'none'

    setTimeout(()=>{
      snackbar.remove()
    },500)
}
}

const snack = new SnackBar();


function showSnackBar(message='Testing the javascript snackbar',type='success'){


snack.showSnack(message,type)
setTimeout(()=>{
    snack.hide()
},4000)
}





// const responseMessage = document.getElementById('response-message');

const handleSubmitPlanRegistration = async (event,id) => {
    event.preventDefault();  // Prevent form from submitting the traditional way
    const form = document.getElementById('register-plan-form');

    const formData = new FormData(form);

    try {
        const response = await fetch(`/create-plan/${id}/`, {
            method: 'POST',
            body: formData,
            headers: {
                'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value,
            }
        });
        
        const result = await response.json();

        if (response.ok) {
            // Display success message
            snack.showSnack(message="Successfully Registered this plan to your profile",type='success')
            closeDialogRegistration();

            setTimeout(()=>{
              window.location.reload()
            },1000)
        } else {
            // Display error message
            snack.showSnack(message=result.message || 'Something Went Wrong',type='error')

        }
    } catch (error) {
        // snack.showSnack(message=result.message || 'Something Went Wrong',type='error')
        console.log('error',error)

    }
};