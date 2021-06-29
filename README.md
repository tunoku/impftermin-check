# impftermin-check
This (rudimentary) script checks if there are any vaccination offer to you on impfterminservice.de and gives a pop-up once at least one offer is available.

For this you need to provide a "Vermittlungscode" (In the format XXXX-XXXX-XXXX) and the information about your "Impfzentrum" (By providing PLZ and Impfzentrum-Code to replace the X's in the following URL: https://XXX-iz.impfterminservice.de/impftermine/service?plz=XXXXX)



# Installation
Setup and activate a conda environment with the required dependencies with the following command.

```
conda env create -f environment.yml
conda activate impf_termin_check
```

Additionally you will need ChromeDriver and make it executable (e.g. on Windows by adding it to PATH).
More information and download links can be found in the following link: https://chromedriver.chromium.org/

You might need to restart your terminal/IDE after this process.

# Running 

Please fill in the information regarding your Vermittlungscode and the Impfzentrum you want to look for appointments in the main.py script.

Then you can run the impftermin-check by running:
```
python main.py
```
