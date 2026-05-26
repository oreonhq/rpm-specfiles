# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 9ac3722fa7f4ec63a48272d0bd96795d2dcfd27b2996d0433c398480f360cdc6
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

BuildRequires:  fontforge
BuildRequires: make

Version:        1.2
Release:        29%{?dist}
URL:            https://github.com/aravindavk/Navilu

%global fontlicense       OFL-1.1
%global fontlicenses      COPYING

%global fontdocs          ChangeLog README
%global fontdocsex        %{fontlicenses}

%global fontfamily        Navilu
%global fontsummary       Free Kannada opentype sans-serif font
%global fonts             *.ttf
%global fontconfs         %{SOURCE1}
%global fontdescription   %{expand:
This package provides a free Kannada opentype sans-serif font.}

Source0:        https://github.com/aravindavk/Navilu/archive/v%{version}.tar.gz#/%{fontfamily}-%{version}.tar.gz
Source1:        67-%{fontpkgname}.conf

%fontpkg

%prep
%oreon_verify_sources
%autosetup -n %{fontfamily}-%{version}

%build
%fontbuild
make

%install
%fontinstall

%check
%fontcheck

%fontfiles

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.2-29
- Prepare for Oreon 11 (RP1)
