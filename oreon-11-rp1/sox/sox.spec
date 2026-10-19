%global source0_hash 20969da7da7d241a581db89e1ec78bf5c76015a9e7135b94e23c348347c2366b
Summary:        A general purpose sound file conversion tool
Name: sox
Version: 14.4.2.0
Release:        1%{?dist}
License: GPL-2.0-or-later AND LicenseRef-Callaway-LGPLv2+ AND LicenseRef-Callaway-MIT
Source0:        https://github.com/i386x/sox-downstream/archive/%{name}-%{version}.modified.tar.gz
URL: http://sox.sourceforge.net/
Patch0: sox-14.4.2-lsx_symbols.patch
Patch1: sox-14.4.2-lpc10.patch
Patch2: sox-14.4.2-fsf_address_fix.patch
Patch1000: sox-14.4.2-bug_1500570_fix.patch
Patch1001: sox-14.4.2-bug_1500554_fix.patch
Patch1002: sox-14.4.2-bug_1500553_fix.patch
Patch1003: sox-14.4.2-bug_1510923_fix.patch
Patch1004: sox-14.4.2-hcom_stopwrite_big_endian_bug_fix.patch
Patch1005: sox-14.4.2-bug_1226675_fix.patch
Patch1006: sox-14.4.2-bug_1480678_fix.patch
Patch1007: sox-14.4.2-bug_1545867_fix.patch
Patch9000: sox-14.4.2-installcheck_fix.patch
Patch9001: sox-sample_tes-t-c99.patch
# oreon:deps
BuildRequires:  alsa-lib-devel
BuildRequires:  flac-devel
BuildRequires:  gcc
BuildRequires:  gsm-devel
BuildRequires:  ladspa-devel
BuildRequires:  lame-devel
BuildRequires:  libao-devel
BuildRequires:  libid3tag-devel
BuildRequires:  libmad-devel
BuildRequires:  libpng-devel
BuildRequires:  libsamplerate-devel
BuildRequires:  libsndfile-devel
BuildRequires:  libtool
BuildRequires:  libtool-ltdl-devel
BuildRequires:  libvorbis-devel
BuildRequires:  make
BuildRequires:  opusfile-devel
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  twolame-devel
BuildRequires:  wavpack-devel
# /oreon:deps
%description
SoX (Sound eXchange) is a sound file format converter. SoX can convert
between many different digitized sound formats and perform simple
sound manipulation functions, including sound effects.

%package -n  sox-devel
Summary: The SoX sound file format converter libraries
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: pkgconfig
%description -n sox-devel
This package contains the library needed for compiling applications
which will use the SoX sound file format converter.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-downstream-%{name}-%{version}.modified
%patch -P0 -p1
%patch -P1 -p1 -b .lpc
%patch -P2 -p1
%patch -P1000 -p1
%patch -P1001 -p1
%patch -P1002 -p1
%patch -P1003 -p1
%patch -P1004 -p1
%patch -P1005 -p1
%patch -P1006 -p1
%patch -P1007 -p1
%patch -P9000 -p1
%patch -P9001 -p1
#regenerate scripts from older autoconf to support aarch64
autoreconf -vfi

%build

CFLAGS="$RPM_OPT_FLAGS -D_FILE_OFFSET_BITS=64"
%configure --without-lpc10 \
           --with-gsm \
           --includedir=%{_includedir}/sox \
           --disable-static \
           --with-distro=Fedora \
           --with-dyn-default
make V=1 %{?_smp_mflags}
%install
make install DESTDIR=$RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT%{_libdir}/libsox.la
rm -f $RPM_BUILD_ROOT%{_libdir}/sox/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/sox/*.a
%ldconfig_scriptlets
%oreon_autofiles sox-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n sox-devel -f %{oreon_filedir}/sox-devel.list

%changelog

%autochangelog
