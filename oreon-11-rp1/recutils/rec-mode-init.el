;; rec-mode for recfiles

(autoload 'rec-mode "rec-mode" " mode." t)
(add-to-list 'auto-mode-alist '("\\.rec\\(\\.in\\)?$" . rec-mode))
