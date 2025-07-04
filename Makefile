STATIC_DIR=bootstrapsidebar/static

.PHONY: build clean bootstrap
PY=.venv/bin/python


bootstrap:
	cd bootstrap-theme && npm install
	cd bootstrap-theme && npm run build
	cp bootstrap-theme/build/*.css $(STATIC_DIR)/bootstrap
	cp bootstrap-theme/node_modules/bootstrap/dist/js/bootstrap.bundle.min.* $(STATIC_DIR)/bootstrap
	cp -r bootstrap-theme/build/fonts $(STATIC_DIR)
	# For compatibility with old versions
	cp bootstrap-theme/build/fonts.css $(STATIC_DIR)/fonts.css

package: .venv
	$(PY) -m build

.venv:
	python3 -m venv .venv
	.venv/bin/pip install --upgrade pip
	.venv/bin/pip install build twine

clean:
	rm -rf bootstrap-theme/node_modules
	rm -f bootstrap-theme/*.css
	rm -rf bootstrap-theme/fonts
	rm -f $(STATIC_DIR)/bootstrap/*.css
	rm -f $(STATIC_DIR)/static/bootstrap/*.js
	rm -f $(STATIC_DIR)/static/fonts.css
	rm -rf .venv
