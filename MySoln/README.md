# Hootsuite Owl Dev Puzzle Soln

This is my soln to the Hootsuite puzzle that can be found [here](https://github.com/WongMatthew/OwlDevPuzzle/tree/master/OriginalPuzzle)

Note: The file ENCRYPTED file is the original Hootsuite puzzle's README file with the header removed

## Explanation

* My Soln opens the ENCRYPTED file (Line 5), takes its contents (Line 6), then closes it (Line 9)
* Using the contents and the base64 package, decodes the contents in base64 (Line 12)
* Makes a list of all uppercase characters (Line 15)
* Finds and adds all uppercase characters in the decoded contents to the list (Line 18-20)
* Using the uppercase characters found and the CaeserCipher package, decodes the uppercase characters with an offset of 1 (Line 23)
* Prints soln (Line 24)

