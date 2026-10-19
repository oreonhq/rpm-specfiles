%global source0_hash cf4619ce1471690e4ecc5544ee6289cef6c5bdf5855a1ac8dcc63f5beedf108d
%global _build_id_links none
%define pkg_version 6.9.1
%define api_version 0.8.8
%bcond minimal 1
%bcond python3 1
%bcond python2 0
%if 0%{?oreon} >= 11
%global tcl_version 9.0
%else
%{!?tcl_version: %global tcl_version 8.6}
%endif
%{!?tcl_sitearch: %global tcl_sitearch %{_libdir}/tcl%{tcl_version}}
%bcond speech_dispatcher %{defined fedora}
%bcond espeak %{defined fedora}
%ifnarch %{ix86}
%bcond ocaml %{defined fedora}
%endif
%ifarch %{java_arches}
%bcond java %{defined fedora}
%endif
%global _privatelibs libbrltty.+\.so.*
%global __provides_exclude ^(%{_privatelibs})$
%global __requires_exclude ^(%{_privatelibs})$
Name: brltty
Version: 6.9.1
Release:        1%{?dist}
License: LGPL-2.0-or-later AND LGPL-2.1-or-later AND GPL-2.0-or-later
URL: http://brltty.app/
Source0:        https://brltty.app/archive/%{name}-%{version}.tar.xz
Source1:        brltty.service
Source2:        brlapi-config.h
Source3:        brlapi-forbuild.h
Source4:        brltty.sysusers
Patch1:        brltty-6.3-loadLibrary.patch
Patch2:        brltty-6.8-libspeechd.patch
Summary:        Braille display driver for Linux/Unix
%if %{with espeak}
%endif
%if %{with python2}
%endif
%if %{with python3}
%endif
Conflicts: brltty-minimal
Requires(post): coreutils
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
# oreon:deps
BuildRequires:  alsa-lib-devel
BuildRequires:  at-spi2-core-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bluez-libs-devel
BuildRequires:  byacc
BuildRequires:  doxygen
BuildRequires:  espeak-devel
BuildRequires:  espeak-ng-devel
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  glibc-kernheaders
BuildRequires:  libICE-devel
BuildRequires:  libSM-devel
BuildRequires:  libX11-devel
BuildRequires:  libXaw-devel
BuildRequires:  libXext-devel
BuildRequires:  libXt-devel
BuildRequires:  libXtst-devel
BuildRequires:  libicu-devel
BuildRequires:  linuxdoc-tools
BuildRequires:  lua-devel
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  ocaml
BuildRequires:  ocaml-findlib
BuildRequires:  polkit-devel
BuildRequires:  python3-Cython
BuildRequires:  python3-devel
BuildRequires:  python3-docutils
BuildRequires:  python3-setuptools
BuildRequires:  speech-dispatcher-devel
BuildRequires:  systemd
BuildRequires:  systemd-rpm-macros
BuildRequires:  tcl-devel
# /oreon:deps
%description
BRLTTY is a background process (daemon) which provides
access to the Linux/Unix console (when in text mode)
for a blind person using a refreshable braille display.
It drives the braille display and provides complete
screen review functionality.
%if %{with speech_dispatcher}
BRLTTY can also work with speech synthesizers; if you want to use it with
Speech Dispatcher, please install also package %{name}-speech-dispatcher.

%package speech-dispatcher
Summary: Speech Dispatcher driver for BRLTTY
BuildRequires: speech-dispatcher-devel
Requires: %{name}%{?_isa} = %{pkg_version}-%{release}
%description speech-dispatcher
This package provides the Speech Dispatcher driver for BRLTTY.
%endif

%package docs
Summary: Documentation for BRLTTY
BuildArch: noarch
%description docs
This package provides the documentation for BRLTTY.

%package xw
Summary: XWindow driver for BRLTTY
BuildRequires: libSM-devel libICE-devel libX11-devel libXaw-devel libXext-devel libXt-devel libXtst-devel
Requires: %{name}%{?_isa} = %{pkg_version}-%{release}
Requires: xorg-x11-fonts-misc
%description xw
This package provides the XWindow driver for BRLTTY.

%package at-spi2
Summary: AtSpi2 driver for BRLTTY
Requires: %{name}%{?_isa} = %{pkg_version}-%{release}
%description at-spi2
This package provides the AtSpi2 driver for BRLTTY.

%if %{with espeak}
%package espeak
Summary: eSpeak driver for BRLTTY
Requires: %{name}%{?_isa} = %{pkg_version}-%{release}
%description espeak
This package provides the eSpeak driver for BRLTTY.
%endif

%package espeak-ng
Summary: eSpeak-NG driver for BRLTTY
Requires: %{name}%{?_isa} = %{pkg_version}-%{release}
%if %{without espeak}
Obsoletes: brltty-espeak <= 5.6-5
%endif
%description espeak-ng
This package provides the eSpeak-NG driver for BRLTTY.

%package -n brlapi
Version: %{api_version}
Summary: Application Programming Interface for BRLTTY
Requires(pre): glibc-common
Requires(post): coreutils, util-linux
%description -n brlapi
This package provides the run-time support for the Application
Programming Interface to BRLTTY.

Install this package if you have an application which directly accesses
a refreshable braille display.

%package -n brlapi-devel
Version: %{api_version}
Requires: brlapi%{?_isa} = %{api_version}-%{release}
Summary: Headers, static archive, and documentation for BrlAPI
%description -n brlapi-devel
This package provides the header files, static archive, shared object
linker reference, and reference documentation for BrlAPI (the
Application Programming Interface to BRLTTY).  It enables the
implementation of applications which take direct advantage of a
refreshable braille display in order to present information in ways
which are more appropriate for blind users and/or to provide user
interfaces which are more specifically attuned to their needs.

Install this package if you are developing or maintaining an application
which directly accesses a refreshable braille display.

%package -n tcl-brlapi
Version: %{api_version}
Requires: brlapi%{?_isa} = %{api_version}-%{release}
BuildRequires: tcl-devel
Summary: Tcl binding for BrlAPI
%description -n tcl-brlapi
This package provides the Tcl binding for BrlAPI.

%if %{with python2}
%package -n python2-brlapi
%{?python_provide:%python_provide python2-brlapi}
Version: %{api_version}
Requires: brlapi%{?_isa} = %{api_version}-%{release}
BuildRequires: Cython
BuildRequires: python2-devel
BuildRequires: python2-setuptools
Summary: Python binding for BrlAPI
%description -n python2-brlapi
This package provides the Python 2 binding for BrlAPI.
%endif

%if %{with python3}
%package -n python3-brlapi
%{?python_provide:%python_provide python3-brlapi}
Version: %{api_version}
Requires: brlapi%{?_isa} = %{api_version}-%{release}
BuildRequires: python3-Cython
BuildRequires: python3-devel
%if %{without python2}
Obsoletes:     python2-brlapi < %{api_version}-%{release}
Obsoletes:     python-brlapi < %{api_version}-%{release}
%endif
Summary: Python 3 binding for BrlAPI
%description -n python3-brlapi
This package provides the Python 3 binding for BrlAPI.
%endif

%if %{with java}
%package -n brlapi-java
Version: %{api_version}
Requires: brlapi%{?_isa} = %{api_version}-%{release}
BuildRequires: jpackage-utils
BuildRequires: java-devel
Summary: Java binding for BrlAPI
%description -n brlapi-java
This package provides the Java binding for BrlAPI.
%endif

%if %{with ocaml}
%package -n ocaml-brlapi
Version: %{api_version}
Requires: brlapi%{?_isa} = %{api_version}-%{release}
BuildRequires: ocaml
BuildRequires: ocaml-findlib
BuildRequires: make
Summary: OCaml binding for BrlAPI
%description -n ocaml-brlapi
This package provides the OCaml binding for BrlAPI.
%endif

%package dracut
Summary: brltty module for Dracut
Requires: %{name}%{?_isa} = %{pkg_version}-%{release}
Requires: dracut
%description dracut
This package provides brltty module for Dracut.

%if %{with minimal}
%package minimal
Summary: Stripped down brltty version for Anaconda installer
Conflicts: brltty
%description minimal
This package provides stripped down brltty version for Anaconda
installer.
%endif

%define version %{pkg_version}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | cut -d' ' -f1); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -qc
mv %{name}-%{version} python2

pushd python2
%autopatch -p1

# remove packaged binary file
rm -f Programs/brltty-ktb

# produce debuginfo for the OCaml interface
sed -i 's/@OCAMLC@/& -g/;s/@OCAMLOPT@/& -g/;s/@OCAMLMKLIB@/& -g/' \
    Bindings/OCaml/Makefile.in
popd

# Make a copy of the source tree for building the Python 3 module
# Make it all time, we just gonna ignore python2 or python3 when not needed
cp -a python2 python3

%if %{with minimal}
cp -a python2 minimal
%endif

%build

unset MAKEFLAGS
%if %{with java}
for i in -I/usr/lib/jvm/java/include{,/linux}; do
      java_inc="$java_inc $i"
done
export CPPFLAGS="$java_inc"
%endif
export LDFLAGS="%{?build_ldflags}"
export CFLAGS="%{optflags} -fno-strict-aliasing $LDFLAGS"
export CXXFLAGS="%{optflags} -fno-strict-aliasing $LDFLAGS"
configure_opts=" \
  --disable-stripping \
  --without-curses \
%if %{with speech_dispatcher}
  --with-speechd=%{_prefix} \
%endif
%if %{without espeak}
  --without-espeak \
%endif
%if %{with java}
  --with-install-root=%{buildroot} \
  JAVA_JAR_DIR=%{_jnidir} \
  JAVA_JNI_DIR=%{_libdir}/brltty \
  JAVA_JNI=yes"
%else
  --with-install-root=%{buildroot}"
%endif
configure_opts_minimal=" \
  --disable-stripping \
  --without-curses \
  --without-speechd \
  --without-espeak \
  --disable-icu \
  --disable-polkit \
  --disable-java-bindings \
  --disable-ocaml-bindings \
  --disable-python-bindings \
  --disable-speech-support \
  --without-pcm-package \
  --without-midi-package \
  --with-install-root=%{buildroot} \
  --with-configuration-file=brltty-minimal.conf \
  --with-drivers-directory=%{_libdir}/brltty-minimal \
  --with-tables-directory=%{_sysconfdir}/brltty-minimal \
  --with-scripts-directory=%{_libexecdir}/brltty-minimal \
  JAVA_JNI=no"
export PYTHONCOERCECLOCALE=0
PYTHONS=
%if %{with python2}
pushd python2
./autogen
%configure $configure_opts PYTHON=%{__python2}
make
pushd Documents
make
popd
popd
PYTHONS="$PYTHONS python2"
%endif
%if %{with minimal}
pushd minimal
./autogen
%configure $configure_opts_minimal
make
popd
%endif
%if %{with python3}
pushd python3
./autogen
%configure $configure_opts PYTHON=%{__python3} CYTHON=%{_bindir}/cython
make
pushd Documents
make
popd
popd
PYTHONS="$PYTHONS python3"
%endif
for python in $PYTHONS
  do pushd $python
    find . -name '*.sgml' |
    while read file; do
       iconv -f iso8859-1 -t utf-8 $file > $file.conv && mv -f $file.conv $file
    done
    find . -name '*.txt' |
    while read file; do
       iconv -f iso8859-1 -t utf-8 $file > $file.conv && mv -f $file.conv $file
    done
    find . -name 'README*' |
    while read file; do
       iconv -f iso8859-1 -t utf-8 $file > $file.conv && mv -f $file.conv $file
    done
    find . \( -path ./doc -o -path ./Documents \) -prune -o \
      \( -name 'README*' -o -name '*.txt' -o -name '*.html' -o \
         -name '*.sgml' -o -name '*.patch' -o \
         \( -path './Bootdisks/*' -type f -perm /ugo=x \) \) -print |
    while read file; do
       mkdir -p ../doc/${file%/*} && cp -rp $file ../doc/$file || exit 1
    done
  popd
done
%install
%if %{with ocaml}
mkdir -p %{buildroot}%{_libdir}/ocaml/stublibs
%endif
%if %{with python2}
pushd python2
make install JAVA_JAR_DIR=%{_jnidir} \
             JAVA_JNI_DIR=%{_libdir}/brltty \
             JAVA_JNI=yes
popd
%endif
%if %{with minimal}
pushd minimal
make install
pushd %{buildroot}%{_libdir}/brltty-minimal
rm -f libbrlttybba.so libbrlttybxw.so libbrlttyxa2.so libbrlttysen.so \
  libbrlttyses.so libbrlapi_java.so
popd
mv %{buildroot}%{_bindir}/brltty %{buildroot}%{_bindir}/brltty-minimal
install -d -m 755 "%{buildroot}%{_sysconfdir}"
install -p -m 644 Documents/brltty.conf "%{buildroot}%{_sysconfdir}/brltty-minimal.conf"
popd
%endif
%if %{with python3}
pushd python3
make install JAVA_JAR_DIR=%{_jnidir} \
             JAVA_JNI_DIR=%{_libdir}/brltty \
             JAVA_JNI=yes
popd
%endif
%if %{with python3}
pushd python3
%else
pushd python2
%endif
pushd Authorization/Polkit
make install
popd
install -d -m 755 "%{buildroot}%{_sysconfdir}" "%{buildroot}%{_mandir}/man5"
install -p -m 644 Documents/brltty.conf "%{buildroot}%{_sysconfdir}"
echo ".so man1/brltty.1" > %{buildroot}%{_mandir}/man5/brltty.conf.5
install -Dpm 644 %{SOURCE1} %{buildroot}%{_unitdir}/brltty.service
cp -p LICENSE* ../
rm Documents/Manual-*/*/{*.mk,*.made,Makefile*}
mv Documents/BrlAPIref/{html,BrlAPIref}
for i in Drivers/Speech/SpeechDispatcher/README \
         Documents/ChangeLog Documents/TODO \
         Documents/Manual-BRLTTY \
         Drivers/Braille/XWindow/README \
         Drivers/Braille/XWindow/README \
         Documents/Manual-BrlAPI \
         Documents/BrlAPIref/BrlAPIref \
; do
   mkdir -p ../${i%/*} && cp -rp $i ../$i || exit 1
done
rm -rf %{buildroot}/%{_libdir}/libbrlapi.a
mkdir -p %{buildroot}%{_localstatedir}/lib/brltty
touch %{buildroot}%{_sysconfdir}/brlapi.key
chmod 0640 %{buildroot}%{_sysconfdir}/brlapi.key
rm -f %{buildroot}%{_datadir}/gdm/greeter/autostart/xbrlapi.desktop
chmod 755 %{buildroot}%{_bindir}/brltty-config.sh
pushd %{buildroot}%{_includedir}/brltty
for f in config forbuild
do
  mv ./$f.h ./$f-$(getconf LONG_BIT).h
done
install -p -m 0644 %{SOURCE2} ./config.h
install -p -m 0644 %{SOURCE3} ./forbuild.h
popd
%find_lang %{name}
cp -p %{name}.lang ../
make install-dracut
popd
rm -f doc/Initramfs/Dracut/README*
rmdir doc/Initramfs/Dracut doc/Initramfs
install -p -D -m 0644 %{SOURCE4} %{buildroot}%{_sysusersdir}/brltty.conf
%if %{without java}
find . -type d -name 'Java' | xargs rm -rf
find %{buildroot}%{_datadir} -type d -name 'Java' | xargs rm -rf
%oreon_autofiles brltty-speech-dispatcher usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles brltty-docs usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles brltty-xw usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles brltty-at-spi2 usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles brltty-espeak usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles brltty-espeak-ng usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles brlapi usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles brlapi-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles tcl-brlapi usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles python3-brlapi usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles ocaml-brlapi usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles brltty-dracut usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles brltty-minimal usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%endif
%post

%systemd_post brltty.service
%preun

%systemd_preun brltty.service
%postun

%systemd_postun_with_restart brltty.service
%post -n brlapi

if [ ! -e %{_sysconfdir}/brlapi.key ]; then
  mcookie > %{_sysconfdir}/brlapi.key
  chgrp brlapi %{_sysconfdir}/brlapi.key
  chmod 0640 %{_sysconfdir}/brlapi.key
fi
%{?ldconfig}
%ldconfig_postun -n brlapi
%files -f %{oreon_filedir}/main.list
%files -n brltty-speech-dispatcher -f %{oreon_filedir}/brltty-speech-dispatcher.list
%files -n brltty-docs -f %{oreon_filedir}/brltty-docs.list
%files -n brltty-xw -f %{oreon_filedir}/brltty-xw.list
%files -n brltty-at-spi2 -f %{oreon_filedir}/brltty-at-spi2.list
%files -n brltty-espeak -f %{oreon_filedir}/brltty-espeak.list
%files -n brltty-espeak-ng -f %{oreon_filedir}/brltty-espeak-ng.list
%files -n brlapi -f %{oreon_filedir}/brlapi.list
%files -n brlapi-devel -f %{oreon_filedir}/brlapi-devel.list
%files -n tcl-brlapi -f %{oreon_filedir}/tcl-brlapi.list
%files -n python3-brlapi -f %{oreon_filedir}/python3-brlapi.list
%files -n ocaml-brlapi -f %{oreon_filedir}/ocaml-brlapi.list
%files -n brltty-dracut -f %{oreon_filedir}/brltty-dracut.list
%files -n brltty-minimal -f %{oreon_filedir}/brltty-minimal.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.9-1
- Import
