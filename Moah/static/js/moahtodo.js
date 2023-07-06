//main-Frame: hamburger-menu-js

document.addEventListener("DOMContentLoaded", function() {
    var hamburgerMenu = document.querySelector(".hamburger-menu");
    var menu = document.querySelector(".menu");

    hamburgerMenu.addEventListener("click", function() {
        menu.classList.toggle("show");
    });
});

// 시간 함수
var today = new Date();
var month = today.toLocaleString('en', { month: 'long' });

var monthElement = document.querySelector(".month");
if(monthElement) {
    monthElement.textContent = month;
};

// 할 일 리스트 체크 함수
function toggleTask(element) {
    element.classList.toggle('checked');
}

// 생성 버튼 and 삭제 버튼
var plusButton = document.querySelector(".plusButton");
plusButton.addEventListener('click',function() {
    var toDoList = document.querySelector(".toDoList");
    var clone = toDoList.cloneNode(true);
    document.body.appendChild(clone);
});

// var minusButtons = document.querySelectorAll('.deleteButton');
// minusButtons.forEach(function(button) {
//   button.addEventListener('click', function() {
//     var toDoList = button.closest('.toDoList');
//     toDoList.remove();
//   });
// });
//  삭제 버튼 오류