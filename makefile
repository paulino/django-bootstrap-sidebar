STATIC_DIR=bootstrapsidebar/static

.PHONY: build clean bootstrap


bootstrap:
	cd bootstrap-theme && npm install
	cd bootstrap-theme && npm run build
	cp bootstrap-theme/sidebar-bootstrap.css $(STATIC_DIR)/bootstrap
	cp bootstrap-theme/sidebar-bootstrap.css.map $(STATIC_DIR)/bootstrap
	cp bootstrap-theme/node_modules/bootstrap/dist/js/bootstrap.bundle.* $(STATIC_DIR)/bootstrap
	cp -r bootstrap-theme/fonts $(STATIC_DIR)
	cp bootstrap-theme/google-fonts-*.css $(STATIC_DIR)/fonts.css

package:
	python3 -m build


clean:
	rm -rf bootstrap-theme/node_modules
	rm -f bootstrap-theme/fonts.css
	rm -f bootstrap-theme/google-fonts*.css
	rm -fr bootstrap-theme/fonts
