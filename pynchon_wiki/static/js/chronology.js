const moreBtns = document.querySelectorAll('.chronology-description__fact-btn');
const chronologyDescriptions = document.querySelectorAll('.chronology-description__fact-text');

function showMore(event) {
  const btn = event.target;
  const fact = btn.closest('.chronology-description__fact');
  const factText = fact.querySelector('.chronology-description__fact-text');

  factText.classList.remove('chronology-description__fact-text_short');
  btn.style.display = 'none';
}

moreBtns.forEach(btn => {
  btn.addEventListener('click', showMore);
});