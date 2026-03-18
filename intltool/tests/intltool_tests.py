#!/usr/bin/python3

import logging
import subprocess
from difflib import Differ

logging.basicConfig(level=logging.INFO)


COMMANDS = [
        "intltool-extract",
        "intltool-merge"
    ]
INPUT_FILE = "cases/context.xml.in"


def test_intltool_installation(cmd: str):
    """
    Check if intltool is installed correctly
    """
    try:
        intltool_cmd = subprocess.Popen([cmd], stdout=subprocess.PIPE)
        intltool_cmd_execution_response = intltool_cmd.communicate()
        assert "Usage" in str(intltool_cmd_execution_response)
    except FileNotFoundError:
        logging.error(f"Either {cmd} is not installed or not accessible.")
    except OSError:
        logging.error(f"Some OSError occurred while executing {cmd}")
    except AssertionError:
        logging.error(f"[CMD] output does not include text: Usage.")
    else:
        logging.info(f"Execution of {cmd} succeed. Test Passed.")


def test_intltool_extract(cmd, input_file):
    """
    Check intltool extract behavior
    """
    try:
        intltool_extract = subprocess.Popen(
            [cmd, "--type=gettext/xml", input_file, "--update"],
            stdout=subprocess.PIPE)
        intltool_extract_execution_response = intltool_extract.communicate()
        assert "Wrote" in str(intltool_extract_execution_response)
    except AssertionError:
        logging.error(f"Writing output file for {input_file} file failed.")
    except Exception as e:
        logging.error(e)
    else:
        logging.info(f"Writing output file for {input_file} succeed.")

    comparison_test_pass = True
    with open("{}.h".format(input_file)) as output_file, open("results/{}.h".format("context.xml.in")) as refer_file:
        differ = Differ()
        for line in differ.compare(output_file.readlines(), refer_file.readlines()):
            if line.startswith("+") or line.startswith("-"):
                comparison_test_pass = False

    try:
        assert comparison_test_pass
    except AssertionError:
        logging.error("Extracted file does NOT match with the result. Test failed.")
    else:
        logging.info("Extracted file does match with the result. Test passed.")


def test_intltool_merge(cmd, input_file):
    """
    Check intltool merge behavior
    """
    merged_file = "context.xml"
    try:
        intltool_merge = subprocess.Popen(
            [cmd, "-o", "cases", input_file, "cases/{}".format(merged_file)],
            stdout=subprocess.PIPE)
        intltool_merge_execution_response = intltool_merge.communicate()
        assert "Merging" in str(intltool_merge_execution_response)
    except AssertionError:
        logging.error(f"Writing output file for {input_file} file failed.")
    except Exception as e:
        logging.error(e)
    else:
        logging.info(f"Writing output file for {input_file} succeed.")

    comparison_test_pass = True
    with open("cases/{}".format(merged_file)) as output_file, open("results/{}".format(merged_file)) as refer_file:
        differ = Differ()
        for line in differ.compare(output_file.readlines(), refer_file.readlines()):
            if line.startswith("+") or line.startswith("-"):
                comparison_test_pass = False

    try:
        assert comparison_test_pass
    except AssertionError:
        logging.error("Merged file does NOT match with the result. Test failed.")
    else:
        logging.info("Merged file does match with the result. Test passed.")


if __name__ == "__main__":
    """
    Executes test cases
    """
    logging.info("Executing test cases for Intltool..")
    for CMD in COMMANDS:
        test_intltool_installation(CMD)
    test_intltool_extract(COMMANDS[0], INPUT_FILE)
    test_intltool_merge(COMMANDS[1], INPUT_FILE)
    logging.info("Tests execution of Intltool completed!")
