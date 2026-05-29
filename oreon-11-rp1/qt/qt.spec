%global source0_hash none

# Fedora Review: http://bugzilla.redhat.com/188180

# configure options
# -no-pch disables precompiled headers, make ccache-friendly
%define no_pch -no-pch

# See http://bugzilla.redhat.com/223663
%define multilib_archs x86_64 %{ix86} %{mips} ppc64 ppc64le ppc s390x s390 sparc64 sparcv9
%define multilib_basearchs x86_64 %{mips64} ppc64 ppc64le s390x sparc64

%if 0%{?fedora} || 0%{?rhel} > 6
# use external qt_settings pkg
%define qt_settings 1
%endif

%if (0%{?fedora} && 0%{?fedora} < 26) || (0%{?rhel} > 6 && 0%{?rhel} <= 7)
%global system_clucene 1
%endif

# See http://bugzilla.redhat.com/1279265
%if 0%{?rhel} && 0%{?rhel} <= 7
%global inject_optflags 1
%endif

%global rpm_macros_dir %(d=%{_rpmconfigdir}/macros.d; [ -d $d ] || d=%{_sysconfdir}/rpm; echo $d)

# trim changelog included in binary rpms
%global _changelog_trimtime %(date +%s -d "1 year ago")

# support qtchooser, except when building for inclusion in a flatpak
%if !0%{?flatpak}
%define qtchooser 1
%endif

%if 0%{?qtchooser}
%define priority 20
%ifarch %{multilib_basearchs}
%define priority 25
%endif
%endif

Summary: Qt toolkit
Name:    qt
Epoch:   1
Version: 4.8.7
Release: 85%{?dist}

# See LGPL_EXCEPTIONS.txt, LICENSE.GPL3, respectively, for exception details
# Automatically converted from old format: (LGPLv2 with exceptions or GPLv3 with exceptions) and ASL 2.0 and BSD and FTL and MIT - review is highly recommended.
License: (LGPL-2.0-or-later WITH FLTK-exception OR LicenseRef-Callaway-GPLv3-with-exceptions) AND Apache-2.0 AND LicenseRef-Callaway-BSD AND FTL AND LicenseRef-Callaway-MIT
Url:     http://qt-project.org/
%if 0%{?beta:1}
Source0:        https://download.qt-project.org/development_releases/qt/4.8/4.8.7-%{beta}/qt-everywhere-opensource-src-4.8.7-%{beta}.tar.gz
%else
Source0:        https://download.qt-project.org/official_releases/qt/4.8/4.8.7/qt-everywhere-opensource-src-4.8.7.tar.gz
%endif

Obsoletes: qt4 < %{version}-%{release}
Provides: qt4 = %{version}-%{release}
%{?_isa:Provides: qt4%{?_isa} = %{version}-%{release}}

# default Qt config file
Source4: Trolltech.conf

# header file to workaround multilib issue
Source5: qconfig-multilib.h

# set default QMAKE_CFLAGS_RELEASE
Patch2: qt-everywhere-opensource-src-4.8.0-tp-multilib-optflags.patch

# get rid of timestamp which causes multilib problem
Patch4: qt-everywhere-opensource-src-4.8.5-uic_multilib.patch

# reduce debuginfo in qtwebkit (webcore)
Patch5: qt-everywhere-opensource-src-4.8.5-webcore_debuginfo.patch

# cups16 printer discovery
Patch6: qt-cupsEnumDests.patch

# prefer adwaita over gtk+ on DE_GNOME
# https://bugzilla.redhat.com/show_bug.cgi?id=1192453
Patch10: qt-prefer_adwaita_on_gnome.patch

# enable ft lcdfilter
Patch15: qt-x11-opensource-src-4.5.1-enable_ft_lcdfilter.patch

# may be upstreamable, not sure yet
# workaround for gdal/grass crashers wrt glib_eventloop null deref's
Patch23: qt-everywhere-opensource-src-4.6.3-glib_eventloop_nullcheck.patch

# hack out largely useless (to users) warnings about qdbusconnection
# (often in kde apps), keep an eye on https://git.reviewboard.kde.org/r/103699/
Patch25: qt-everywhere-opensource-src-4.8.3-qdbusconnection_no_debug.patch

# lrelease-qt4 tries to run qmake not qmake-qt4 (http://bugzilla.redhat.com/820767)
Patch26: qt-everywhere-opensource-src-4.8.1-linguist_qmake-qt4.patch

# enable debuginfo in libQt3Support
Patch27: qt-everywhere-opensource-src-4.8.1-qt3support_debuginfo.patch

# kde4/multilib QT_PLUGIN_PATH
Patch28: qt-everywhere-opensource-src-4.8.5-qt_plugin_path.patch

## upstreamable bits
# add support for pkgconfig's Requires.private to qmake
Patch50: qt-everywhere-opensource-src-4.8.4-qmake_pkgconfig_requires_private.patch

# FTBFS against newer firebird-4.0.0
Patch51: qt-everywhere-opensource-src-4.8.7-firebird-4.0.0.patch

# workaround major/minor macros possibly being defined already
Patch52: qt-everywhere-opensource-src-4.8.7-QT_VERSION_CHECK.patch

# fix invalid inline assembly in qatomic_{i386,x86_64}.h (de)ref implementations
Patch53: qt-x11-opensource-src-4.5.0-fix-qatomic-inline-asm.patch

# fix invalid assumptions about mysql_config --libs
# http://bugzilla.redhat.com/440673
Patch54: qt-everywhere-opensource-src-4.8.5-mysql_config.patch

# http://bugs.kde.org/show_bug.cgi?id=180051#c22
Patch55: qt-everywhere-opensource-src-4.6.2-cups.patch

# backport https://codereview.qt-project.org/#/c/205874/
Patch56: qt-everywhere-opensource-src-4.8.7-mariadb.patch

# use QMAKE_LFLAGS_RELEASE when building qmake
Patch57: qt-everywhere-opensource-src-4.8.7-qmake_LFLAGS.patch

# Fails to create debug build of Qt projects on mingw (rhbz#653674)
Patch64: qt-everywhere-opensource-src-4.8.5-QTBUG-14467.patch

# fix QTreeView crash triggered by KPackageKit (patch by David Faure)
Patch65: qt-everywhere-opensource-src-4.8.0-tp-qtreeview-kpackagekit-crash.patch

# fix the outdated standalone copy of JavaScriptCore
Patch67: qt-everywhere-opensource-src-4.8.6-s390.patch

# https://bugs.webkit.org/show_bug.cgi?id=63941
# -Wall + -Werror = fail
Patch68: qt-everywhere-opensource-src-4.8.3-no_Werror.patch

# revert qlist.h commit that seems to induce crashes in qDeleteAll<QList (QTBUG-22037)
Patch69: qt-everywhere-opensource-src-4.8.0-QTBUG-22037.patch

# Buttons in Qt applications not clickable when run under gnome-shell (#742658, QTBUG-21900)
Patch71:  qt-everywhere-opensource-src-4.8.5-QTBUG-21900.patch

# workaround
# sql/drivers/tds/qsql_tds.cpp:341:49: warning: dereferencing type-punned pointer will break strict-aliasing rules [-Wstrict-aliasing]
Patch74: qt-everywhere-opensource-src-4.8.5-tds_no_strict_aliasing.patch

# add missing method for QBasicAtomicPointer on s390(x)
Patch76: qt-everywhere-opensource-src-4.8.0-s390-atomic.patch

# don't spam in release/no_debug mode if libicu is not present at runtime
Patch77: qt-everywhere-opensource-src-4.8.3-icu_no_debug.patch

# https://bugzilla.redhat.com/show_bug.cgi?id=810500
Patch81: qt-everywhere-opensource-src-4.8.2--assistant-crash.patch

# https://bugzilla.redhat.com/show_bug.cgi?id=694385
# https://bugs.kde.org/show_bug.cgi?id=249217
# https://bugreports.qt-project.org/browse/QTBUG-4862
# QDir::homePath() should account for an empty HOME environment variable on X11
Patch82: qt-everywhere-opensource-src-4.8.5-QTBUG-4862.patch

# poll support
Patch83: qt-4.8-poll.patch

# fix QTBUG-35459 (too low entityCharacterLimit=1024 for CVE-2013-4549)
Patch84: qt-everywhere-opensource-src-4.8.5-QTBUG-35459.patch

# systemtrayicon plugin support (for appindicators)
Patch86: qt-everywhere-opensource-src-4.8.6-systemtrayicon.patch

# fixes for LibreOffice from the upstream Qt bug tracker (#1105422):
Patch87: qt-everywhere-opensource-src-4.8.6-QTBUG-37380.patch
Patch88: qt-everywhere-opensource-src-4.8.6-QTBUG-34614.patch
Patch89: qt-everywhere-opensource-src-4.8.6-QTBUG-38585.patch

# build against the system clucene09-core
Patch90: qt-everywhere-opensource-src-4.8.6-system-clucene.patch

# fix arch autodetection for 64-bit MIPS
Patch91: qt-everywhere-opensource-src-4.8.7-mips64.patch

# fix build issue(s) with gcc6
Patch92: qt-everywhere-opensource-src-4.8.7-gcc6.patch

# support alsa-1.1.x
Patch93: qt-everywhere-opensource-src-4.8.7-alsa-1.1.patch

# support OpenSSL 1.1.x, from Debian (Gert Wollny, Dmitry Eremin-Solenikov)
# https://anonscm.debian.org/cgit/pkg-kde/qt/qt4-x11.git/tree/debian/patches/openssl_1.1.patch?h=experimental
# fixes for -openssl-linked by Kevin Kofler
Patch94: qt-everywhere-opensource-src-4.8.7-openssl-1.1.patch

# fix build with ICU >= 59, from OpenSUSE (Fabian Vogt)
# https://build.opensuse.org/package/view_file/KDE:Qt/libqt4/fix-build-icu59.patch?expand=1
Patch95: qt-everywhere-opensource-src-4.8.7-icu59.patch

# workaround qtscript failures when building with f28's gcc8
# https://bugzilla.redhat.com/show_bug.cgi?id=1580047
Patch96: qt-everywhere-opensource-src-4.8.7-gcc8_qtscript.patch

# Fix ordered pointer comparison against zero problem reported by gcc-11
Patch97: qt-everywhere-opensource-src-4.8.7-gcc11.patch

# hardcode the compiler version in the build key once and for all
Patch98: qt-everywhere-opensource-src-4.8.7-hardcode-buildkey.patch

# FTBFS openssl3
Patch99: qt-everywhere-opensource-src-4.8.7-openssl3.patch

# FTBFS icu76
Patch100: qt-4.6-ftbfs-icu76.patch

# upstream patches
# backported from Qt5 (essentially)
# http://bugzilla.redhat.com/702493
# https://bugreports.qt-project.org/browse/QTBUG-5545
Patch102: qt-everywhere-opensource-src-4.8.5-qgtkstyle_disable_gtk_theme_check.patch
# workaround for MOC issues with Boost headers (#756395)
# https://bugreports.qt-project.org/browse/QTBUG-22829
Patch113: qt-everywhere-opensource-src-4.8.6-QTBUG-22829.patch

# aarch64 support, https://bugreports.qt-project.org/browse/QTBUG-35442
Patch180: qt-aarch64.patch

# Fix problem caused by gcc 9 fixing a longstanding bug.
# https://github.com/qt/qtbase/commit/c35a3f519007af44c3b364b9af86f6a336f6411b.patch
Patch181: qt-everywhere-opensource-src-4.8.7-qforeach.patch

# riscv64 support
Patch182: qt-everywhere-opensource-src-4.8.7-riscv64.patch

## upstream git

## security patches
# CVE-2018-19872 qt: malformed PPM image causing division by zero and crash in qppmhandler.cpp
Patch500: qt-everywhere-opensource-src-4.8.7-crash-in-qppmhandler.patch

# CVE-2020-17507 qt: buffer over-read in read_xbm_body in gui/image/qxbmhandler.cpp
Patch501: qt-CVE-2020-17507.patch

# no CVE qt: Clamp parsed doubles to float representable values
Patch502: qt-everywhere-opensource-src-4.8.7-clamp-parsed-doubles-to-float-representtable-values.patch

# CVE-2020-24741 qt: QLibrary loads libraries relative to CWD which could result in arbitrary code execution
Patch503: qt-everywhere-opensource-src-4.8.5-CVE-2020-24741.patch

# CVE-2023-32573 qt: Uninitialized variable usage in m_unitsPerEm
Patch504: qt-CVE-2023-32573.patch
Patch505: qt-CVE-2023-34410.patch

# desktop files
Source20: assistant.desktop
Source21: designer.desktop
Source22: linguist.desktop
Source23: qdbusviewer.desktop
Source24: qtdemo.desktop
Source25: qtconfig.desktop

# upstream qt4-logo, http://trolltech.com/images/products/qt/qt4-logo
Source30: https://pkgs.fedoraproject.org/repo/pkgs/qt4/hi128-app-qt4-logo.png/d9f511e4b51983b4e10eb58b320416d5/hi128-app-qt4-logo.png
Source31: https://pkgs.fedoraproject.org/repo/pkgs/qt4/hi48-app-qt4-logo.png/6dcc0672ff9e60a6b83f95c5f42bec5b/hi48-app-qt4-logo.png

## BOOTSTRAPPING, undef docs, demos, examples, phonon, webkit

## optional plugin bits
# set to -no-sql-<driver> to disable
# set to -qt-sql-<driver> to enable *in* qt library
%global mysql -plugin-sql-mysql
%define odbc -plugin-sql-odbc
%define psql -plugin-sql-psql
%define sqlite -plugin-sql-sqlite
%if 0%{?rhel} && 0%{?rhel} <= 7
%define phonon -phonon
%define phonon_backend -phonon-backend
%endif
%define dbus -dbus-linked
%define graphicssystem -graphicssystem raster
%define gtkstyle -gtkstyle
%if 0%{?fedora} || 0%{?rhel} > 7
# FIXME/TODO: use system webkit for assistant, examples/webkit, demos/browser
# %%define webkit -webkit
%define ibase -plugin-sql-ibase
%define tds -plugin-sql-tds
%endif
%if 0%{?rhel} && 0%{?rhel} <= 7
%define no_javascript_jit -no-javascript-jit
%define ibase -no-sql-ibase
%define tds -no-sql-tds
%endif
# disable it temporary (firebird build failed on s390x, bz#1969393)
%if 0%{?fedora} > 34
%define ibase -no-sql-ibase
%endif

# workaround FTBFS with gcc9
#if 0%{?fedora} > 29
%if 0
%global no_javascript_jit -no-javascript-jit
%endif

%ifarch riscv64
%define no_javascript_jit -no-javascript-jit
%endif

# macros, be mindful to keep sync'd with macros.qt4
Source1: macros.qt4
%define _qt4 %{name}
%define _qt4_prefix %{_libdir}/qt4
%define _qt4_bindir %{_qt4_prefix}/bin
# _qt4_datadir is not multilib clean, and hacks to workaround that breaks stuff.
#define _qt4_datadir %{_datadir}/qt4
%define _qt4_datadir %{_qt4_prefix}
%define _qt4_demosdir %{_qt4_prefix}/demos
%define _qt4_docdir %{_docdir}/qt4
%define _qt4_examplesdir %{_qt4_prefix}/examples
%define _qt4_headerdir %{_includedir} 
%define _qt4_importdir %{_qt4_prefix}/imports 
%define _qt4_libdir %{_libdir}
%define _qt4_plugindir %{_qt4_prefix}/plugins
%define _qt4_sysconfdir %{_sysconfdir}
%define _qt4_translationdir %{_datadir}/qt4/translations

BuildRequires: make
BuildRequires: cups-devel
BuildRequires: desktop-file-utils
BuildRequires: findutils
BuildRequires: gcc-c++
BuildRequires: libjpeg-devel
BuildRequires: libmng-devel
BuildRequires: libtiff-devel
BuildRequires: pkgconfig
BuildRequires: pkgconfig(alsa) 
BuildRequires: pkgconfig(dbus-1)
BuildRequires: pkgconfig(fontconfig)
BuildRequires: pkgconfig(glib-2.0)
%if 0%{?fedora} || 0%{?rhel} > 6
BuildRequires: pkgconfig(icu-i18n)
%else
BuildRequires: libicu-devel
%endif
## as far as I can tell, this isn't used anywhere, omitting for now
## https://bugzilla.redhat.com/show_bug.cgi?id=1606047
#BuildRequires: pkgconfig(NetworkManager)
%global openssl -openssl-linked
%if 0%{?fedora} == 27
BuildRequires: compat-openssl10-devel
%else
BuildRequires: openssl-devel
%endif
BuildRequires: pkgconfig(libpng)
BuildRequires: pkgconfig(libpulse)
BuildRequires: pkgconfig(xtst) 
BuildRequires: pkgconfig(zlib)
BuildRequires: rsync

%define gl_deps pkgconfig(gl) pkgconfig(glu)
%define x_deps pkgconfig(ice) pkgconfig(sm) pkgconfig(xcursor) pkgconfig(xext) pkgconfig(xfixes) pkgconfig(xft) pkgconfig(xi) pkgconfig(xinerama) pkgconfig(xrandr) pkgconfig(xrender) pkgconfig(xt) pkgconfig(xv) pkgconfig(x11) pkgconfig(xproto)
BuildRequires: %{gl_deps}
BuildRequires: %{x_deps}

%if 0%{?system_clucene}
BuildRequires: clucene09-core-devel >= 0.9.21b-12
%endif

%if "%{?ibase}" != "-no-sql-ibase"
BuildRequires: firebird-devel
%endif

%if "%{?mysql}" == "-no-sql-mysql"
Obsoletes: %{name}-mysql < %{epoch}:%{version}-%{release}
%else
%if 0%{?fedora} > 27 || 0%{?rhel} > 7
BuildRequires: mariadb-connector-c-devel
%else
BuildRequires: mysql-devel >= 4.0
%endif
%endif

%if "%{?phonon_backend}" == "-phonon-backend"
BuildRequires: pkgconfig(gstreamer-0.10) 
BuildRequires: pkgconfig(gstreamer-plugins-base-0.10) 
%endif

%if "%{?gtkstyle}" == "-gtkstyle"
BuildRequires: pkgconfig(gtk+-2.0) 
%endif

%if "%{?psql}" != "-no-sql-psql"
BuildRequires: libpq-devel
%endif

%if "%{?odbc}" != "-no-sql-odbc"
BuildRequires: unixODBC-devel
%endif

%if "%{?sqlite}" != "-no-sql-sqlite"
%define _system_sqlite -system-sqlite
BuildRequires: pkgconfig(sqlite3) 
%endif

Provides:  qt4-sqlite = %{version}-%{release}
%{?_isa:Provides: qt4-sqlite%{?_isa} = %{version}-%{release}}
Obsoletes: qt-sqlite < 1:4.7.1-16
Provides:  qt-sqlite = %{?epoch:%{epoch}:}%{version}-%{release} 
%{?_isa:Provides: qt-sqlite%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}}

%if "%{?tds}" != "-no-sql-tds"
BuildRequires: freetds-devel
%endif

Obsoletes: qgtkstyle < 0.1
Provides:  qgtkstyle = 0.1-1
Requires: %{name}-common = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: ca-certificates
%if 0%{?qt_settings}
Requires: qt-settings
%endif
%if 0%{?qtchooser}
Requires(post): %{_sbindir}/update-alternatives
Requires(postun): %{_sbindir}/update-alternatives
%endif
Recommends: (ibus-qt if ibus)

%description 
Qt is a software toolkit for developing applications.

This package contains base tools, like string, xml, and network
handling.

%package common
Summary: Common files for Qt
Requires: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
BuildArch: noarch
%description common
%{summary}.

%package assistant
Summary: Documentation browser for Qt 4
Requires: %{name}-sqlite%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Provides: qt4-assistant = %{version}-%{release}
Requires: %{name}-x11%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
%if ! 0%{?system_clucene}
Provides: bundled(clucene09)
%endif
%description assistant
%{summary}.

%package config
Summary: Graphical configuration tool for programs using Qt 4 
# -config introduced in 4.7.1-10 , for upgrade path
# seems to tickle a pk bug, https://bugzilla.redhat.com/674326
#Obsoletes: %{name}-x11 < 1:4.7.1-10
Obsoletes: qt4-config < 4.5.0
Provides:  qt4-config = %{version}-%{release}
Requires: %{name}-x11%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
%description config 
%{summary}.

%define demos 1
%package demos
Summary: Demonstration applications for %{name}
Requires: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: %{name}-doc
%description demos
%{summary}.

%define docs 1
%package doc
Summary: API documentation for %{name}
Requires: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: %{name}-assistant
Obsoletes: qt4-doc < %{version}-%{release}
Provides:  qt4-doc = %{version}-%{release}
# help workaround yum bug http://bugzilla.redhat.com/502401
Obsoletes: qt-doc < 1:4.5.1-4
BuildArch: noarch
%description doc
%{summary}.

%package designer-plugin-webkit
Summary: Qt designer plugin for WebKit
Requires: %{name}-x11%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
%description designer-plugin-webkit
%{summary}.

%package devel
Summary: Development files for the Qt toolkit
Requires: %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: %{name}-x11%{?_isa}
Requires: %{name}-sqlite%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
# qmake defaults, could also consider something like:
# Requires: (gcc-c++ if redhat-rpm-config
# or
# Recommends: gcc-c++
# or a combination of the 2
Requires: gcc-c++
Requires: %{gl_deps}
Requires: %{x_deps}
Requires: pkgconfig
%if 0%{?phonon:1}
Provides: qt4-phonon-devel = %{version}-%{release}
%endif
Obsoletes: qt4-designer < %{version}-%{release}
Provides:  qt4-designer = %{version}-%{release}
# as long as libQtUiTools.a is included
Provides:  %{name}-static = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:  qt4-static = %{version}-%{release}
Obsoletes: qt4-devel < %{version}-%{release}
Provides:  qt4-devel = %{version}-%{release}
%{?_isa:Provides: qt4-devel%{?_isa} = %{version}-%{release}}
%if (0%{?fedora} && 0%{?inject_optflags}) || (0%{?rhel} > 7 && 0%{?inject_optflags})
# default flags are used, important configuration is contained here (#1279265)
Requires: redhat-rpm-config
%endif
%description devel
This package contains the files necessary to develop
applications using the Qt toolkit.  Includes:
Qt Linguist

# make a devel private subpkg or not?
%define private 1
%package devel-private
Summary: Private headers for Qt toolkit 
Provides: qt4-devel-private = %{version}-%{release}
Provides: %{name}-private-devel = %{?epoch:%{epoch}:}%{version}-%{release}
Provides: qt4-private-devel = %{version}-%{release}
Requires: %{name}-devel = %{?epoch:%{epoch}:}%{version}-%{release}
BuildArch: noarch
%description devel-private
%{summary}.

%define examples 1
%package examples
Summary: Programming examples for %{name}
Requires: %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
%description examples
%{summary}.

%define qvfb 1
%package qvfb
Summary: Virtual frame buffer for Qt for Embedded Linux
Requires: %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
%description qvfb
%{summary}.

%package ibase
Summary: IBase driver for Qt's SQL classes
Requires: %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:  qt4-ibase = %{version}-%{release}
%{?_isa:Provides: qt4-ibase%{?_isa} = %{version}-%{release}}
%description ibase
%{summary}.

%package mysql
Summary: MySQL driver for Qt's SQL classes
Requires: %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes: qt4-MySQL < %{version}-%{release}
Provides:  qt4-MySQL = %{version}-%{release}
Obsoletes: qt4-mysql < %{version}-%{release}
Provides:  qt4-mysql = %{version}-%{release}
%{?_isa:Provides: qt4-mysql%{?_isa} = %{version}-%{release}}
%description mysql 
%{summary}.

%package odbc 
Summary: ODBC driver for Qt's SQL classes
Requires: %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes: qt4-ODBC < %{version}-%{release}
Provides:  qt4-ODBC = %{version}-%{release}
Obsoletes: qt4-odbc < %{version}-%{release}
Provides:  qt4-odbc = %{version}-%{release}
%{?_isa:Provides: qt4-odbc%{?_isa} = %{version}-%{release}}
%description odbc 
%{summary}.

%package postgresql 
Summary: PostgreSQL driver for Qt's SQL classes
Requires: %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes: qt4-PostgreSQL < %{version}-%{release}
Provides:  qt4-PostgreSQL = %{version}-%{release}
Obsoletes: qt4-postgresql < %{version}-%{release}
Provides:  qt4-postgresql = %{version}-%{release}
%{?_isa:Provides: qt4-postgresql%{?_isa} = %{version}-%{release}}
%description postgresql 
%{summary}.

%package tds
Summary: TDS driver for Qt's SQL classes
Requires: %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Provides: qt4-tds = %{version}-%{release}
%{?_isa:Provides: qt4-tds%{?_isa} = %{version}-%{release}}
%description tds
%{summary}.

%package x11
Summary: Qt GUI-related libraries
# include Obsoletes here to be safe(r) bootstrap-wise with phonon-4.5.0
# that will Provides: it -- Rex
Obsoletes: qt-designer-plugin-phonon < 1:4.7.2-6
Requires: %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes: qt4-x11 < %{version}-%{release}
Provides:  qt4-x11 = %{version}-%{release}
%{?_isa:Provides: qt4-x11%{?_isa} = %{version}-%{release}}
%if 0%{?fedora} || 0%{?rhel} > 7
## add kde-workspace too? -- rex
#Requires: (sni-qt%{?_isa} if plasma-workspace)
## yum-based tools still cannot handle rich deps ^^, so settle for Recommends until fixed
Recommends: sni-qt%{?_isa}
%endif
%description x11
Qt libraries used for drawing widgets and OpenGL items.

%package qdbusviewer
Summary: D-Bus debugger and viewer
# When split out from qt-x11
Obsoletes: qt-x11 < 1:4.8.5-2
Requires: %{name}-x11%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
%description qdbusviewer
QDbusviewer can be used to inspect D-Bus objects of running programs
and invoke methods on those objects.


%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q -n qt-everywhere-opensource-src-%{version} 

%patch -P4 -p1 -b .uic_multilib
%patch -P5 -p1 -b .webcore_debuginfo
# ie, where cups-1.6+ is present
%if 0%{?fedora} || 0%{?rhel} > 7
#patch6 -p1 -b .cupsEnumDests
%endif
%patch -P10 -p0 -b .prefer_adwaita_on_gnome
%patch -P15 -p1 -b .enable_ft_lcdfilter
%patch -P23 -p1 -b .glib_eventloop_nullcheck
%patch -P25 -p1 -b .qdbusconnection_no_debug
%patch -P26 -p1 -b .linguist_qtmake-qt4
%patch -P27 -p1 -b .qt3support_debuginfo
%patch -P28 -p1 -b .qt_plugin_path
%patch -P50 -p1 -b .qmake_pkgconfig_requires_private
%patch -P51 -p1 -b .firebird
%patch -P52 -p1 -b .QT_VERSION_CHECK
## TODO: still worth carrying?  if so, upstream it.
%patch -P53 -p1 -b .qatomic-inline-asm
## TODO: upstream me
%patch -P54 -p1 -b .mysql_config
%patch -P55 -p1 -b .cups-1
%patch -P56 -p1 -b .mariadb
%patch -P57 -p1 -b .qmake_LFLAGS
%patch -P64 -p1 -b .QTBUG-14467
%patch -P65 -p1 -b .qtreeview-kpackagekit-crash
%patch -P67 -p1 -b .s390
%patch -P68 -p1 -b .no_Werror
%patch -P69 -p1 -b .QTBUG-22037
%patch -P71 -p1 -b .QTBUG-21900
%patch -P74 -p1 -b .tds_no_strict_aliasing
%patch -P76 -p1 -b .s390-atomic
%patch -P77 -p1 -b .icu_no_debug
%patch -P81 -p1 -b .assistant-crash
%patch -P82 -p1 -b .QTBUG-4862
%patch -P83 -p1 -b .poll
%patch -P87 -p1 -b .QTBUG-37380
%patch -P88 -p0 -b .QTBUG-34614
%patch -P89 -p0 -b .QTBUG-38585

%if 0%{?system_clucene}
%patch -P90 -p1 -b .system_clucene
# delete bundled copy
rm -rf src/3rdparty/clucene
%endif
%patch -P91 -p1 -b .mips64
%patch -P92 -p1 -b .gcc6
%patch -P93 -p1 -b .alsa1.1
%if 0%{?fedora} > 27 || 0%{?rhel} > 7
%patch -P94 -p1 -b .openssl1.1
%endif
%patch -P95 -p1 -b .icu59
%if 0%{?fedora} > 27
%patch -P96 -p1 -b .gcc8_qtscript
%endif
%patch -P97 -p1 -b .gcc11
%patch -P98 -p1 -b .hardcode-buildkey
%patch -P99 -p1 -b .ssl3
%patch -P100 -p1 -b .ftbfs-icu76

# upstream patches
%patch -P102 -p1 -b .qgtkstyle_disable_gtk_theme_check
%patch -P113 -p1 -b .QTBUG-22829

%patch -P180 -p1 -b .aarch64
%patch -P181 -p1 -b .qforeach

%patch -P182 -p1 -b .riscv64
# upstream git

# security fixes
%patch -P500 -p1 -b .malformed-ppb-image-causing-crash
%patch -P501 -p1 -b .buffer-over-read-in-read_xbm_body
%patch -P502 -p1 -b .clamp-parsed-doubles-to-float-representtable-values
%patch -P503 -p1 -b .CVE-2020-24741
%patch -P504 -p1 -b .CVE-2023-32573
%patch -P505 -p1 -b .CVE-2023-34410

# regression fixes for the security fixes
%patch -P84 -p1 -b .QTBUG-35459

%patch -P86 -p1 -b .systemtrayicon

%define platform linux-g++

# some 64bit platforms assume -64 suffix, https://bugzilla.redhat.com/569542
%if "%{?__isa_bits}"  == "64"
%define platform linux-g++-64
%endif

# https://bugzilla.redhat.com/478481
%ifarch x86_64 aarch64 riscv64
%define platform linux-g++
%endif

%if 0%{?inject_optflags}
%patch -P2 -p1 -b .multilib-optflags
# drop backup file(s), else they get installed too, http://bugzilla.redhat.com/639463
rm -fv mkspecs/linux-g++*/qmake.conf.multilib-optflags

# drop -fexceptions from $RPM_OPT_FLAGS
RPM_OPT_FLAGS=`echo $RPM_OPT_FLAGS | sed 's|-fexceptions||g'`

sed -i -e "s|-O2|$RPM_OPT_FLAGS|g" \
  mkspecs/%{platform}/qmake.conf 

sed -i -e "s|^\(QMAKE_LFLAGS_RELEASE.*\)|\1 $RPM_LD_FLAGS|" \
  mkspecs/common/g++-unix.conf
%endif

# undefine QMAKE_STRIP (and friends), so we get useful -debuginfo pkgs (#193602)
sed -i -e 's|^\(QMAKE_STRIP.*=\).*$|\1|g' mkspecs/common/linux.conf

# set correct lib path
if [ "%{_lib}" == "lib64" ] ; then
  sed -i -e "s,/usr/lib /lib,/usr/%{_lib} /%{_lib},g" config.tests/{unix,x11}/*.test
  sed -i -e "s,/lib /usr/lib,/%{_lib} /usr/%{_lib},g" config.tests/{unix,x11}/*.test
fi

# some architectures do not accept -m64/-m32 flags
%ifarch %{mips} riscv64
sed -i -e 's,-m32,,' mkspecs/linux-g++-32/qmake.conf
sed -i -e 's,-m64,,' mkspecs/linux-g++-64/qmake.conf
%endif

# let makefile create missing .qm files, the .qm files should be included in qt upstream
for f in translations/*.ts ; do
  touch ${f%.ts}.qm
done


%build
# QT is known not to work properly with LTO at this point.  Some of the issues
# are being worked on upstream and disabling LTO should be re-evaluated as
# we update this change.  Until such time...
# Disable LTO
%define _lto_cflags %{nil}

# drop -fexceptions from $RPM_OPT_FLAGS
RPM_OPT_FLAGS=`echo $RPM_OPT_FLAGS | sed 's|-fexceptions||g'`

%if 0%{?fedora} || 0%{?rhel} > 7
# workaround for class std::auto_ptr' is deprecated with gcc-6
CXXFLAGS="$CXXFLAGS -std=gnu++98"
# javascriptcore FTBFS with gcc-6
CXXFLAGS="$CXXFLAGS -Wno-deprecated"
%endif

export QTDIR=$PWD
export PATH=$PWD/bin:$PATH
export LD_LIBRARY_PATH=$PWD/lib/
# TODO: opensuse adds -DOPENSSL_LOAD_CONF, find out if we want that too -- rex
export CXXFLAGS="$CXXFLAGS $RPM_OPT_FLAGS"
export CFLAGS="$CFLAGS $RPM_OPT_FLAGS"
export LDFLAGS="$LDFLAGS $RPM_LD_FLAGS"
export MAKEFLAGS="%{?_smp_mflags}"
export CXX="$CXX -std=gnu++98"

./configure -v \
  -confirm-license \
  -opensource \
  -optimized-qmake \
  -fast \
  -prefix %{_qt4_prefix} \
  -bindir %{_qt4_bindir} \
  -datadir %{_qt4_datadir} \
  -demosdir %{_qt4_demosdir} \
  -docdir %{_qt4_docdir} \
  -examplesdir %{_qt4_examplesdir} \
  -headerdir %{_qt4_headerdir} \
  -importdir %{_qt4_importdir} \
  -libdir %{_qt4_libdir} \
  -plugindir %{_qt4_plugindir} \
  -sysconfdir %{_qt4_sysconfdir} \
  -translationdir %{_qt4_translationdir} \
  -platform %{platform} \
  -release \
  -shared \
  -cups \
  -fontconfig \
  -largefile \
  -gtkstyle \
  -no-rpath \
  %{?reduce_relocations} \
  -no-separate-debug-info \
  %{?phonon} %{!?phonon:-no-phonon} \
  %{?phonon_backend} \
  %{?no_pch} \
  %{?no_javascript_jit} \
  -sm \
  -stl \
  -system-libmng \
  -system-libpng \
  -system-libjpeg \
  -system-libtiff \
  -system-zlib \
  -xinput \
  -xcursor \
  -xfixes \
  -xinerama \
  -xshape \
  -xrandr \
  -xrender \
  -xkb \
  -glib \
  -icu \
  %{?openssl} \
  -xmlpatterns \
  %{?dbus} %{!?dbus:-no-dbus} \
  %{?graphicssystem} \
  %{?webkit} %{!?webkit:-no-webkit } \
  %{?ibase} \
  %{?mysql} \
  %{?psql} \
  %{?odbc} \
  %{?sqlite} %{?_system_sqlite} \
  %{?tds} \
  %{!?docs:-nomake docs} \
  %{!?demos:-nomake demos} \
  %{!?examples:-nomake examples}

# verify QT_BUILD_KEY
grep '^#define QT_BUILD_KEY ' src/corelib/global/qconfig.h
QT_BUILD_KEY_COMPILER="$(grep '^#define QT_BUILD_KEY ' src/corelib/global/qconfig.h | cut -d' ' -f5)"
if [ "$QT_BUILD_KEY_COMPILER" != 'g++-4' ]; then
  echo "QT_BUILD_KEY_COMPILER failure"
  exit 1
fi

%if ! 0%{?inject_optflags}
# ensure qmake build using optflags (which can happen if not munging qmake.conf defaults)
make clean -C qmake
%make_build -C qmake \
  QMAKE_CFLAGS_RELEASE="${CFLAGS:-$RPM_OPT_FLAGS}" \
  QMAKE_CXXFLAGS_RELEASE="${CXXFLAGS:-$RPM_OPT_FLAGS}" \
  QMAKE_LFLAGS_RELEASE="${LDFLAGS:-$RPM_LD_FLAGS}" \
  QMAKE_STRIP=
%endif

%make_build

# TODO: consider patching tools/tools.pro to enable building this by default
%{?qvfb:%make_build -C tools/qvfb}

# recreate .qm files
bin/lrelease translations/*.ts


%install
make install INSTALL_ROOT=%{buildroot}

%if 0%{?qvfb}
make install INSTALL_ROOT=%{buildroot} -C tools/qvfb
%find_lang qvfb --with-qt --without-mo
%else
rm -f %{buildroot}%{_qt4_translationdir}/qvfb*.qm
%endif

%if 0%{?private}
# install private headers
# using rsync -R as easy way to preserve relative path names
# we're cheating and using %%_prefix (/usr) directly here
rsync -aR \
  include/Qt{Core,Declarative,Gui,Script}/private \
  src/{corelib,declarative,gui,script}/*/*_p.h \
  %{buildroot}%{_prefix}/
%endif

# Add desktop files, --vendor=qt4 helps avoid possible conflicts with qt3/qt5
desktop-file-install \
  --dir=%{buildroot}%{_datadir}/applications \
  --vendor="qt4" \
  %{SOURCE20} %{SOURCE21} %{SOURCE22} %{?dbus:%{SOURCE23}} %{?demos:%{SOURCE24}} %{SOURCE25}

## pkg-config
# strip extraneous dirs/libraries 
# safe ones
glib2_libs=$(pkg-config --libs glib-2.0 gobject-2.0 gthread-2.0)
if [ "%{?openssl}" == "-openssl-linked" ]; then
ssl_libs=$(pkg-config --libs openssl)
fi
for dep in \
  -laudio -ldbus-1 -lfreetype -lfontconfig ${glib2_libs} \
  -ljpeg -lm -lmng -lpng -lpulse -lpulse-mainloop-glib ${ssl_libs} -lsqlite3 -lz \
  -L/usr/X11R6/lib -L/usr/X11R6/%{_lib} -L%{_libdir} ; do
  sed -i -e "s|$dep ||g" %{buildroot}%{_qt4_libdir}/lib*.la 
#  sed -i -e "s|$dep ||g" %{buildroot}%{_qt4_libdir}/pkgconfig/*.pc
  sed -i -e "s|$dep ||g" %{buildroot}%{_qt4_libdir}/*.prl
done
# riskier
for dep in -ldl -lphonon -lpthread -lICE -lSM -lX11 -lXcursor -lXext -lXfixes -lXft -lXinerama -lXi -lXrandr -lXrender -lXt ; do
  sed -i -e "s|$dep ||g" %{buildroot}%{_qt4_libdir}/lib*.la 
#  sed -i -e "s|$dep ||g" %{buildroot}%{_qt4_libdir}/pkgconfig/*.pc 
  sed -i -e "s|$dep ||g" %{buildroot}%{_qt4_libdir}/*.prl
done

# nuke dangling reference(s) to %buildroot
sed -i -e "/^QMAKE_PRL_BUILD_DIR/d" %{buildroot}%{_qt4_libdir}/*.prl
sed -i -e "s|-L%{_builddir}/qt-everywhere-opensource-src-%{version}%{?beta:-%{beta}}/lib||g" \
  %{buildroot}%{_qt4_libdir}/pkgconfig/*.pc \
  %{buildroot}%{_qt4_libdir}/*.prl

# nuke QMAKE_PRL_LIBS, seems similar to static linking and .la files (#520323)
# don't nuke, just drop -lphonon (above)
#sed -i -e "s|^QMAKE_PRL_LIBS|#QMAKE_PRL_LIBS|" %{buildroot}%{_qt4_libdir}/*.prl

# .la files, die, die, die.
rm -f %{buildroot}%{_qt4_libdir}/lib*.la

%if 0
#if "%{_qt4_docdir}" != "%{_qt4_prefix}/doc"
# -doc make symbolic link to _qt4_docdir
rm -rf %{buildroot}%{_qt4_prefix}/doc
ln -s  ../../share/doc/qt4 %{buildroot}%{_qt4_prefix}/doc
%endif

# hardlink files to %{_bindir}, add -qt4 postfix to not conflict
mkdir %{buildroot}%{_bindir}
pushd %{buildroot}%{_qt4_bindir}
for i in * ; do
  case "${i}" in
    # qt3 stuff
    assistant|designer|linguist|lrelease|lupdate|moc|qmake|qtconfig|qtdemo|uic)
      ln -v  ${i} %{buildroot}%{_bindir}/${i}-qt4
      ln -sv ${i} ${i}-qt4
      ;;
    # qt5/qtchooser stuff
    qmlviewer)
      ln -v  ${i} %{buildroot}%{_bindir}/${i}
      ln -v  ${i} %{buildroot}%{_bindir}/${i}-qt4
      ln -sv ${i} ${i}-qt4
      ;;
    *)
      ln -v  ${i} %{buildroot}%{_bindir}/${i}
      ;;
  esac
done
popd

# _debug targets (see bug #196513)
pushd %{buildroot}%{_qt4_libdir}
for lib in libQt*.so ; do
   libbase=`basename $lib .so | sed -e 's/^lib//'`
#  ln -s $lib lib${libbase}_debug.so
   echo "INPUT(-l${libbase})" > lib${libbase}_debug.so 
done
for lib in libQt*.a ; do
   libbase=`basename $lib .a | sed -e 's/^lib//' `
#  ln -s $lib lib${libbase}_debug.a
   echo "INPUT(-l${libbase})" > lib${libbase}_debug.a
done
popd

%ifarch %{multilib_archs}
# multilib: qconfig.h
  mv %{buildroot}%{_qt4_headerdir}/Qt/qconfig.h %{buildroot}%{_qt4_headerdir}/QtCore/qconfig-%{__isa_bits}.h
  install -p -m644 -D %{SOURCE5} %{buildroot}%{_qt4_headerdir}/QtCore/qconfig-multilib.h
  ln -sf qconfig-multilib.h %{buildroot}%{_qt4_headerdir}/QtCore/qconfig.h
  ln -sf ../QtCore/qconfig.h %{buildroot}%{_qt4_headerdir}/Qt/qconfig.h
%endif

%if "%{_qt4_libdir}" != "%{_libdir}"
  mkdir -p %{buildroot}/etc/ld.so.conf.d
  echo "%{_qt4_libdir}" > %{buildroot}/etc/ld.so.conf.d/qt4-%{__isa_bits}.conf
%endif

# qtchooser conf
%if 0%{?qtchooser}
  mkdir -p %{buildroot}%{_sysconfdir}/xdg/qtchooser
  pushd    %{buildroot}%{_sysconfdir}/xdg/qtchooser
  echo "%{_qt4_bindir}" >  4-%{__isa_bits}.conf
  echo "%{_qt4_prefix}" >> 4-%{__isa_bits}.conf
  # alternatives targets
  touch default.conf 4.conf
  popd
%endif

%if ! 0%{?qt_settings}
# Trolltech.conf
install -p -m644 -D %{SOURCE4} %{buildroot}%{_qt4_sysconfdir}/Trolltech.conf
%endif

# qt4-logo (generic) icons
install -p -m644 -D %{SOURCE30} %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/qt4-logo.png
install -p -m644 -D %{SOURCE31} %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/qt4-logo.png

# assistant icons
install -p -m644 -D tools/assistant/tools/assistant/images/assistant.png %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/assistant.png
install -p -m644 -D tools/assistant/tools/assistant/images/assistant-128.png %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/assistant.png

# designer icons
install -p -m644 -D tools/designer/src/designer/images/designer.png %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/designer.png

# linguist icons
for icon in tools/linguist/linguist/images/icons/linguist-*-32.png ; do
  size=$(echo $(basename ${icon}) | cut -d- -f2)
  install -p -m644 -D ${icon} %{buildroot}%{_datadir}/icons/hicolor/${size}x${size}/apps/linguist.png
done

# qdbusviewer icons
install -p -m644 -D tools/qdbus/qdbusviewer/images/qdbusviewer.png %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/qdbusviewer.png
install -p -m644 -D tools/qdbus/qdbusviewer/images/qdbusviewer-128.png %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/qdbusviewer.png

# Qt.pc
cat >%{buildroot}%{_libdir}/pkgconfig/Qt.pc<<EOF
prefix=%{_qt4_prefix}
bindir=%{_qt4_bindir}
datadir=%{_qt4_datadir}
demosdir=%{_qt4_demosdir}
docdir=%{_qt4_docdir}
examplesdir=%{_qt4_examplesdir}
headerdir=%{_qt4_headerdir}
importdir=%{_qt4_importdir}
libdir=%{_qt4_libdir}
moc=%{_qt4_bindir}/moc
plugindir=%{_qt4_plugindir}
qmake=%{_qt4_bindir}/qmake
sysconfdir=%{_qt4_sysconfdir}
translationdir=%{_qt4_translationdir}

Name: Qt
Description: Qt Configuration
Version: %{version}
EOF

# rpm macros
install -p -m644 -D %{SOURCE1} \
  %{buildroot}%{rpm_macros_dir}/macros.qt4
sed -i \
  -e "s|@@NAME@@|%{name}|g" \
  -e "s|@@EPOCH@@|%{?epoch}%{!?epoch:0}|g" \
  -e "s|@@VERSION@@|%{version}|g" \
  -e "s|@@EVR@@|%{?epoch:%{epoch}:}%{version}-%{release}|g" \
  %{buildroot}%{rpm_macros_dir}/macros.qt4

# create/own stuff under %%_qt4_docdir
mkdir -p %{buildroot}%{_qt4_docdir}/{html,qch,src}

 # create/own stuff under %%_qt4_plugindir
mkdir -p %{buildroot}%{_qt4_plugindir}/{crypto,gui_platform,styles}

## nuke bundled phonon bits
rm -fv  %{buildroot}%{_qt4_libdir}/libphonon.so*
rm -rfv %{buildroot}%{_libdir}/pkgconfig/phonon.pc
# contents slightly different between phonon-4.3.1 and qt-4.5.0
rm -fv  %{buildroot}%{_includedir}/phonon/phononnamespace.h
# contents dup'd but should remove just in case
rm -fv  %{buildroot}%{_includedir}/phonon/*.h
rm -rfv %{buildroot}%{_qt4_headerdir}/phonon*
#rm -rfv %{buildroot}%{_qt4_headerdir}/Qt/phonon*
rm -fv %{buildroot}%{_datadir}/dbus-1/interfaces/org.kde.Phonon.AudioOutput.xml
rm -fv %{buildroot}%{_qt4_plugindir}/designer/libphononwidgets.so
# backend
rm -fv %{buildroot}%{_qt4_plugindir}/phonon_backend/*_gstreamer.so
rm -fv %{buildroot}%{_datadir}/kde4/services/phononbackends/gstreamer.desktop

# nuke bundled webkit bits 
rm -fv %{buildroot}%{_qt4_datadir}/mkspecs/modules/qt_webkit_version.pri
rm -fv %{buildroot}%{_qt4_headerdir}/Qt/qgraphicswebview.h
rm -fv %{buildroot}%{_qt4_headerdir}/Qt/qweb*.h
rm -fv %{buildroot}%{_qt4_headerdir}/Qt/QtWebKit
rm -frv %{buildroot}%{_qt4_headerdir}/QtWebKit/
rm -frv %{buildroot}%{_qt4_importdir}/QtWebKit/
rm -fv %{buildroot}%{_qt4_libdir}/libQtWebKit*
rm -fv %{buildroot}%{_libdir}/pkgconfig/QtWebKit.pc
rm -frv %{buildroot}%{_qt4_prefix}/tests/

%find_lang qt --with-qt --without-mo

%find_lang assistant --with-qt --without-mo
%find_lang qt_help --with-qt --without-mo
%find_lang qtconfig --with-qt --without-mo
%find_lang qtscript --with-qt --without-mo
cat assistant.lang qt_help.lang qtconfig.lang qtscript.lang >qt-x11.lang

%find_lang designer --with-qt --without-mo
%find_lang linguist --with-qt --without-mo
cat designer.lang linguist.lang >qt-devel.lang



%if 0%{?qtchooser}
%pre
if [ $1 -gt 1 ] ; then
# remove short-lived qt4.conf alternatives
%{_sbindir}/update-alternatives  \
  --remove qtchooser-qt4 \
  %{_sysconfdir}/xdg/qtchooser/qt4-%{__isa_bits}.conf >& /dev/null ||:

%{_sbindir}/update-alternatives  \
  --remove qtchooser-default \
  %{_sysconfdir}/xdg/qtchooser/qt4.conf >& /dev/null ||:
fi
%endif

%post
%{?ldconfig}
%if 0%{?qtchooser}
%{_sbindir}/update-alternatives \
  --install %{_sysconfdir}/xdg/qtchooser/4.conf \
  qtchooser-4 \
  %{_sysconfdir}/xdg/qtchooser/4-%{__isa_bits}.conf \
  %{priority}

%{_sbindir}/update-alternatives \
  --install %{_sysconfdir}/xdg/qtchooser/default.conf \
  qtchooser-default \
  %{_sysconfdir}/xdg/qtchooser/4.conf \
  %{priority}
%endif

%postun
%{?ldconfig}
%if 0%{?qtchooser}
if [ $1 -eq 0 ]; then
%{_sbindir}/update-alternatives  \
  --remove qtchooser-4 \
  %{_sysconfdir}/xdg/qtchooser/4-%{__isa_bits}.conf

%{_sbindir}/update-alternatives  \
  --remove qtchooser-default \
  %{_sysconfdir}/xdg/qtchooser/4.conf
fi
%endif

%files -f qt.lang
%doc README
%license LICENSE.GPL3 LICENSE.LGPL LGPL_EXCEPTION.txt
%if 0%{?qtchooser}
%dir %{_sysconfdir}/xdg/qtchooser
# not editable config files, so not using %%config here
%ghost %{_sysconfdir}/xdg/qtchooser/default.conf
%ghost %{_sysconfdir}/xdg/qtchooser/4.conf
%{_sysconfdir}/xdg/qtchooser/4-%{__isa_bits}.conf
%endif
%if "%{_qt4_libdir}" != "%{_libdir}"
/etc/ld.so.conf.d/*
%dir %{_qt4_libdir}
%endif
%dir %{_qt4_prefix}
%if "%{_qt4_bindir}" == "%{_bindir}"
%{_qt4_prefix}/bin
%else
%dir %{_qt4_bindir}
%endif
%if "%{_qt4_datadir}" != "%{_datadir}/qt4"
%dir %{_datadir}/qt4
%else
%dir %{_qt4_datadir}
%endif
%dir %{_qt4_docdir}
%dir %{_qt4_docdir}/html/
%dir %{_qt4_docdir}/qch/
%dir %{_qt4_docdir}/src/

%if "%{_qt4_sysconfdir}" != "%{_sysconfdir}"
%dir %{_qt4_sysconfdir}
%endif
%if ! 0%{?qt_settings}
%config(noreplace) %{_qt4_sysconfdir}/Trolltech.conf
%endif
%{_qt4_datadir}/phrasebooks/
%{_qt4_libdir}/libQtCore.so.4*
%if 0%{?dbus:1}
%if "%{_qt4_bindir}" != "%{_bindir}"
%{_bindir}/qdbus
%endif
%{_qt4_bindir}/qdbus
%{_qt4_libdir}/libQtDBus.so.4*
%endif
%{_qt4_libdir}/libQtNetwork.so.4*
%{_qt4_libdir}/libQtScript.so.4*
%{_qt4_libdir}/libQtSql.so.4*
%{_qt4_libdir}/libQtTest.so.4*
%{_qt4_libdir}/libQtXml.so.4*
%{_qt4_libdir}/libQtXmlPatterns.so.4*
%dir %{_qt4_plugindir}
%dir %{_qt4_plugindir}/crypto/
%dir %{_qt4_plugindir}/sqldrivers/
%dir %{_qt4_translationdir}/
%{_qt4_plugindir}/sqldrivers/libqsqlite*

%files common
# empty for now, consider: filesystem/dir ownership, licenses

%files assistant
%if "%{_qt4_bindir}" != "%{_bindir}"
%{_bindir}/assistant*
%endif
%{_qt4_bindir}/assistant*
%{_datadir}/applications/*assistant.desktop
%{_datadir}/icons/hicolor/*/apps/assistant*

%files config
%if "%{_qt4_bindir}" != "%{_bindir}"
%{_bindir}/qt*config*
%endif
%{_qt4_bindir}/qt*config*
%{_datadir}/applications/*qtconfig.desktop

%if 0%{?demos}
%files demos
%{_qt4_bindir}/qt*demo*
%if "%{_qt4_bindir}" != "%{_bindir}"
%{_bindir}/qt*demo*
%endif
%{_datadir}/applications/*qtdemo.desktop
%{_qt4_demosdir}/
%endif

%if "%{?webkit}" == "-webkit"
%files designer-plugin-webkit
%{_qt4_plugindir}/designer/libqwebview.so
%endif

%files devel -f qt-devel.lang
%{rpm_macros_dir}/macros.qt4
%{_qt4_bindir}/lconvert
%{_qt4_bindir}/lrelease*
%{_qt4_bindir}/lupdate*
%{_qt4_bindir}/moc*
%{_qt4_bindir}/pixeltool*
%{_qt4_bindir}/qdoc3*
%{_qt4_bindir}/qmake*
%{_qt4_bindir}/qmlviewer*
%{_qt4_bindir}/qmlplugindump
%{_qt4_bindir}/qt3to4
%{_qt4_bindir}/qttracereplay
%{_qt4_bindir}/rcc*
%{_qt4_bindir}/uic*
%{_qt4_bindir}/qcollectiongenerator
%if 0%{?dbus:1}
%{_qt4_bindir}/qdbuscpp2xml
%{_qt4_bindir}/qdbusxml2cpp
%endif
%{_qt4_bindir}/qhelpconverter
%{_qt4_bindir}/qhelpgenerator
%{_qt4_bindir}/xmlpatterns
%{_qt4_bindir}/xmlpatternsvalidator
%if "%{_qt4_bindir}" != "%{_bindir}"
%{_bindir}/lrelease*
%{_bindir}/lupdate*
%{_bindir}/moc*
%{_bindir}/uic*
%{_bindir}/designer*
%{_bindir}/linguist*
%{_bindir}/lconvert
%{_bindir}/pixeltool
%{_bindir}/qcollectiongenerator
%{_bindir}/qdoc3
%{_bindir}/qmake*
%{_bindir}/qmlviewer*
%{_bindir}/qt3to4
%{_bindir}/qttracereplay
%if 0%{?dbus:1}
%{_bindir}/qdbuscpp2xml
%{_bindir}/qdbusxml2cpp
%endif
%{_bindir}/qhelpconverter
%{_bindir}/qhelpgenerator
%{_bindir}/qmlplugindump
%{_bindir}/rcc
%{_bindir}/xmlpatterns
%{_bindir}/xmlpatternsvalidator
%endif
%if "%{_qt4_headerdir}" != "%{_includedir}"
%dir %{_qt4_headerdir}/
%endif
%{_qt4_headerdir}/*
%{_qt4_datadir}/mkspecs/
%if "%{_qt4_datadir}" != "%{_qt4_prefix}"
%{_qt4_prefix}/mkspecs/
%endif
%{_qt4_datadir}/q3porting.xml
%if 0%{?phonon:1}
## nuke this one too?  -- Rex
%{_qt4_libdir}/libphonon.prl
%endif
%{_qt4_libdir}/libQt*.so
%{_qt4_libdir}/libQtUiTools*.a
%{_qt4_libdir}/libQt*.prl
%{_libdir}/pkgconfig/*.pc
# Qt designer
%{_qt4_bindir}/designer*
%{_datadir}/applications/*designer.desktop
%{_datadir}/icons/hicolor/*/apps/designer*
%{?docs:%{_qt4_docdir}/qch/designer.qch}
# Qt Linguist
%{_qt4_bindir}/linguist*
%{_datadir}/applications/*linguist.desktop
%{_datadir}/icons/hicolor/*/apps/linguist*
%{?docs:%{_qt4_docdir}/qch/linguist.qch}
%if 0%{?private}
%exclude %{_qt4_headerdir}/*/private/

%files devel-private
%{_qt4_headerdir}/QtCore/private/
%{_qt4_headerdir}/QtDeclarative/private/
%{_qt4_headerdir}/QtGui/private/
%{_qt4_headerdir}/QtScript/private/
%{_qt4_headerdir}/../src/corelib/
%{_qt4_headerdir}/../src/declarative/
%{_qt4_headerdir}/../src/gui/
%{_qt4_headerdir}/../src/script/
%endif

%if 0%{?docs}
%files doc
%{_qt4_docdir}/html/*
%{_qt4_docdir}/qch/*.qch
%exclude %{_qt4_docdir}/qch/designer.qch
%exclude %{_qt4_docdir}/qch/linguist.qch
%{_qt4_docdir}/src/*
#{_qt4_prefix}/doc
%endif

%if 0%{?examples}
%files examples
%{_qt4_examplesdir}/
%endif

%if 0%{?qvfb}
%files qvfb -f qvfb.lang
%{_bindir}/qvfb
%{_qt4_bindir}/qvfb
%endif

%if "%{?ibase}" == "-plugin-sql-ibase"
%files ibase
%{_qt4_plugindir}/sqldrivers/libqsqlibase*
%endif

%if "%{?mysql}" == "-plugin-sql-mysql"
%files mysql
%{_qt4_plugindir}/sqldrivers/libqsqlmysql*
%endif

%if "%{?odbc}" == "-plugin-sql-odbc"
%files odbc 
%{_qt4_plugindir}/sqldrivers/libqsqlodbc*
%endif

%if "%{?psql}" == "-plugin-sql-psql"
%files postgresql 
%{_qt4_plugindir}/sqldrivers/libqsqlpsql*
%endif

%if "%{?tds}" == "-plugin-sql-tds"
%files tds
%{_qt4_plugindir}/sqldrivers/libqsqltds*
%endif

%ldconfig_scriptlets x11

%files x11 -f qt-x11.lang
%dir %{_qt4_importdir}/
%{_qt4_importdir}/Qt/
%{_qt4_libdir}/libQt3Support.so.4*
%{_qt4_libdir}/libQtCLucene.so.4*
%{_qt4_libdir}/libQtDesigner.so.4*
%{_qt4_libdir}/libQtDeclarative.so.4*
%{_qt4_libdir}/libQtDesignerComponents.so.4*
%{_qt4_libdir}/libQtGui.so.4*
%{_qt4_libdir}/libQtHelp.so.4*
%{_qt4_libdir}/libQtMultimedia.so.4*
%{_qt4_libdir}/libQtOpenGL.so.4*
%{_qt4_libdir}/libQtScriptTools.so.4*
%{_qt4_libdir}/libQtSvg.so.4*
%{_qt4_plugindir}/*
%exclude %{_qt4_plugindir}/crypto
%if "%{?webkit}" == "-webkit"
%exclude %{_qt4_plugindir}/designer/libqwebview.so
%endif
%exclude %{_qt4_plugindir}/sqldrivers
%{_datadir}/icons/hicolor/*/apps/qt4-logo.*

%if 0%{?dbus:1}
%post qdbusviewer
touch --no-create %{_datadir}/icons/hicolor ||:

%posttrans qdbusviewer
gtk-update-icon-cache -q %{_datadir}/icons/hicolor 2> /dev/null ||:

%postun qdbusviewer
if [ $1 -eq 0 ] ; then
touch --no-create %{_datadir}/icons/hicolor ||:
gtk-update-icon-cache -q %{_datadir}/icons/hicolor 2> /dev/null ||:
fi

%files qdbusviewer
%if "%{_qt4_bindir}" != "%{_bindir}"
%{_bindir}/qdbusviewer
%endif
%{_qt4_bindir}/qdbusviewer
%{_datadir}/applications/*qdbusviewer.desktop
%{_datadir}/icons/hicolor/*/apps/qdbusviewer.*
%endif


%changelog
* Mon May 18 2026 Oreon Packaging Team <packaging@oreonhq.com> - 4.8.7
%{version}-85
- Import from Fedora 44 dist-git, debrand
