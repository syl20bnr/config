# ----------------------------------------------------------------------------
# oh-my-fish config
# ----------------------------------------------------------------------------
set fish_path ~/.oh-my-fish
set fish_theme syl20bnr

# Load oh-my-fish configuration.
. $fish_path/oh-my-fish.fish

function my_fish_key_bindings
  fish_vi_key_bindings
  set fish_bind_mode default
  bind -M insert -m default \n execute
  bind \co 'ranger-cd ; fish_prompt'  
end
set fish_key_bindings my_fish_key_bindings

# for mac port
set -xg PATH /opt/local/bin /opt/local/sbin $PATH

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
# force english language
alias git='env LC_ALL=en_US git'