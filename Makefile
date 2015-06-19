.PHONY: clean publish

clean:
	rm -rf build dist schematec.contrib.egg-info

publish:
	git push
	python setup.py bdist_wheel upload
