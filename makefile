report.pdf: report.tex vanderpol-1.png vanderpol-2.png getparams.txt report.blg report.bbl
	pdflatex report.tex
	pdflatex report.tex

vanderpol-1.png vanderpol-2.png getparams.txt: van_der_pol.py
	python3 van_der_pol.py

report.blg report.bbl: references.bib
	pdflatex report.tex
	bibtex report

clean:
	rm -rf *.png *.out *.pdf *.aux *.toc *.lof *.bbl *.blg *.log *.txt
