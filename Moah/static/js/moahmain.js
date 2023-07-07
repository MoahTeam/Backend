//main-Frame: hamburger-menu-js

document.addEventListener("DOMContentLoaded", function () {
    var hamburgerMenu = document.querySelector(".hamburger-menu");
    var menu = document.querySelector(".menu");

    hamburgerMenu.addEventListener("click", function () {
        menu.classList.toggle("show");
    });
});

// 시간 함수
var today = new Date();
var year = today.getFullYear();
var month = String(today.getMonth() + 1).padStart(2, '0');
var day = String(today.getDate()).padStart(2, '0');
var formattedDate = year + "." + month + "." + day;

var dateElement = document.querySelectorAll(".date");
if (dateElement) {
    dateElement.forEach(function (dateElement) {
        dateElement.textContent = formattedDate;
    });
}

// 할 일 체크 함수
function toggleTask(element) {
    element.classList.toggle('checked');
}

// 메인 페이지 Todo 배열 함수 (3개가 넘어가면 다음줄로 넘어가게 하고 싶었는데 안됨)
// function arrangeMainTodoItems() {
//     var container = document.getElementsByClassName("toDoTaskList");
//     var items = container.querySelectorAll("li");

//     var itemsPerRow = 3;
//     var currentItems = 0;

//     for (var i = 0; i < items.length; i++) {
//         if (currentItems >= itemsPerRow) {
//             items[i].style.clear = "left";
//             currentItems = 0;
//         }
//         currentItems++;
//     }
// }
// arrangeMainTodoItems();

// 메인 페이지에서 To do 화면 나타내기
document.getElementById("TodoBoxId").style.display = "none";
function toggleTodoBox() {
    var todoBox = document.getElementById("TodoBoxId");
    var allBox = document.getElementById('AllBoxId');
    var diaryBox = document.getElementById('DiaryBoxId');
    if (todoBox.style.display === 'none') {
        todoBox.style.display ='block';
        allBox.style.display = 'none';
        diaryBox.style.display = 'none';
    }
    else {
        todoBox.style.display = 'none';
        allBox.style.display = 'flex';
    }
}

// 메인 페이지에서 Diary 화면 나타내기
document.getElementById("DiaryBoxId").style.display = "none";
function toggleDiaryBox() {
    var diaryBox = document.getElementById("DiaryBoxId");
    var allBox = document.getElementById("AllBoxId");
    var todoBox = document.getElementById("TodoBoxId");
    if(diaryBox.style.display === 'none') {
        diaryBox.style.display = 'block';
        allBox.style.display = 'none'
        todoBox.style.display = 'none';
    }
    else {
        diaryBox.style.display = 'none';
        allBox.style.display = 'flex';
    }
}

// littleMenuBox 나타내기
function toggleAllBox() {
    var todoBox = document.getElementById("TodoBoxId");
    var allBox = document.getElementById('AllBoxId');
    var diaryBox = document.getElementById('DiaryBoxId');
    if (allBox.style.display === 'none') {
        todoBox.style.display ='none';
        diaryBox.style.display = 'none';
        allBox.style.display = 'flex';
    }
    else {
        todoBox.style.display = 'none';
        diaryBox.style.display = 'none';
        allBox.style.display = 'flex';
    }
}