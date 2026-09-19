(defvar ansible-key-map (make-sparse-keymap) "\
Keymap for Ansible.")

(autoload 'ansible-mode "ansible" "\
Ansible minor mode.

This is a minor mode.  If called interactively, toggle the `Ansible
mode' mode.  If the prefix argument is positive, enable the mode, and if
it is zero or negative, disable the mode.

If called from Lisp, toggle the mode if ARG is `toggle'.  Enable the
mode if ARG is nil, omitted, or is a positive number.  Disable the mode
if ARG is a negative number.

To check whether the minor mode is enabled in the current buffer,
evaluate the variable `ansible-mode'.

The mode's hook is called both when the mode is enabled and when it is
disabled.

\(fn &optional ARG)" t)

(autoload 'ansible-dict-initialize "ansible" "\
Initialize Ansible auto-complete.")

(register-definition-prefixes "ansible" '("ansible-"))
