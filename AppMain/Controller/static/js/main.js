
var number = 0
var cicle = 3
const btnDelete = document.getElementById('btnDelete');
const btnContainer = document.getElementById('btnContainers');
const btnDelette = document.createElement('a');

const btnEdit = document.createElement('a');
const btnAdd = document.createElement('button');
const btnTest = document.getElementById('btnTest');

const inputsTable = document.querySelectorAll('.inputsTable');
const itemsDelete = document.getElementById('itemsDelete');

const itemData = document.getElementById('itemData');
const itemContent = itemData.textContent;
const data = itemData.getAttribute('data-value')

const flash_message = document.getElementById('flash_container')


const modal = document.getElementById('modal');
const overlay = document.getElementById('modal-overlay');

// if(btnDelete){
//     console.log("this is a test for javascript") 
//     for(let i = 0; i < cicle; i++){
//         number += 1
//         console.log(number)
//     }
// } 

setTimeout(() =>{
    if(flash_message){
        flash_message.style.transition = 'opacity 0.5s ease';
        flash_message.style.opacity = '0';
        setTimeout(()=> flash_message.remove(), 500);
    }
}, 2000);

function itemsDeleteFu(item_id, item_information) {
    // btnDelette.className = 'btn btn-danger';
    // btnDelette.textContent = 'Delete';
    // btnDelette.href = '/itemDelete';
    // btnContainer.appendChild(btnDelette);

    btnEdit.className = 'btn btn-info me-4';
    btnEdit.textContent = 'Edit';
    btnEdit.href = "#";
    btnContainer.appendChild(btnEdit);

    btnContainer.removeChild(btnAdd); 

}

function openModal(){
    modal.style.display = 'block';
    overlay.style.display = 'block';
}

function closeModal(){
    modal.style.display = 'none';
    overlay.style.display = 'none';
}

function handleInput(){
    const userInput = document.getElementById('user-input').value;
    if (userInput) {
        alert(`You entered: ${userInput}`);
        closeModal();
    } else {
        alert('Please enter something before submitting.');
    }
}


// if(itemsDelete.addEventListener('click', function(){
    
//     btnDelette.className = 'btn btn-danger';
//     btnDelette.textContent = 'Delete';
//     btnDelette.href = '#'
//     btnContainer.appendChild(btnDelette);

//     btnEdit.className = 'btn btn-info me-4';
//     btnEdit.textContent = 'Edit';
//     btnEdit.href = "#";
//     btnContainer.appendChild(btnEdit);

//     btnContainer.removeChild(btnAdd);
    
//     // btnDelete.removeAttribute('style');
//     // btnDelete.classList.remove('btn-secundary');
//     // btnDelete.classList.add('btn-danger');
//     // btnEdit.classList.remove('btn-secundary');
//     // btnEdit.classList.add('btn-info');  

// }));

// btnDelette.className = 'btn btn-danger';
// btnDelette.textContent = 'Delete';
// btnDelette.href = '#'


// btnEdit.className = 'btn btn-info me-4';
// btnEdit.textContent = 'Edit';
// btnEdit.href = "#";

// itemsDelete.forEach(link =>{
//     link.addEventListener('focus', (event) => {
//         btnContainer.appendChild(btnEdit);
//         btnContainer.appendChild(btnDelete);
//     });
// });


// if(inputsTable.addEventListener('click', function () {
//     console.log("hello world")
//     btnAdd.className = 'btn btn-primary';
//     btnAdd.textContent = 'Add';
//     btnContainer.appendChild(btnAdd)

//     btnContainer.removeChild(btnEdit);
//     btnContainer.removeChild(btnDelette);
// }));
btnAdd.className = 'btn btn-primary me-4';
btnAdd.textContent = 'Add'
inputsTable.forEach(input=>{
    input.addEventListener('focus', (event)=> {
        if(!btnContainer.contains(btnAdd)){
            btnContainer.appendChild(btnAdd);
            btnContainer.removeChild(btnEdit);
            btnContainer.removeChild(btnDelette);
        }   
    }); 
});

function emptyInputs(){
    inputsTable.forEach(input =>{
        if (input.type === 'text' || input.type === 'number') {
            input.value = '';
        } else if(input.tagName === 'SELECT'){
            input.seletedIndex = '';
        }
    })
}