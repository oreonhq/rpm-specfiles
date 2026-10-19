%global source0_hash beb7528f1e9adf3decf841f02510a3752820561a06842f9097d9f2565fe41f34
Version:        3.0.5
Release:        1%{?dist}
URL:            https://github.com/RedHatBrand/overpass/
%global         fontlicense     OFL-1.1 or LGPL-2.0-or-later
%global         fontlicenses    LICENSE.md
%global         fontdocsex      %{fontlicenses}
%global common_description %{expand:
Free and open source typeface based on the U.S. interstate highway road signage\
type system.}
%global fontfamily0       Overpass
%global fontsummary0      Typeface based on the U.S. interstate highway road signage type system
%global fonts0            desktop-fonts/overpass/overpass-*.otf
%global fontconfs0        %{SOURCE10}
%global fontdocs0         README.md overpass-specimen.pdf
%global fontdescription  %{expand:
%{common_description}
This package provide sans-serif fonts which are suitable for both body and \
titling text.}
%global fontfamily1       Overpass Mono
%global fontsummary1      Monospace version of overpass fonts
%global fonts1            desktop-fonts/overpass-mono/overpass-*.otf
%global fontconfs1        %{SOURCE11}
%global fontdocs1         README.md overpass-mono-specimen.pdf
%global fontdescription1  %{expand:
%{common_description}
This package provide monospace version of overpass fonts.}
Source0:        https://github.com/RedHatBrand/Overpass/archive/refs/tags/v%{version}.tar.gz#/overpass-fonts-%{version}.tar.gz
Source10: 60-%{fontpkgname0}.conf
Source11: 60-%{fontpkgname1}.conf
%fontpkg -a
# oreon:deps
BuildRequires:  fonts-rpm-macros
# /oreon:deps
%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir Overpass-%{version}
%oreon_prep
%build

%fontbuild -a
%install
%fontinstall -a
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%fontcheck -a
%fontfiles -z 0
%fontfiles -z 1
%files -f %{oreon_filedir}/main.list
%files -n bitmap-lucida-typewriter-fonts -f %{oreon_filedir}/bitmap-lucida-typewriter-fonts.list
%files -n bitmap-lucida-typewriter-opentype-fonts -f %{oreon_filedir}/bitmap-lucida-typewriter-opentype-fonts.list
%files -n bitmap-fangsongti-fonts -f %{oreon_filedir}/bitmap-fangsongti-fonts.list
%files -n bitmap-fangsongti-opentype-fonts -f %{oreon_filedir}/bitmap-fangsongti-opentype-fonts.list
%files -n bitmap-console-fonts -f %{oreon_filedir}/bitmap-console-fonts.list
%files -n bitmap-console-opentype-fonts -f %{oreon_filedir}/bitmap-console-opentype-fonts.list
%files -n bitmap-fixed-fonts -f %{oreon_filedir}/bitmap-fixed-fonts.list
%files -n bitmap-fixed-opentype-fonts -f %{oreon_filedir}/bitmap-fixed-opentype-fonts.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.0.4-17
- Prepare for Oreon 11 (RP1)
