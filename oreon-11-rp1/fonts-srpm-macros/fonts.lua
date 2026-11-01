-- Copyright © 2018-2019 Nicolas Mailhot <nim@fedoraproject.org>
--
-- This program is free software: you can redistribute it and/or modify
-- it under the terms of the GNU General Public License as published by
-- the Free Software Foundation, either version 3 of the License, or
-- (at your option) any later version.
--
-- This program is distributed in the hope that it will be useful,
-- but WITHOUT ANY WARRANTY; without even the implied warranty of
-- MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
-- GNU General Public License for more details.
--
-- You should have received a copy of the GNU General Public License
-- along with this program.  If not, see <https://www.gnu.org/licenses/>.
--
-- SPDX-License-Identifier: GPL-3.0-or-later

-- Convenience lua functions used to create rpm font packages

local globargs = {fonts = "f", fontsex = "F", fontconfs = "c", fontconfsex = "C",
                  fontconfngs = "n", fontconfngsex = "N",
                  fontappstreams = "s", fontappstreamsex = "S",
                  fontdocs = "d", fontdocsex = "D",
                  fontlicenses = "l", fontlicensesex = "L"}

-- Return a normalized name
local function norm(name)
  local r = name
  r = string.gsub(r, "[%p%s]+", "-")
  r = string.gsub(r, "^-", "")
  r = string.gsub(r, "-$", "")
  r = string.lower(r)
  return r
end

-- loop over suffixlist and return name minus the first suffix that matches
-- - is used as suffix separator
-- name should have passed through norm at one point in the past
local function dropsuffix(name,suffixlist)
  local r = name
  for _, s in ipairs(suffixlist) do
    r, n = string.gsub(r, "-" .. norm(s) .. "$", "")
    if (n == 1) then break end
  end
  return r
end

-- Compute a font family name that can be used in packaging, lowercasing, using
-- - as separator, and applying  “WPF font selection model” whitepaper
-- simplifications
local function rpmname(name)
  local r = norm(name)
  -- Normal & co
  r = dropsuffix(r,{"normal","book","regular","upright"})
  -- Slant
  r = dropsuffix(r,{"italic","ita","ital","cursive","kursiv",
                    "oblique","inclined","backslanted","backslant","slanted"})
  -- Width / Stretch
  r = dropsuffix(r,{"ultracondensed","extra-compressed","ext-compressed","ultra-compressed","ultra-condensed",
                    "extracondensed","compressed","extra-condensed","ext-condensed","extra-cond",
                    "semicondensed","narrow","semi-condens",
                    "semiexpanded","wide","semi-expanded","semi-extended",
                    "extraexpanded","extra-expanded","ext-expanded","extra-extended","ext-extended",
                    "ultraexpanded","ultra-expanded","ultra-extended",
                    "condensed","cond",
                    "expanded","extended"})
  -- Weight (no abbreviated suffix handling, too dangerous)
  r = dropsuffix(r,{"thin","extra-thin","ext-thin","ultra-thin",
                    "extralight","extra-light","ext-light","ultra-light",
                    "demibold","semi-bold","demi-bold",
                    "extrabold","extra-bold","ext-bold","ultra-bold",
                    "extrablack","extra-black","ext-black","ultra-black",
                    "bold","thin","light","medium",
                    "black","heavy","nord",
                    "demi","ultra"})
  local tokens = {}
  for _, t in ipairs({"font","fonts"}) do
    tokens[t] = true
  end
  local ts = string.gmatch(r, "[^%-]+")
  r = ""
  for t in ts do
     if not tokens[t] then
       r = r .. "-" .. t
       tokens[t] = true
     end
  end
  r = string.gsub(r, "^-", "") .. "-fonts"
  return r
end

-- The fontenv macro main processing function
-- See the documentation in the macros.fonts file for argument description
local function env(suffix, verbose, globvalues)
  local fedora = require "fedora.common"
  local ismain = (suffix == "") or (suffix == "0")
  fedora.zalias({"foundry", "fontlicense"}, verbose)
  fedora.safeset("fontlicense", "%{license}", verbose)
  if ismain then
    fedora.zalias({"fontsummary", "fontdescription", "fontpkgname", "fonthumanname",
                   "fontpkgheader", "fonts", "fontsex", "fontconfs", "fontconfsex",
                   "fontconfngs", "fontconfngsex",
                   "fontappstreams", "fontappstreamsex",
                   "fontdocs", "fontdocsex", "fontlicense", "fontlicenses", "fontlicensesex",
                   "fontdir", "fontfilelist"}, verbose)
  end
  for _, v in ipairs({"foundry", "fontdocs", "fontdocsex",
                      "fontlicense", "fontlicenses", "fontlicensesex"}) do
    if (rpm.expand("%{" .. v .. "}") ~= "%{" .. v .. "}") then
      fedora.safeset(v .. suffix, "%{" .. v .. "}", verbose)
    end
  end
  for g, _ in pairs(globargs) do
    local v = rpm.expand("%{?" .. g .. suffix .. "} " .. (globvalues[g] or ""))
    if (string.gsub(v, "[%s]+", "") ~= "") then
      fedora.explicitset(  "current" .. g, v, verbose)
    else
      fedora.explicitunset("current" .. g,    verbose)
    end
  end
  local foundry = rpm.expand("%{?foundry" .. suffix .. ":%{foundry" .. suffix .. "}}")
  local family = string.gsub(rpm.expand("%{fontfamily" .. suffix .. "}"), "^" .. foundry, "")
  local basename = foundry .. " " .. family
  fedora.safeset("fontpkgname"   .. suffix, rpmname(basename), verbose)
  fedora.safeset("fonthumanname" .. suffix, basename, verbose)
  fedora.safeset("fontdir"       .. suffix, "%{_fontbasedir}/%{fontpkgname"  .. suffix .. "}", verbose)
  fedora.safeset("fontfilelist"  .. suffix, "%{_builddir}/%{?buildsubdir}/%{fontpkgname" .. suffix .. "}.list", verbose)
  if ismain then
    fedora.zalias({"fontpkgname", "fontdir", "fontfilelist"})
  end
  for _, v in ipairs({"foundry", "fontpkgname", "fonthumanname", "fontpkgheader",
                      "fontdir", "fontfilelist", "fontfamily", "fontlicense",
                      "fontsummary", "fontdescription"}) do
    if (rpm.expand("%{?" .. v .. suffix .. "}") ~= "") then
      fedora.explicitset(  "current" .. v, "%{" .. v .. suffix .. "}", verbose)
    else
      fedora.explicitunset("current" .. v,                             verbose)
    end
  end
end

-- Create a single %package section for a fonts subpackage
local function singlepkg(forcemain, forcesub, suffix, verbose)
  local fedora = require "fedora.common"
  local    sub = (not forcemain) and (forcesub or ((suffix ~= nil) and (suffix ~= "") and (suffix ~= "0")))
  env(suffix, verbose, {})
  name = sub and "%package     -n " or "Name:           "
  print(
    name ..
    rpm.expand(
      "%{currentfontpkgname}\n" ..
      "Summary:        %{currentfontsummary}\n" ..
      "License:        %{currentfontlicense}\n" ..
      "BuildArch:      noarch\n" ..
      "BuildRequires:  fonts-rpm-macros\n" ..
      "Requires:       fontpackages-filesystem\n" ..
      "%{?currentfontpkgheader}\n" ..
      "%description -n %{currentfontpkgname}\n") ..
    fedora.wordwrap("%{?currentfontdescription}") ..
    "\n")
end

-- Create one or all %package sections for fonts subpackages
local function pkg(forcemain, forcesub, suffix, processall, verbose)
  local fedora = require "fedora.common"
  if processall then
    for _, suffix in pairs(fedora.getsuffixes("fontfamily")) do
       singlepkg(forcemain, forcesub, suffix, verbose)
    end
  else
    singlepkg(forcemain, forcesub, suffix, verbose)
  end
end

-- Output Requires(meta) line
local function output_requires(fontpkg)
  if tonumber(rpm.expand("0%{?epoch}")) == 0 then
    print(rpm.expand(  "Requires(meta):  " .. fontpkg .. " = %{version}-%{release}\n"))
  else
    print(rpm.expand(  "Requires(meta):  " .. fontpkg .. " = %{epoch}:%{version}-%{release}\n"))
  end
end

-- Create a font (sub)metapackage header
local function metapkg(name, summary, description, suffixes)
  local   fedora = require "fedora.common"
  local fontpkgs = fedora.getsuffixed("fontpkgname")
  local hsuffix
  if (name == "") then
    name, _ = string.gsub(rpm.expand("%{name}"), "-fonts$", "")
    name    = name .. "-fonts-all"
    hsuffix = "all"
  else
    hsuffix = norm(name)
  end
  if (rpm.expand("%{?fontpkgheader" .. hsuffix .. "}") ~= "") then
    fedora.explicitset(  "currentfontpkgheader", "%{fontpkgheader" .. hsuffix .. "}", false)
  else
    fedora.explicitunset(  "currentfontpkgheader",                                 false)
  end
  if (summary == "") then
    summary = "All the font packages, generated from %{name}"
  end
  if (description == "") then
    description = "This meta-package installs all the font packages, generated from the %{name} source package."
  end
  description = fedora.wordwrap(description)
  print(rpm.expand(
    "%package   -n " .. name    .. "\n" ..
    "Summary:   "    .. summary .. "\n"))
  if (suffixes == "") then
    for _, fontpkg in pairs(fontpkgs) do
      output_requires(fontpkg)
    end
  else
    for suffix in string.gmatch(rpm.expand(suffixes), "[^%s%p]+") do
      local fontpkg = fontpkgs[suffix]
      if (fontpkg ~= nil) then
        output_requires(fontpkg)
      end
    end
  end
  print(rpm.expand(
    "BuildArch: noarch\n" ..
    "%{?currentfontpkgheader}\n" ..
    "%description -n "    .. name .. "\n" ..
    description                   .. "\n" ..
    "%files -n "          .. name .. "\n\n"))
end

return {
  globargs = globargs,
  rpmname  = rpmname,
  env      = env,
  pkg      = pkg,
  metapkg  = metapkg,
}


