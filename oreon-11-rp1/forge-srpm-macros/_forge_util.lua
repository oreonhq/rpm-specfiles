-- Copyright (C) 2024 Maxwell G <maxwell@gtmx.me>
-- SPDX-License-Identifier: GPL-1.0-or-later

-- Utilities for evaluating macros without having to construct rpm.expand() statements.
-- Uses the macros table on RPM >= 4.17.

--- Return true if a macro is defined and false otherwise.
local function is_defined(name)
  if macros then
    return macros[name] ~= nil
  end
  return rpm.expand("%{?" .. name .. ":1}") == "1"
end

--- Expand a macro. Return nil if the macro is undefined.
local function get_macro(name)
  if macros then
    return macros[name]
  end
  if not is_defined(name) then
    return nil
  end
  return rpm.expand("%{" .. name .. "}")
end

-- Get a flag. Pass true to has_arg if the flag accepts an argument.
-- For flags with arguments, return the flag argument or nil.
-- For flags without arguments, return a truthy value for defined or nil if the
-- flag was not passed.
local function get_flag(name, has_arg)
  if opt then
    return opt[name]
  end
  if not is_defined("-" .. name) then
    return nil
  end
  local ender = "}"
  if has_arg then
    ender = "*" .. ender
  end
  return rpm.expand("%{-" .. name .. ender)
end

return {
  is_defined = is_defined,
  get_macro = get_macro,
  get_flag = get_flag,
}
