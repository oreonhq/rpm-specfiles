(autoload 'hcl-mode "hcl-mode" "\
Major mode for editing hcl configuration file

\(fn)" t nil)

(add-to-list 'auto-mode-alist '("\\.hcl\\'" . hcl-mode))

(add-to-list 'auto-mode-alist '("\\.nomad\\'" . hcl-mode))
