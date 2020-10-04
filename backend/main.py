from text_pdf_output import create_output
from UserInputs import UserInputs
from textManipulation.summarization import summarize_text, summarize_speech_transcription, summarize_article_text
from inputs.article_scraper import article_or_video, collect_text, url_text_conversion
from inputs.scanned_input import pdf_to_image, image_to_text
import re
import logging


# ignore cpu warnings for tensorflow
# warnings.filterwarnings("ignore")


# fill out the user inputs class with the corresponding values from input file
def initialize_user_inputs(vars, file):
    f = open(vars, "r")

    for i, row in enumerate(f):
        if i == 5:
            UserInputs.num_sentences = int(row[16:]) - 1
        elif i == 6:
            # UserInputs.input_type = str(row[12:])
            # placeholder for now
            UserInputs.input_type = 'text'

    if UserInputs.input_type == 'text' or UserInputs.input_type == 'video' or UserInputs.input_type == 'article':
        f2 = open(file, "r")
        for row in (f2):
            UserInputs.input += str(row[:].encode('latin-1', 'ignore'))
        f2.close
        if UserInputs.input_type == 'article':
            collect_text(UserInputs.input)
        # must be able to read bytes
        f2 = open(file, "r", errors='ignore')
        for row in (f2):
            UserInputs.input += row[:]

        # re.sub("[\(\[].*?[\)\]]", "", UserInputs.input)

    elif UserInputs.input_type == 'pdf':
        image_to_text(pdf_to_image(UserInputs.INPUT_PDF))
        f2 = open(file, "r")
        for row in (f2):
            UserInputs.input += row[:]

    elif UserInputs.input_type == 'image':
        image_to_text(UserInputs.INPUT_IMAGE)
        f2 = open(file, "r")
        for row in (f2):
            UserInputs.input += row[:]


# main function
if __name__ == "__main__":

    # initialize inputs, pulling from user filled out files
    initialize_user_inputs(UserInputs.INPUT_VARS, UserInputs.INPUT_FILE)

    print("______________Elements Initialized!______________")


    # depending on the input type, do the following
    if UserInputs.input_type == "text" or UserInputs.input_type == "pdf" or UserInputs.input_type == "image":
        UserInputs.output, UserInputs.outputTitle = summarize_text(UserInputs.input,
                                            num_sentences = UserInputs.num_sentences)

    elif UserInputs.input_type == "article":
        UserInputs.output, UserInputs.outputTitle = summarize_article_text(UserInputs.input,
                                            num_sentences = UserInputs.num_sentences)

    elif UserInputs.input_type == "video":
        UserInputs.output, UserInputs.outputTitle = summarize_speech_transcription_text(UserInputs.input,
                                            num_sentences = UserInputs.num_sentences)

    else:
        print("Invalid input type entered!")

    # uses UserInputs.ouput to create an output pdf
    create_output()
    print("-----------------------------Output Created-----------------------------")
