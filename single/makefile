all: plot.pdf

clean:
	rm data.txt mean.txt spread.txt plot.pdf

data.txt: make_data.py
	python make_data.py

mean.txt: mean.py data.txt
	python mean.py

spread.txt: spread.py data.txt
	python spread.py

plot.pdf: plot.py mean.txt spread.txt data.txt
	 python plot.py