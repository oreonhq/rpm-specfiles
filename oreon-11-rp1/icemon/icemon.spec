%global source0_hash 75f79aa21e0524e384c9041b558d3b55ad5e2ce9a8c851d6c7ca94ce0bfe7e9a
Name:           icemon
Version:        3.4
Release:        1%{?dist}
Summary:        Icecream GUI monitor
License:        GPL-2.0-or-later
URL:            https://kfunk.org/tag/icemon/
Source0:        https://github.com/icecc/icemon/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        icemon.metainfo.xml
Patch1:         icemon-asciidoc.patch
Requires:    hicolor-icon-theme
# oreon:deps
BuildRequires:  asciidoc
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  pkgconfig(icecc)
BuildRequires:  qt5-qtbase-devel
# /oreon:deps
%description
A GUI monitor for Icecream, a distributed compiler system.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake
%cmake_build
%install
%cmake_install
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{SOURCE1}
install -m644 -D %{SOURCE1} %{buildroot}/%{_metainfodir}/%{name}.metainfo.xml
%oreon_autofiles main

%check

%ctest
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
