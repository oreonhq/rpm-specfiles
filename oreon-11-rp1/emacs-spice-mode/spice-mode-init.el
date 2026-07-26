;init file for spice-mode
(autoload 'spice-mode "spice-mode" "Spice Editing Mode" t)
(custom-set-variables
  '(spice-simulator "Gnucap")                        ;; default simulator
  '(spice-waveform-viewer "Gwave")                   ;; default waveform 
  '(spice-output-local "Gnucap")
)
(setq auto-mode-alist (append (list (cons "\\.sp$" 'spice-mode)
                                     (cons "\\.cir$" 'spice-mode)
                                     (cons "\\.ckt$" 'spice-mode)
                                     (cons "\\.mod$" 'spice-mode)
                                     (cons "\\.spc$" 'spice-mode) ; xcircuit output
                                     (cons "\\.spice$" 'spice-mode) ; magic output
                                     (cons "\\.cdl$" 'spice-mode)
                                     (cons "\\.chi$" 'spice-mode) ;eldo output
                                     (cons "\\.inp$" 'spice-mode))
                               auto-mode-alist))
