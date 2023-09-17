STATIC_DIR=bootstrapsidebar/static

.PHONY: build clean bootstrap


bootstrap:
	cd bootstrap-theme && npm install
	cd bootstrap-theme && npm run build
	cp bootstrap-theme/sidebar-bootstrap.min.* $(STATIC_DIR)/bootstrap
	cp bootstrap-theme/node_modules/bootstrap/dist/js/bootstrap.bundle.min.* $(STATIC_DIR)/bootstrap
	cp -r bootstrap-theme/fonts $(STATIC_DIR)
	cp bootstrap-theme/fonts.css $(STATIC_DIR)/fonts.css

package:
	python3 -m build


clean:
	rm -rf bootstrap-theme/node_modules
	rm -f bootstrap-theme/*.css
	rm -rf bootstrap-theme/fonts
