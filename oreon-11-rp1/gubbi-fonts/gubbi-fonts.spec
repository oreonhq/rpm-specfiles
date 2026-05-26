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
# oreon url source checksums begin
%global source0_sha256 49011eb884137a403520214a67a046e508de4cc693406a5a311305529f337b51
%global source0_file v1.3.tar.gz
# oreon url source checksums end

%fontpkg

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/v1.3.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "49011eb884137a403520214a67a046e508de4cc693406a5a311305529f337b51" || { echo "oreon: Source0 SHA256 mismatch for v1.3.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
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
