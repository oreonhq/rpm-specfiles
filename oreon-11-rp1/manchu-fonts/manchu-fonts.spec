%global source0_hash 840e5649caf3396185c85f0700c6de5f71517b9d6aa806082472054618d7414f

# SPDX-License-Identifier: MIT

Version: 2.006
Release: 32%{?dist}
URL:     http://sourceforge.net/projects/manchufont/

%global foundry           Manchu
%global fontlicense       GPL-2.0-or-later
%global fontlicenses      "GNU GENERAL PUBLIC LICENSE.txt"

%global fontfamily        Manchu
%global fontsummary       A Manchu OpenType (TrueType-flavored) font
%global fonts             *.ttf
%global fontconfs         %{SOURCE10}
%global fontdescription   %{expand:
A Manchu OpenType (TrueType-flavored) font
which allows you write and read Manchu script articles correctly.
}

Source0:  http://sourceforge.net/projects/manchufont/files/ManchuFont2005%20%28Obsolete%29/ManchuFont2005%20v2.006/Manchu_Font_2005_2.006.zip
Source10: 66-%{fontpkgname}.conf

%fontpkg

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -c
%linuxtext *.txt

%build
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles

%changelog
%autochangelog
