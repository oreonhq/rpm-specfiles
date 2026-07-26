%global source0_hash 3caf14731313c99967f6e4e11ff261b061e4e3d0c7ef7565e89b12e0307814ca

Name:           icemon
Version:        3.3
Release:        18%{?dist}
Summary:        Icecream GUI monitor

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://kfunk.org/tag/icemon/
Source0:        https://github.com/icecc/icemon/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        icemon.metainfo.xml
# Backport of docbook -> asciidoc from upstream
# https://github.com/icecc/icemon/commit/479490ffbe0d13ed3059b67241671cb78521a10a
Patch1:         icemon-asciidoc.patch

BuildRequires:    gcc-c++
BuildRequires:    pkgconfig(icecc) >= 1.3
BuildRequires:    cmake
BuildRequires:    desktop-file-utils
BuildRequires:    extra-cmake-modules
BuildRequires:    qt5-qtbase-devel
BuildRequires:    asciidoc
BuildRequires:    libappstream-glib

Requires:    hicolor-icon-theme

%description
A GUI monitor for Icecream, a distributed compiler system.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{SOURCE1}
# FIXME: This command would install it to /usr/share/appdata .
# DESTDIR=%{buildroot} appstream-util install %{SOURCE1}
install -m644 -D %{SOURCE1} %{buildroot}/%{_metainfodir}/%{name}.metainfo.xml

%check
%ctest

%files
%{_bindir}/%{name}
%{_datadir}/applications/icemon.desktop
%{_datadir}/icons/hicolor/*/apps/icemon.png
%{_mandir}/man1/icemon.1.*
%{_metainfodir}/icemon.metainfo.xml
%license COPYING
%doc CHANGELOG.md README.md

%changelog
%autochangelog
