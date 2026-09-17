%global source0_hash 356680d63fca885806c49987ebd4720107873ecbcb050fe8711a8131cc68c268
%global _build_id_links none

%define pkg_version 6.9
%define api_version 0.8.8

# minimal means brltty-minimal subpackage with minimal deps for
# braille support in Anaconda installer
# https://bugzilla.redhat.com/show_bug.cgi?id=1584679
%bcond minimal 1

# enable python3 by default
%bcond python3 1

# disable python2 by default
%bcond python2 0

%if 0%{?oreon} >= 11
%global tcl_version 9.0
%else
%{!?tcl_version: %global tcl_version 8.6}
%endif
%{!?tcl_sitearch: %global tcl_sitearch %{_libdir}/tcl%{tcl_version}}

# with speech dispatcher iff on Fedora:
%bcond speech_dispatcher %{defined fedora}

# with espeak support iff on Fedora:
%bcond espeak %{defined fedora}

# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
%ifnarch %{ix86}
%bcond ocaml %{defined fedora}
%endif

%ifarch %{java_arches}
%bcond java %{defined fedora}
%endif

# Filter private libraries
%global _privatelibs libbrltty.+\.so.*
%global __provides_exclude ^(%{_privatelibs})$
%global __requires_exclude ^(%{_privatelibs})$

Name: brltty
Version: 6.9
Release: 2%{?dist}
License: LGPL-2.0-or-later AND LGPL-2.1-or-later AND GPL-2.0-or-later
URL: http://brltty.app/
Source0:        https://brltty.app/archive/%{name}-%{version}.tar.xz
Source1:        brltty.service
Source2:        brlapi-config.h
Source3:        brlapi-forbuild.h
Source4:        brltty.sysusers
Patch1:        brltty-6.3-loadLibrary.patch
# libspeechd.h moved in latest speech-dispatch (NOT sent upstream)
Patch2:        brltty-6.8-libspeechd.patch
Summary: Braille display driver for Linux/Unix
BuildRequires: byacc
BuildRequires: glibc-kernheaders
BuildRequires: gcc
BuildRequires: bluez-libs-devel
BuildRequires: systemd
BuildRequires: systemd-rpm-macros
BuildRequires: lua-devel
BuildRequires: gettext
BuildRequires: at-spi2-core-devel
BuildRequires: alsa-lib-devel
%if %{with espeak}
BuildRequires: espeak-devel
%endif
BuildRequires: espeak-ng-devel
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: polkit-devel
BuildRequires: libicu-devel
BuildRequires: doxygen
BuildRequires: linuxdoc-tools
BuildRequires: ncurses-devel
%if %{with python2}
BuildRequires: python2-docutils
BuildRequires: python2-setuptools
%endif
%if %{with python3}
BuildRequires: python3-docutils
BuildRequires: python3-setuptools
%endif
Conflicts: brltty-minimal

# work around a bug in the install process:
Requires(post): coreutils
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd

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
# If MAKEFLAGS=-jN is set it would break local builds.
unset MAKEFLAGS

%if %{with java}
# Add the openjdk include directories to CPPFLAGS
for i in -I/usr/lib/jvm/java/include{,/linux}; do
      java_inc="$java_inc $i"
done
export CPPFLAGS="$java_inc"
%endif

export LDFLAGS="%{?build_ldflags}"
export CFLAGS="%{optflags} -fno-strict-aliasing $LDFLAGS"
export CXXFLAGS="%{optflags} -fno-strict-aliasing $LDFLAGS"

# there is no curses packages in BuildRequires, so the package builds
# without them in mock; let's express this decision explicitly
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
# First build everything with Python 2 support
pushd python2
./autogen
%configure $configure_opts PYTHON=%{__python2}
# Parallel build seems broken, thus disabling it
make

# documents
pushd Documents
make
popd

popd
PYTHONS="$PYTHONS python2"
%endif


%if %{with minimal}
# ... and then do it again for minimal
pushd minimal
./autogen
%configure $configure_opts_minimal
make

popd
%endif


%if %{with python3}
# ... and then do it again for the Python 3 module
pushd python3
./autogen
%configure $configure_opts PYTHON=%{__python3} CYTHON=%{_bindir}/cython
make

# documents
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
# Python 2
pushd python2
make install JAVA_JAR_DIR=%{_jnidir} \
             JAVA_JNI_DIR=%{_libdir}/brltty \
             JAVA_JNI=yes
popd
%endif


%if %{with minimal}
# minimal
pushd minimal
make install

# drop extra drivers
pushd %{buildroot}%{_libdir}/brltty-minimal
rm -f libbrlttybba.so libbrlttybxw.so libbrlttyxa2.so libbrlttysen.so \
  libbrlttyses.so libbrlapi_java.so
popd

# rename brltty to brltty-minimal
mv %{buildroot}%{_bindir}/brltty %{buildroot}%{_bindir}/brltty-minimal

# install config
install -d -m 755 "%{buildroot}%{_sysconfdir}"
install -p -m 644 Documents/brltty.conf "%{buildroot}%{_sysconfdir}/brltty-minimal.conf"
popd
%endif


%if %{with python3}
# Python 3
pushd python3
make install JAVA_JAR_DIR=%{_jnidir} \
             JAVA_JNI_DIR=%{_libdir}/brltty \
             JAVA_JNI=yes
popd
%endif

%if %{with python3}
# just use the higher number here
pushd python3
%else
pushd python2
%endif

# install polkit rules
pushd Authorization/Polkit
make install
popd

install -d -m 755 "%{buildroot}%{_sysconfdir}" "%{buildroot}%{_mandir}/man5"
install -p -m 644 Documents/brltty.conf "%{buildroot}%{_sysconfdir}"
echo ".so man1/brltty.1" > %{buildroot}%{_mandir}/man5/brltty.conf.5

install -Dpm 644 %{SOURCE1} %{buildroot}%{_unitdir}/brltty.service

cp -p LICENSE* ../

# clean up the manuals:
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

# don't want static lib
rm -rf %{buildroot}/%{_libdir}/libbrlapi.a

# create /var/lib/brltty directory
mkdir -p %{buildroot}%{_localstatedir}/lib/brltty

# ghost brlapi.key
touch %{buildroot}%{_sysconfdir}/brlapi.key
chmod 0640 %{buildroot}%{_sysconfdir}/brlapi.key

# disable xbrlapi gdm autostart, there is already orca
rm -f %{buildroot}%{_datadir}/gdm/greeter/autostart/xbrlapi.desktop

# make brltty-config executable
chmod 755 %{buildroot}%{_bindir}/brltty-config.sh

# fix multilib
pushd %{buildroot}%{_includedir}/brltty
for f in config forbuild
do
  mv ./$f.h ./$f-$(getconf LONG_BIT).h
done
install -p -m 0644 %{SOURCE2} ./config.h
install -p -m 0644 %{SOURCE3} ./forbuild.h
popd

# handle locales
%find_lang %{name}
cp -p %{name}.lang ../

# install dracut module
make install-dracut

popd

# drop documentation already instaled by the dracut subpackage
rm -f doc/Initramfs/Dracut/README*
rmdir doc/Initramfs/Dracut doc/Initramfs

# Install group creation file
install -p -D -m 0644 %{SOURCE4} %{buildroot}%{_sysusersdir}/brltty.conf

%if %{without java}
find . -type d -name 'Java' | xargs rm -rf
find %{buildroot}%{_datadir} -type d -name 'Java' | xargs rm -rf
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

%files -f %{name}.lang
%dir %{_localstatedir}/lib/brltty
%config(noreplace) %{_sysconfdir}/brltty.conf
%{_sysconfdir}/brltty/
%exclude %{_sysconfdir}/brltty/Initramfs
%{_unitdir}/brltty.service
%{_bindir}/brltty
%{_bindir}/brltty-*
%exclude %{_bindir}/brltty-minimal
%{_libdir}/brltty/
%if %{with java}
%exclude %{_libdir}/brltty/libbrlapi_java.so
%endif
# brlapi subpackage
%exclude %{_libdir}/brltty/libbrlttybba.so
# xw subpackage
%exclude %{_libdir}/brltty/libbrlttybxw.so
# at-spi2 subpackage
%exclude %{_libdir}/brltty/libbrlttyxa2.so
# espeak-ng subpackage
%exclude %{_libdir}/brltty/libbrlttysen.so
%if %{with espeak}
%exclude %{_libdir}/brltty/libbrlttyses.so
%endif
%if %{with speech_dispatcher}
%exclude %{_libdir}/brltty/libbrlttyssd.so
%endif
%license LICENSE-LGPL
%doc %{_mandir}/man[15]/brltty.*
%{_sysconfdir}/X11/Xsession.d/90xbrlapi
%{_datadir}/polkit-1/actions/org.a11y.brlapi.policy
%{_datadir}/polkit-1/rules.d/org.a11y.brlapi.rules

%if %{with minimal}
%files minimal -f %{name}.lang
%config(noreplace) %{_sysconfdir}/brltty-minimal.conf
%{_sysconfdir}/brltty-minimal/
%{_bindir}/brltty-minimal
%{_libdir}/brltty-minimal/
%license LICENSE-LGPL
%endif

%if %{with speech_dispatcher}
%files speech-dispatcher
%doc Drivers/Speech/SpeechDispatcher/README
%{_libdir}/brltty/libbrlttyssd.so
%endif

%files docs
%doc Documents/ChangeLog Documents/TODO
%doc Documents/Manual-BRLTTY/
#%doc doc/*

%files xw
%doc Drivers/Braille/XWindow/README
%{_libdir}/brltty/libbrlttybxw.so

%files at-spi2
%{_libdir}/brltty/libbrlttyxa2.so

%if %{with espeak}
%files espeak
%{_libdir}/brltty/libbrlttyses.so
%endif

%files espeak-ng
%{_libdir}/brltty/libbrlttysen.so

%files -n brlapi
%{_bindir}/vstp
%{_bindir}/eutp
%{_bindir}/xbrlapi
%dir %{_libdir}/brltty
%{_libdir}/brltty/libbrlttybba.so
%{_libdir}/libbrlapi.so.*
%ghost %verify(not group) %{_sysconfdir}/brlapi.key
%doc Drivers/Braille/XWindow/README
%doc Documents/Manual-BrlAPI/
%doc %{_mandir}/man1/xbrlapi.*
%doc %{_mandir}/man1/vstp.*
%doc %{_mandir}/man1/eutp.*
%{_sysusersdir}/brltty.conf
%{lua_libdir}/brlapi.so

%files -n brlapi-devel
%{_libdir}/libbrlapi.so
%{_includedir}/brltty
%{_includedir}/brlapi*.h
%{_libdir}/pkgconfig/brltty.pc
%doc %{_mandir}/man3/brlapi_*.3*
%doc Documents/BrlAPIref/BrlAPIref/

%files -n tcl-brlapi
%{tcl_sitearch}/brlapi-%{api_version}

%if %{with python2}
%files -n python2-brlapi
%{python2_sitearch}/brlapi.so
%{python2_sitearch}/Brlapi-%{api_version}-*.egg-info
%endif

%if %{with python3}
%files -n python3-brlapi
%{python3_sitearch}/brlapi.cpython-*.so
%{python3_sitearch}/Brlapi-%{api_version}-*.egg-info
%endif

%if %{with java}
%files -n brlapi-java
%{_libdir}/brltty/libbrlapi_java.so
%{_jnidir}/brlapi.jar
%endif

%if %{with ocaml}
%files -n ocaml-brlapi
%{_libdir}/ocaml/brlapi/
%{_libdir}/ocaml/stublibs/
%endif

%files dracut
%{_prefix}/lib/dracut/modules.d/99brltty/
%dir %{_sysconfdir}/brltty/Initramfs
%config(noreplace) %verify(not size md5 mtime) %{_sysconfdir}/brltty/Initramfs/dracut.conf
%config(noreplace) %verify(not size md5 mtime) %{_sysconfdir}/brltty/Initramfs/cmdline

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.9-1
- Import
