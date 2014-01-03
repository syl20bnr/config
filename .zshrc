ZSH=$HOME/.oh-my-zsh

# ----------------------------------------------------------------------------
# Prompt
# ----------------------------------------------------------------------------
if [[ $EMACS == "" ]]; then
  # regular mode
  ZSH_THEME="syl20bnr"
  plugins=(git vi-mode)
else
  # runs inside an emacs process
  ZSH_THEME="robbyrussell"
  chpwd() { print -P "\033AnSiTc %d" }
  print -P "\033AnSiTu %n"
  print -P "\033AnSiTc %d"
fi


# ----------------------------------------------------------------------------
# Environment
# ----------------------------------------------------------------------------
export PATH=\
/home/sbenner/.rbenv/shims:\
/home/sbenner/.rbenv/bin:\
/usr/lib/lightdm/lightdm:\
/usr/local/sbin:\
/usr/local/bin:\
/usr/sbin:/usr/bin:\
/sbin:/bin:/usr/games
export GIT_AUTHOR_EMAIL=sylvain.benner@gmail.com
export EDITOR=vi
if [[ -z "$TMUX" ]]; then
  export TERM=xterm-256color
fi

# ----------------------------------------------------------------------------
# oh my zsh settings
# ----------------------------------------------------------------------------
source $ZSH/oh-my-zsh.sh
# red dots while waiting for completion
COMPLETION_WAITING_DOTS="true"
# case-sensitive completion
CASE_SENSITIVE="true"
# wait before auto-updates occur
export UPDATE_ZSH_DAYS=31

# ----------------------------------------------------------------------------
# aliases
# ----------------------------------------------------------------------------
alias noproxy='http_proxy= HTTP_PROXY= https_proxy= HTTPS_PROXY='
alias np='noproxy'

# ----------------------------------------------------------------------------
# Ranger auto launch
# ----------------------------------------------------------------------------
#if [[ $RANGER == "" ]]; then
#  export RANGER=1
#  ranger "`pwd`"
#fi

