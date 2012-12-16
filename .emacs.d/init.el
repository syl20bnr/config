(require 'cl)

(defvar user-home-directory
  (expand-file-name (concat user-emacs-directory "../"))
  "The user's home directory.")

(defvar user-projects-dir
  (expand-file-name (concat user-home-directory "Projects/"))
  "The directory containing the user's checked out source code.")

(defvar user-dropbox-directory
  (expand-file-name (concat user-home-directory "Dropbox/"))
  "The user's Dropbox root directory.")

(add-to-list 'load-path user-emacs-directory)

(require 'my-funcs)

;; auto-save
(add-hook 'before-save-hook (lambda () (delete-trailing-whitespace)))
;;number colon mode
(global-linum-mode t)
;;no tool bar
(tool-bar-mode -1)
;; whitespace-mode
(setq-default show-trailing-whitespace t)

;; Config files
(progn
  (setq user-emacs-config-dir (concat user-emacs-directory "config/"))
  (when (file-exists-p user-emacs-config-dir)
    (dolist (l (directory-files user-emacs-config-dir nil "^[^#].*el$"))
      (load (concat user-emacs-config-dir l)))))

(require 'my-packages)
(require 'my-keybindings)

