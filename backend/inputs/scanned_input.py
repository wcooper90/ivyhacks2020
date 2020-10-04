import cv2
import pytesseract
from pdf2image import convert_from_path, convert_from_bytes
from UserInputs import UserInputs
import os


def pdf_to_image(inputFile):
    return convert_from_path(os.path.abspath(os.path.join(os.getcwd(), os.pardir)) + '/project/' + inputFile)


def image_text_conversion(image):
    # from https://www.geeksforgeeks.org/text-detection-and-extraction-using-opencv-and-ocr/

    # Read image from which text needs to be extracted
    returned_text = ""

    img = cv2.imread(image)
    # Preprocessing the image starts

    # Convert the image to gray scale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Performing OTSU threshold
    ret, thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)

    # Specify structure shape and kernel size.
    # Kernel size increases or decreases the area
    # of the rectangle to be detected.
    # A smaller value like (10, 10) will detect
    # each word instead of a sentence.
    rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (18, 18))

    # Appplying dilation on the threshold image
    dilation = cv2.dilate(thresh1, rect_kernel, iterations = 1)

    # Finding contours
    contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL,
                                                     cv2.CHAIN_APPROX_NONE)
    # Creating a copy of image
    im2 = img.copy()

    # A text file is created and flushed
    file = open("recognized.txt", "w+")
    file.write("")
    file.close()



    # delete contents from input file originally
    raw = open(UserInputs.INPUT_FILE, "r+")
    contents = raw.read().split("\n")
    raw.seek(0)
    raw.truncate()

    # Looping through the identified contours
    # Then rectangular part is cropped and passed on
    # to pytesseract for extracting text from it
    # Extracted text is then written into the text file
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)

        # Drawing a rectangle on copied image
        rect = cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Cropping the text block for giving input to OCR
        cropped = im2[y:y + h, x:x + w]

        # Open the file in append mode
        file = open(UserInputs.INPUT_FILE, "ab")

        # Apply OCR on the cropped image
        text = pytesseract.image_to_string(cropped).encode('latin-1', 'ignore')

        returned_text += text

        # Appending the text into file
        file.write(text)
        # file.write("\n")

        # Close the file
        file.close

    return returned_text
