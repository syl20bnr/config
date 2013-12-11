ZSH=$HOME/.oh-my-zsh

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

# Uncomment following line if you want red dots to be displayed while waiting for completion
COMPLETION_WAITING_DOTS="true"
# Set to this to use case-sensitive completion
CASE_SENSITIVE="true"

# Customize to your needs...
export PATH=/home/sbenner/.rbenv/shims:/home/sbenner/.rbenv/bin:/usr/lib/lightdm/lightdm:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games
export GIT_AUTHOR_EMAIL=sylvain.benner@ubisoft.com
export EDITOR=vi

# aliases
alias noproxy='http_proxy= HTTP_PROXY= https_proxy= HTTPS_PROXY='
alias np='noproxy'

source $ZSH/oh-my-zsh.sh

# Always launch a ranger session
if [[ $RANGER == "" ]]; then
  export RANGER=1
  ranger "`pwd`"
fi

# Some doc

# Example aliases
# alias zshconfig="mate ~/.zshrc"
# alias ohmyzsh="mate ~/.oh-my-zsh"

# Comment this out to disable bi-weekly auto-update checks
# DISABLE_AUTO_UPDATE="true"

# Uncomment to change how many often would you like to wait before auto-updates occur? (in days)
# export UPDATE_ZSH_DAYS=13

# Uncomment following line if you want to disable colors in ls
# DISABLE_LS_COLORS="true"

# Uncomment following line if you want to disable autosetting terminal title.
# DISABLE_AUTO_TITLE="true"
