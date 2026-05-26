# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 07600d6745f5199ad210c7f39e934dcd9716b54615e44ccf1f830001a0da3597
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

Version:        3.0.4
Release:        17%{?dist}
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

Source0: https://github.com/RedHatBrand/Overpass/archive/%{version}.tar.gz
Source10: 60-%{fontpkgname0}.conf
Source11: 60-%{fontpkgname1}.conf

%fontpkg -a

%prep
%oreon_verify_sources
%autosetup -n Overpass-%{version}

%build
%fontbuild -a

%install
%fontinstall -a
# I do not think this is useful to package, but if it is...
%if 0
mkdir -p %{buildroot}/usr/lib/node_modules/overpass/
cp -a bower.json package.json %{buildroot}/usr/lib/node_modules/overpass/
%endif

%check
%fontcheck -a

%fontfiles -z 0
%if 0
/usr/lib/node_modules/overpass/
%endif

%fontfiles -z 1

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.0.4-17
- Prepare for Oreon 11 (RP1)
