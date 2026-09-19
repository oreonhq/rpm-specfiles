%global source0_hash d549b10e31ca79c8f0c11df1b613e5e35b93cd01519fdcde17ba88d097cb96a7

# Packaging template: basic single-family fonts packaging.
#
# SPDX-License-Identifier: MIT
#
# This template documents the minimal set of spec declarations, necessary to
# package a single font family, from a single dedicated source archive.
#
# It is part of the following set of packaging templates:
# “fonts-0-simple”: basic single-family fonts packaging
# “fonts-1-full”:   less common patterns for single-family fonts packaging
# “fonts-2-multi”:  multi-family fonts packaging
# “fonts-3-sub”:    packaging fonts, released as part of something else
#
# A font family is composed of font files, that share a single design, and
# differ ONLY in:
# — Weight        Bold, Black…
# – Width∕Stretch Narrow, Condensed, Expanded…
# — Slope/Slant   Italic, Oblique
# Optical sizing  Caption…
#
# Those parameters correspond to the default axes of OpenType variable fonts:
# https://docs.microsoft.com/en-us/typography/opentype/spec/dvaraxisreg#registered-axis-tags
# The variable fonts model is an extension of the WWS model described in the
# WPF Font Selection Model whitepaper (2007):
# https://msdnshared.blob.core.windows.net/media/MSDNBlogsFS/prod.evol.blogs.msdn.com/CommunityServer.Components.PostAttachments/00/02/24/90/36/WPF%20Font%20Selection%20Model.pdf
#
# Do not rely on the naming upstream chose, to define family boundaries, it
# will often be wrong.
#
# Declaration order is chosen to limit divergence between those templates, and
# simplify cut and pasting.
#
Version: 003.03
Release: 31%{?dist}
URL:     http://ossipedia.ipa.go.jp/ipafont/
BuildRequires: fonts-rpm-macros >= 1:2.0.5-9

# The identifier of the entity, that released the font family.
%global foundry           IPA 
# The font family license identifier. Adjust as necessary. The OFL is our
# recommended font license.
%global fontlicense       IPA
#
# The following directives are lists of space-separated shell globs
#   – matching files associated with the font family,
#   – as they exist in the build root,
#   — at the end of the %build stage:
# – legal files (licensing…)
%global fontlicenses      IPA_Font_License_Agreement_v1.0.txt
# – documentation files
%global fontdocs          Readme_ipamp00303.txt
# – exclusions from the ”fontdocs” list
%global fontdocsex        %{fontlicenses}

# The human-friendly font family name, whitespace included, restricted to the
# the Basic Latin Unicode block.
%global fontfamily        IPAPMincho
%global fontsummary       Japanese Proportional Mincho-typeface OpenType font by IPA
#
# More shell glob lists:
# – font family files
%global fonts             ipamp.ttf
# – fontconfig files
%global fontconfs         %{SOURCE10}
#
# A multi-line description block for the generated package.
%global fontdescription   %{expand:
IPA Font is a Japanese OpenType fonts that is JIS X 0213:2004
compliant, provided by Information-technology Promotion Agency, Japan.

This package contains Proportional Mincho style font.
}

# http://info.openlab.ipa.go.jp/ipafont/fontdata/%{archivename}.zip
Source0:  http://info.openlab.ipa.go.jp/ipafont/fontdata/ipamp00303.zip
# Adjust as necessary. Keeping the filename in sync with the package name is a good idea.
# See the fontconfig templates in fonts-rpm-templates for information on how to
# write good fontconfig files and choose the correct priority [number].
Source10: 68-ipa-pmincho-fonts.conf

%fontpkg

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n ipamp00303

%build
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles

%changelog
%autochangelog
