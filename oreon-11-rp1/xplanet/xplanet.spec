%global source0_hash 4380d570a8bf27b81fb629c97a636c1673407f4ac4989ce931720078a90aece7

Summary:	Render a planetary image into an X window
Name:		xplanet
Version:	1.3.1
Release:	26%{?dist}

# src/ParseGeom.c.	... under review https://gitlab.com/fedora/legal/fedora-license-data/-/issues/502
# src/ParseGeom.h	... the same review
# src/getopt.c	LGPL-2.1-or-later
# src/getopt1.c	LGPL-2.1-or-later
# src/libdisplay/DesktopPicture.m	(unused)
# src/libdisplay/vroot.h	HPND
# src/libimage/bmp.c	GPL-2.0-or-later
# xplanet/fonts/README	GPL-3.0-or-later
# xplanet/images/README	not copyrighted
# xplanet/rgb.txt	.... the same review
#
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
Source:		http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Patch0:		https://gitweb.gentoo.org/repo/gentoo.git/plain/x11-misc/xplanet/files/xplanet-1.3.1-giflib.patch
URL:		http://%{name}.sourceforge.net

BuildRequires:	make
BuildRequires:	gcc-c++
BuildRequires:	expat-devel
BuildRequires:	glib2-devel
BuildRequires:	libXScrnSaver-devel
BuildRequires:	libXt-devel
BuildRequires:	libjpeg-devel
BuildRequires:	giflib-devel
BuildRequires:	libtiff-devel
BuildRequires:	netpbm-devel
BuildRequires:	pango-devel
Requires:	gnu-free-mono-fonts

%description
Xplanet is similar to Xearth, where an image of the earth is rendered
into an X window.  Azimuthal, Mercator, Mollweide, orthographic, or
rectangular projections can be displayed as well as a window with a
globe the user can rotate interactively.  The other terrestrial
planets may also be displayed. The Xplanet home page has links to
locations with map files.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1 -b .gif

%if 0%{?fedora} >= 24
LANG=C grep -rl "inFile\.getline" . | \
	xargs sed -i.c++11 \
		-e '\@inFile\.getline@s|\(inFile\.getline[ \t]*\)\((.*)\)[ \t]*!= NULL|static_cast<bool> (\1\2)|' \
		-e '\@inFile\.getline@s|\(inFile\.getline[ \t]*\)\((.*)\)[ \t]*== NULL|(!(static_cast<bool> (\1\2)))|'
%endif

%build
%configure
make %{?_smp_mflags} -k

%install
CPPROG="cp -p" make DESTDIR=%{buildroot} install

ln -sf ../fonts/gnu-free/FreeMonoBold.ttf \
	%{buildroot}%{_datadir}/%{name}/FreeMonoBold.ttf

%files
%doc AUTHORS ChangeLog NEWS README TODO
%license COPYING
%{_bindir}/*
%{_mandir}/man1/*
%{_datadir}/xplanet

%changelog
%autochangelog
