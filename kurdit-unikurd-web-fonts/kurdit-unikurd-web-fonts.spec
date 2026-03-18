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

Source0:       https://www.kurditgroup.org/sites/default/files/%{archivename}.zip
Source1:       65-%{fontpkgname}.conf

%fontpkg

%prep
%autosetup -c %{archivename}

%build
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 20020502-39
- Prepare for Oreon 11 (RP1)
