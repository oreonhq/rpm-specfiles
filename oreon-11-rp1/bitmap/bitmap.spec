%global source0_hash 5c6d2637244c575a9cc65a6b1ee15ced480ef0184821aceeab29650daf323c12
Name: bitmap
Version: 1.1.2
Release:        1%{?dist}
Summary:        Bitmaps editor and converter utilities for the X Window System
Url: http://www.x.org
Source0:        http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.xz
Source1: bitmap.desktop
Source2: bitmap.png
License: MIT
Requires: xorg-x11-xbitmaps
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  libXaw-devel
BuildRequires:  libXext-devel
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  xorg-x11-xbitmaps
# /oreon:deps
%description
Bitmap provides a bitmap editor and misc converter utilities for the X
Window System.

The package also includes files defining bitmaps associated with the 
Bitmap x11 editor.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

%configure --disable-dependency-tracking
%make_build AM_LDFLAGS=-lXmu
%install
%make_install INSTALL='install -p'
desktop-file-install --dir %{buildroot}%{_datadir}/applications %{SOURCE1}
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/32x32/apps
install -p -m644 %{SOURCE2} %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
