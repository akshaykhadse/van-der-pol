template = source/report.tex
py_out = vanderpol-1.png vanderpol-2.png getparams.txt
jup_nb = source/van_der_pol.ipynb
py_script = source/van_der_pol.py
note_book = output/153079011.html

.PHONY: clean

output/153079011.pdf: $(template) $(py_out) 153079011.blg 153079011.bbl $(note_book)
	pdflatex -jobname 153079011 $(template)
	pdflatex -jobname 153079011 $(template)
	mv 153079011.pdf output/

$(note_book): $(jup_nb)
	jupyter nbconvert $(jup_nb)
	mkdir -p output
	mv source/van_der_pol.html output/153079011.html

$(py_out): $(py_script)
	python3 $(py_script)

153079011.blg 153079011.bbl: source/references.bib
	pdflatex -jobname 153079011 $(template)
	bibtex 153079011

test: source/tests.py source/van_der_pol.py
	python3 source/tests.py

clean:
	rm -rf *.png *.out *.aux *.toc *.lof *.bbl *.blg *.log *.txt source/__pycache__
	rm -rf output
