INSTALL_DIR=~

.PHONY: install
install: clean update

.PHONY: update
 update: symlinks
	mkdir -p $(INSTALL_DIR)/.config
	cp -r .config/fish $(INSTALL_DIR)/.config
	cp -r .config/powerlinerepo $(INSTALL_DIR)/.config
	cp -r .config/ranger $(INSTALL_DIR)/.config
	cp -r .config/solarized $(INSTALL_DIR)/.config
	cp -r .oh-my-fish $(INSTALL_DIR)
	cp -r .scripts $(INSTALL_DIR)
	cp -r .urxvt $(INSTALL_DIR)
	cp -r .vim $(INSTALL_DIR)
	cp .minttyrc $(INSTALL_DIR)
	cp .tmux.conf $(INSTALL_DIR)
	cp _vimrc $(INSTALL_DIR)
	cp _vrapperrc $(INSTALL_DIR)
	cp .Xdefaults $(INSTALL_DIR)
	cp .zshrc $(INSTALL_DIR)

.PHONY: symlinks
symlinks:
	ln --force $(HOME)/.scripts/emacsclientc.sh /usr/local/bin/ec
	ln --force $(HOME)/.scripts/emacsclientt.sh /usr/local/bin/et

.PHONY: clean
clean:
	rm -rf $(INSTALL_DIR)/.config/fish/functions
	rm -rf $(INSTALL_DIR)/.config/powerlinerepo
	rm -rf $(INSTALL_DIR)/.config/solarized
	rm -rf $(INSTALL_DIR)/.oh-my-fish
	rm -rf $(INSTALL_DIR)/.urxvt
	rm -rf $(INSTALL_DIR)/.vim
	rm -rf /usr/local/bin/ec
	rm -rf /usr/local/bin/et
# do no clean
#	rm -rf $(INSTALL_DIR)/.config/ranger
