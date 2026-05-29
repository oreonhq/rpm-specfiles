%global source0_hash b30b7e80e5df817e3e4a259c18c6b62fd938d96a3143a6e349529324a6763021

Version:       20020502
Release:       39%{?dist}
# Below is only working Project URL
URL:           https://www.kurditgroup.org/d/unikurd-web

%global foundry           kurdit
# License tag determined based on gpl.txt and no information in fontfile itself
%global fontlicense       GPL-3.0-only
%global fontlicenses      gpl.txt

%global fontfamily        Unikurd Web
%global fontsummary       A widely used Kurdish font for Arabic-like scripts and Latin
%global archivename       unikurdweb_0
%global fonts             *.ttf
%global fontconfs         %{SOURCE1}
%global fontdescription   %{expand:
A widely used Kurdish font which supports various Arabic-like scripts
(Arabic, Kurdish, Persian) and also Latin.}

Source0:        https://www.kurditgroup.org/sites/default/files/%{archivename}.zip
Source1:       65-%{fontpkgname}.conf

%fontpkg

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -c %{archivename}

%build
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 20020502-39
- Import
