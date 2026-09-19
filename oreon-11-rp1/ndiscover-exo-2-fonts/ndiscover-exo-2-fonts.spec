%global source0_hash ce9c39cf8cc201ebcef6e911a5f34473cf1fb7313b8dd97f6cc61f5ca39f7a93

# SPDX-License-Identifier: MIT
%global forgeurl    https://github.com/NDISCOVER/Exo-2.0
%global commit      22a4e995451acbc50634a8399c4a0ded6aa7d75e
%forgemeta

Version: 2.000
Release: 15%{?dist}
URL:     %{forgeurl}

%global foundry           NDISCOVER
%global fontlicense       OFL-1.1
%global fontlicenses      OFL.txt
%global fontdocs          *txt *md
%global fontdocsex        %{fontlicenses}

%global fontfamily        Exo 2
%global fontsummary       Exo 2, a contemporary geometric sans serif font family
%global fonts             fonts/otf/*otf fonts/vf/*ttf
%global fontconfngs       %{SOURCE10}
%global fontdescription   %{expand:
Exo 2 is a complete redrawing of Exo, a contemporary geometric sans serif
font family that tries to convey a technological/futuristic feeling while keeping
an elegant design. Exo is a very versatile font, so it has 9 weights (the
maximum on the web) and each with a true italic version. Exo 2 has a more
organic look that will perform much better at small text sizes and in long
texts.}

Source0:  %{forgesource}
Source10: 60-%{fontpkgname}.xml

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
