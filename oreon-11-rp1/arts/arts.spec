%global source0_hash 92e23839eb4042d2a15cf59614824cadc0a23e92fa139c50d5e3bd4989a8cc39
%define multilib_arches %{ix86} x86_64 ppc ppc64 s390 s390x sparcv9 sparc64
%global __brp_remove_la_files %nil
%global _lto_cflags %nil
Name:    arts
Summary:        aRts (analog realtime synthesizer) - the KDE sound system
Epoch:   8
Version: 1.5.10
Release:        1%{?dist}
License: LGPL-2.0-or-later
Url: http://www.kde.org
Source0:        ftp://ftp.kde.org/pub/kde/stable/3.5.10/src/%{name}-%{version}.tar.bz2
Source1: gslconfig-wrapper.h
Patch1: arts-1.1.4-debug.patch
Patch2: arts-1.3.92-glib2.patch
Patch5: arts-1.3.1-alsa.patch
Patch6: arts-1.5.8-glibc.patch
Patch8: arts-1.5.2-multilib.patch
Patch9: arts-1.5.10-cpu-overload-quiet.patch
Patch10: arts-1.5.10-assertion-failure.patch
Patch11: arts-1.5.10-alsa11.patch
Patch50: arts-1.5.4-dlopenext.patch
Patch51: kde-3.5-libtool-shlibext.patch
Patch52: arts-1.5.8-glibc-libio.patch
Patch53: arts-autoconf-2.7x.patch
Patch54: arts-c99.patch
Patch55: kde3-autoconf-2.72.patch
Patch200: libltdl-CVE-2009-3736.patch
Patch201: arts-1.5.10-CVE-2015-7543.patch
Patch300: kde3-acinclude.patch
Patch301: kde3-automake-version.patch
Patch302: kde3-automake-add-missing.patch
Patch303: kde3-libtool-aarch64.patch
Patch304: args-1.5.8-configure.patch
Patch305: file-literal.patch
Requires: which
# oreon:deps
BuildRequires:  alsa-lib-devel
BuildRequires:  audiofile-devel
BuildRequires:  automake
BuildRequires:  chrpath
BuildRequires:  findutils
BuildRequires:  gcc-c++
BuildRequires:  glib2-devel
BuildRequires:  libmad-devel
BuildRequires:  libtool
BuildRequires:  libvorbis-devel
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  qt3-devel
BuildRequires:  sed
# /oreon:deps
%description
arts (analog real-time synthesizer) is the sound system of KDE 3.

The principle of arts is to create/process sound using small modules which do
certain tasks. These may be create a waveform (oscillators), play samples,
filter data, add signals, perform effects like delay/flanger/chorus, or
output the data to the soundcard.

By connecting all those small modules together, you can perform complex
tasks like simulating a mixer, generating an instrument or things like
playing a wave file with some effects.

%package devel
Summary: Development files for the aRts sound server
Requires: %{name}%{?_isa} = %{epoch}:%{version}-%{release}
Requires: qt3-devel
Requires: pkgconfig
Requires: glib2-devel
%description devel
Install %{name}-devel if you intend to write applications using aRts.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P1 -p1 -b .debug
%patch -P2 -p1 -b .glib
%patch -P5 -p1 -b .alsa
%patch -P6 -p1 -b .glibc
%patch -P8 -p1 -b .multilib
%patch -P9 -p1 -b .cpu-overload-quiet
%patch -P10 -p1 -b .assertion-failure
%patch -P11 -p1 -b .alsa11

%patch -P50 -p1 -b .dlopenext
%patch -P51 -p1 -b .libtool-shlibext
%patch -P52 -p1 -b .glibc-libio
%patch -P53 -p1 -b .autoconf2.7x
%patch -P54 -p1 -b .c99
%patch -P55 -p1 -b .autoconf-2.72

%patch -P200 -p1 -b .CVE-2009-3736
%patch -P201 -p1 -b .CVE-2015-7543

%patch -P300 -p1 -b .acinclude
%patch -P301 -p1 -b .automake-version
%patch -P302 -p1 -b .automake-add-missing
%patch -P303 -p1 -b .libtool-aarch64
%patch -P304 -p1 -b .configure
%patch -P305 -p1 -b .file-literal
make -f admin/Makefile.common cvs

%build

unset QTDIR && . /etc/profile.d/qt.sh
export CXXFLAGS="%{optflags} -Wno-error=narrowing --std=gnu++17"
%configure \
  --includedir=%{_includedir}/kde \
  --disable-rpath \
  --disable-debug --disable-warnings \
  --disable-dependency-tracking \
  --enable-new-ldflags \
  --with-alsa \
  --enable-final
sed -i -e 's|"/lib /usr/lib|"/%{_lib} %{_libdir}|' libtool
%make_build
%install
export PATH=`pwd`:$PATH
%make_install
%ifarch %{multilib_arches}
  mv  %{buildroot}%{_includedir}/kde/arts/gsl/gslconfig.h \
      %{buildroot}%{_includedir}/kde/arts/gsl/gslconfig-%{_arch}.h
  install -p -m644 %{SOURCE1}  %{buildroot}%{_includedir}/kde/arts/gsl/gslconfig.h
%endif
find $RPM_BUILD_ROOT%{_libdir} -name "*.la" | xargs \
 sed -i \
 -e "s|-lmad||g" \
 -e "s|%{_libdir}/libmad.la||g" \
 -e "s|-lvorbisfile||g" \
 -e "s|-lvorbisenc||g" \
 -e "s|-lvorbis||g" \
 -e "s|-logg||g" \
 -e "s|-lasound||g" \
 -e "s|-laudiofile||g" \
 -e "s|-lesd||g" \
 -e "s|%{_libdir}/libesd.la||g" \
 -e "s|-lgmodule-2.0||g" \
 -e "s|-lgthread-2.0||g" \
 -e "s|-lglib-2.0||g" \
 -e "s|-laudio ||g" \
 -e "s|-lpng -lz ||g" \
 -e "s|%{_libdir}/libartsc.la||g" \
 -e "s@-lboost_filesystem@@g" \
 -e "s@-lboost_regex@@g" \
 -e "s@-ljack@@g"
%oreon_autofiles arts-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

test -z "$(chrpath --list %{buildroot}%{_bindir}/artsd 2>/dev/null | grep RPATH=)"
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n arts-devel -f %{oreon_filedir}/arts-devel.list

%changelog

%autochangelog
