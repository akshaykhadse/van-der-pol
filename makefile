template = source/report.tex
py_out = vanderpol-1.png vanderpol-2.png getparams.txt
jup_nb = source/van_der_pol.ipynb
py_script = source/van_der_pol.py
note_book = output/van_der_pol.html

.PHONY: clean

report.pdf: $(template) $(py_out) report.blg report.bbl $(note_book)
	pdflatex -jobname 153079011 $(template)
	pdflatex -jobname 153079011 $(template)
	mv 153079011.pdf output/
	
$(note_book): $(jup_nb)
	jupyter nbconvert $(jup_nb)
	mv source/van_der_pol.html output/

$(py_out): $(py_script)
	python3 $(py_script)

report.blg report.bbl: source/references.bib
	pdflatex -jobname 153079011 $(template)
	bibtex 153079011

clean:
	rm -rf *.png *.out *.aux *.toc *.lof *.bbl *.blg *.log *.txt

cleanall: clean
	rm -rf output/*.pdf output/*.html
