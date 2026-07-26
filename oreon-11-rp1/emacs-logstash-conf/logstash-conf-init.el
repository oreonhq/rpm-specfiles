(autoload 'logstash-conf-mode "logstash-conf" "\
Major mode for editing logstash configuration files.

\\{logstash-conf-mode-map\\}

\(fn)" t nil)

(add-to-list 'auto-mode-alist '("\\.logstash\\'" . logstash-conf-mode))

(add-to-list 'interpreter-mode-alist '("logstash" . logstash-conf-mode))

(if (fboundp 'register-definition-prefixes) (register-definition-prefixes "logstash-conf" '("logstash-")))
