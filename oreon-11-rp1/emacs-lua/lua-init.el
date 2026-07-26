; Lua major mode, init file by Tim Niemueller [www.niemueller.de], GPLv2+
; Add mode to automatically recognized modes
(setq auto-mode-alist (cons '("\\.lua$" . lua-mode) auto-mode-alist))
(autoload 'lua-mode "lua-mode" "Lua editing mode." t)
; Turn on colorization by default
(add-hook 'lua-mode-hook 'turn-on-font-lock)
; Enable hideshow for Lua by default, does not work atm
; (add-hook 'lua-mode-hook 'hs-minor-mode)
