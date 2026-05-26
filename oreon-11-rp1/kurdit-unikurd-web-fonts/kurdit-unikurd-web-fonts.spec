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
# oreon url source checksums begin
%global source0_sha256 b049a7cffd9747ad834663f7785e23c00a9b30a949cfe407ad54fdcbbbca68ee
%global source0_file unikurdweb_0.zip
# oreon url source checksums end

%fontpkg

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/unikurdweb_0.zip; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "b049a7cffd9747ad834663f7785e23c00a9b30a949cfe407ad54fdcbbbca68ee" || { echo "oreon: Source0 SHA256 mismatch for unikurdweb_0.zip" >&2; exit 1; })
# oreon verify url source checksums end
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
