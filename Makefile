STATIC_DIR=bootstrapsidebar/static

.PHONY: build clean bootstrap
PY=.venv/bin/python


bootstrap:
	[ -d bootstrap-theme/build ] || mkdir -p bootstrap-theme/build
	cd bootstrap-theme && npm install
	cd bootstrap-theme && npm run build
	cp bootstrap-theme/node_modules/bootstrap/dist/js/bootstrap.bundle.min.* $(STATIC_DIR)/bootstrap
	cp bootstrap-theme/build/sidebar-bootstrap.min.css* $(STATIC_DIR)/bootstrap
	cp bootstrap-theme/build/bootstrapsidebar-fonts.min.css* $(STATIC_DIR)
	cp -r bootstrap-theme/build/fonts $(STATIC_DIR)

package: .venv
	$(PY) -m build

.venv:
	python3 -m venv .venv
	.venv/bin/pip install --upgrade pip
	.venv/bin/pip install build twine

clean:
	rm -rf bootstrap-theme/node_modules
	rm -rf bootstrap-theme/build
	rm -f $(STATIC_DIR)/bootstrap/*.css*
	rm -f $(STATIC_DIR)/bootstrap/*.js*
	rm -f $(STATIC_DIR)/bootstrapsidebar-fonts.css*
	rm -f $(STATIC_DIR)/fonts/*.woff2
	rm -rf .venv
