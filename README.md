# cross-correlation
A simple python implementation of a discrete cross-correlation like score to assess similarity between raw XRPD patterns. This tool script was applied in the context of XRPD pattern matching in the following paper:
"Can X-ray powder diffraction be a suitable forensic method for illicit drug identification?" (insert citation here)

## usage
place XRPD patterns in ASC format inside of the subdirectory "spectra/", place the known standard in the main directory as "standard.ASC" and use the command
```
python cross3.py
```
This will give the cross-correlation score as defined in the paper of the standard with all the patterns in the "spectra/" folder.
