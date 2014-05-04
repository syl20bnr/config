# ----------------------------------------------------------------------------
# oh-my-fish config
# ----------------------------------------------------------------------------
set fish_path ~/.oh-my-fish
set fish_theme syl20bnr
set vi_mode_default vi_mode_normal
set fish_plugins vi-mode

function vi_mode_user_key_bindings
    bind \co 'ranger-cd ; fish_prompt'  
end

# Load oh-my-fish configuration.
. $fish_path/oh-my-fish.fish

# ----------------------------------------------------------------------------
# Environment
# ----------------------------------------------------------------------------
set fish_greeting
set -x ALTERNATE_EDITOR ""
set -x EDITOR et
if test -z "$TMUX"
  set -x TERM xterm-256color
end

# ----------------------------------------------------------------------------
# aliases
# ----------------------------------------------------------------------------
alias np=noproxy