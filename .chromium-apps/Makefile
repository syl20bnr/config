INSTALL=~/.chromium-apps/
LN=/usr/local/bin/

DEFAULT=freenode       \
        github         \
        gmail          \
        googlegroups   \
        grooveshark    \
        psytrancepower

WORK=stratus-wiki     \
     virga-gitlab     \
     virga-jenkins    \
     virga-portal     \
     virga-quickbuild \
     virga-rb

OBJ_DEFAULT=$(addprefix $(INSTALL),$(DEFAULT))
OBJ_WORK=$(addprefix $(INSTALL),$(WORK))

default: $(OBJ_DEFAULT)

work: default $(OBJ_WORK)

$(INSTALL)% : %
	mkdir -p $(INSTALL)
	cp $< $@
	sudo ln -f -s $@ $(LN)$<

clean:
	rm -rf $(INSTALL)
	sudo rm -rf $(addprefix $(LN),$(DEFAULT))
	sudo rm -rf $(addprefix $(LN),$(WORK))
