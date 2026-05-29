%global source0_hash 7b632550ea1048fc10c741e46e2e3b093e5ca94dfa6209e9e0848800e247023b

# See http://bugzilla.redhat.com/223663
%global multilib_archs x86_64 %{ix86} %{?mips} ppc64 ppc s390x s390 sparc64 sparcv9
%global multilib_basearchs x86_64 %{?mips64} ppc64 s390x sparc64

%if 0%{?fedora} < 29 && 0%{?rhel} < 9 || (0%{?oreon} >= 11)
%ifarch %{ix86}
%global no_sse2  -no-sse2
%endif
%endif


# workaround https://bugzilla.redhat.com/show_bug.cgi?id=1668865
# for current stable releases
%if 0%{?fedora} < 30  || 0%{?rhel} > 6 || (0%{?oreon} >= 11)
%global no_feature_statx -no-feature-statx
%global no_feature_renameat2 -no-feature-renameat2
%endif
%if 0%{?rhel} && 0%{?rhel} > 6 || (0%{?oreon} >= 11)
%global no_feature_getentropy -no-feature-getentropy
%endif

# support qtchooser (adds qtchooser .conf file)
%if 0%{?flatpak}
%global qtchooser 0
%else
%global qtchooser 1
%endif
%if 0%{?qtchooser}
%global priority 10
%ifarch %{multilib_basearchs}
%global priority 15
%endif
%endif

# Disable automatic .la file removal
%global __brp_remove_la_files %nil

%global platform linux-g++

%if 0%{?use_clang}
%global platform linux-clang
%endif

%global qt_module qtbase

%global rpm_macros_dir %(d=%{_rpmconfigdir}/macros.d; [ -d $d ] || d=%{_sysconfdir}/rpm; echo $d)

# use external qt_settings pkg
%if 0%{?fedora} || (0%{?oreon} >= 11)
%global qt_settings 1
%endif

%global examples 1
## skip for now, until we're better at it --rex
#global tests 1

Name:    qt5-qtbase
Summary: Qt5 - QtBase components
Version: 5.15.18
Release: 2%{?dist}

# See LGPL_EXCEPTIONS.txt, for exception details
License: LGPL-3.0-only OR GPL-3.0-only WITH Qt-GPL-exception-1.0
Url:     http://qt-project.org/
%global  majmin %(echo %{version} | cut -d. -f1-2)
Source0:        https://download.qt.io/archive/qt/%{majmin}/%{version}/submodules/%{qt_module}-everywhere-opensource-src-%{version}.tar.xz
# https://bugzilla.redhat.com/show_bug.cgi?id=1227295
Source1: qtlogging.ini

# header file to workaround multilib issue
# https://bugzilla.redhat.com/show_bug.cgi?id=1036956
Source5: qconfig-multilib.h

# xinitrc script to check for OpenGL 1 only drivers and automatically set
# QT_XCB_FORCE_SOFTWARE_OPENGL for them
Source6: 10-qt5-check-opengl2.sh

# macros
Source10: macros.qt5-qtbase

# support multilib optflags
Patch2: qtbase-multilib_optflags.patch

# make mixing versions with private apis a warning instead of fatal error
Patch3: qtbase-everywhere-src-5.15.6-private_api_warning.patch

# upstreamable patches
# namespace QT_VERSION_CHECK to workaround major/minor being pre-defined (#1396755)
Patch50: qtbase-opensource-src-5.8.0-QT_VERSION_CHECK.patch

# 1381828 - Broken window scaling for some QT5 applications (#1381828)
# This patch moves the threshold for 2x scaling from the DPI of 144 to 192,
# the same value GNOME uses. It's not a complete solution...
Patch51: qtbase-hidpi_scale_at_192.patch

# 1. Workaround moc/multilib issues
# https://bugzilla.redhat.com/show_bug.cgi?id=1290020
# https://bugreports.qt.io/browse/QTBUG-49972
# 2. Workaround sysmacros.h (pre)defining major/minor a breaking stuff
Patch52: qtbase-opensource-src-5.7.1-moc_macros.patch

# CMake generates wrong -isystem /usr/include compilations flags with Qt5::Gui
# https://bugzilla.redhat.com/1704474
Patch53: qtbase-everywhere-src-5.12.1-qt5gui_cmake_isystem_includes.patch

# respect QMAKE_LFLAGS_RELEASE when building qmake
Patch54: qtbase-qmake_LFLAGS.patch

# don't use relocatable heuristics to guess prefix when using -no-feature-relocatable
Patch55: qtbase-everywhere-src-5.14.2-no_relocatable.patch

# fix FTBFS against libglvnd-1.3.4+
Patch56: qtbase-everywhere-src-5.15.2-libglvnd.patch

# drop -O3 and make -O2 by default
Patch57: qt5-qtbase-cxxflag.patch

# support firebird version 3.x
Patch58: qt5-qtbase-5.12.1-firebird.patch

# support firebird version 4.x
Patch59: qt5-qtbase-5.12.1-firebird-4.0.0.patch

# fix for new mariadb
Patch60: qtbase-opensource-src-5.9.0-mysql.patch

# FIXME This patch is completely meaningless in the context of C++.
# It is a workaround for a pyside2 build failure with Qt 5.15.9,
# pyside2 5.15.9, clang 16.0.1 -- the generated code thinks a
# not otherwise specified "Type" is in fact a
# QFlags<QOpenGLShader::ShaderTypeBit>, causing many functions
# looking for a QEvent::Type to be bogus.
# Since there are no side effects to superfluously specifying
# QEvent::Type instead of plain "Type" in a QEvent derived class,
# this workaround is acceptable, if not nice.
Patch61: qtbase-5.15.10-work-around-pyside2-brokenness.patch

# Bug 1954359 - Many emoji don't show up in Qt apps because qt does not handle 'emoji' font family
# Patch63: qtbase-cache-emoji-font.patch

# gcc-11
Patch90: %{name}-gcc11.patch

## upstream patches
# https://invent.kde.org/qt/qt/qtbase, kde/5.15 branch
# git diff v5.15.18-lts-lgpl..HEAD | gzip > kde-5.15-rollup-$(date +%Y%m%d).patch.gz
# patch100 in lookaside cache due to large'ish size -- rdieter
Patch100: kde-5.15-rollup-20251104.patch.gz
# HACK to make 'fedpkg sources' consider it 'used"
Source100: kde-5.15-rollup-20251104.patch.gz

Patch101: qtbase-5.15.10-fix-missing-qtsan-include.patch
# Workaround for font rendering issue with cjk-vf-fonts
# https://bugreports.qt.io/browse/QTBUG-111994
# https://bugreports.qt.io/browse/QTBUG-112136
Patch102: qtbase-QTBUG-111994.patch
Patch103: qtbase-QTBUG-112136.patch

# qt5 backport of https://codereview.qt-project.org/c/qt/qtbase/+/664056
# to fix ssl trust store discovery with
# 
Patch104: 0001-Update-SSL-trust-store-locations-for-modern-Red-Hat-.patch

## Qt 6 backports for better Gtk/GNOME integration
# 
# https://bugzilla.redhat.com/show_bug.cgi?id=1732129
Patch150: 0001-Use-Wayland-by-default-on-GNOME.patch

# 
# https://bugzilla.redhat.com/show_bug.cgi?id=2226797
Patch151: 0002-Add-enum-class-Qt-Appearance.patch
Patch152: 0003-Sync-and-assert-StandardPixmap-enums-in-QPlatformThe.patch
Patch153: 0004-QGtk3Theme-subscribe-to-theme-hint-changes.patch
# Patch154: 0005-Gtk3Theme-set-XCURSOR_SIZE-and-XCURSOR_THEME-for-way.patch
Patch155: 0006-Re-implement-palette-standardPixmap-file-icons-fonts.patch
# Patch156: 0007-GTK3-theme-simplify-code.patch
Patch157: 0008-Fix-checkbox-and-radiobutton-background-in-QGtk3Them.patch
Patch158: 0009-Cleanup-QGtk3Theme.patch
Patch159: 0010-Detect-appearance-by-colors-unless-GTK-theme-name-co.patch
Patch160: 0011-Change-parsing-log-output-in-QGtk3Json-from-qCDebug-.patch
Patch161: 0012-Document-QGtk3Interface.patch
Patch162: 0013-Document-QGtk3Storage.patch
Patch163: 0014-QGtk3Theme-Improve-fixed-font-delivery.patch
Patch164: 0015-QGtk3Theme-Do-not-default-Active-WindowText-to-butto.patch
Patch165: 0016-Fix-memory-leak-in-QGtk3Interface-themename.patch
Patch166: 0017-Fix-disabled-button-color-in-Linux-x11-wayland.patch
Patch167: 0018-Fix-inactive-palette-in-gtk3-theme.patch
Patch168: 0019-Fix-tooltip-palette-issue-in-gtk3-theme.patch
Patch169: 0020-QGtk3Theme-define-light-midlight-mid-dark-shadow-colors.patch

# Security


# Latest QGnomePlatform needs to be specified to be used
Patch200: qtbase-use-qgnomeplatform-as-default-platform-theme-on-gnome.patch

# Do not check any files in %%{_qt5_plugindir}/platformthemes/ for requires.
# Those themes are there for platform integration. If the required libraries are
# not there, the platform to integrate with isn't either. Then Qt will just
# silently ignore the plugin that fails to load. Thus, there is no need to let
# RPM drag in gtk3 as a dependency for the GTK+3 dialog support.
%global __requires_exclude_from ^%{_qt5_plugindir}/platformthemes/.*$
# filter plugin provides
%global __provides_exclude_from ^%{_qt5_plugindir}/.*\\.so$

%if 0%{?use_clang}
BuildRequires: clang >= 3.7.0
%else
BuildRequires: gcc-c++
%endif
BuildRequires: make
BuildRequires: cups-devel
BuildRequires: desktop-file-utils
BuildRequires: double-conversion-devel
BuildRequires: findutils
BuildRequires: libjpeg-devel
BuildRequires: libmng-devel
BuildRequires: libtiff-devel
BuildRequires: pkgconfig(alsa)
# required for -accessibility
BuildRequires: pkgconfig(atspi-2)
BuildRequires: pkgconfig(dbus-1)
BuildRequires: pkgconfig(libdrm)
BuildRequires: pkgconfig(fontconfig)
BuildRequires: pkgconfig(gl)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(libproxy-1.0)
BuildRequires: pkgconfig(libsctp)
# xcb-sm
BuildRequires: pkgconfig(ice) pkgconfig(sm)
BuildRequires: pkgconfig(libpng)
BuildRequires: pkgconfig(libudev)
BuildRequires: openssl-devel
BuildRequires: pkgconfig(libpulse) pkgconfig(libpulse-mainloop-glib)
BuildRequires: pkgconfig(libinput)
BuildRequires: pkgconfig(libsystemd)
BuildRequires: pkgconfig(xcb-xkb) >= 1.10
BuildRequires: pkgconfig(xcb-util)
BuildRequires: pkgconfig(xkbcommon) >= 0.4.1
BuildRequires: pkgconfig(xkbcommon-x11) >= 0.4.1
BuildRequires: pkgconfig(xkeyboard-config)
%global vulkan 1
BuildRequires: pkgconfig(vulkan)
%if 0%{?fedora} || 0%{?rhel} > 6 || (0%{?oreon} >= 11)
%global egl 1
BuildRequires: pkgconfig(egl)
BuildRequires: pkgconfig(gbm)
## TODO: apparently only needed if building opengl_es2 support, do we actually use it?  -- rex
BuildRequires: pkgconfig(glesv2)
%global sqlite -system-sqlite
BuildRequires: pkgconfig(sqlite3) >= 3.7
%if 0%{?fedora} > 22 || (0%{?oreon} >= 11)
%global harfbuzz -system-harfbuzz
BuildRequires: pkgconfig(harfbuzz) >= 0.9.42
%endif
BuildRequires: pkgconfig(icu-i18n)
%if 0%{?fedora} > 37 || 0%{?rhel} > 7 || (0%{?oreon} >= 11)
BuildRequires: pkgconfig(libpcre2-16) >= 10.20
%else
BuildRequires: pkgconfig(libpcre) >= 8.0
%endif
%global pcre -system-pcre
BuildRequires: pkgconfig(xcb-xkb)
%else
BuildRequires: libicu-devel
%global pcre -qt-pcre
%endif
BuildRequires: pkgconfig(xcb) pkgconfig(xcb-glx) pkgconfig(xcb-icccm) pkgconfig(xcb-image) pkgconfig(xcb-keysyms) pkgconfig(xcb-renderutil)
BuildRequires: pkgconfig(zlib)
BuildRequires: pkgconfig(libzstd)
BuildRequires: perl-generators
# see patch68
BuildRequires: python3
BuildRequires: qt5-rpm-macros

%if 0%{?tests}
BuildRequires: dbus-x11
BuildRequires: mesa-dri-drivers
BuildRequires: time
BuildRequires: xorg-x11-server-Xvfb
%endif

Requires:      qt5-filesystem

%if 0%{?qtchooser}
%if 0%{?fedora} || (0%{?oreon} >= 11)
Conflicts: qt < 1:4.8.6-10
%endif
Requires(post): %{_sbindir}/update-alternatives
Requires(postun): %{_sbindir}/update-alternatives
%endif
%if 0%{?qt_settings}
Requires: qt-settings
%endif
Requires: %{name}-common = %{version}-%{release}

## Sql drivers
%if 0%{?rhel} || (0%{?oreon} >= 11)
%global ibase -no-sql-ibase
%global tds -no-sql-tds
%endif

# workaround gold linker bug(s) by not using it
# https://bugzilla.redhat.com/1458003
# https://sourceware.org/bugzilla/show_bug.cgi?id=21074
# reportedly fixed or worked-around, re-enable if there's evidence of problems -- rex
# https://bugzilla.redhat.com/show_bug.cgi?id=1635973
%global use_gold_linker -no-use-gold-linker

%description
Qt is a software toolkit for developing applications.

This package contains base tools, like string, xml, and network
handling.

%package common
Summary: Common files for Qt5
# offer upgrade path for qtquick1 somewhere... may as well be here -- rex
Obsoletes: qt5-qtquick1 < 5.9.0
Obsoletes: qt5-qtquick1-devel < 5.9.0
%if "%{?ibase}" == "-no-sql-ibase"
Obsoletes: qt5-qtbase-ibase < %{version}-%{release}
%endif
%if "%{?tds}" == "-no-sql-tds"
Obsoletes: qt5-qtbase-tds < %{version}-%{release}
%endif
Requires: %{name} = %{version}-%{release}
BuildArch: noarch
%description common
%{summary}.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-gui%{?_isa}
%if 0%{?egl}
Requires: pkgconfig(egl)
%endif
Requires: pkgconfig(gl)
%if 0%{?vulkan}
Requires: pkgconfig(vulkan)
%endif
Requires: qt5-rpm-macros
%if 0%{?use_clang}
Requires: clang >= 3.7.0
%endif
%description devel
%{summary}.

%package private-devel
Summary: Development files for %{name} private APIs
# upgrade path, when private-devel was introduced
Obsoletes: %{name}-devel < 5.12.1-3
Requires: %{name}-devel%{?_isa} = %{version}-%{release}
# QtPrintSupport/private requires cups/ppd.h
Requires: cups-devel
%description private-devel
%{summary}.

%package examples
Summary: Programming examples for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description examples
%{summary}.

%package static
Summary: Static library files for %{name}
Requires: %{name}-devel%{?_isa} = %{version}-%{release}
Requires: pkgconfig(fontconfig)
Requires: pkgconfig(glib-2.0)
Requires: pkgconfig(libinput)
Requires: pkgconfig(xkbcommon)
Requires: pkgconfig(zlib)

%description static
%{summary}.

%if "%{?ibase}" != "-no-sql-ibase"
%package ibase
Summary: IBase driver for Qt5's SQL classes
BuildRequires: firebird-devel
Requires: %{name}%{?_isa} = %{version}-%{release}
%description ibase
%{summary}.
%endif

%package mysql
Summary: MySQL driver for Qt5's SQL classes
%if 0%{?rhel} && 0%{?rhel} < 9 || (0%{?oreon} >= 11)
BuildRequires: mysql-devel
%else
BuildRequires: mariadb-connector-c-devel
%endif
Requires: %{name}%{?_isa} = %{version}-%{release}
%description mysql
%{summary}.

%package odbc
Summary: ODBC driver for Qt5's SQL classes
BuildRequires: unixODBC-devel
Requires: %{name}%{?_isa} = %{version}-%{release}
%description odbc
%{summary}.

%package postgresql
Summary: PostgreSQL driver for Qt5's SQL classes
BuildRequires: libpq-devel
Requires: %{name}%{?_isa} = %{version}-%{release}
%description postgresql
%{summary}.

%if "%{?tds}" != "-no-sql-tds"
%package tds
Summary: TDS driver for Qt5's SQL classes
BuildRequires: freetds-devel
Requires: %{name}%{?_isa} = %{version}-%{release}
%description tds
%{summary}.
%endif

# debating whether to do 1 subpkg per library or not -- rex
%package gui
Summary: Qt5 GUI-related libraries
Requires: %{name}%{?_isa} = %{version}-%{release}
# where Recommends are supported
%if 0%{?fedora} || 0%{?rhel} >= 8 || (0%{?oreon} >= 11)
Recommends: mesa-dri-drivers%{?_isa}
Recommends: qt5-qtwayland%{?_isa}
# Required for some locales: https://pagure.io/fedora-kde/SIG/issue/311
Recommends: qt5-qttranslations
%endif
Obsoletes: qt5-qtbase-x11 < 5.2.0
Provides:  qt5-qtbase-x11 = %{version}-%{release}
Obsoletes: adwaita-qt5 <= 1.4.2
Obsoletes: libadwaita-qt5 <= 1.4.2
Obsoletes: qgnomeplatform-qt5 <= 0.9.2
Provides:  qgnomeplatform-qt5 = %{version}-%{release}
# for Source6: 10-qt5-check-opengl2.sh:
# glxinfo
Requires: glx-utils
%description gui
Qt5 libraries used for drawing widgets and OpenGL items.


%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q -n %{qt_module}-everywhere-src-%{version}

## dowstream patches
%patch -P3 -p1 -b .private_api_warning

## upstream fixes

%patch -P50 -p1 -b .QT_VERSION_CHECK
# FIXME/TODO : rebase or drop -- rdieter
#patch -P51 -p1 -b .hidpi_scale_at_192
%patch -P52 -p1 -b .moc_macros
%patch -P53 -p1 -b .qt5gui_cmake_isystem_includes
%patch -P54 -p1 -b .qmake_LFLAGS
%patch -P55 -p1 -b .no_relocatable
%patch -P56 -p1 -b .libglvnd
%patch -P57 -p1 -b .qt5-qtbase-cxxflag
%if 0%{?fedora} < 35 || (0%{?oreon} >= 11)
%patch -P58 -p1 -b .firebird
%else
%patch -P59 -p1 -b .firebird
%endif
%if 0%{?fedora} > 27 || (0%{?oreon} >= 11)
%patch -P60 -p1 -b .mysql
%endif
%patch -P61 -p1
# FIXME seems to break text rendering completely for some people
# patch -P63 -p1 -b .cache-emoji-font

%patch -P90 -p1 -b .gcc11

## upstream patches
%patch -P100 -p1
%patch -P101 -p1
%patch -P102 -p1
%patch -P103 -p1
%patch -P104 -p1

## Qt 6 backports
%if 0%{?fedora} > 30 || 0%{?rhel} > 8 || (0%{?oreon} >= 11)
%patch -P150 -p1 -b .use-wayland-on-gnome.patch
%endif
%if 0%{?fedora} > 38 || 0%{?rhel} > 9 || (0%{?oreon} >= 11)
%patch -P151 -p1
%patch -P152 -p1
%patch -P153 -p1
# patch -P154 -p1
%patch -P155 -p1
# patch -P156 -p1
%patch -P157 -p1
%patch -P158 -p1
%patch -P159 -p1
%patch -P160 -p1
%patch -P161 -p1
%patch -P162 -p1
%patch -P163 -p1
%patch -P164 -p1
%patch -P165 -p1
%patch -P166 -p1
%patch -P167 -p1
%patch -P168 -p1
%patch -P169 -p1
%endif

%if 0%{?fedora} < 39 || (0%{?oreon} >= 11)
# Use QGnomePlatform by default
%patch -P200 -p1
%endif

# move some bundled libs to ensure they're not accidentally used
pushd src/3rdparty
mkdir UNUSED
mv freetype libjpeg libpng zlib UNUSED/
%if "%{?sqlite}" == "-system-sqlite"
mv sqlite UNUSED/
%endif
%if "%{?xcb}" != "-qt-xcb"
mv xcb UNUSED/
%endif
popd

# builds failing mysteriously on f20
# ./configure: Permission denied
# check to ensure that can't happen -- rex
test -x configure || chmod +x configure

# use proper perl interpretter so autodeps work as expected
sed -i -e "s|^#!/usr/bin/env perl$|#!%{__perl}|" \
 bin/fixqt4headers.pl \
 bin/syncqt.pl \
 mkspecs/features/data/unix/findclasslist.pl


%build
# QT is known not to work properly with LTO at this point.  Some of the issues
# are being worked on upstream and disabling LTO should be re-evaluated as
# we update this change.  Until such time...
# Disable LTO
# https://bugzilla.redhat.com/1900527
%define _lto_cflags %{nil}

## FIXME/TODO:
# * for %%ix86, add sse2 enabled builds for Qt5Gui, Qt5Core, QtNetwork, see also:
#   http://anonscm.debian.org/cgit/pkg-kde/qt/qtbase.git/tree/debian/rules (234-249)

## adjust $RPM_OPT_FLAGS
# remove -fexceptions
RPM_OPT_FLAGS=`echo $RPM_OPT_FLAGS | sed 's|-fexceptions||g'`
RPM_OPT_FLAGS="$RPM_OPT_FLAGS %{?qt5_arm_flag} %{?qt5_deprecated_flag} %{?qt5_null_flag}"

%if 0%{?use_clang}
RPM_OPT_FLAGS=`echo $RPM_OPT_FLAGS | sed 's|-fno-delete-null-pointer-checks||g'`
%endif

export CFLAGS="$CFLAGS $RPM_OPT_FLAGS"
export CXXFLAGS="$CXXFLAGS $RPM_OPT_FLAGS"
export LDFLAGS="$LDFLAGS $RPM_LD_FLAGS"
export MAKEFLAGS="%{?_smp_mflags}"

./configure \
  -verbose \
  -confirm-license \
  -opensource \
  -prefix %{_qt5_prefix} \
  -archdatadir %{_qt5_archdatadir} \
  -bindir %{_qt5_bindir} \
  -libdir %{_qt5_libdir} \
  -libexecdir %{_qt5_libexecdir} \
  -datadir %{_qt5_datadir} \
  -docdir %{_qt5_docdir} \
  -examplesdir %{_qt5_examplesdir} \
  -headerdir %{_qt5_headerdir} \
  -importdir %{_qt5_importdir} \
  -plugindir %{_qt5_plugindir} \
  -sysconfdir %{_qt5_sysconfdir} \
  -translationdir %{_qt5_translationdir} \
  -platform %{platform} \
  -release \
  -shared \
  -accessibility \
  -dbus-linked \
  %{?egl:-egl -eglfs} \
  -fontconfig \
  -glib \
  -gtk \
  %{?ibase} \
  -icu \
  -journald \
  -optimized-qmake \
  -openssl-linked \
  -libproxy \
  -sctp \
  %{!?examples:-nomake examples} \
  %{!?tests:-nomake tests} \
  -no-pch \
  -no-reduce-relocations \
  -no-rpath \
  -no-separate-debug-info \
  %{?no_sse2} \
  -no-strip \
  -system-libjpeg \
  -system-libpng \
  %{?harfbuzz} \
  %{?pcre} \
  %{?sqlite} \
  %{?tds} \
  %{?xcb} \
  %{?xkbcommon} \
  -system-zlib \
  %{?use_gold_linker} \
  -no-directfb \
  -no-feature-relocatable \
  %{?no_feature_renameat2} \
  %{?no_feature_statx} \
  %{?no_feature_getentropy} \
  QMAKE_CFLAGS_RELEASE="${CFLAGS:-$RPM_OPT_FLAGS}" \
  QMAKE_CXXFLAGS_RELEASE="${CXXFLAGS:-$RPM_OPT_FLAGS}" \
  QMAKE_LFLAGS_RELEASE="${LDFLAGS:-$RPM_LD_FLAGS}"

# Validate config results
%if "%{?ibase}" != "-no-sql-ibase"
for config_test in egl-x11 ibase ; do
%else
for config_test in egl-x11 ; do
%endif
config_result="$(grep ^cache.${config_test}.result config.cache | cut -d= -f2 | tr -d ' ')"
if [ "${config_result}" != "true" ]; then
  echo "${config_test} detection failed"
  config_failed=1
fi
done
if [ ${config_failed} -eq 1 ]; then exit 1; fi

# ensure qmake build using optflags (which can happen if not munging qmake.conf defaults)
make clean -C qmake
%make_build -C qmake all binary \
  QMAKE_CFLAGS_RELEASE="${CFLAGS:-$RPM_OPT_FLAGS}" \
  QMAKE_CXXFLAGS_RELEASE="${CXXFLAGS:-$RPM_OPT_FLAGS}" \
  QMAKE_LFLAGS_RELEASE="${LDFLAGS:-$RPM_LD_FLAGS}" \
  QMAKE_STRIP=

%make_build


%install
make install INSTALL_ROOT=%{buildroot}

install -m644 -p -D %{SOURCE1} %{buildroot}%{_qt5_datadir}/qtlogging.ini

# Qt5.pc
cat >%{buildroot}%{_libdir}/pkgconfig/Qt5.pc<<EOF
prefix=%{_qt5_prefix}
archdatadir=%{_qt5_archdatadir}
bindir=%{_qt5_bindir}
datadir=%{_qt5_datadir}

docdir=%{_qt5_docdir}
examplesdir=%{_qt5_examplesdir}
headerdir=%{_qt5_headerdir}
importdir=%{_qt5_importdir}
libdir=%{_qt5_libdir}
libexecdir=%{_qt5_libexecdir}
moc=%{_qt5_bindir}/moc
plugindir=%{_qt5_plugindir}
qmake=%{_qt5_bindir}/qmake
settingsdir=%{_qt5_settingsdir}
sysconfdir=%{_qt5_sysconfdir}
translationdir=%{_qt5_translationdir}

Name: Qt5
Description: Qt5 Configuration
Version: 5.15.18
EOF

# rpm macros
install -p -m644 -D %{SOURCE10} \
  %{buildroot}%{rpm_macros_dir}/macros.qt5-qtbase
sed -i \
  -e "s|@@NAME@@|%{name}|g" \
  -e "s|@@EPOCH@@|%{?epoch}%{!?epoch:0}|g" \
  -e "s|@@VERSION@@|%{version}|g" \
  -e "s|@@EVR@@|%{?epoch:%{epoch:}}%{version}-%{release}|g" \
  %{buildroot}%{rpm_macros_dir}/macros.qt5-qtbase

# create/own dirs
mkdir -p %{buildroot}%{_qt5_plugindir}/{designer,iconengines,script,styles}
mkdir -p %{buildroot}%{_sysconfdir}/xdg/QtProject

# hardlink files to {_bindir}, add -qt5 postfix to not conflict
mkdir %{buildroot}%{_bindir}
pushd %{buildroot}%{_qt5_bindir}
for i in * ; do
  case "${i}" in
    moc|qdbuscpp2xml|qdbusxml2cpp|qmake|rcc|syncqt|uic)
      ln -v  ${i} %{buildroot}%{_bindir}/${i}-qt5
      ln -sv ${i} ${i}-qt5
      ;;
    *)
      ln -v  ${i} %{buildroot}%{_bindir}/${i}
      ;;
  esac
done
popd

%ifarch %{multilib_archs}
# multilib: qconfig.h
  mv %{buildroot}%{_qt5_headerdir}/QtCore/qconfig.h %{buildroot}%{_qt5_headerdir}/QtCore/qconfig-%{__isa_bits}.h
  install -p -m644 -D %{SOURCE5} %{buildroot}%{_qt5_headerdir}/QtCore/qconfig.h
%endif

# qtchooser conf
%if 0%{?qtchooser}
  mkdir -p %{buildroot}%{_sysconfdir}/xdg/qtchooser
  pushd    %{buildroot}%{_sysconfdir}/xdg/qtchooser
  echo "%{_qt5_bindir}" >  5-%{__isa_bits}.conf
## FIXME/TODO: verify qtchooser (still) happy if _qt5_prefix uses %%_prefix instead of %%_libdir/qt5
  echo "%{_qt5_prefix}" >> 5-%{__isa_bits}.conf
  # alternatives targets
  touch default.conf 5.conf
  popd
%endif

## .prl/.la file love
# nuke .prl reference(s) to %%buildroot, excessive (.la-like) libs
pushd %{buildroot}%{_qt5_libdir}
for prl_file in libQt5*.prl ; do
  sed -i -e "/^QMAKE_PRL_BUILD_DIR/d" ${prl_file}
  if [ -f "$(basename ${prl_file} .prl).so" ]; then
    rm -fv "$(basename ${prl_file} .prl).la"
    sed -i -e "/^QMAKE_PRL_LIBS/d" ${prl_file}
  fi
done
popd

install -p -m755 -D %{SOURCE6} %{buildroot}%{_sysconfdir}/X11/xinit/xinitrc.d/10-qt5-check-opengl2.sh

# f29+ enables sse2 unconditionally on ix86 -- rex
%if 0%{?fedora} < 29 && 0%{?rhel} < 9 || (0%{?oreon} >= 11)
# fix bz#1442553 multilib issue
privat_header_file=%{buildroot}%{_qt5_headerdir}/QtCore/%{version}/QtCore/private/qconfig_p.h
grep -v QT_FEATURE_sse2 $privat_header_file > ${privat_header_file}.me
mv ${privat_header_file}.me ${privat_header_file}
cat >>${privat_header_file}<<EOF
# if defined(__x86_64__)
#define QT_FEATURE_sse2 1
#elif defined(__i386__)
#define QT_FEATURE_sse2 -1
# endif
EOF
%endif

# install privat headers for qtxcb
mkdir -p %{buildroot}%{_qt5_headerdir}/QtXcb
install -m 644 src/plugins/platforms/xcb/*.h %{buildroot}%{_qt5_headerdir}/QtXcb/

# drop Qt5Bootstrap from -static (#2017661)
rm -f %{buildroot}%{_qt5_libdir}/libQt5Bootstrap.*a
rm -f %{buildroot}%{_qt5_libdir}/libQt5Bootstrap.prl


%check
# verify Qt5.pc
export PKG_CONFIG_PATH=%{buildroot}%{_libdir}/pkgconfig
test "$(pkg-config --modversion Qt5)" = "%{version}"
%if 0%{?tests}
## see tests/README for expected environment (running a plasma session essentially)
## we are not quite there yet
export CTEST_OUTPUT_ON_FAILURE=1
export PATH=%{buildroot}%{_qt5_bindir}:$PATH
export LD_LIBRARY_PATH=%{buildroot}%{_qt5_libdir}
# dbus tests error out when building if session bus is not available
dbus-launch --exit-with-session \
%make_build sub-tests  -k ||:
xvfb-run -a --server-args="-screen 0 1280x1024x32" \
dbus-launch --exit-with-session \
time \
make check -k ||:
%endif


%if 0%{?qtchooser}
%pre
if [ $1 -gt 1 ] ; then
# remove short-lived qt5.conf alternatives
%{_sbindir}/update-alternatives  \
  --remove qtchooser-qt5 \
  %{_sysconfdir}/xdg/qtchooser/qt5-%{__isa_bits}.conf >& /dev/null ||:

%{_sbindir}/update-alternatives  \
  --remove qtchooser-default \
  %{_sysconfdir}/xdg/qtchooser/qt5.conf >& /dev/null ||:
fi
%endif

%post
%{?ldconfig}
%if 0%{?qtchooser}
%{_sbindir}/update-alternatives \
  --install %{_sysconfdir}/xdg/qtchooser/5.conf \
  qtchooser-5 \
  %{_sysconfdir}/xdg/qtchooser/5-%{__isa_bits}.conf \
  %{priority}

%{_sbindir}/update-alternatives \
  --install %{_sysconfdir}/xdg/qtchooser/default.conf \
  qtchooser-default \
  %{_sysconfdir}/xdg/qtchooser/5.conf \
  %{priority}
%endif

%postun
%{?ldconfig}
%if 0%{?qtchooser}
if [ $1 -eq 0 ]; then
%{_sbindir}/update-alternatives  \
  --remove qtchooser-5 \
  %{_sysconfdir}/xdg/qtchooser/5-%{__isa_bits}.conf

%{_sbindir}/update-alternatives  \
  --remove qtchooser-default \
  %{_sysconfdir}/xdg/qtchooser/5.conf
fi
%endif

%files
%license LICENSE.FDL
%license LICENSE.GPL*
%license LICENSE.LGPL*
%if 0%{?qtchooser}
%dir %{_sysconfdir}/xdg/qtchooser
# not editable config files, so not using %%config here
%ghost %{_sysconfdir}/xdg/qtchooser/default.conf
%ghost %{_sysconfdir}/xdg/qtchooser/5.conf
%{_sysconfdir}/xdg/qtchooser/5-%{__isa_bits}.conf
%endif
%dir %{_sysconfdir}/xdg/QtProject/
%{_qt5_libdir}/libQt5Concurrent.so.5*
%{_qt5_libdir}/libQt5Core.so.5*
%{_qt5_libdir}/libQt5DBus.so.5*
%{_qt5_libdir}/libQt5Network.so.5*
%{_qt5_libdir}/libQt5Sql.so.5*
%{_qt5_libdir}/libQt5Test.so.5*
%{_qt5_libdir}/libQt5Xml.so.5*
%dir %{_qt5_libdir}/cmake/Qt5/
%dir %{_qt5_libdir}/cmake/Qt5Concurrent/
%dir %{_qt5_libdir}/cmake/Qt5Core/
%dir %{_qt5_libdir}/cmake/Qt5DBus/
%dir %{_qt5_libdir}/cmake/Qt5Gui/
%dir %{_qt5_libdir}/cmake/Qt5Network/
%dir %{_qt5_libdir}/cmake/Qt5OpenGL/
%dir %{_qt5_libdir}/cmake/Qt5PrintSupport/
%dir %{_qt5_libdir}/cmake/Qt5Sql/
%dir %{_qt5_libdir}/cmake/Qt5Test/
%dir %{_qt5_libdir}/cmake/Qt5Widgets/
%dir %{_qt5_libdir}/cmake/Qt5Xml/
%{_qt5_docdir}/global/
%{_qt5_docdir}/config/
%{_qt5_datadir}/qtlogging.ini
%dir %{_qt5_plugindir}/bearer/
%{_qt5_plugindir}/bearer/libqconnmanbearer.so
%{_qt5_plugindir}/bearer/libqgenericbearer.so
%{_qt5_plugindir}/bearer/libqnmbearer.so
%{_qt5_libdir}/cmake/Qt5Network/Qt5Network_QConnmanEnginePlugin.cmake
%{_qt5_libdir}/cmake/Qt5Network/Qt5Network_QGenericEnginePlugin.cmake
%{_qt5_libdir}/cmake/Qt5Network/Qt5Network_QNetworkManagerEnginePlugin.cmake
%dir %{_qt5_plugindir}/designer/
%dir %{_qt5_plugindir}/generic/
%dir %{_qt5_plugindir}/iconengines/
%dir %{_qt5_plugindir}/imageformats/
%dir %{_qt5_plugindir}/platforminputcontexts/
%dir %{_qt5_plugindir}/platforms/
%dir %{_qt5_plugindir}/platformthemes/
%dir %{_qt5_plugindir}/printsupport/
%dir %{_qt5_plugindir}/script/
%dir %{_qt5_plugindir}/sqldrivers/
%dir %{_qt5_plugindir}/styles/
%{_qt5_plugindir}/sqldrivers/libqsqlite.so
%{_qt5_libdir}/cmake/Qt5Sql/Qt5Sql_QSQLiteDriverPlugin.cmake

%files common
# mostly empty for now, consider: filesystem/dir ownership, licenses
%{rpm_macros_dir}/macros.qt5-qtbase

%files devel
%if "%{_qt5_bindir}" != "%{_bindir}"
%dir %{_qt5_bindir}
%endif
%{_bindir}/moc*
%{_bindir}/qdbuscpp2xml*
%{_bindir}/qdbusxml2cpp*
%{_bindir}/qmake*
%{_bindir}/rcc*
%{_bindir}/syncqt*
%{_bindir}/uic*
%{_bindir}/qlalr
%{_bindir}/fixqt4headers.pl
%{_bindir}/qvkgen
%{_bindir}/tracegen
%{_qt5_bindir}/moc*
%{_qt5_bindir}/qdbuscpp2xml*
%{_qt5_bindir}/qdbusxml2cpp*
%{_qt5_bindir}/qmake*
%{_qt5_bindir}/rcc*
%{_qt5_bindir}/syncqt*
%{_qt5_bindir}/uic*
%{_qt5_bindir}/qlalr
%{_qt5_bindir}/fixqt4headers.pl
%{_qt5_bindir}/qvkgen
%{_qt5_headerdir}/QtConcurrent/
%{_qt5_headerdir}/QtCore/
%{_qt5_headerdir}/QtDBus/
%{_qt5_headerdir}/QtGui/
%{_qt5_headerdir}/QtNetwork/
%{_qt5_headerdir}/QtOpenGL/
%{_qt5_headerdir}/QtPlatformHeaders/
%{_qt5_headerdir}/QtPrintSupport/
%{_qt5_headerdir}/QtSql/
%{_qt5_headerdir}/QtTest/
%{_qt5_headerdir}/QtWidgets/
%{_qt5_headerdir}/QtXcb/
%{_qt5_headerdir}/QtXml/
%{_qt5_headerdir}/QtEglFSDeviceIntegration
%{_qt5_headerdir}/QtInputSupport
%{_qt5_headerdir}/QtEdidSupport
%{_qt5_headerdir}/QtXkbCommonSupport
%{_qt5_archdatadir}/mkspecs/
%{_qt5_libdir}/libQt5Concurrent.prl
%{_qt5_libdir}/libQt5Concurrent.so
%{_qt5_libdir}/libQt5Core.prl
%{_qt5_libdir}/libQt5Core.so
%{_qt5_libdir}/libQt5DBus.prl
%{_qt5_libdir}/libQt5DBus.so
%{_qt5_libdir}/libQt5Gui.prl
%{_qt5_libdir}/libQt5Gui.so
%{_qt5_libdir}/libQt5Network.prl
%{_qt5_libdir}/libQt5Network.so
%{_qt5_libdir}/libQt5OpenGL.prl
%{_qt5_libdir}/libQt5OpenGL.so
%{_qt5_libdir}/libQt5PrintSupport.prl
%{_qt5_libdir}/libQt5PrintSupport.so
%{_qt5_libdir}/libQt5Sql.prl
%{_qt5_libdir}/libQt5Sql.so
%{_qt5_libdir}/libQt5Test.prl
%{_qt5_libdir}/libQt5Test.so
%{_qt5_libdir}/libQt5Widgets.prl
%{_qt5_libdir}/libQt5Widgets.so
%{_qt5_libdir}/libQt5XcbQpa.prl
%{_qt5_libdir}/libQt5XcbQpa.so
%{_qt5_libdir}/libQt5Xml.prl
%{_qt5_libdir}/libQt5Xml.so
%{_qt5_libdir}/libQt5EglFSDeviceIntegration.prl
%{_qt5_libdir}/libQt5EglFSDeviceIntegration.so
%{_qt5_libdir}/cmake/Qt5/Qt5Config*.cmake
%{_qt5_libdir}/cmake/Qt5Concurrent/Qt5ConcurrentConfig*.cmake
%{_qt5_libdir}/cmake/Qt5Core/Qt5CoreConfig*.cmake
%{_qt5_libdir}/cmake/Qt5Core/Qt5CoreMacros.cmake
%{_qt5_libdir}/cmake/Qt5Core/Qt5CTestMacros.cmake
%{_qt5_libdir}/cmake/Qt5DBus/Qt5DBusConfig*.cmake
%{_qt5_libdir}/cmake/Qt5DBus/Qt5DBusMacros.cmake
%{_qt5_libdir}/cmake/Qt5Gui/Qt5GuiConfig*.cmake
%{_qt5_libdir}/cmake/Qt5Network/Qt5NetworkConfig*.cmake
%{_qt5_libdir}/cmake/Qt5OpenGL/Qt5OpenGLConfig*.cmake
%{_qt5_libdir}/cmake/Qt5PrintSupport/Qt5PrintSupportConfig*.cmake
%{_qt5_libdir}/cmake/Qt5Sql/Qt5SqlConfig*.cmake
%{_qt5_libdir}/cmake/Qt5Test/Qt5TestConfig*.cmake
%{_qt5_libdir}/cmake/Qt5Widgets/Qt5WidgetsConfig*.cmake
%{_qt5_libdir}/cmake/Qt5Widgets/Qt5WidgetsMacros.cmake
%{_qt5_libdir}/cmake/Qt5Xml/Qt5XmlConfig*.cmake
%{_qt5_libdir}/cmake/Qt5/Qt5ModuleLocation.cmake
%{_qt5_libdir}/cmake/Qt5AccessibilitySupport/
%{_qt5_libdir}/cmake/Qt5DeviceDiscoverySupport/
%{_qt5_libdir}/cmake/Qt5EdidSupport/
%{_qt5_libdir}/cmake/Qt5EglFSDeviceIntegration/
%{_qt5_libdir}/cmake/Qt5EglFsKmsSupport/
%{_qt5_libdir}/cmake/Qt5EglSupport/
%{_qt5_libdir}/cmake/Qt5EventDispatcherSupport/
%{_qt5_libdir}/cmake/Qt5FbSupport/
%{_qt5_libdir}/cmake/Qt5FontDatabaseSupport/
%{_qt5_libdir}/cmake/Qt5GlxSupport/
%{_qt5_libdir}/cmake/Qt5InputSupport/
%{_qt5_libdir}/cmake/Qt5KmsSupport/
%{_qt5_libdir}/cmake/Qt5LinuxAccessibilitySupport/
%{_qt5_libdir}/cmake/Qt5PlatformCompositorSupport/
%{_qt5_libdir}/cmake/Qt5ServiceSupport/
%{_qt5_libdir}/cmake/Qt5ThemeSupport/
%{_qt5_libdir}/cmake/Qt5XcbQpa/
%{_qt5_libdir}/cmake/Qt5XkbCommonSupport/
%{_qt5_libdir}/metatypes/qt5core_metatypes.json
%{_qt5_libdir}/metatypes/qt5gui_metatypes.json
%{_qt5_libdir}/metatypes/qt5widgets_metatypes.json
%{_qt5_libdir}/pkgconfig/Qt5.pc
%{_qt5_libdir}/pkgconfig/Qt5Concurrent.pc
%{_qt5_libdir}/pkgconfig/Qt5Core.pc
%{_qt5_libdir}/pkgconfig/Qt5DBus.pc
%{_qt5_libdir}/pkgconfig/Qt5Gui.pc
%{_qt5_libdir}/pkgconfig/Qt5Network.pc
%{_qt5_libdir}/pkgconfig/Qt5OpenGL.pc
%{_qt5_libdir}/pkgconfig/Qt5PrintSupport.pc
%{_qt5_libdir}/pkgconfig/Qt5Sql.pc
%{_qt5_libdir}/pkgconfig/Qt5Test.pc
%{_qt5_libdir}/pkgconfig/Qt5Widgets.pc
%{_qt5_libdir}/pkgconfig/Qt5Xml.pc
%if 0%{?egl}
%{_qt5_libdir}/libQt5EglFsKmsSupport.prl
%{_qt5_libdir}/libQt5EglFsKmsSupport.so
%endif
%{_qt5_libdir}/qt5/bin/tracegen
## private-devel globs
# keep mkspecs/modules stuff  in -devel for now, https://bugzilla.redhat.com/show_bug.cgi?id=1705280
%{_qt5_archdatadir}/mkspecs/modules/qt_lib_*_private.pri
%exclude %{_qt5_headerdir}/*/%{version}/

%files private-devel
%{_qt5_headerdir}/*/%{version}/
#{_qt5_archdatadir}/mkspecs/modules/qt_lib_*_private.pri

%files static
%{_qt5_headerdir}/QtOpenGLExtensions/
%{_qt5_libdir}/libQt5OpenGLExtensions.*a
%{_qt5_libdir}/libQt5OpenGLExtensions.prl
%{_qt5_libdir}/cmake/Qt5OpenGLExtensions/
%{_qt5_libdir}/pkgconfig/Qt5OpenGLExtensions.pc
%{_qt5_libdir}/libQt5AccessibilitySupport.*a
%{_qt5_libdir}/libQt5AccessibilitySupport.prl
%{_qt5_headerdir}/QtAccessibilitySupport
%{_qt5_libdir}/libQt5DeviceDiscoverySupport.*a
%{_qt5_libdir}/libQt5DeviceDiscoverySupport.prl
%{_qt5_headerdir}/QtDeviceDiscoverySupport
%{_qt5_libdir}/libQt5EglSupport.*a
%{_qt5_libdir}/libQt5EglSupport.prl
%{_qt5_headerdir}/QtEglSupport
%{_qt5_libdir}/libQt5EventDispatcherSupport.*a
%{_qt5_libdir}/libQt5EventDispatcherSupport.prl
%{_qt5_headerdir}/QtEventDispatcherSupport
%{_qt5_libdir}/libQt5FbSupport.*a
%{_qt5_libdir}/libQt5FbSupport.prl
%{_qt5_headerdir}/QtFbSupport
%{_qt5_libdir}/libQt5FontDatabaseSupport.*a
%{_qt5_libdir}/libQt5FontDatabaseSupport.prl
%{_qt5_headerdir}/QtFontDatabaseSupport
%{_qt5_libdir}/libQt5GlxSupport.*a
%{_qt5_libdir}/libQt5GlxSupport.prl
%{_qt5_headerdir}/QtGlxSupport
%{_qt5_libdir}/libQt5InputSupport.*a
%{_qt5_libdir}/libQt5InputSupport.prl
%{_qt5_libdir}/libQt5LinuxAccessibilitySupport.*a
%{_qt5_libdir}/libQt5LinuxAccessibilitySupport.prl
%{_qt5_headerdir}/QtLinuxAccessibilitySupport
%{_qt5_libdir}/libQt5PlatformCompositorSupport.*a
%{_qt5_libdir}/libQt5PlatformCompositorSupport.prl
%{_qt5_headerdir}/QtPlatformCompositorSupport
%{_qt5_libdir}/libQt5ServiceSupport.*a
%{_qt5_libdir}/libQt5ServiceSupport.prl
%{_qt5_headerdir}/QtServiceSupport
%{_qt5_libdir}/libQt5ThemeSupport.*a
%{_qt5_libdir}/libQt5ThemeSupport.prl
%{_qt5_headerdir}/QtThemeSupport
%{_qt5_libdir}/libQt5KmsSupport.*a
%{_qt5_libdir}/libQt5KmsSupport.prl
%{_qt5_headerdir}/QtKmsSupport
%{_qt5_libdir}/libQt5EdidSupport.*a
%{_qt5_libdir}/libQt5EdidSupport.prl
%{_qt5_libdir}/libQt5XkbCommonSupport.*a
%{_qt5_libdir}/libQt5XkbCommonSupport.prl
%if 0%{?vulkan}
%{_qt5_headerdir}/QtVulkanSupport/
%{_qt5_libdir}/cmake/Qt5VulkanSupport/
%{_qt5_libdir}/libQt5VulkanSupport.*a
%{_qt5_libdir}/libQt5VulkanSupport.prl
%endif

%if 0%{?examples}
%files examples
%{_qt5_examplesdir}/
%endif

%if "%{?ibase}" != "-no-sql-ibase"
%files ibase
%{_qt5_plugindir}/sqldrivers/libqsqlibase.so
%{_qt5_libdir}/cmake/Qt5Sql/Qt5Sql_QIBaseDriverPlugin.cmake
%endif

%files mysql
%{_qt5_plugindir}/sqldrivers/libqsqlmysql.so
%{_qt5_libdir}/cmake/Qt5Sql/Qt5Sql_QMYSQLDriverPlugin.cmake

%files odbc
%{_qt5_plugindir}/sqldrivers/libqsqlodbc.so
%{_qt5_libdir}/cmake/Qt5Sql/Qt5Sql_QODBCDriverPlugin.cmake

%files postgresql
%{_qt5_plugindir}/sqldrivers/libqsqlpsql.so
%{_qt5_libdir}/cmake/Qt5Sql/Qt5Sql_QPSQLDriverPlugin.cmake

%if "%{?tds}" != "-no-sql-tds"
%files tds
%{_qt5_plugindir}/sqldrivers/libqsqltds.so
%{_qt5_libdir}/cmake/Qt5Sql/Qt5Sql_QTDSDriverPlugin.cmake
%endif

%ldconfig_scriptlets gui

%files gui
%dir %{_sysconfdir}/X11/xinit
%dir %{_sysconfdir}/X11/xinit/xinitrc.d/
%{_sysconfdir}/X11/xinit/xinitrc.d/10-qt5-check-opengl2.sh
%{_qt5_libdir}/libQt5Gui.so.5*
%{_qt5_libdir}/libQt5OpenGL.so.5*
%{_qt5_libdir}/libQt5PrintSupport.so.5*
%{_qt5_libdir}/libQt5Widgets.so.5*
%{_qt5_libdir}/libQt5XcbQpa.so.5*
%{_qt5_plugindir}/generic/libqevdevkeyboardplugin.so
%{_qt5_plugindir}/generic/libqevdevmouseplugin.so
%{_qt5_plugindir}/generic/libqevdevtabletplugin.so
%{_qt5_plugindir}/generic/libqevdevtouchplugin.so
%{_qt5_plugindir}/generic/libqlibinputplugin.so
%{_qt5_libdir}/cmake/Qt5Gui/Qt5Gui_QLibInputPlugin.cmake
%{_qt5_plugindir}/generic/libqtuiotouchplugin.so
%{_qt5_libdir}/cmake/Qt5Gui/Qt5Gui_QEvdevKeyboardPlugin.cmake
%{_qt5_libdir}/cmake/Qt5Gui/Qt5Gui_QEvdevMousePlugin.cmake
%{_qt5_libdir}/cmake/Qt5Gui/Qt5Gui_QEvdevTabletPlugin.cmake
%{_qt5_libdir}/cmake/Qt5Gui/Qt5Gui_QEvdevTouchScreenPlugin.cmake
%{_qt5_libdir}/cmake/Qt5Gui/Qt5Gui_QTuioTouchPlugin.cmake
%{_qt5_plugindir}/imageformats/libqgif.so
%{_qt5_plugindir}/imageformats/libqico.so
%{_qt5_plugindir}/imageformats/libqjpeg.so
%{_qt5_libdir}/cmake/Qt5Gui/Qt5Gui_QGifPlugin.cmake
%{_qt5_libdir}/cmake/Qt5Gui/Qt5Gui_QICOPlugin.cmake
%{_qt5_libdir}/cmake/Qt5Gui/Qt5Gui_QJpegPlugin.cmake
%{_qt5_plugindir}/platforminputcontexts/libcomposeplatforminputcontextplugin.so
%{_qt5_plugindir}/platforminputcontexts/libibusplatforminputcontextplugin.so
%{_qt5_libdir}/cmake/Qt5Gui/Qt5Gui_QComposePlatformInputContextPlugin.cmake
%{_qt5_libdir}/cmake/Qt5Gui/Qt5Gui_QIbusPlatformInputContextPlugin.cmake
%if 0%{?egl}
%{_qt5_libdir}/libQt5EglFSDeviceIntegration.so.5*
%{_qt5_libdir}/libQt5EglFsKmsSupport.so.5*
%{_qt5_plugindir}/platforms/libqeglfs.so
%{_qt5_plugindir}/platforms/libqminimalegl.so
%dir %{_qt5_plugindir}/egldeviceintegrations/
%{_qt5_plugindir}/egldeviceintegrations/libqeglfs-kms-integration.so
%{_qt5_plugindir}/egldeviceintegrations/libqeglfs-x11-integration.so
%{_qt5_plugindir}/xcbglintegrations/libqxcb-egl-integration.so
%{_qt5_plugindir}/egldeviceintegrations/libqeglfs-kms-egldevice-integration.so
%{_qt5_plugindir}/egldeviceintegrations/libqeglfs-emu-integration.so
%{_qt5_libdir}/cmake/Qt5Gui/Qt5Gui_QMinimalEglIntegrationPlugin.cmake
%{_qt5_libdir}/cmake/Qt5Gui/Qt5Gui_QEglFSIntegrationPlugin.cmake
%{_qt5_libdir}/cmake/Qt5Gui/Qt5Gui_QEglFSX11IntegrationPlugin.cmake
%{_qt5_libdir}/cmake/Qt5Gui/Qt5Gui_QEglFSKmsGbmIntegrationPlugin.cmake
%{_qt5_libdir}/cmake/Qt5Gui/Qt5Gui_QXcbEglIntegrationPlugin.cmake
%{_qt5_libdir}/cmake/Qt5Gui/Qt5Gui_QEglFSKmsEglDeviceIntegrationPlugin.cmake
%{_qt5_libdir}/cmake/Qt5Gui/Qt5Gui_QEglFSEmulatorIntegrationPlugin.cmake
%endif
%{_qt5_plugindir}/platforms/libqlinuxfb.so
%{_qt5_plugindir}/platforms/libqminimal.so
%{_qt5_plugindir}/platforms/libqoffscreen.so
%{_qt5_plugindir}/platforms/libqxcb.so
%{_qt5_plugindir}/platforms/libqvnc.so
%{_qt5_libdir}/cmake/Qt5Gui/Qt5Gui_QLinuxFbIntegrationPlugin.cmake
%{_qt5_libdir}/cmake/Qt5Gui/Qt5Gui_QMinimalIntegrationPlugin.cmake
%{_qt5_libdir}/cmake/Qt5Gui/Qt5Gui_QOffscreenIntegrationPlugin.cmake
%{_qt5_libdir}/cmake/Qt5Gui/Qt5Gui_QVncIntegrationPlugin.cmake
%{_qt5_libdir}/cmake/Qt5Gui/Qt5Gui_QXcbIntegrationPlugin.cmake
%{_qt5_plugindir}/xcbglintegrations/libqxcb-glx-integration.so
%{_qt5_libdir}/cmake/Qt5Gui/Qt5Gui_QXcbGlxIntegrationPlugin.cmake
%{_qt5_plugindir}/platformthemes/libqxdgdesktopportal.so
%{_qt5_plugindir}/platformthemes/libqgtk3.so
%{_qt5_libdir}/cmake/Qt5Gui/Qt5Gui_QXdgDesktopPortalThemePlugin.cmake
%{_qt5_libdir}/cmake/Qt5Gui/Qt5Gui_QGtk3ThemePlugin.cmake
%{_qt5_plugindir}/printsupport/libcupsprintersupport.so
%{_qt5_libdir}/cmake/Qt5PrintSupport/Qt5PrintSupport_QCupsPrinterSupportPlugin.cmake


%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.15.18-2
- Import
