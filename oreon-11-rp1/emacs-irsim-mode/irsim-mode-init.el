;; Init file for irsim mode
(autoload 'irsim-mode "irsim-mode" nil t)
(setq auto-mode-alist
      (cons '("\\.sim$" . irsim-mode) auto-mode-alist))
(setq auto-mode-alist
      (cons '("\\.cmd$" . irsim-mode) auto-mode-alist))
(setq auto-mode-alist
      (cons '("\\.out$" . irsim-mode) auto-mode-alist))
(setq auto-mode-alist
      (cons '("\\.flt$" . irsim-mode) auto-mode-alist))