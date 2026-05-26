# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 b049a7cffd9747ad834663f7785e23c00a9b30a949cfe407ad54fdcbbbca68ee
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

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
%oreon_verify_sources
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
