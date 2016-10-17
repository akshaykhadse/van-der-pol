template = report.tex
py_out = vanderpol-1.png vanderpol-2.png getparams.txt
jup_nb = van_der_pol.ipynb
py_script = van_der_pol.py

.PHONY: clean

report.pdf: $(template) $(py_out) report.blg report.bbl note_book
	pdflatex $(template)
	pdflatex $(template)
	
note_book: $(jup_nb)
	jupyter nbconvert $(jup_nb)

$(py_out): $(py_script)
	python3 $(py_script)

report.blg report.bbl: references.bib
	pdflatex $(template)
	bibtex report

clean:
	rm -rf *.png *.out *.aux *.toc *.lof *.bbl *.blg *.log *.txt

cleanall: clean
	rm -rf *.pdf *.html
