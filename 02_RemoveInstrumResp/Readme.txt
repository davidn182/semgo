For Instrument correction:

1. Give the mseed data folder path in line 3 of Run4All.bat. (for example, .\Data\001* or .\Data\*.mseed)
2. Provide equipment specs in line 49 of DoInstrumentCor.py (gain, poles, zeros, sensitivity).
   The specs of the equipment used in Kwintsheul are already set in the script.
3. You can change filtering parameters of the applied pre-filtering in line 59 of DoInstrumentCor.py.
4. You run Run4All.bat through a terminal. Corrected files are created inside the same folder with a -cor added to their names.