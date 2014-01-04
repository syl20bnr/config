INSTALL_DIR=~

.PHONY: install
install: clean update

.PHONY: update
 update:
	mkdir -p $(INSTALL_DIR)/.config
	cp -r .config/powerlinerepo $(INSTALL_DIR)/.config
	cp -r .config/ranger $(INSTALL_DIR)/.config
	cp -r .config/solarized $(INSTALL_DIR)/.config
	cp -r .urxvt $(INSTALL_DIR)
	cp -r .vim $(INSTALL_DIR)
	cp _vimrc $(INSTALL_DIR)
	cp _vrapperrc $(INSTALL_DIR)
	cp .minttyrc $(INSTALL_DIR)
	cp .tmux.conf $(INSTALL_DIR)
	cp .Xdefaults $(INSTALL_DIR)
	cp .zshrc $(INSTALL_DIR)

.PHONY: clean
clean:
	rm -rf $(INSTALL_DIR)/.config/powerlinerepo
	rm -rf $(INSTALL_DIR)/.config/ranger
	rm -rf $(INSTALL_DIR)/.config/solarized
	rm -rf $(INSTALL_DIR)/.urxvt
	rm -rf $(INSTALL_DIR)/.vim

