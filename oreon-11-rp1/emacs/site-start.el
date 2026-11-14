;;; site-start.el --- loaded before user's ".emacs" file and default.el -*- lexical-binding: t -*-

;;; Commentary:
;;
;; Load *.el and *.elc in /usr/share/emacs/site-lisp/site-start.d on startup

;;; Code:

(dolist
    (file
     (delete-dups
      (mapcar 'file-name-sans-extension
              (directory-files
               "/usr/share/emacs/site-lisp/site-start.d" t "\\.elc?\\'"))))
  (let ((inhibit-message t))
    (load file nil nil nil t)))

;;; site-start.el ends here
