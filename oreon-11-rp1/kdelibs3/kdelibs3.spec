%global source0_hash 617e9cb01c70ed4c1b554b373f55deffbd0e12e2cdfeacd7b3d9409372285c72

# kdelibs3 review: http://bugzilla.redhat.com/248899

%define _default_patch_fuzz 2

%define arts_ev 8:1.5.10
%define qt3 qt3
%define qt3_version 3.3.8b
%define qt3_ev %{?qt3_epoch}%{qt3_version} 
%define qt3_docdir %{_docdir}/qt-devel-%{qt3_version}

%define kde_major_version 3

%define apidocs 0

# trim changelog included in binary rpms
%global _changelog_trimtime %(date +%s -d "1 year ago")

# Disable automatic .la file removal
%global __brp_remove_la_files %nil

Summary: KDE 3 Libraries
Name:    kdelibs3
Version: 3.5.10
Release: 135%{?dist}

License: LGPL-2.0-only
Url: http://www.kde.org/

Source0: ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kdelibs-%{version}.tar.bz2
Source3: devices.protocol

Patch1: kdelibs-3.5.1-xdg-menu.patch
Patch2: kdelibs-3.0.0-ndebug.patch
Patch4: kdelibs-3.0.4-ksyscoca.patch
Patch5: kdelibs-3.5.10-openssl.patch
Patch15: kdelibs-3.4.91-buildroot.patch
Patch32: kdelibs-3.2.3-cups.patch
Patch33: kdelibs-3.3.2-ppc.patch
Patch34: kdelibs-3.4.0-qtdoc.patch
Patch35: kdelibs-3.4.92-inttype.patch
Patch37: kdelibs-3.5.2-kdebug-kmail-quiet.patch
Patch38: kdelibs-3.5.2-cupsdconf2-group.patch
Patch39: kdelibs-3.5.4-kabc-make.patch
Patch40: kdelibs-3.5.4-kdeprint-utf8.patch
Patch41: kdelibs-3.5.6-utempter.patch
Patch43: kdelibs-3.5.6-lang.patch
Patch45: kdelibs-3.5.7-autostart.patch
Patch46: kdelibs-3.5.8-kate-vhdl.patch
Patch48: kdelibs-3.5.8-kspell-hunspell.patch
Patch49: kdelibs-3.5.8-kspell2-enchant.patch
Patch50: kdelibs-3.5.8-kspell2-no-ispell.patch
Patch51: kdelibs-3.5.9-cupsserverbin.patch
# initial support for (Only|Not)ShowIn=KDE3
Patch52: kdelibs-3.5.9-KDE3.patch
# use newer/plasma drkonqi in KCrash (#453243)
Patch53: kdelibs-3.5.10-drkonqi-plasma5.patch
# use inotify_* functions which are defined in glibc-header
Patch54: kdelibs-3.5.10-inotify.patch
# update the KatePart latex.xml syntax definition to the version from Kile 2.0.3
Patch55: kdelibs-3.5.10-latex-syntax-kile-2.0.3.patch
# fix ftbfs (#631195)
Patch56: kdelibs-3.5.10-qcolor_gcc_ftbfs.patch
# fix FTBFS (cups-util.c must include stdio.h, #714133)
Patch57: kdelibs-3.5.10-cups-util-missing-header.patch
# fix FTBFS with CUPS 2.0 due to bad CUPS_VERSION_MAJOR checks
Patch58: kdelibs-3.5.10-cups20.patch
Patch59: kdelibs-3.5.10-gcc6.patch
# fix endless loop in svgicon
Patch60: kdelibs-3.5.10-svgicon-endlessloop.patch
# fix FTBFS with gcc7
Patch61: kdelibs-3.5.10-gcc7.patch

# libidn2 support for > f26
Patch62:  kdelibs-3-libidn2.patch

# use /etc/kde in addition to /usr/share/config, borrowed from debian
Patch100: kdelibs-3.5.5-kstandarddirs.patch
# http://bugs.kde.org/93359, alternative to export libltdl_cv_shlibext=".so" hack.
Patch101: kde-3.5-libtool-shlibext.patch
# kget ignores simultaneous download limit (kde #101956)
Patch103: kdelibs-3.5.0-101956.patch
Patch104: kdelibs-3.5.10-gcc44.patch
Patch105: kdelibs-3.5.10-ossl-1.x.patch
Patch106: kdelibs-3.5.10-kio.patch
Patch107: kdelibs-3.5.10-assert.patch
Patch108: kdelibs-3.5.10-dtoa.patch
Patch109: kdelibs-3.5.10-kabc.patch
# kde4.4 backport
Patch111: kdelibs-3.5.10-kde-config_kde-version.patch
# ftbfs
Patch112: kdelibs-3.5.10-dup-ftbfs.patch

## Trinity backports
# build fix for CUPS 1.6 by Timothy Pearson, backported by Kevin Kofler
# http://git.trinitydesktop.org/cgit/tdelibs/commit?id=9bc0d2cd9d38750658770e69bf0445dc5162beb7
# http://git.trinitydesktop.org/cgit/tdelibs/commit?id=91bf63b43bf4cc9ff640bd3c11549644cef05e6e
Patch150: kdelibs-3.5.10-cups16.patch
# build fix for CUPS 2.2 by Slávek Banko, backported by Kevin Kofler
# http://git.trinitydesktop.org/cgit/tdelibs/commit/?id=52a1b55368ec53b14347996851aca7eb29374397
Patch151: kdelibs-3.5.10-cups22.patch
# OpenSSL 1.1 support by Slávek Banko (with prerequisite patch by Timothy
# Pearson), backported by Kevin Kofler
# http://git.trinitydesktop.org/cgit/tdelibs/commit/?id=e757d3d6ae93cf967d54c566e9c003b0f9cc3a9c
# http://git.trinitydesktop.org/cgit/tdelibs/commit/?id=e1861cb6811f7bac405ece204407ca46c000a453
Patch152: kdelibs-3.5.10-openssl-1.1.patch
# native support for xdg-user-dirs, without shelling out to xdg-user-dir from
# the config file (by Timothy Pearson), needed after the CVE-2019-14744 fix,
# backported by Kevin Kofler
# http://mirror.git.trinitydesktop.org/cgit/tdelibs/commit/kdecore/kglobalsettings.cpp?id=865f314dd5ed55508f45a32973b709b79a541e36
# http://mirror.git.trinitydesktop.org/cgit/tdelibs/commit/?id=ae5384b4bdea0c9ab28322bb53183bef569c77c5
Patch153: kdelibs-3.5.10-kglobalsettings-xdg-user-dirs.patch
# fix accidental double-free in KJS garbage collector, by Timothy Pearson
# backported by Wolfgang Bauer from OpenSUSE
# http://mirror.git.trinitydesktop.org/cgit/tdelibs/commit/?id=36a7df39b0f89c467fc6d9c957a7a30f20d96994
# https://bugs.trinitydesktop.org/show_bug.cgi?id=2116
Patch154: kdelibs-3.5.10-fix-accidental-double-free-in-kjs-garbage-collector.patch
# Process the new (libice 1.0.10) location of the ICEauthority file (#1768193)
# patch by Slávek Banko, backported by Kevin Kofler
# http://mirror.git.trinitydesktop.org/cgit/tdelibs/commit/?id=38b2b0be7840d868c21093a406ab98a646212de1
# https://bugs.trinitydesktop.org/show_bug.cgi?id=3027
Patch155: kdelibs-3.5.10-libice-1.0.10.patch

## security fixes
# fix CVE-2009-2537 - select length DoS
Patch200: kdelibs-3.5.10-cve-2009-2537-select-length.patch
# fix CVE-2009-1725 - crash, possible ACE in numeric character references
Patch201: kdelibs-3.5.10-cve-2009-1725.patch
# fix CVE-2009-1690 - crash, possible ACE in KHTML (<head> use-after-free)
Patch202: kdelibs-3.5.4-CVE-2009-1687.patch
# fix CVE-2009-1687 - possible ACE in KJS (FIXME: still crashes?)
Patch203: kdelibs-3.5.4-CVE-2009-1690.patch
# fix CVE-2009-1698 - crash, possible ACE in CSS style attribute handling
Patch204: kdelibs-3.5.10-cve-2009-1698.patch
# fix CVE-2009-2702 - ssl incorrect verification of SSL certificate with NUL in subjectAltName
Patch205: kdelibs-3.5.10-CVE-2009-2702.patch
# fix oCERT-2009-015 - unrestricted XMLHttpRequest access to local URLs
Patch206: kdelibs-3.5.10-oCERT-2009-015-xmlhttprequest.patch
# CVE-2009-3736, libltdl may load and execute code from a library in the current directory
Patch207: libltdl-CVE-2009-3736.patch
# CVE-2011-3365, input validation failure in KSSL
Patch208: kdelibs-3.5.x-CVE-2011-3365.patch
# CVE-2013-2074, prints passwords contained in HTTP URLs in error messages
Patch209: kdelibs-3.5.10-CVE-2013-2074.patch
# CVE-2015-7543 arts,kdelibs3: Use of mktemp(3) allows attacker to hijack the IPC
# backport upstream fix (the lnusertemp.c change) from kdelibs 4:
# http://commits.kde.org/kdelibs/cc5515ed7ce8884c9b18169158ba29ab2f7a3db7
# upstream fix by Joseph Wenninger, rediffed for kdelibs 3.5.10 by Kevin Kofler
Patch210: kdelibs-3.5.10-CVE-2015-7543.patch
# CVE-2016-6232 - directory traversal vulnerability in KArchive
# patch from Trinity (Slávek Banko), based on KF5 fix (Andreas Cord-Landwehr)
Patch211: kdelibs-3.5.10-CVE-2016-6232.patch
# CVE-2017-6410 - info leak when accessing https when using a malicious PAC file
# backport upstream fix (by Albert Astals Cid) from kdelibs 4:
# http://commits.kde.org/kdelibs/1804c2fde7bf4e432c6cf5bb8cce5701c7010559
Patch212: kdelibs-3.5.10-CVE-2017-6410.patch
# CVE-2019-14744 - kconfig: malicious .desktop files (and others) would execute code
# backport upstream fix (by David Faure, backported to kdelibs 4 by Kai Uwe
# Broulik) from kdelibs 4 (backported by Kevin Kofler):
# http://commits.kde.org/kdelibs/2c3762feddf7e66cf6b64d9058f625a715694a00
Patch213: kdelibs-3.5.10-CVE-2019-14744.patch

## fixes to common KDE 3 autotools machinery
# tweak autoconfigury so that it builds with autoconf 2.64 or 2.65
Patch300: kde3-acinclude.patch
# remove flawed and obsolete automake version check in admin/cvs.sh
Patch301: kde3-automake-version.patch
# fix build failure with automake 1.13: add the --add-missing --copy flags
# also add --force-missing to get aarch64 support (#925029/#925627)
Patch302: kde3-automake-add-missing.patch
# fix aarch64 FTBFS due to libtool not liking the file output on *.so files
Patch303: kde3-libtool-aarch64.patch
# Fix configure bits compromised by LTO optimizations
Patch304: kdelibs-3.5.10-configure.patch
# autoconf 2.7x
Patch305: kde3-autoconf-version.patch
Patch306: kdelibs3-c99.patch
# Fix compilation with libxml2 2.12.0
Patch307: kdelibs-3.5.10-libxml2-2_12_0.patch
Patch308: kdelibs3-c99-2.patch
# tweak autoconfigury so that it builds with autoconf 2.72
# https://src.fedoraproject.org/rpms/kdebase3/c/91233a5b909d09775930236bd21556faa993176f?branch=rawhide
Patch309: kde3-autoconf-2.72.patch

Requires: /etc/pki/ca-trust/extracted/pem/tls-ca-bundle.pem
Requires: hicolor-icon-theme
Requires: kde-settings >= 3.5
%if 0%{?fedora} >= 40 || 0%{?rhel} >= 10
Requires: kde3-filesystem
%else
Requires: kde-filesystem
%endif
Requires: kdelibs-common
Requires: redhat-menus
Requires: shadow-utils
#Requires: sudo
BuildRequires: sudo

BuildRequires: xorg-x11-proto-devel libX11-devel
%define _with_rgbfile --with-rgbfile=%{_datadir}/X11/rgb.txt
Requires: iceauth

Requires(pre): coreutils
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
Requires: hunspell

BuildRequires: gcc-c++
BuildRequires: gettext
BuildRequires: pcre-devel
BuildRequires: cups-devel cups
BuildRequires: %{qt3}-devel %{qt3}-devel-docs
BuildRequires: arts-devel >= %{arts_ev}
BuildRequires: flex >= 2.5.4a-13
BuildRequires: doxygen
BuildRequires: libxslt-devel
BuildRequires: sgml-common
BuildRequires: openjade
BuildRequires: jadetex
BuildRequires: docbook-dtd31-sgml
BuildRequires: docbook-style-dsssl
BuildRequires: perl-generators
BuildRequires: perl-SGMLSpm
BuildRequires: docbook-utils
BuildRequires: zlib-devel
%if 0%{?fedora} > 26 || 0%{?rhel} > 7
BuildRequires: libidn2-devel
%else
BuildRequires: libidn-devel
%endif
BuildRequires: audiofile-devel
BuildRequires: openssl-devel
BuildRequires: perl-interpreter
BuildRequires: gawk
BuildRequires: byacc
BuildRequires: libart_lgpl-devel
BuildRequires: bzip2-devel
BuildRequires: libtiff-devel
BuildRequires: libacl-devel libattr-devel
BuildRequires: enchant-devel
BuildRequires: krb5-devel
BuildRequires: openldap-devel
BuildRequires: alsa-lib-devel
%if 0%{?fedora} > 25 || 0%{?rhel} > 7
BuildRequires: pkgconf-pkg-config
%else
BuildRequires: pkgconfig
%endif
BuildRequires: glibc-kernheaders
BuildRequires: libutempter-devel
BuildRequires: findutils
BuildRequires: jasper-devel
BuildRequires: OpenEXR-devel
BuildRequires: automake libtool
BuildRequires: chrpath
BuildRequires: make
BuildRequires: /etc/pki/ca-trust/extracted/pem/tls-ca-bundle.pem

%if "%{name}" != "kdelibs" && "%{?apidocs}" != "1"
Obsoletes: kdelibs-apidocs < 6:%{version}-%{release}
%endif

Provides: crystalsvg-icon-theme = 1:%{version}-%{release}
Obsoletes: crystalsvg-icon-theme < 1:%{version}-%{release}

%description
Libraries for KDE 3:
KDE Libraries included: kdecore (KDE core library), kdeui (user interface),
kfm (file manager), khtmlw (HTML widget), kio (Input/Output, networking),
kspell (spelling checker), jscript (javascript), kab (addressbook),
kimgio (image manipulation).

%package devel
Summary: Header files and documentation for compiling KDE 3 applications.
Requires: %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: %{qt3}-devel
Requires: openssl-devel
Requires: arts-devel
Requires: gcc-c++
%{?libkdnssd:Requires: libkdnssd-devel}
%description devel
This package includes the header files you will need to compile
applications for KDE 3.

%package apidocs
Summary: KDE 3 API documentation.
Requires: kde-filesystem
BuildArch: noarch
%description apidocs
This package includes the KDE 3 API documentation in HTML
format for easy browsing

%package tools
Summary: KDE 3 tools.
Requires: %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
%description tools
This package includes tools kgrantpty and kpac_dhcp_helper.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n kdelibs-%{version}

%patch -P1 -p1 -b .xdg-menu
%patch -P2 -p1 -b .debug
%patch -P4 -p1 -b .ksyscoca
%patch -P5 -p1 -b .openssl
%patch -P15 -p1 -b .buildroot
%patch -P32 -p1 -b .cups
%patch -P33 -p1 -b .ppc
%patch -P34 -p1 -b .qtdoc
%patch -P35 -p1 -b .inttype
%patch -P37 -p1 -b .kdebug-kmail-quiet
%patch -P38 -p1 -b .cupsdconf2-group
%patch -P39 -p1 -b .kabc-make
%patch -P40 -p1 -b .kdeprint-utf8
%patch -P41 -p1 -b .utempter
%patch -P43 -p1 -b .lang
%patch -P45 -p1 -b .xdg-autostart
%patch -P46 -p1 -b .kate-vhdl
%patch -P48 -p1 -b .kspell
%patch -P49 -p1 -b .kspell2
%patch -P50 -p1 -b .no-ispell
%patch -P51 -p1 -b .cupsserverbin
%patch -P52 -p1 -b .KDE3
%patch -P53 -p1 -b .drkonqi-plasma5
%patch -P54 -p1 -b .inotify
%patch -P55 -p1 -b .latex-syntax
%patch -P56 -p1 -b .qcolor_gcc_ftbfs
%patch -P57 -p1 -b .cups-util
%patch -P58 -p1 -b .cups20
%patch -P59 -p1 -b .gcc6
%patch -P60 -p1 -b .endless-loop
%patch -P61 -p1 -b .gcc7
%if 0%{?fedora} > 26 || 0%{?rhel} > 7
%patch -P62 -p1 -b .libidn2
%endif
%patch -P100 -p1 -b .kstandarddirs
%patch -P101 -p1 -b .libtool-shlibext
%patch -P104 -p1 -b .gcc44
%patch -P105 -p1 -b .ossl-1.x
%patch -P106 -p1 -b .kio
%patch -P107 -p1 -b .assert
%patch -P108 -p1 -b .alias
%patch -P109 -p1 -b .kabc
%patch -P111 -p1 -b .kde-config_kde-version
%patch -P112 -p1 -b .dup

%patch -P150 -p1 -b .cups16
%patch -P151 -p1 -b .cups22
%patch -P155 -p1 -b .libice-1.0.10

# security fixes
%patch -P200 -p1 -b .cve-2009-2537
%patch -P201 -p0 -b .cve-2009-1725
%patch -P202 -p1 -b .cve-2009-1687
%patch -P203 -p1 -b .cve-2009-1690
%patch -P204 -p1 -b .cve-2009-1698
%patch -P205 -p1 -b .cve-2009-2702
%patch -P206 -p0 -b .oCERT-2009-015-xmlhttprequest
%patch -P207 -p1 -b .CVE-2009-3736
%patch -P208 -p1 -b .CVE-2011-3365
%patch -P209 -p1 -b .CVE-2013-2074
%patch -P210 -p1 -b .CVE-2015-7543
%patch -P211 -p1 -b .CVE-2016-6232
%patch -P212 -p1 -b .CVE-2017-6410
%patch -P213 -p1 -b .CVE-2019-14744

# must be applied after the ossl-1.x patch (105) and the CVE-2009-2702 fix (205)
%patch -P152 -p1 -b .openssl-1.1
# goes along with the CVE-2019-14744 fix (ordering not strictly required)
%patch -P153 -p1 -b .xdg-user-dirs
# must be applied after the CVE-2009-1687 fix
%patch -P154 -p1 -b .kjs-double-free

%patch -P300 -p1 -b .acinclude
%patch -P301 -p1 -b .automake-version
%patch -P302 -p1 -b .automake-add-missing
%patch -P303 -p1 -b .libtool-aarch64
%patch -P304 -p1 -b .configure
%patch -P305 -p1 -b .autoconf2.7x
%patch -P306 -p1
%patch -P307 -p1 -b .libxml2_2_12_0
%patch -P 308 -p1
%patch -P 309 -p1

make -f admin/Makefile.common cvs

%build
unset QTDIR && . /etc/profile.d/qt.sh

export QTDOC=%{qt3_docdir}

if [ -x /etc/profile.d/krb5.sh ]; then
  . /etc/profile.d/krb5.sh
elif ! echo ${PATH} | grep -q /usr/kerberos/bin ; then
  export PATH=/usr/kerberos/bin:${PATH}
fi

%if "%{name}" != "kdelibs"
export DO_NOT_COMPILE="libkscreensaver"
%endif

# drop the extra -Werror= flags for C, they break the configure script
export CFLAGS="%{optflags}"
export CXXFLAGS="%{optflags} -Wno-deprecated-declarations -Wno-narrowing -std=gnu++98"

%configure \
   --includedir=%{_includedir}/kde \
   --disable-rpath \
   --disable-new-ldflags \
   --disable-debug --disable-warnings \
   --disable-final \
   --disable-fast-malloc \
%if "%{_lib}" == "lib64"
  --enable-libsuffix="64" \
%endif
   --enable-cups \
   --enable-mitshm \
   --enable-pie \
   --enable-sendfile \
   --with-distribution="$(cat /etc/redhat-release 2>/dev/null)" \
   --with-alsa \
   --without-aspell \
   --without-hspell \
   --disable-libfam \
   --enable-dnotify \
   --enable-inotify \
   --with-utempter \
   %{?_with_rgbfile} \
   --with-jasper \
   --with-openexr \
   --with-xinerama

# kill rpath harder, inspired by https://fedoraproject.org/wiki/Packaging:Guidelines?rd=Packaging/Guidelines#Removing_Rpath
# other more standard variants didnt work or caused other problems
sed -i -e 's|"/lib /usr/lib|"/%{_lib} %{_libdir}|' libtool

%if 0%{?apidocs}
  doxygen -s -u admin/Doxyfile.global
  %make_build apidox
%endif

# https://koji.fedoraproject.org/koji/taskinfo?taskID=82799269
# agent.cpp:21:10: warning: addressee.h is shorter than expected
# disable parallel make for now
%make_build -j1

%install
%make_install

# create/own, see http://bugzilla.redhat.com/483318
mkdir -p %{buildroot}%{_libdir}/kconf_update_bin

chmod a+x %{buildroot}%{_libdir}/*
install -p -m 644 %{SOURCE3} %{buildroot}%{_datadir}/services/devices.protocol

%if 0%{?apidocs}
pushd %{buildroot}%{_docdir}
ln -sf HTML/en/kdelibs-apidocs %{name}-devel-%{kde_major_version}
popd
%endif

# Make symlinks relative
pushd %{buildroot}%{_docdir}/HTML/en
for i in *; do
   if [ -d $i -a -L $i/common ]; then
      rm -f $i/common
      ln -sf ../common $i
   fi
done
popd

# Use hicolor-icon-theme rpm/pkg instead (#178319)
rm -rf $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/

# ghost'd files
touch $RPM_BUILD_ROOT%{_datadir}/services/ksycoca

# remove references to extraneous/optional libraries in .la files (#170602)
# fam, libart_lgpl, pcre, libidn, libpng, libjpeg, libdns_sd, libacl/libattr, alsa-lib/asound
find $RPM_BUILD_ROOT%{_libdir} -name "*.la" | xargs \
 sed -i \
 -e "s@-lfam@@g" \
 -e "s@%{_libdir}/libfam.la@@g" \
 -e "s@-lart_lgpl_2@@g" \
 -e "s@%{_libdir}/libpcreposix.la@@g" \
 -e "s@-lpcreposix@@g" \
 -e "s@-lpcre@@g" \
 -e "s@-lidn2\?@@g" \
 -e "s@%{_libdir}/libidn2\?.la@@g" \
 -e "s@-lpng@@g" \
 -e "s@-ljpeg@@g" \
 -e "s@%{_libdir}/libjpeg.la@@g" \
 -e "s@-ldns_sd@@g" \
 -e "s@-lacl@@g" \
 -e "s@%{_libdir}/libacl.la@@g" \
 -e "s@/%{_lib}/libacl.la@@g" \
 -e "s@-lattr@@g" \
 -e "s@%{_libdir}/libattr.la@@g" \
 -e "s@/%{_lib}/libattr.la@@g" \
 -e "s@-lasound@@g"  \
 -e "s@-lutempter@@g"

# libkdnssd bits
rm -f %{buildroot}%{_libdir}/libkdnssd.la
%{?libkdnssd:rm -rf %{buildroot}{%{_libdir}/libkdnssd.*,%{_includedir}/kde/dnssd}}

# remove conflicts with kdelibs-4
rm -f %{buildroot}%{_bindir}/checkXML
rm -fv %{buildroot}%{_bindir}/kmailservice
rm -fv %{buildroot}%{_bindir}/ksvgtopng
rm -fv %{buildroot}%{_bindir}/ktelnetservice
rm -f %{buildroot}%{_bindir}/kunittestmodrunner
rm -f %{buildroot}%{_datadir}/config/kdebug.areas
rm -f %{buildroot}%{_datadir}/config/kdebugrc
rm -f %{buildroot}%{_datadir}/config/ui/ui_standards.rc
rm -f %{buildroot}%{_docdir}/HTML/en/common/1.png
rm -f %{buildroot}%{_docdir}/HTML/en/common/10.png
rm -f %{buildroot}%{_docdir}/HTML/en/common/2.png
rm -f %{buildroot}%{_docdir}/HTML/en/common/3.png
rm -f %{buildroot}%{_docdir}/HTML/en/common/4.png
rm -f %{buildroot}%{_docdir}/HTML/en/common/5.png
rm -f %{buildroot}%{_docdir}/HTML/en/common/6.png
rm -f %{buildroot}%{_docdir}/HTML/en/common/7.png
rm -f %{buildroot}%{_docdir}/HTML/en/common/8.png
rm -f %{buildroot}%{_docdir}/HTML/en/common/9.png
rm -f %{buildroot}%{_docdir}/HTML/en/common/artistic-license.html
rm -f %{buildroot}%{_docdir}/HTML/en/common/bottom-left.png
rm -f %{buildroot}%{_docdir}/HTML/en/common/bottom-middle.png
rm -f %{buildroot}%{_docdir}/HTML/en/common/bottom-right.png
rm -f %{buildroot}%{_docdir}/HTML/en/common/bsd-license.html
rm -f %{buildroot}%{_docdir}/HTML/en/common/doxygen.css
rm -f %{buildroot}%{_docdir}/HTML/en/common/favicon.ico
rm -f %{buildroot}%{_docdir}/HTML/en/common/fdl-license
rm -f %{buildroot}%{_docdir}/HTML/en/common/fdl-license.html
rm -f %{buildroot}%{_docdir}/HTML/en/common/fdl-notice.html
rm -f %{buildroot}%{_docdir}/HTML/en/common/footer.html
rm -f %{buildroot}%{_docdir}/HTML/en/common/gpl-license
rm -f %{buildroot}%{_docdir}/HTML/en/common/gpl-license.html
rm -f %{buildroot}%{_docdir}/HTML/en/common/header.html
rm -f %{buildroot}%{_docdir}/HTML/en/common/kde-default.css
rm -f %{buildroot}%{_docdir}/HTML/en/common/kde_logo_bg.png
rm -f %{buildroot}%{_docdir}/HTML/en/common/lgpl-license
rm -f %{buildroot}%{_docdir}/HTML/en/common/lgpl-license.html
rm -f %{buildroot}%{_docdir}/HTML/en/common/mainfooter.html
rm -f %{buildroot}%{_docdir}/HTML/en/common/mainheader.html
rm -f %{buildroot}%{_docdir}/HTML/en/common/qpl-license.html
rm -f %{buildroot}%{_docdir}/HTML/en/common/top-left.png
rm -f %{buildroot}%{_docdir}/HTML/en/common/top-middle.png
rm -f %{buildroot}%{_docdir}/HTML/en/common/top-right-konqueror.png
rm -f %{buildroot}%{_docdir}/HTML/en/common/top-right.jpg
rm -f %{buildroot}%{_docdir}/HTML/en/common/x11-license.html
rm -f %{buildroot}%{_docdir}/HTML/en/common/xml.dcl
rm -rf %{buildroot}%{_datadir}/locale/all_languages
rm -rf %{buildroot}%{_sysconfdir}/xdg/menus/
rm -rf %{buildroot}%{_datadir}/autostart/
rm -f %{buildroot}%{_datadir}/config/colors/40.colors
rm -f %{buildroot}%{_datadir}/config/colors/Rainbow.colors
rm -f %{buildroot}%{_datadir}/config/colors/Royal.colors
rm -f %{buildroot}%{_datadir}/config/colors/Web.colors
rm -f %{buildroot}%{_datadir}/config/ksslcalist
rm -f %{buildroot}%{_bindir}/preparetips
# remove conflicts with kate-4.9.80+
rm -fv %{buildroot}%{_datadir}/config/katesyntaxhighlightingrc

# fix file conflict with leptonica-tools (#2156905)
mv -f %{buildroot}%{_bindir}/imagetops %{buildroot}%{_bindir}/imagetops-kde3
sed -i -e 's!exec:/imagetops!exec:/imagetops-kde3!g' %{buildroot}%{_datadir}/apps/kdeprint/filters/imagetops.desktop
sed -i -e 's/imagetops /imagetops-kde3 /g' %{buildroot}%{_datadir}/apps/kdeprint/filters/imagetops.xml

# don't show kresources
sed -i -e "s,^OnlyShowIn=KDE;,OnlyShowIn=KDE3;," %{buildroot}%{_datadir}/applications/kde/kresources.desktop 

# use ca-certificates' ca-bundle.crt, symlink as what most other
# distros do these days (http://bugzilla.redhat.com/521902)
if [  -f %{buildroot}%{_datadir}/apps/kssl/ca-bundle.crt -a \
      -f /etc/pki/ca-trust/extracted/pem/tls-ca-bundle.pem ]; then
  ln -sf /etc/pki/ca-trust/extracted/pem/tls-ca-bundle.pem \
         %{buildroot}%{_datadir}/apps/kssl/ca-bundle.crt
fi

%check
ERROR=0
# verify rpath, or lack thereof
if [ ! -z "$(chrpath --list %{buildroot}%{_bindir}/kioexec 2>/dev/null | grep RPATH=)" ]; then
  echo "ERROR: the end is neigh, rpath has returned!"
  ERROR=1
fi
%if 0%{?apidocs}
if [ ! -f %{buildroot}%{_docdir}/HTML/en/kdelibs-apidocs/index.html ]; then
  echo "ERROR: %{_docdir}/HTML/en/kdelibs-apidocs/index.html not generated"
  ERROR=1
fi 
%endif
exit $ERROR

%if 0%{?fedora} > 25
%ldconfig_scriptlets

%filetriggerin -- %{_datadir}/icons/crystalsvg
touch %{_datadir}/icons/crystalsvg &> /dev/null || :

%transfiletriggerin -- %{_datadir}/icons/crystalsvg
gtk-update-icon-cache %{_datadir}/icons/crystalsvg &>/dev/null || :

%transfiletriggerpostun -- %{_datadir}/icons/crystalsvg
gtk-update-icon-cache %{_datadir}/icons/crystalsvg &>/dev/null || :

%else
# classic scriptlets
%post
%{?ldconfig}
touch --no-create %{_datadir}/icons/crystalsvg &> /dev/null || :

%posttrans
gtk-update-icon-cache %{_datadir}/icons/crystalsvg &> /dev/null || :

%postun
%{?ldconfig}
if [ $1 -eq 0 ] ; then
touch --no-create %{_datadir}/icons/crystalsvg &> /dev/null || :
gtk-update-icon-cache %{_datadir}/icons/crystalsvg &> /dev/null || :
fi
%endif

%files
%doc README
%license COPYING.LIB
%{_bindir}/artsmessage
%{_bindir}/cupsdconf
%{_bindir}/cupsdoprint
%{_bindir}/make_driver_db_cups
%{_bindir}/dcop
%{_bindir}/dcopclient
%{_bindir}/dcopfind
%{_bindir}/dcopobject
%{_bindir}/dcopquit
%{_bindir}/dcopref
%{_bindir}/dcopserver
%{_bindir}/dcopserver_shutdown
%{_bindir}/dcopstart
%{_bindir}/filesharelist
%{_bindir}/fileshareset
%{_bindir}/imagetops-kde3
%{_bindir}/kab2kabc
%{_bindir}/kaddprinterwizard
%{_bindir}/kbuildsycoca
%{_bindir}/kcmshell
%{_bindir}/kconf_update
%{_bindir}/kcookiejar
%{_bindir}/kde-config
%{_bindir}/kde-menu
%{_bindir}/kded
%{_bindir}/kdeinit
%{_bindir}/kdeinit_shutdown
%{_bindir}/kdeinit_wrapper
%{_bindir}/kdesu_stub
%{_bindir}/kdontchangethehostname
%{_bindir}/kdostartupconfig
%{_bindir}/kfile
%{_bindir}/kfmexec
%{_bindir}/khotnewstuff
%{_bindir}/kinstalltheme
%{_bindir}/kio_http_cache_cleaner
%{_bindir}/kio_uiserver
%{_bindir}/kioexec
%{_bindir}/kioslave
%{_bindir}/klauncher
%{_bindir}/ksendbugmail
%{_bindir}/kshell
%{_bindir}/kstartupconfig
%{_bindir}/ktradertest
%{_bindir}/kwrapper
%{_bindir}/lnusertemp
%{_bindir}/make_driver_db_lpr
%{_bindir}/meinproc
%{_bindir}/start_kdeinit
%{_bindir}/start_kdeinit_wrapper
%{_libdir}/lib*.so.*
%{_libdir}/libkdeinit_*.so
%{_libdir}/lib*.la
%{_libdir}/kconf_update_bin/
%{_libdir}/kde3/
%{_datadir}/applications/kde/*.desktop
%{_datadir}/apps/*
%exclude %{_datadir}/apps/ksgmltools2/
%config(noreplace) %{_datadir}/config/*
%{_datadir}/emoticons/*
%{_datadir}/icons/default.kde
%{_datadir}/mimelnk/magic
%{_datadir}/mimelnk/*/*.desktop
%{_datadir}/services/*
%{_datadir}/servicetypes/*
%ghost %{_datadir}/services/ksycoca
%{_docdir}/HTML/en/kspell
%{_docdir}/HTML/en/common/*
# split out someday? -- rex
%{_datadir}/icons/crystalsvg/

%files devel
%{_bindir}/dcopidl*
%{_bindir}/kconfig_compiler
%{_bindir}/makekdewidgets
%{_datadir}/apps/ksgmltools2/
%{_includedir}/kde/
%{_libdir}/lib*.so
%{_libdir}/lib*.a
%exclude %{_libdir}/libkdeinit_*.so

%if 0%{?apidocs}
%files apidocs
%{_docdir}/%{name}-devel-%{kde_major_version}
%{_docdir}/HTML/en/kdelibs*
%endif

%files tools
%attr(4755,root,root) %{_bindir}/kgrantpty
%attr(4755,root,root) %{_bindir}/kpac_dhcp_helper

%changelog
%autochangelog
