%global source0_hash 859b723666eeac7df018209d66045c9853b50b4218cecadb794e2359619ebce7

Summary: Run-time libraries and programs
Name: motif
Version: 2.3.8
Release: 3%{?dist}
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License: LicenseRef-Callaway-LGPLv2+
Source:        http://downloads.sf.net/motif/motif-%{version}.tar.gz
Source1: xmbind
URL: http://www.motifzone.net/
Obsoletes: openmotif < 2.3.4
Provides: openmotif = %{version}-%{release}
Requires: xorg-x11-xbitmaps

BuildRequires: make
BuildRequires: automake, libtool, autoconf, flex
BuildRequires: flex-static
BuildRequires: byacc, pkgconfig
BuildRequires: libjpeg-devel libpng-devel
BuildRequires: libXft-devel libXmu-devel libXp-devel libXt-devel libXext-devel
BuildRequires: xorg-x11-xbitmaps
BuildRequires: perl-interpreter

Patch22: motif-2.3.4-no_demos.patch
Patch23: openMotif-2.2.3-uil_lib.patch
Patch43: openMotif-2.3.0-rgbtxt.patch
Patch45: motif-2.3.4-mwmrc_dir.patch
Patch46: motif-2.3.4-bindings.patch
Patch47: openMotif-2.3.0-no_X11R6.patch
# FTBFS #1448819
Patch48: motif-2.3.4-Fix-issues-with-Werror-format-security.patch
Patch49: motif-configure-c99.patch
Patch50: motif-c99-void-sprintf.patch
Patch51: motif-c99-string.patch
# CVE-2023-43788
Patch55: 0001-Fix-CVE-2023-43788-Out-of-bounds-read-in-XpmCreateXp.patch
# CVE-2023-43789
Patch56: 0001-Fix-CVE-2023-43789-Out-of-bounds-read-on-XPM-with-co.patch
# https://sourceforge.net/p/motif/code/merge-requests/9/
Patch58: 0001-build-Check-for-Xinerama-availability.patch
Patch59: 0002-Xm-Display-Add-optional-Xinerama-support.patch
Patch60: 0003-Xm-MenuShell-Use-Xinerama-to-place-menus.patch
Patch61: 0004-Xm-DropDown-Use-Xinerama-for-placement.patch
Patch62: 0005-Xm-RCMenu-Use-Xinerama-for-placement.patch
Patch63: 0006-Xm-Tooltip-Use-Xinerama-for-placement.patch
Patch64: 0007-Xm-ComboBox-Use-Xinerama-for-placement.patch
# https://sourceforge.net/p/motif/code/merge-requests/10/
Patch65: 0001-Xm-String-Fix-memory-leak.patch
# https://sourceforge.net/p/motif/code/merge-requests/11/
Patch66:  0001-Xm-Screen-Add-_NET_WORKAREA-support.patch
Patch67:  0002-Xm-Screen-Add-_GTK_WORKAREAS-support-for-multi-monit.patch

Patch68: includes.patch

Conflicts: lesstif <= 0.92.32-6

%description
This is the Motif %{version} run-time environment. It includes the
Motif shared libraries, needed to run applications which are dynamically
linked against Motif and the Motif Window Manager mwm.

%package devel
Summary: Development libraries and header files
Conflicts: lesstif-devel <= 0.92.32-6
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: libjpeg-devel%{?_isa} libpng-devel%{?_isa}
Requires: libXft-devel%{?_isa} libXmu-devel%{?_isa} libXp-devel%{?_isa}
Requires: libXt-devel%{?_isa} libXext-devel%{?_isa}
Obsoletes: openmotif-devel < 2.3.4
Provides: openmotif-devel = %{version}-%{release}

%description devel
This is the Motif %{version} development environment. It includes the
header files and also static libraries necessary to build Motif applications.

%package static
Summary: Static libraries
Conflicts: lesstif-devel <= 0.92.32-6
Requires: %{name}-devel%{?_isa} = %{version}-%{release}

%description static
This package contains the static Motif libraries.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q
%patch -P 22 -p1 -b .no_demos
%patch -P 23 -p1 -b .uil_lib
%patch -P 43 -p1 -b .rgbtxt
%patch -P 45 -p1 -b .mwmrc_dir
%patch -P 46 -p1 -b .bindings
%patch -P 47 -p1 -b .no_X11R6
%patch -P 48 -p1 -b .format-security
%patch -P 49 -p1
%patch -P 50 -p1
%patch -P 51 -p1
%patch -P 55 -p1
%patch -P 56 -p1
%patch -P 58 -p1 -b .xinerama
%patch -P 59 -p1 -b .xinerama
%patch -P 60 -p1 -b .xinerama
%patch -P 61 -p1 -b .xinerama
%patch -P 62 -p1 -b .xinerama
%patch -P 63 -p1 -b .xinerama
%patch -P 64 -p1 -b .xinerama
%patch -P 65 -p1 -b .utf8-memleak
%patch -P 66 -p1 -b .net-workarea
%patch -P 67 -p1 -b .gtk-workareas

%patch -P 68 -p1 -b .includes

%build
export CFLAGS="$CFLAGS -std=gnu17"
touch AUTHORS NEWS
autoreconf -fi
%configure --enable-static --enable-xft --enable-jpeg --enable-png

make clean %{?_smp_mflags}
make -C include
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install

install -d %{buildroot}/etc/X11/xinit/xinitrc.d
install -m 755 %{SOURCE1} %{buildroot}/etc/X11/xinit/xinitrc.d/xmbind.sh

rm -f %{buildroot}%{_libdir}/*.la

%ldconfig_scriptlets

%files
%doc COPYING README RELEASE RELNOTES
/etc/X11/xinit/xinitrc.d/xmbind.sh
%dir /etc/X11/mwm
%config(noreplace) /etc/X11/mwm/system.mwmrc
%{_bindir}/mwm
%{_bindir}/xmbind
%{_includedir}/X11/bitmaps/*
%{_libdir}/libMrm.so.*
%{_libdir}/libUil.so.*
%{_libdir}/libXm.so.*
%{_datadir}/X11/bindings
%{_mandir}/man1/mwm*
%{_mandir}/man1/xmbind*
%{_mandir}/man4/mwmrc*

%files devel
%{_bindir}/uil
%{_includedir}/Mrm
%{_includedir}/Xm
%{_includedir}/uil
%{_libdir}/lib*.so
%{_mandir}/man1/uil.1*
%{_mandir}/man3/*
%{_mandir}/man5/*

%files static
%{_libdir}/lib*.a

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.3.8-3
- Prepare for Oreon 11 (RP1)
