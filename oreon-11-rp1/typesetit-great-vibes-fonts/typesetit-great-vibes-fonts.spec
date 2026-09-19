%global source0_hash b69f0cc1156c1b3ddbe34c4e55e20d7561c8a7ff1775993936fd3b016e41ff77

# SPDX-License-Identifier: MIT
%global forgeurl    https://github.com/googlefonts/GreatVibesFont
%global commit      a82e16d27e13b0d1337abeab05fdfd99a51d044c
%forgemeta

Version: 1.101
Release: 18%{?dist}
URL:     %{forgeurl}

%global foundry           TypeSETit
%global fontlicense       OFL-1.1
%global fontlicenses      OFL.txt
%global fontdocs          *.txt *.md
%global fontdocsex        %{fontlicenses}

%global fontfamily        Great Vibes
%global fontsummary       Great Vibes, a beautifully flowing cursive font family
%global fonts             fonts/*ttf
%global fontconfngs       %{SOURCE10}
%global fontdescription   %{expand:
Great Vibes is a beautifully flowing connecting cursive font family. It has
cleanly looping ascenders and descenders as well as elegant uppercase forms.}

Source0:  %{forgesource}
Source10: 57-%{fontpkgname}.xml

%fontpkg

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgesetup

%build
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles

%changelog
%autochangelog
