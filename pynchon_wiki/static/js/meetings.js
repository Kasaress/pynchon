// Обработчики клика по кнопкам "Мероприятий"
const plannedMeetingsButton = document.getElementById('plannedMeetingsButton');
const pastMeetingsButton = document.getElementById('pastMeetingsButton');
const plannedMeetingsContainer = document.getElementById('plannedMeetingsContainer');
const pastMeetingsContainer = document.getElementById('pastMeetingsContainer');

plannedMeetingsButton.addEventListener('click', function () {
  plannedMeetingsContainer.style.display = 'block';
  pastMeetingsContainer.style.display = 'none';
});
pastMeetingsButton.addEventListener('click', function () {
  plannedMeetingsContainer.style.display = 'none';
  pastMeetingsContainer.style.display = 'block';
});