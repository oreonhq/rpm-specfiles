;;; editorconfig-init.el --- Startup code for EditorConfig plugin
;;
;; Extracted from README.md.  No need to modify the load path since
;; the RPM installs files within the standard site-lisp directory.

(require 'editorconfig)
(editorconfig-mode 1)
