To produce a handout use the command:

jupyter nbconvert file.ipynb --to slides --reveal-prefix=https://cdnjs.cloudflare.com/ajax/libs/reveal.js/3.5.0

Open resulting slides.html file in browser

Then modify html to remove !important; color:#000 and save (MS: I did not have to do this)

Point browser to .html?print-pdf#/

In browser print set to landscape and paper US letter. Then save as PDF - should be colour and 1 slide per page.