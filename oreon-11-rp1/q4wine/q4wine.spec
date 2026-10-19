%global source0_hash e27d32c09e53c36cdd6ab9e9a2587f1d5a8800b3efab8784ead3e1713c8cbfd9
%undefine __cmake_in_source_build
Name:           q4wine
Version:        1.4.2
Release:        1%{?dist}
Summary:        Qt GUI for wine
License:        GPL-3.0-or-later
URL:            http://q4wine.brezblock.org.ua/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Requires:       wine-core icoutils sqlite
ExclusiveArch:  %{ix86} x86_64 %{arm} aarch64
# oreon:deps
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  icoutils
BuildRequires:  libappstream-glib
BuildRequires:  qt6-linguist
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtsvg-devel
BuildRequires:  qt6-qttools-devel
# /oreon:deps
%description
Q4Wine is a qt GUI for wine. It will help
you manage wine prefixes and installed applications.

General features:
* Can export QT color theme into wine colors settings.
* Can easy work with different wine versions at same time;
* Easy creating, deleting and managing prefixes (WINEPREFIX);
* Easy controlling for wine process;
* Autostart icons support;
* Easy cd-image use;
* You can extract icons from PE files (.exe .dll);
* Easy backup and restore for managed prefixes.
* Winetriks support.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
# It's SingleAplication now, not QtSingleApplication, which is not in Fedora
# SingleApplication licensed under BSD-like
#rm -rf src/third-party/SingleApplication*

%build

%{cmake} \
    -DWITH_SYSTEM_SINGLEAPP=OFF \
    -DWITH_ICOUTILS=ON \
    -DUSE_GZIP=ON \
    -DRELEASE=ON ..
%cmake_build
%install
%cmake_install
mkdir -p %{buildroot}%{_metainfodir}
install -pm 644 ua.org.brezblock.q4wine.appdata.xml %{buildroot}%{_metainfodir}/
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml
rm -f %{buildroot}%{_datadir}/icons/ubuntu-mono-dark/scalable/apps/q4wine.svg
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/q4wine.desktop
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/metainfo/*.appdata.xml
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
