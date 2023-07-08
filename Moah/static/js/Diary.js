// function DateChange() {
//   var elements = document.getElementsByClassName('Date-list-circle');
//   for (var i = 0; i < elements.length; i++) {
//     var element = elements[i];
//     if (element === event.target) {
//       // 클릭된 요소에 대해서만 CSS를 변경합니다.
//       element.style.background = 'var(--1, linear-gradient(180deg, #FF9F9F 0%, #FFBFBF 100%))';
//       element.style.boxShadow = '4px 4px 4px 0px rgba(0, 0, 0, 0.15) inset';
//     } else {
//       // 다른 요소들은 이전의 CSS 유지합니다.
//       element.style.background = '';
//       element.style.boxShadow = '';
//     }
//   }
// }

//공개 비공개 토글 버튼
function nextWriting() {
  window.location = "/Diary/Diary-Writing.html";
}

function toggleVisibility(option) {
  var publicLabel = document.querySelector('label[for="public"]');
  var privateLabel = document.querySelector('label[for="private"]');

  if (option === "public") {
    publicLabel.style.color = "#434343";
    privateLabel.style.color = "#848484";
  } else if (option === "private") {
    publicLabel.style.color = "#848484";
    privateLabel.style.color = "#434343";
  }
}

//textarea 자동 높이 조절
const DEFAULT_HEIGHT = 250;

const $textarea = document.querySelector("#content");

$textarea.oninput = (event) => {
  const $target = event.target;

  $target.style.height = 0;
  $target.style.height = DEFAULT_HEIGHT + $target.scrollHeight + "px";
};

function checkInput() {
  var titleInput = document.getElementById("title");
  var savedBtn = document.getElementById("savedBtn");
  var saveBtnImg = document.querySelector("#savedBtn img");

  if (titleInput.value.trim() !== "") {
    savedBtn.disabled = false;
    saveBtnImg.src = "/image/Diary-saveBtn-hover.svg"; // 활성화 상태 이미지 소스
  } else {
    savedBtn.disabled = true;
    saveBtnImg.src = "/image/Diary-saveBtn.svg"; // 비활성화 상태 이미지 소스
  }
}
