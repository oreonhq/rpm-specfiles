# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 49011eb884137a403520214a67a046e508de4cc693406a5a311305529f337b51
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

BuildRequires:  fontforge
BuildRequires:  make

Version:        1.3
Release:        21%{?dist}
URL:            https://github.com/aravindavk/Gubbi

%global fontlicense       GPL-3.0-or-later WITH Font-exception-2.0
%global fontlicenses      COPYING

%global fontdocs          ChangeLog README
%global fontdocsex        %{fontlicenses}

%global fontfamily        Gubbi
%global fontsummary       Free Kannada Opentype serif font
%global fonts             *.ttf
%global fontconfs         %{SOURCE1}
%global fontdescription   %{expand:
This package provides a free Kannada opentype serif font.}

Source0:        https://github.com/aravindavk/Gubbi/archive/v%{version}.tar.gz#/%{fontfamily}-%{version}.tar.gz
Source1:        65-0-%{fontpkgname}.conf

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
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.3-21
- Prepare for Oreon 11 (RP1)
