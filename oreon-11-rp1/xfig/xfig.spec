%global source0_hash ea949ece7910042274a5fbcb7609e82887d64409a76b54f230d022af0d534758
%global commit ce9782a404b6a527393839369aac13dcfb66ff16
%global commitdate 20250317
%global shortcommit %(c=%{commit}; echo ${c:0:7})
Summary:        An X Window System tool for drawing basic vector graphics
Name: xfig
Version: 3.2.9a
Release:        1%{?dist}
License: MIT
URL:     https://en.wikipedia.org/wiki/Xfig
Source0:        https://sourceforge.net/code-snapshots/git/m/mc/mcj/%{name}.git/mcj-%{name}-%{commit}.zip
Source1: xfig-icons.tar.gz
Requires: ghostscript
Requires: transfig
Requires: xorg-x11-fonts-misc
Requires: urw-base35-fonts-legacy
Obsoletes: %{name}-common < %{version}-%{release}
Provides:  %{name}-common = %{version}-%{release}
Obsoletes: %{name}-plain < %{version}-%{release}
Provides:  %{name}-plain = %{version}-%{release}
Obsoletes: %{name}-Xaw3d < %{version}-%{release}
Provides:  %{name}-Xaw3d = %{version}-%{release}
# oreon:deps
BuildRequires:  ImageMagick
BuildRequires:  Xaw3d-devel
BuildRequires:  gcc
BuildRequires:  libICE-devel
BuildRequires:  libSM-devel
BuildRequires:  libX11-devel
BuildRequires:  libXaw-devel
BuildRequires:  libXext-devel
BuildRequires:  libXft-devel
BuildRequires:  libXi-devel
BuildRequires:  libXmu-devel
BuildRequires:  libXpm-devel
BuildRequires:  libXt-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  libtiff-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  man2html-core
BuildRequires:  transfig
# /oreon:deps
%description
Xfig is an X Window System tool for creating basic vector graphics,
including bezier curves, lines, rulers and more.  The resulting
graphics can be saved, printed on PostScript printers or converted to
a variety of other formats (e.g., X11 bitmaps, Encapsulated
PostScript, LaTeX).

You should install xfig if you need a simple program to create vector
graphics.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -a 1 -n mcj-xfig-%{commit}
for i in doc/html/japanese/button_frame.fig doc/html/japanese/japanese.ps \
         doc/html/animate.js; do
  sed -i.orig 's/\r//' $i; touch -r $i.orig $i; rm $i.orig
done
autoreconf -i

%build

export CFLAGS="-DXAW_ARROW_SCROLLBARS $RPM_OPT_FLAGS -fno-strength-reduce -fno-strict-aliasing"
%configure
%make_build
%install
%make_install INSTALL="install -p"
cp -p README CHANGES FIGAPPS $RPM_BUILD_ROOT%{_docdir}/%{name}
rm -r $RPM_BUILD_ROOT%{_datadir}/pixmaps
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/{16x16,32x32,64x64}/apps
convert %{name}16x16.xpm \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
convert %{name}32x32.xpm \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
convert %{name}64x64.xpm \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/64x64/apps/%{name}.png
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
