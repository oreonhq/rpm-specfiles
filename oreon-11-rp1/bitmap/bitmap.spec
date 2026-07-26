%global source0_hash 63d42eb63fe48198b39344af49949e5e424cc62ce8d722781fdad4a4fa3426e6

Name: bitmap
Version: 1.1.1
Release: %autorelease
Summary: Bitmaps editor and converter utilities for the X Window System
Url: http://www.x.org

Source0: http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.xz
Source1: bitmap.desktop
Source2: bitmap.png

License: MIT

# libXaw-devel requires libXmu-devel 
# libXmu-devel requires libX11-devel, libXt-devel, xorg-x11-util-macros
BuildRequires:  gcc
BuildRequires: xorg-x11-xbitmaps libXaw-devel libXext-devel
BuildRequires: desktop-file-utils pkgconfig
BuildRequires: make
# also needed at runtime
Requires: xorg-x11-xbitmaps

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

%files
# COPYING is a stub!
%doc ChangeLog
%{_bindir}/atobm
%{_bindir}/bmtoa
%{_bindir}/bitmap
%{_includedir}/X11/bitmaps/*
%{_datadir}/X11/app-defaults/Bitmap*
%{_datadir}/applications/*bitmap*
%{_datadir}/icons/hicolor/32x32/apps/bitmap.png
%{_mandir}/man1/*.1*

%changelog
%autochangelog
