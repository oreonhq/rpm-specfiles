%global source0_hash 6698f72e2018eaebb810c8a47345fc8a40a3f945551380ce88a0da6c434a010a

Summary: Run-time libraries and programs
Name: motif
Version: 2.5.2
Release: 1%{?dist}
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License: LicenseRef-Callaway-LGPLv2+
# upstream host unreachable; tarball from Fedora lookaside cache
Source:        https://src.fedoraproject.org/repo/pkgs/motif/motif-2.5.2.tar.gz/sha512/76b3c5182b15ae6a6eec3732d5c69ff3d4013a438b855d8214779c655e9db2514f13917eeee2ee7a9270dca006db55b3f5dd8688cc20a21e8bb9f3de98686732/motif-2.5.2.tar.gz
Source1: xmbind
URL: http://www.motifzone.net/
Obsoletes: openmotif < 2.3.4
Provides: openmotif = %{version}-%{release}
Requires: xorg-x11-xbitmaps

BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xpm)
BuildRequires:  pkgconfig(xt)
BuildRequires:  pkgconfig(xmu)
BuildRequires:  pkgconfig(xext)
BuildRequires: make
BuildRequires: automake, libtool, autoconf, flex
BuildRequires: flex-static
BuildRequires: byacc, pkgconfig
BuildRequires: libjpeg-devel libpng-devel
BuildRequires: libXft-devel libXmu-devel libXp-devel libXt-devel libXext-devel
BuildRequires: xorg-x11-xbitmaps
BuildRequires: perl-interpreter

# FTBFS #1448819
# CVE-2023-43788
# CVE-2023-43789
# https://sourceforge.net/p/motif/code/merge-requests/9/
# https://sourceforge.net/p/motif/code/merge-requests/10/
# https://sourceforge.net/p/motif/code/merge-requests/11/


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
