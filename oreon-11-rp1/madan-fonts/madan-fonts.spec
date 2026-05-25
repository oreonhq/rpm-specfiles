%if 0%{?rhel} > 10 || 0%{?oreon}
%bcond build_from_src 0
%else
%bcond build_from_src 1
%endif

%if %{with build_from_src}
BuildRequires: fontforge
BuildRequires: python3
%endif

Version: 2.000
Release: 43%{?dist}
URL: http://madanpuraskar.org/

%global fontlicense       GPL-1.0-or-later
%global fontlicenses      license.txt

%global fontfamily        Madan
%global fontsummary       Font for Nepali language
%global fonts             madan.ttf
%global fontconfs         %{SOURCE1}
%global fontdescription   %{expand:
This package provides the Madan font for Nepali made by the
Madan Puraskar Pustakalaya project.}

# Found new following working Source URL. Use wget to download this archive
Source0: http://ltk.org.np/downloads/fonts.zip
Source1: 65-0-%{fontpkgname}.conf
# Extract from font info
Source2: license.txt
Source3: sfd2ttf.pe
# Below files will make sure "fc-scan madan.ttf |grep lang:" will show ne
Source4: madan.py
Source5: madan_u0970_glyph.svg
Source6: madan.ttf

%fontpkg

%prep
%if %{with build_from_src}
%autosetup -c
cp -p %{SOURCE2} %{SOURCE3} \
      %{SOURCE4} %{SOURCE5} .
chmod 755 sfd2ttf.pe madan.py 
%{python3} ./madan.py madan.ttf madan_u0970_glyph.svg
./sfd2ttf.pe madan.sfd
%else
%setup -c -T
cp -p %{SOURCE2} %{SOURCE6} .
%endif
%linuxtext license.txt

%build
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.000-43
- Import
