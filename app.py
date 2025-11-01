from flask import Flask, render_template, request, redirect, session, url_for, jsonify
import base64
import numpy as np
import cv2

app=Flask(__name__)




@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route("/design", methods=["GET", "POST"])
def design():
    return render_template("design.html")

@app.route("/save_image_array", methods=["POST"])
def save_image_array():
    data = request.get_json()

    width = data["width"]
    height = data["height"]
    pixels = np.array(data["pixels"], dtype=np.uint8)

    image_array = pixels.reshape((height, width, 4))


    rgb = cv2.cvtColor(image_array, cv2.COLOR_RGBA2RGB)
    gray = cv2.cvtColor(rgb, cv2.COLOR_RGB2GRAY)
    blurred = cv2.GaussianBlur(gray, (3, 3), 0)

    _, thresh = cv2.threshold(
        blurred, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU
    )
    cv2.imwrite("debug_thresh.png", thresh)

    contours, _ = cv2.findContours(
        thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )

    shapes = []

    for contour in contours:
        if cv2.contourArea(contour) < 100:
            continue

        peri = cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, 0.04 * peri, True)
        vertices = len(approx)

        shape_type = "unidentified"
        if vertices == 3:
            shape_type = "triangle"
        elif vertices == 4:
            x, y, w, h = cv2.boundingRect(approx)
            ar = w / float(h)
            shape_type = "square" if 0.95 <= ar <= 1.05 else "rectangle"
        elif vertices > 5:
            shape_type = "circle"
        else:
            area = cv2.contourArea(contour)
            circularity = 4 * np.pi * (area / (peri * peri))
            shape_type = "circle" if circularity > 1.8 else "oval"

        shapes.append(shape_type)

    print(shapes)
    debug_img = rgb.copy()
    cv2.drawContours(debug_img, contours, -1, (0, 255, 0), 2)
    cv2.imwrite("debug_contours.png", debug_img)

    return jsonify({
        "status": "success",
        "shape_count": len(shapes),
        "shapes_found": shapes
    })





if __name__ == "__main__":
    app.run()
