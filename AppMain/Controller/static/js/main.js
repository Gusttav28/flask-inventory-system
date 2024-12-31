
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

// if(btnDelete){
//     console.log("this is a test for javascript") 
//     for(let i = 0; i < cicle; i++){
//         number += 1
//         console.log(number)
//     }
// } 

function itemsDeleteFu() {
    btnDelette.className = 'btn btn-danger';
    btnDelette.textContent = 'Delete';
    btnDelette.href = '#'
    btnContainer.appendChild(btnDelette);

    btnEdit.className = 'btn btn-info me-4';
    btnEdit.textContent = 'Edit';
    btnEdit.href = "#";
    btnContainer.appendChild(btnEdit);

    btnContainer.removeChild(btnAdd);
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
btnAdd.className = 'btn btn-primary';
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