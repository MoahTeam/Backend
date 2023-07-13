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
var thisMonth = today.toLocaleString('en', { month: 'long' });

var monthElement = document.querySelector(".month");
if(monthElement) {
    monthElement.textContent = thisMonth;
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
    var deleteButton = clone.querySelector(".minusButton");
    var inputField = clone.querySelector("#field");
    inputField.value = '';
    // document.getElementById(deleteButton).style.top = "0.5rem"
    // deleteButton.forEach(function(button) {
    //     button.addEventListener('click', function() {
    //         button.closest(".toDoList").remove();
    //     });
    // });
    // clone.style.position = "relative";
    // deleteButton.style.postion = "absolute";
    // deleteButton.style.right = "0.5rem";
    // deleteButton.style.top = "0.44rem";
    deleteButton.addEventListener("click", function() {
        var listItem = deleteButton.closest(".toDoList");
        listItem.remove();
    });
    // var clonedForm = clone.querySelector("form");
    // clonedForm.style.display = "inherit";
    // clonedForm.style.alignItems = "center";
    // clonedForm.style.margin = "auto";
    document.body.appendChild(clone);
});

// 달력 생성
function getDaysInMonth(year, month) {
    return new Date(year, month+1, 0).getDate();
}

var currentDate = today.getDate();
var currentMonth = today.getMonth();
var currentYear = today.getFullYear();
var daysInMonth = getDaysInMonth(currentYear, currentMonth);

var firstLine = '';
for (var i =1; i<=17; i++) {
    if (i===currentDate){
        firstLine += '<div class="current">'+i+'</div>';
    }
    else {
        firstLine += '<div>'+i+'</div>';
    }
}

var secondLine = '';
for (var i=1; i<=daysInMonth-17; i++) {
    if((i+17)===currentDate) {
        secondLine += '<div class="current">'+(i+17)+'</div>';
    }
    else {
        secondLine += '<div>'+(i+17)+'</div>';
    }
}

var calendarDiv = document.getElementById("calendar");
calendarDiv.innerHTML = '<div class="firstRow">' + firstLine + '</div>';
calendarDiv.innerHTML += '<div class="secondRow">: ' + secondLine + '</div>';
calendarDiv.innerHTML = calendarDiv.innerHTML.replace(':', '');