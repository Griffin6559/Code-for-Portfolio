const canvas = document.getElementById('drawing-board');
const colorInput = document.getElementById('colorInput');
const clearButton = document.getElementById('clearButton');
const undoButton = document.getElementById('undoButton');
const redoButton = document.getElementById('redoButton');
const saveButton = document.getElementById('finishButton');
const drawButton = document.getElementById('draw');
const eraseButton = document.getElementById('erase');

const guide = document.getElementById("guide");
const ctx = canvas.getContext('2d', { willReadFrequently: true });
const CELL_SIDE_COUNT = 70;
const cellPixelLength = Math.floor(canvas.width / CELL_SIDE_COUNT);
const colorHistory = {};
const toggleGuide = document.getElementById("toggleGuide");
toggleGuide.addEventListener("change", handleToggleGuideChange);


// const COLS = Math.floor(canvas.width / CELL_SIDE_COUNT);
// const ROWS = Math.floor(canvas.height / CELL_SIDE_COUNT);
const COLS = Math.floor(canvas.width / cellPixelLength);
const normalRows = Math.floor(canvas.height / cellPixelLength);
const leftover = canvas.height - (normalRows * cellPixelLength);


const ROWS = leftover > 0 ? normalRows + 1 : normalRows;
const cellWidth = cellPixelLength;
const cellHeight = cellPixelLength;


let isDrawing = false;
let isErasing= false;

//guide
{
    // guide.style.width = `${canvas.width}px`;
    // guide.style.height = `${canvas.height}px`;
    guide.style.display = "grid";

    guide.style.gridTemplateColumns = `repeat(${COLS}, ${cellWidth}px)`;

    //last grid row
    let rowHeights = Array(normalRows).fill(`${cellHeight}px`);
    if (leftover > 0) rowHeights.push(`${leftover}px`);
    guide.style.gridTemplateRows = rowHeights.join(" ");

    guide.innerHTML = "";
    for (let i = 0; i < COLS * ROWS; i++) {
        guide.insertAdjacentHTML("beforeend", "<div></div>");
    }
    guide.classList.remove("hidden");
    toggleGuide.checked = true;
}

function handleToggleGuideChange(e) {
    if (e.target.checked) {
        guide.classList.remove("hidden");
    } else {
        guide.classList.add("hidden");
    }
}

clearButton.addEventListener("click", handleClearButtonCLick);


function handleClearButtonCLick() {
    const yes = confirm("Are you sure you wish to clear the canvas?");
    if (!yes) return;

    ctx.fillStyle = "#ffffff";
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    saveState();
}

drawButton.addEventListener("click", () => {
    isErasing = false;
    drawButton.classList.add("active");
    eraseButton.classList.remove("active");
});

eraseButton.addEventListener("click", () => {
    isErasing = true;
    eraseButton.classList.add("active");
    drawButton.classList.remove("active");
});

function getCellFromEvent(e) {
    const rect = canvas.getBoundingClientRect();
    const x = e.clientX - rect.left;
    const y = e.clientY - rect.top;
    const cellX = Math.floor(x / cellWidth);
    const cellY = Math.floor(y / cellHeight);
    return { cellX, cellY };
}

function fillCell(cellX, cellY) {
    const startX = cellX * cellWidth;
    let startY = cellY * cellHeight;
    let height = cellHeight;

    //last row of grid
    if (cellY === ROWS - 1 && leftover > 0) {
        height = leftover;
        startY = canvas.height - leftover;
    }

    ctx.fillStyle = colorInput.value;
    ctx.fillRect(startX, startY, cellWidth, height);

    colorHistory[`${cellX}_${cellY}`] = colorInput.value;
}

function eraseCell(cellX, cellY) {
    const startX = cellX * cellWidth;
    let startY = cellY * cellHeight;
    let height = cellHeight;

    //last row of grid
    if (cellY === ROWS - 1 && leftover > 0) {
        height = leftover;
        startY = canvas.height - leftover;
    }

    ctx.fillStyle = "#ffffff";
    ctx.fillRect(startX, startY, cellWidth, height);

    colorHistory[`${cellX}_${cellY}`] = colorInput.value;
}
canvas.addEventListener("mousedown", (e) => {
    if (e.button !== 0) return;
    isDrawing = true;
    const { cellX, cellY } = getCellFromEvent(e);

    if (isErasing) {
        eraseCell(cellX, cellY);
    } else {
        fillCell(cellX, cellY);
    }
});

canvas.addEventListener("mousemove", (e) => {
    if (!isDrawing) return;
    const { cellX, cellY } = getCellFromEvent(e);

    if (isErasing) {
        eraseCell(cellX, cellY);
    } else {
        fillCell(cellX, cellY);
    }
});

canvas.addEventListener("mouseup", () => {
    isDrawing = false;
    saveState();
});
canvas.addEventListener("mouseleave", () => {
    isDrawing = false;
    isErasing=false;
});


let undoStack = [canvas.toDataURL()];
let redoStack = [];

function getTopImage() {
    return undoStack[undoStack.length-1]
}

undoButton.addEventListener('click', handleUndo);
redoButton.addEventListener('click', handleRedo);

function saveState() {
    undoStack.push(canvas.toDataURL());
    redoStack = [];
}

function handleUndo() {
    if (undoStack.length > 1) {
        redoStack.push(undoStack.pop());
        restoreFromDataURL(undoStack[undoStack.length - 1]);
    }
}

function handleRedo() {
    if (redoStack.length > 0) {
        const state = redoStack.pop();
        undoStack.push(state);
        restoreFromDataURL(state);
    }
}
function restoreFromDataURL(dataURL) {
    const img = new Image();
    img.src = dataURL;
    img.onload = () => {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        ctx.drawImage(img, 0, 0, canvas.width, canvas.height);
    };
}
saveButton.addEventListener('click', handleSave);


function handleSave(){
    const imageData = ctx.getImageData(0,0,canvas.width,canvas.height);
    const pixelData= imageData.data;
    console.log(pixelData);

    const pixels = Array.from(imageData.data);

    fetch("/save_image_array", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            width: canvas.width,
            height: canvas.height,
            pixels: pixels
        }),
    })
    .then(response => response.json())
    .then(data => {
        console.log("Server response:", data);
    })
    .catch(error => {
        console.error("Error sending image data:", error);
    });
}

//Write this so it reflects drawing on the other side of canvas am
//if (isDrawing && )

// function imageDataURL(canvas) {
//     var canvas2 = document.createElement("canvas");
//     canvas2.width = canvas.width;
//     canvas2.height = canvas.height;

//     var ctx = canvas2.getContext("2d");
//     ctx.drawImage(canvas, 0, 0);


//     var dataURL = canvas.toDataURL("image/png");
//     return dataURL.replace(/^data:image\/(png|jpg);base64,/, "");

// }






