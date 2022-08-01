# MZMLSTATISTICS MODEL

## Usage:
`
    python mzml_statistics.py 
        mzml_dataframe 
        --data_folder [-d]
`

## Input
A folder contains mzMLs.

## Output
A CSV contains the mass spectral information required for QC reporting.

|File_Name|SpectrumID|MSLevel|Charge|MS2_peaks|Base_Peak_Intensity|
|---|---:|---:|---:|---:|---:|
|BSA1_F1.mzML|spectrum=1011|1|null|null|null|
|BSA1_F1.mzML|spectrum=1012|1|null|null|null|
|BSA1_F2.mzML|spectrum=3098|2|3|198|662.8287964|
|BSA1_F2.mzML|spectrum=3099|2|2|26|72.35897064|
|...|...|...|...|...|...|


