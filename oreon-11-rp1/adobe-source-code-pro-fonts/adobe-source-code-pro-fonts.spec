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
Release:        %autorelease
URL:            https://github.com/adobe-fonts/source-code-pro

Source:         https://github.com/adobe-fonts/source-code-pro/archive/%{version_roman}R-u/%{version_italic}R-i/%{version_vf}R-vf.tar.gz#/source-code-pro-%{version_roman}R-u-%{version_italic}R-i-%{version_vf}R-vf.tar.gz
Source10:       61-%{name}.conf
Source11:       61-%{fontpkgname2}.conf
# oreon url source checksums begin
%global source0_sha256 19d2c07eff0d91927c47a482c38e591ba855664fc65440006fb65d0157841249
%global source0_file 1.026R-vf.tar.gz
# oreon url source checksums end

%fontpkg -a

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/1.026R-vf.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "19d2c07eff0d91927c47a482c38e591ba855664fc65440006fb65d0157841249" || { echo "oreon: Source0 SHA256 mismatch for 1.026R-vf.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -n source-code-pro-%{version_roman}R-u-%{version_italic}R-i-%{version_vf}R-vf

%build
%fontbuild -a

%install
%fontinstall -a

%check
%fontcheck -a

%fontfiles -a

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - %{version_roman}.%{version_italic}.%{version_vf}-1
- Prepare for Oreon 11 (RP1)
