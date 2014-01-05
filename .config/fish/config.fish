# ----------------------------------------------------------------------------
# Environment
# ----------------------------------------------------------------------------
set fish_greeting ""
set --export EDITOR vi

# ----------------------------------------------------------------------------
# Prompt
# ----------------------------------------------------------------------------
. ~/.config/fish/functions/vi-mode.fish

function fish_user_key_bindings
  __vi_mode_normal
end

function fish_prompt -d "Write out the prompt"
  printf '%s@%s%s%s%s [%s]> ' (whoami) (hostname|cut -d . -f 1) (set_color $fish_color_cwd) (prompt_pwd) (set_color normal) $vi_mode
end
