# Sentence Length Analysis Scripts

This is a set of scripts used to separate, preprocess, parse, analyze, and visualize the DTAW and RSC corpora.

## Document Extraction
- These scripts are used to split large files with many documents into many files each with a single document for further processing. 
```
extractdocument-DTAW.py
```
is used to extract German documents from the DTAW corpus.
```
extractdocument-RSC.py
```
is used to extract English documents from the RSC corpus.

## Subset Making
- These scripts are used to group documents that belong to the same time period together by taking period start and end as input.
```
subsetmaker-txt.py
```
is used to create groups of documents which are in txt format.
```
subsetmaker-vrt.py
```
is used to create groups of documents which are in vrt format.
```
subsetmaker-DTAW.sh
```
calls the vrt subset maker many times to create groups from DTAW corpus
```
subsetmaker-RSC.sh
```
calls the vrt subset maker many times to create groups from RSC corpus

## Parsing Scripts
- These scripts are used to parse the documents using the UDPipe parser and generate conllu files with the results.
```
generatemetadatafiles-vrt.py
```
generates metadata files for RSC used for further processing.
```
readfromxml-RSC.py
```
parses RSC documents and generates the relevant conllu file.
```
ud-english.py
```
is used to parse any English dataset in the vrt proper format.
```
ud-german.py
```
is used to parse any German dataset in the vrt proper format.
```
parse-RSC.sh
```
is used to parse documents of RSC in groups and create a separate conllu file for each group.
```
fixacl-DTAW.sh
```
applies a German grammar rule that is valid in all cases and doesn't need to be learnt.

## Dependency Length Calculations
- These scripts are used to calculate some metrics related to dependency length.
```
splitfilestosentences-tsv.py
```
splits tsv files into sentences for further processing.
```
calculatedependencylength-vrt.py
```
calculates and adds the required metrics to the conllu files.

## Random Sampling
- These scripts are used to create random samples of the large conllu files for manual validation and investigation.
```
simplerandomsampler.py
```
creates samples from small conllu files.
```
randomsampler.py
```
creates samples from large conllu files in a memory-efficient manner (suitable for non powerful machines).

## Visualization
- These scripts are used to visualize some results.
```
excel_data.py
```
The p-values in a pythonic data structure.
```
heat_map.py
```
creates the heat map visualization for a given result matrix.
```
loop.py
```
creates the heat map visualization for all result matrices.
