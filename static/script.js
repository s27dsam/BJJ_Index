// static/script.js
// Get elements
const moreInfoBtn = document.getElementById('moreInfoBtn');
const sourcesBtn = document.getElementById('sourcesBtn');
const closeMoreInfo = document.getElementById('closeMoreInfo');
const closeSources = document.getElementById('closeSources');
const moreInfoPanel = document.getElementById('moreInfoPanel');
const sourcesPanel = document.getElementById('sourcesPanel');
const overlay = document.getElementById('overlay');

// Function to open a panel
function openPanel(panel) {
    panel.style.width = '300px';
    overlay.style.display = 'block';
}

// Function to close all panels
function closePanels() {
    moreInfoPanel.style.width = '0';
    sourcesPanel.style.width = '0';
    overlay.style.display = 'none';
}

// Event listeners
moreInfoBtn.addEventListener('click', (e) => {
    e.preventDefault();
    openPanel(moreInfoPanel);
});

sourcesBtn.addEventListener('click', (e) => {
    e.preventDefault();
    openPanel(sourcesPanel);
});

closeMoreInfo.addEventListener('click', closePanels);
closeSources.addEventListener('click', closePanels);
overlay.addEventListener('click', closePanels);

