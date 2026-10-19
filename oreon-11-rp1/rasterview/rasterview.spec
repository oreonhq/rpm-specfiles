%global source0_hash 084d08076ce66680b7e3b192e591fd99781464d46f2ac13a5d86305fee933929
Name: rasterview
Summary:        CUPS raster file viewer
Version: 1.9.1
Release:        1%{?dist}
License: GPL-2.0-or-later
Source0:        https://www.msweet.org/files/project7/rasterview-%{version}.tar.gz
Url: http://www.msweet.org/projects.php/rasterview
Patch1: rasterview-desktop-file.patch
Patch2: rasterview-cxxflags.patch
# oreon:deps
BuildRequires:  cups-devel
BuildRequires:  desktop-file-utils
BuildRequires:  fltk-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  make
BuildRequires:  zlib-devel
# /oreon:deps
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
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
