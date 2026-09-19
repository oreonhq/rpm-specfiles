(autoload 'blacken-buffer "blacken" "\
Try to blacken the current buffer.

Show black output, if black exit abnormally and DISPLAY is t.

\(fn &optional DISPLAY)" t nil)

(autoload 'blacken-mode "blacken" "\
Automatically run black before saving.

If called interactively, enable Blacken mode if ARG is positive,
and disable it if ARG is zero or negative.  If called from Lisp,
also enable the mode if ARG is omitted or nil, and toggle it if
ARG is `toggle'; disable the mode otherwise.

\(fn &optional ARG)" t nil)
