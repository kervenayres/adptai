
const formInputs = document.querySelectorAll("form input");



const generateAttrs = async (event) => {
    const formElement = document.querySelector("form");
    event.preventDefault();
    const formData = new FormData(formElement);
    const jsonData = {};

    formData.forEach((value, key) => {
        const intValue = parseFloat(value);
        if (!isNaN(intValue)) {
            jsonData[key] = intValue;
            return;
        }
        jsonData[key] = value;
    });
    const response = await fetch("http://18.231.186.141:8000/", {
        method: "POST",
        body: JSON.stringify(jsonData),
        headers: {
            "Content-Type": "application/json",
        },
    });
    const responseData = JSON.parse(await response.json());
    console.log(responseData);

    formInputs.forEach(input => {
        if (input.type === 'number') {
            input.value = Math.floor(responseData[input.name]);
            return;
        }
        input.value = responseData[input.name];
    });
};

const cancelAttrs = () => {
    formInputs.forEach(input => {
        if (input.type === 'number') {
            input.value = 0;
            return;
        }
        input.value = '';
    });
};