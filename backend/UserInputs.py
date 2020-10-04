# User input class, to be used across all files
import os


class UserInputs():
    """
    A class which allows the user to select type of input, which
    text-summarization techniques to use, and parameters to specify output
    form and type.
    """

    # output can be pdf or txt file
    # pdf is the only file format accepted right now
    output_type = "pdf"

    # input type to be adjusted at the beginning of main, can be url, or text
    input_type = ""

    # input itself
    input = ""

    # output, to be filled in by program
    output = ""

    # default number of sentences for the summarization to be
    num_sentences = 0

    # the title of the output PDF
    outputTitle = ""

    # set to be true, can be turned to false by input.txt
    summary = True
    analysis = True

    # generated summary
    summary_results = ""


    # generic file names
    root = os.getcwd() + '/inputFiles/'
    INPUT_FILE = root + 'input.txt'
    INPUT_VARS = root + 'vars.txt'
    INPUT_IMAGE = root + 'input.jpg'
    INPUT_PDF = root + 'input.pdf'
