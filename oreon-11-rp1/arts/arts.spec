%global source0_hash 92e23839eb4042d2a15cf59614824cadc0a23e92fa139c50d5e3bd4989a8cc39

%define multilib_arches %{ix86} x86_64 ppc ppc64 s390 s390x sparcv9 sparc64
# This package ships .la files
%global __brp_remove_la_files %nil
# Disable LTO because it breaks ALSA versioned symbol use, crashing (#1910437)
%global _lto_cflags %nil

Name:    arts
Summary: aRts (analog realtime synthesizer) - the KDE sound system 
Epoch:   8
Version: 1.5.10
Release: 68%{?dist}

License: LGPL-2.0-or-later
Url: http://www.kde.org
Source0: ftp://ftp.kde.org/pub/kde/stable/3.5.10/src/%{name}-%{version}.tar.bz2
Source1: gslconfig-wrapper.h

Patch1: arts-1.1.4-debug.patch
Patch2: arts-1.3.92-glib2.patch
Patch5: arts-1.3.1-alsa.patch
Patch6: arts-1.5.8-glibc.patch
Patch8: arts-1.5.2-multilib.patch
# don't pop up a dialog on CPU overload (#361891)
Patch9: arts-1.5.10-cpu-overload-quiet.patch
# don't call snd_pcm_close(NULL), triggers assertion failure in ALSA (#558570)
Patch10: arts-1.5.10-assertion-failure.patch
# fix detection of ALSA 1.1 (and future 1.x) in configure.in.in
Patch11: arts-1.5.10-alsa11.patch
# kde#93359
Patch50: arts-1.5.4-dlopenext.patch
Patch51: kde-3.5-libtool-shlibext.patch
Patch52: arts-1.5.8-glibc-libio.patch
Patch53: arts-autoconf-2.7x.patch
Patch54: arts-c99.patch
Patch55: kde3-autoconf-2.72.patch

# upstream patches

# security patches
# CVE-2009-3736 libtool: libltdl may load and execute code from a library in the current directory 
Patch200: libltdl-CVE-2009-3736.patch
# CVE-2015-7543 arts,kdelibs3: Use of mktemp(3) allows attacker to hijack the IPC
# backport upstream fix (the lnusertemp.c change) from kdelibs 4:
# http://commits.kde.org/kdelibs/cc5515ed7ce8884c9b18169158ba29ab2f7a3db7
# upstream fix by Joseph Wenninger, rediffed for aRts by Kevin Kofler
Patch201: arts-1.5.10-CVE-2015-7543.patch

# fixes to common KDE 3 autotools machinery
# tweak autoconfigury so that it builds with autoconf 2.64 or 2.65
Patch300: kde3-acinclude.patch
# remove flawed and obsolete automake version check in admin/cvs.sh
Patch301: kde3-automake-version.patch
# fix build failure with automake 1.13: add the --add-missing --copy flags
# also add --force-missing to get aarch64 support (#925029/#925627)
Patch302: kde3-automake-add-missing.patch
# fix aarch64 FTBFS due to libtool not liking the file output on *.so files
Patch303: kde3-libtool-aarch64.patch
Patch304: args-1.5.8-configure.patch

# Don't use __FILE__ like a string literal
Patch305: file-literal.patch

# used in artsdsp
Requires: which

BuildRequires:  gcc-c++
BuildRequires: qt3-devel >= 3.3.8
BuildRequires: alsa-lib-devel
BuildRequires: audiofile-devel
BuildRequires: automake libtool
BuildRequires: findutils sed
BuildRequires: glib2-devel
BuildRequires: libvorbis-devel
BuildRequires: pkgconfig
BuildRequires: chrpath
BuildRequires: libmad-devel
BuildRequires: make

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

# kill rpath harder, inspired by https://fedoraproject.org/wiki/Packaging:Guidelines?rd=Packaging/Guidelines#Removing_Rpath
# other more standard variants didnt work or caused other problems
sed -i -e 's|"/lib /usr/lib|"/%{_lib} %{_libdir}|' libtool

## hack for artsdsp (see http://bugzilla.redhat.com/329671)
#make %{?_smp_mflags} -k || \
#  sed -i -e "s|-Wp,-D_FORTIFY_SOURCE=2||" artsc/Makefile && \
%make_build

%install
export PATH=`pwd`:$PATH

%make_install

%ifarch %{multilib_arches}
# Ugly hack to allow parallel installation of 32-bit and 64-bit arts-devel
  mv  %{buildroot}%{_includedir}/kde/arts/gsl/gslconfig.h \
      %{buildroot}%{_includedir}/kde/arts/gsl/gslconfig-%{_arch}.h
  install -p -m644 %{SOURCE1}  %{buildroot}%{_includedir}/kde/arts/gsl/gslconfig.h
%endif

## remove references to optional external libraries in .la files (#178733)
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

%check
## Verify rpath, or lack thereof
test -z "$(chrpath --list %{buildroot}%{_bindir}/artsd 2>/dev/null | grep RPATH=)"

%ldconfig_scriptlets

%files
%license COPYING.LIB
%dir %{_libdir}/mcop
%dir %{_libdir}/mcop/Arts
%{_libdir}/mcop/Arts/*
%{_libdir}/mcop/*.mcopclass
%{_libdir}/mcop/*.mcoptype
%{_libdir}/lib*.so.*
%{_libdir}/lib*.la
%{_bindir}/artscat
%{_bindir}/artsd
%{_bindir}/artsdsp
%{_bindir}/artsplay
%{_bindir}/artsrec
%{_bindir}/artsshell
%{_bindir}/artswrapper

%files devel
%{_bindir}/mcopidl
%dir %{_includedir}/kde
%{_includedir}/kde/arts/
%{_includedir}/kde/artsc/
%{_bindir}/artsc-config
%{_libdir}/pkgconfig/artsc.pc
%{_libdir}/lib*.so

%changelog
%autochangelog
