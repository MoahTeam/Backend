function DateChange() {
    var DateList = document.getElementsByClassName("Date-list-circle");

    if (DateList.innerHTML === "Jan") {
      DateList.style.background = 'red';
    }
  }