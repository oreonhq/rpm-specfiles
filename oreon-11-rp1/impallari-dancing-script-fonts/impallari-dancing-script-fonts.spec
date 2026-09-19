%global source0_hash f9e396da5f5ead7073d6106c39d4bc849fb193afd0dd4cece2fae7549401bedd

# SPDX-License-Identifier: MIT
%global forgeurl    https://github.com/impallari/DancingScript
%global commit      f7f54bc1b8836601dae8696666bfacd306f77e34
%forgemeta

Version: 2.000
Release: 23%{?dist}
URL:     %{forgeurl}

%global foundry           Impallari
%global fontlicense       OFL-1.1
%global fontlicenses      OFL.txt
%global fontdocs          *.txt *.md *.html
%global fontdocsex        %{fontlicenses}

%global fontfamily        Dancing Script
%global fontsummary       Dancing Script, a friendly, informal and spontaneous cursive font family
%global fonts             fonts/otf/*otf
%global fontconfngs       %{SOURCE10}
%global fontdescription   %{expand:
Dancing Script is a lively casual script where the letters bounce and change
size slightly. Caps are big, and goes below the baseline.

Dancing Script references popular scripts typefaces from the 50’s. It relates
to Murray Hill (Emil Klumpp. 1956) in his weight distribution, and to Mistral
(Roger Excoffon. 1953) in his lively bouncing effect.

Use it when you want a friendly, informal and spontaneous look.}

Source0:  %{forgesource}
Source10: 57-%{fontpkgname}.xml

%fontpkg

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgesetup
%linuxtext %{fontdocs}
chmod 644 %{fontdocs} %{fontlicenses}

%build
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles

%changelog
%autochangelog
