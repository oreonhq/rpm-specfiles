%global source0_hash b2f63cba605e79cc2a08714bf3888f7be7174384ed724db3c70f8bf25c36f554

%global	short_version	3.10

%undefine        _changelog_trimtime
%undefine   __brp_mangle_shebangs

Name:			xcircuit
Version:		%{short_version}.30
Release:		16%{?dist}
Summary:		Electronic circuit schematic drawing program

# Xw/		HPND unused
# asg/	non-free	unused
# flate.c	GPL-2.0-only	from acroformtool
# lib/tcl/matgen.tcl		GPL-2.0-or-later
# spiceparser/	GPL-2.0-or-later	unused
# utf8encodings.c	not-a-license https://gitlab.com/fedora/legal/fedora-license-data/-/issues/498
# xcircuit.c	GPL-2.0-or-later
# SPDX confirmed
License:		GPL-2.0-or-later AND GPL-2.0-only
URL:			http://opencircuitdesign.com/xcircuit

Source:		http://opencircuitdesign.com/xcircuit/archive/%{name}-%{version}.tgz
Source1:		%{name}.desktop
# http://opencircuitdesign.com/xcircuit/archive/xcircuit.xpm as 64x64
Source2:		%{name}.png

Patch0:		xcircuit-3.9.40-format-security.patch
Patch1:		xcircuit-c99.patch
# C23 fix, include math.h instead of declare atan2 internally
Patch2:		xcircuit-3.10.30-c23-math-include.patch

BuildRequires:	make
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(fontconfig)
BuildRequires:	libgs-devel
BuildRequires:	libXpm-devel
BuildRequires:	libXt-devel
BuildRequires:	pkgconfig(tcl) <= 8.999
BuildRequires:	pkgconfig(tk) <= 8.999
BuildRequires:	zlib-devel
BuildRequires:	desktop-file-utils
BuildRequires:	ngspice

BuildRequires:	automake
BuildRequires:	autoconf
BuildRequires:	libtool

# Need check
Requires:		coreutils
Requires:		gtk2
Requires:		tk

# Special FEL Gnome/KDE menu structure
Requires:		electronics-menu

%description
Xcircuit is a general-purpose drawing program and also a specific-purpose
CAD program for circuit schematic drawing and schematic capture.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1 -b .format
%patch -P1 -p1 -b .c99
%patch -P2 -p1 -b .c23

#439604: TCL 8.5.1
sed -i lib/tcl/tkcon.tcl \
	-e "s|package require -exact|package require|" 
sed -i Makefile.am \
	-e 's|/lib/|/%{_lib}/|'

autoreconf

sed -i Makefile.in -e 's|LD_RUN_PATH =|LD_RUN_PATH_DIE =|'
sed -i examples/xc_remote.sh -e 's|/usr/local/bin|%{_bindir}|'
chmod ugo-x lib/tcl/console.tcl

%build
export WISH=/usr/bin/wish

#01/08/09 Without --enable-asg \ because it's broken
%configure \
	--with-tcl=%{_libdir} \
	--with-tk=%{_libdir} \
	%{nil}
%make_build

%install
%make_install
make install-man mandir="%{buildroot}%{_mandir}"

rm -rf examples/win32
chmod -x examples/*

# They stay
#W: xcircuit hidden-file-or-dir examples/python/.xcircuitrc
#W: xcircuit hidden-file-or-dir examples/.xcircuitrc

mkdir -p %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/
install -cpm 0644 %{SOURCE2} \
	%{buildroot}%{_datadir}/icons/hicolor/32x32/apps/%{name}.png

sed -i '7 a\export TCLLIBPATH=%{_libdir}' %{buildroot}%{_bindir}/xcircuit

desktop-file-install \
	--vendor "" \
	--dir %{buildroot}%{_datadir}/applications \
	%{SOURCE1}

%files
%doc	CHANGES
%doc	README*
%doc	TODO
%doc	examples/
%license	COPYRIGHT

%{_bindir}/%{name}
%{_libdir}/%{name}-%{short_version}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
%{_mandir}/man1/%{name}.1.*

%changelog
%autochangelog
