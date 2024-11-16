function displayRandomNumber() {
    const numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]; 

    const randomIndex = Math.floor(Math.random() * numbers.length);
    const randomNumber = numbers[randomIndex];

    document.getElementById("randomNumber").textContent = `המספר הרנדומלי הוא: ${randomNumber}`;
    document.getElementById("randomNumber").textContent = `המספר הרנדומלי הוא: ${randomNumber}`;
    document.getElementById("randomNumber").textContent = `המספר הרנדומלי הוא: ${randomNumber}`;
    document.getElementById("randomNumber").textContent = `המספר הרנדומלי הוא: ${randomNumber}`;

}