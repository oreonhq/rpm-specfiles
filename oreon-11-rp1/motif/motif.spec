%global source0_hash 6698f72e2018eaebb810c8a47345fc8a40a3f945551380ce88a0da6c434a010a
Summary:        Run-time libraries and programs
Name: motif
Version: 2.5.2
Release:        1%{?dist}
License: LicenseRef-Callaway-LGPLv2+
Source0:        https://src.fedoraproject.org/repo/pkgs/motif/motif-2.5.2.tar.gz/sha512/76b3c5182b15ae6a6eec3732d5c69ff3d4013a438b855d8214779c655e9db2514f13917eeee2ee7a9270dca006db55b3f5dd8688cc20a21e8bb9f3de98686732/motif-2.5.2.tar.gz
Source1: xmbind
URL: http://www.motifzone.net/
Obsoletes: openmotif < 2.3.4
Provides: openmotif = %{version}-%{release}
Requires: xorg-x11-xbitmaps
Conflicts: lesstif <= 0.92.32-6
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  byacc
BuildRequires:  flex
BuildRequires:  flex-static
BuildRequires:  libXext-devel
BuildRequires:  libXft-devel
BuildRequires:  libXmu-devel
BuildRequires:  libXp-devel
BuildRequires:  libXt-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xmu)
BuildRequires:  pkgconfig(xpm)
BuildRequires:  pkgconfig(xt)
BuildRequires:  xorg-x11-xbitmaps
# /oreon:deps
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
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n motif-devel -f %{oreon_filedir}/motif-devel.list
%files -n motif-static -f %{oreon_filedir}/motif-static.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.3.8-3
- Prepare for Oreon 11 (RP1)
