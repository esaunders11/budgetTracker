let selects = document.querySelectorAll(".options select");
let inputs = document.querySelectorAll(".input input");
let inp1 = inputs[0];
let inp2 = inputs[1];
let addBtn = document.querySelector(".add");
let sel = selects[0];
let outputs = document.querySelectorAll(".output");
let out1 = outputs[0];
let out2 = outputs[1];
let login = document.querySelectorAll(".loginInput input");
let uname = login[0];
let psw = login[1];
let loginBtn = document.querySelector(".loginBtn");



let data = {};
populate();
addWeeks();


loginBtn.addEventListener("click", ()=>{
 
    data.username = uname.value;
    data.password = psw.value;
});

function populate(){
    let weeks = "";
    for (let i = 1; i < 53; i++) {
        let str = `<option value="week${i}">Week ${i}</option>`;
        weeks += str;
    }
    selects.forEach((s) => (s.innerHTML = weeks));
}

function addWeeks(){
    data.purchases = {}
    for (let i = 1; i < 53; i++) {
        let s = `week${i}`;
        data.purchases[s] = {};
    }
}

function addExpense(week, pur, pri){
    data.purchases[week][pur] = pri;
}

function getTotal(week){
    let total = 0;
    for (const val of Object.values(data.purchases[week])) {
        total += val;
    }
    return total
}

function displayBudget(week){
    let output = ""
    for (const [key, value] of Object.entries(data.purchases[week])) {
        output += `${key}: $${value}<br>`;
    }
    out1.innerHTML = `${output}`;
    out2.innerHTML = `<br>total: $${getTotal(week)}`;
    inp1.value = '';
    inp2.value = '';
}

addBtn.addEventListener("click", ()=>{
    let purchase = inp1.value;
    let price = parseFloat(inp2.value);
    let week = sel.value;

    if (isNaN(price)) {
        alert("Enter a number");
    }
    else {
        addExpense(week, purchase, price);
        displayBudget(week);
        
    }
});

selects.forEach(s=>s.addEventListener("change", ()=>{
    out1.innerHTML = '';
    out2.innerHTML = '';
}));


