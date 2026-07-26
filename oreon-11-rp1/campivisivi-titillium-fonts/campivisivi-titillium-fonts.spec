%global source0_hash 649fb98c5fca9967d18c3243aa549c9c460cbf3ea6dd4ccd46c970f3585a7225

Version: 20120913
Release: 34%{?dist}
URL: http://www.campivisivi.net/titillium/

%global foundry           Campivisivi
%global fontlicense       OFL-1.1
%global fontlicenses      OFL-titillium.txt
%global fontdocs          OFL-FAQ.txt
%global fontdocsex        %{fontlicenses}

%global fontfamily        Titillium
%global fontsummary       Sans-serif typeface from the Master of Visual Design Campi Visivi
%global fonts             *.otf
%global fontconfs         %{SOURCE1}
%global fontdescription   %{expand:
Sans-serif typeface from the Master of Visual Design Campi Visivi.}

Source0: http://www.campivisivi.net/titillium/download/Titillium_roman_upright_italic_2_0_OT.zip
Source1: 61-%{fontpkgname}.conf

%fontpkg

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n "Titillium_roman_upright_italic_2_0_OT"
%linuxtext OFL-titillium.txt OFL-FAQ.txt

%build
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles

%changelog
%autochangelog
