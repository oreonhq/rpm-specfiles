%global source0_hash 084d08076ce66680b7e3b192e591fd99781464d46f2ac13a5d86305fee933929

Name: rasterview
Summary: CUPS raster file viewer
Version: 1.9.1
Release: 3%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
Source: https://www.msweet.org/files/project7/rasterview-%{version}.tar.gz
Url: http://www.msweet.org/projects.php/rasterview

BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:  gcc
BuildRequires: fltk-devel
BuildRequires: cups-devel
BuildRequires: libpng-devel
BuildRequires: libjpeg-devel
BuildRequires: zlib-devel
BuildRequires: desktop-file-utils >= 0.2.92

Patch1: rasterview-desktop-file.patch
Patch2: rasterview-cxxflags.patch

%description
CUPS uses an intermediate format called raster for inkjet printers and
others that require rasterized input.  This program can be used to
view this intermediate format and is mainly used for debugging printer
drivers.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

# Fixes for desktop file.
%patch -P1 -p1 -b .desktop-file

# Fix CPPFLAGS/CXXFLAGS typo
%patch -P2 -p1 -b .cxxflags

%build
%configure
make

%install
rm -rf %{buildroot}
make BUILDROOT=%{buildroot} INSTALL='install -p' install

rm -rf %{buildroot}%{_sysconfdir}/X11/applnk
rm -f %{buildroot}%{_datadir}/applnk/Development/rasterview.desktop
desktop-file-install \
	--dir %{buildroot}%{_datadir}/applications \
	--add-category System \
	rasterview.desktop

%files
%doc README.md LICENSE NOTICE
%{_bindir}/rasterview
%{_datadir}/icons/hicolor/*/apps/rasterview.png
%{_datadir}/mime/packages/rasterview.xml
%{_datadir}/applications/rasterview.desktop

%changelog
%autochangelog
