i=1650
j=1700
until [ $i -gt 1850 ]
do
  python3 subset_maker_vrt_variable.py $i $j german_documents
  ((i=i+50))
  ((j=j+50))
done
