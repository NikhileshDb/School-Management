import {
    Country,
    State,
    City
} from 'country-state-city';

import intlTelInput from 'intl-tel-input';

window.onload = function () {
    // Get the target element
    var el = document.getElementById('country');
    // generate country list from the library 
    var countryList = Country.getAllCountries();
    // add the country list to the options
    if (countryList.length == 0) {
        el.innerHTML = "<option>Select Country</p>";
    } else {
        let optionCountry = "";
        for (let item in countryList) {
            optionCountry += `<option value="${countryList[item].isoCode}">${countryList[item].name}</option>`;
        }
        el.innerHTML = optionCountry;
    }
// get the DOM element
    const elState = document.getElementById('state');
// get the states and create states option
    const generateState = (value) => {
        const states = State.getStatesOfCountry(value);
        if(states.length == 0){
            elState.innerHTML = "<option>Select State</option>";
        } else {
            let optionState = ""; 
            for (let i in states){
                optionState += `<option value="${states[i].countryCode},${states[i].isoCode}">${states[i].name}</option>`
            }
            elState.innerHTML = optionState;
        }
    }
    el.addEventListener('change', (e) => generateState(e.target.value));

    // console.log(City.getCitiesOfState("IN", "TR"));
    // target the city element
    const elCity = document.getElementById('city');


    const generateCity = (value) => {
        let x = value.split(",");
        var cities = City.getCitiesOfState(x[0].toString() , x[1].toString());
        if(cities.length == 0){
            elCity.innerHTML = "<option>Select City </option>";
        } else {
            let optionCities = "";
            for(let i in cities){
                optionCities += `<option>${cities[i].name}</option>`
            }
            elCity.innerHTML = optionCities;
        }
    }

    elState.addEventListener('change', (e) => generateCity(e.target.value));



    // phonenumber intl input
    

    const input = document.getElementById("phone");
    const phone1 = document.getElementById("phone1");
    const phone2 = document.getElementById("phone2");
    intlTelInput(input, {
        allowDropdown: true,
        initialCountry: "auto",
        separateDialCode: true,
        customContainer: "w-[80%] float-right",
        preferredCountries:["IN"],

        // any initialisation options go here
    });
    intlTelInput(phone1, {
        allowDropdown: true,
        initialCountry: "auto",
        separateDialCode: true,
        customContainer: "w-[70%]",
        preferredCountries:["IN"],

        // any initialisation options go here
    });
    intlTelInput(phone2, {
        allowDropdown: true,
        initialCountry: "auto",
        separateDialCode: true,
        customContainer: "w-[70%]",
        preferredCountries:["IN"],

        // any initialisation options go here
    });
}