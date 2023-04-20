const trigger = document.getElementById("id_fixed_cost")

function isFixed() {
    const elementsArray = document.querySelectorAll('#id_unit, #id_current_counter, #id_consumption, #id_cost_per_unit');
    if (trigger.checked) {
       for (let i = 0; i < elementsArray.length; i++) {
        elementsArray[i].disabled = true;
        }
    }else{
        for (let i = 0; i < elementsArray.length; i++) {
        elementsArray[i].disabled = false;
        }
    }

}

trigger.addEventListener("change", isFixed);