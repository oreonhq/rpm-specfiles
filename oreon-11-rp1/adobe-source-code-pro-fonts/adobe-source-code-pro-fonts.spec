%global source0_hash 19d2c07eff0d91927c47a482c38e591ba855664fc65440006fb65d0157841249
%global foundry           adobe
%global fontlicense       OFL-1.1
%global fontlicenses      LICENSE.md
%global fontdocs          README.md
%global fontdocsex        %{fontlicenses}
%global fontfamily        Source Code Pro
%global fontsummary       A set of mono-spaced OpenType fonts designed for coding environments
%global fontpkgheader    %{expand:
Suggests: font(sourcecodevf)}
%global fonts             OTF/*.otf
%global fontconfs         %{SOURCE10}
%global fontdescription   %{expand:
This font was designed by Paul D. Hunt as a companion to Source Sans. It has
the same weight range as the corresponding Source Sans design.  It supports
a wide range of languages using the Latin script, and includes all the
characters in the Adobe Latin 4 glyph set.}
%global fontfamily2       Source Code VF
%global fontsummary2      OpenType fonts designed for coding environments, variable versions
%global fontpkgheader1    %{expand:
Suggests: font(sourcecodepro)}
%global fonts2            VF/*.otf
%global fontconfs2        %{SOURCE11}
%global fontdescription2  %{expand:
%{fontdescription}
This is the variable versions of the font Source Code Pro.}}
%global version_roman  2.042
%global version_italic 1.062
%global version_vf     1.026
Version:        %{version_roman}.%{version_italic}.%{version_vf}
Release:        1%{?dist}
URL:            https://github.com/adobe-fonts/source-code-pro
Source0:        https://github.com/adobe-fonts/source-code-pro/archive/2.042R-u/1.062R-i/1.026R-vf.tar.gz#/source-code-pro-2.042R-u-1.062R-i-1.026R-vf.tar.gz
Source10:       61-%{name}.conf
Source11:       61-%{fontpkgname2}.conf
%fontpkg -a
# oreon:deps
BuildRequires:  fonts-rpm-macros
# /oreon:deps
%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n source-code-pro-%{version_roman}R-u-%{version_italic}R-i-%{version_vf}R-vf

%build

%fontbuild -a
%install
%fontinstall -a
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%fontcheck -a
%fontfiles -a
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - %{version_roman}.%{version_italic}.%{version_vf}-1
- Prepare for Oreon 11 (RP1)
