[![DOI](https://zenodo.org/badge/310220554.svg)](https://zenodo.org/badge/latestdoi/310220554)

# Validity Check
A simple app to examine attention checks in survey data.

## How to use Validity Check
Validity Check was designed for convenient access to attention checking questions in survey data. In order to gain insights into your attention checks:
1. Run the installer
    1. For Mac, drag the app into your Applications folder when the popup window appears (after opening "ValidityCheck.dmg").
    1. _Coming soon_: Windows and Linux apps.
1. Run Validity Check from your installation location.
1. Open a data file (these must be CSV files, if in another format convert to CSV first).
1. Select any rows you need to delete (especially common with Qualtrics datasets).
    1. If not necessary, feel free to press the "Skip" button to bypass this option.
1. Select the row that has the column headers you will identify your attention-checking questions with.
1. Select the column holding your participants unique identification (typically a coded identifier and not personal information).
1. Select the column that holds any date or time information you would like to use to sort responses by (useful for realtime analysis of data when deciding whether the most recent participants were paying attention).
    1. If not necessary, feel free to press the "Skip" button to bypass this option.
1. Select the questions in your data that are attention checks (by header, selected in step `5.`).
1. Select the correct response to your attention check questions.
    1. These are listed as drop-down menus of all the responses to each question in your dataset.
    1. If you don't see the correct responses listed, type your correct response in and it will be used instead of what's listed.
1. The final report will be displayed, with color-coded cells to dstinguish correct/incorrect responses for each participant (row) with the option to sort by column (by clicking the column headers).
1. These settings can be saved and reused by clicking the "Save Validity Settings" button, and later reopening through the "Open Validity Settings" section of the main window.
    1. The settings are saved to a `.json` file, which can be manually edited if knowledgeable about this format and your dataset.
1. This report can be saved as a CSV data file by clicking the "Export Validity Report" button.

This is a beta release, so feel free to send me questions at [joshua.e.zosky@gmail.com](mailto:joshua.e.zosky@gmail.com).
