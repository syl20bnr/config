(require 'package)
(setq package-archives '(("ELPA" . "http://tromey.com/elpa/")
                         ("gnu" . "http://elpa.gnu.org/packages/")
                         ("melpa" . "http://melpa.milkbox.net/packages/")
                         ("marmalade" . "http://marmalade-repo.org/packages/")
                         ("melpa" . "http://melpa.milkbox.net/packages/")
                         ("technomancy" . "http://repo.technomancy.us/emacs/")))
(package-initialize)

;; Various settings
;;number colon mode
(global-linum-mode t)
;;no tool bar
(tool-bar-mode -1)

;; colors
(color-theme-initialize)
    (color-theme-solarized-dark)

;; whitespace-mode
(setq-default show-trailing-whitespace t)

;; draw 80th column
(require 'fill-column-indicator)
(fci-mode 1)
(setq fci-rule-column 80)
(setq fci-rule-width 2)
(setq fci-rule-color "#073642") ;; color for dark solarized

;; evil settings
(evil-mode 1)
    ;;Make evil-mode up/down operate in screen lines instead of logical lines
    (define-key evil-normal-state-map (kbd "j") 'evil-next-visual-line)
    (define-key evil-normal-state-map (kbd "k") 'evil-previous-visual-line)
    ;;Exit insert mode by pressing j and then k quickly
    (setq key-chord-two-keys-delay 0.2)
    (key-chord-define evil-insert-state-map "jk" 'evil-normal-state)
    (key-chord-mode 1)

;; parens management
(global-rainbow-delimiters-mode)
(show-paren-mode 1)
    (require 'paren)
    (set-face-background 'show-paren-match-face "#000")
    (set-face-attribute 'show-paren-match-face nil :weight 'extra-bold)

;; erlang
(require 'erlang-start)
(add-to-list 'auto-mode-alist '("\\.erl?$" . erlang-mode))
(add-to-list 'auto-mode-alist '("\\.hrl?$" . erlang-mode))
(setq erlang-root-dir "/usr/local/lib/erlang/erts-5.9.2")
(add-to-list 'exec-path "/usr/local/lib/erlang/erts-5.9.2/bin")
(setq erlang-man-root-dir "/usr/local/lib/erlang/erts-5.9.2/man")

