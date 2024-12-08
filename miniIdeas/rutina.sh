
echo "spune mi fisierul: "
read fisier

cat $fisier

git add $fisier
git commit -m "some commits to file $fisier"
git branch -M main
git push -u origin main
