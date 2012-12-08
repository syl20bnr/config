(require 'package)
(setq package-archives '(("ELPA" . "http://tromey.com/elpa/")
                         ("gnu" . "http://elpa.gnu.org/packages/")
                         ("melpa" . "http://melpa.milkbox.net/packages/")
                         ("marmalade" . "http://marmalade-repo.org/packages/")
                         ("technomancy" . "http://repo.technomancy.us/emacs/")))

;; Various settings
;;number colon mode
(global-linum-mode t)
;;no tool bar
(tool-bar-mode -1)

(package-initialize)

;; colors
(color-theme-initialize)
(color-theme-solarized-dark)

;; evil settings
(evil-mode 1)
;;Make evil-mode up/down operate in screen lines instead of logical lines
(define-key evil-normal-state-map (kbd "j") 'evil-next-visual-line)
(define-key evil-normal-state-map (kbd "k") 'evil-previous-visual-line)
;;Exit insert mode by pressing j and then k quickly
(setq key-chord-two-keys-delay 0.2)
(key-chord-define evil-insert-state-map "jk" 'evil-normal-state)
(key-chord-mode 1)

