(autoload 'terraform-mode "terraform-mode" "\
Major mode for editing terraform configuration file

\(fn)" t)

(add-to-list 'auto-mode-alist '("\\.t\\(f\\(vars\\)?\\|ofu\\)\\'" . terraform-mode))

(register-definition-prefixes "terraform-mode" '("terraform-"))
