# ----------------------------------------------------------------------------
# oh-my-fish config
# ----------------------------------------------------------------------------
set fish_path ~/.oh-my-fish
set fish_theme simplevi
set vi_mode_default vi_mode_normal
set fish_plugins vi-mode

# Load oh-my-fish configuration.
. $fish_path/oh-my-fish.fish

# ----------------------------------------------------------------------------
# Environment
# ----------------------------------------------------------------------------
set fish_greeting
set -x ALTERNATE_EDITOR ""
set -x EDITOR emacsclient
if test -z "$TMUX"
  set -x TERM xterm-256color
end