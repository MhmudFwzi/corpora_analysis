i=1650

until [ $i -gt 1890 ]
do
  python3 ud-ciep_18thcentury_english.py ../$i con$i -p english en-gum
  ((i=i+50))
done
