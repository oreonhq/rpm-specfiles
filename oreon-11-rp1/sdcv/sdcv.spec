%global source0_hash 4d2519e8f8479b9301dc91e9cda3e1eefef19970ece0e8c05f0c7b7ade5dc94b
Name:           sdcv
Version:        0.5.5
Release:        1%{?dist}
Summary:        Console version of StarDict program
License:        GPL-2.0-or-later
URL:            http://sdcv.sourceforge.net/
Source0:        http://github.com/Dushistov/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch1:         0000-invalid-conversion.patch
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gettext-devel
BuildRequires:  glib2-devel
BuildRequires:  readline-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
SDCV is simple, cross-platform text-base utility for work with
dictionaries in StarDict's format.

%description -l ru
SDCV - простая, консольная утилита работы 
со словарям в формате StarDict

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake
%cmake_build
%cmake_build --target=lang
%install
%cmake_install
%find_lang %{name}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
