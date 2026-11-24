# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 7b632550ea1048fc10c741e46e2e3b093e5ca94dfa6209e9e0848800e247023b
%global source1_hash 7493edc0df47c1bb9040331694922d4500b897b30515d698ec482c866ee5d9d3
%global source10_hash a2a2f8f341f17493bcba3cef1c5c6c32072648f981bc0aefde68055aab74a31b
%global source100_hash 5f6fb23a6c2f87ebc570dc2aa1d64d100c36b4abe0279ffa16805289532de34b
%global source5_hash 2d01cdbfd11a887a1729f1ce2c4e0ad0c080509cc009279090bd68521845be93
%global source6_hash 5f44f1723eb599d4b82d22dc022725764b13c387aec66de51d6c06bee8cf50de
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%global multilib_archs x86_64 %{ix86} %{?mips} ppc64 ppc s390x s390 sparc64 sparcv9
%global multilib_basearchs x86_64 %{?mips64} ppc64 s390x sparc64

%if 0%{?fedora} < 29 && 0%{?rhel} < 9
%ifarch %{ix86}
%global no_sse2  -no-sse2
%endif
%endif

%if 0%{?fedora} < 30  || 0%{?rhel} > 6
%global no_feature_statx -no-feature-statx
%global no_feature_renameat2 -no-feature-renameat2
%endif
%if 0%{?rhel} && 0%{?rhel} > 6
%global no_feature_getentropy -no-feature-getentropy
%endif

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

%global __brp_remove_la_files %nil

%global platform linux-g++

%if 0%{?use_clang}
%global platform linux-clang
%endif

%global qt_module qtbase

%global rpm_macros_dir %(d=%{_rpmconfigdir}/macros.d; [ -d $d ] || d=%{_sysconfdir}/rpm; echo $d)

%if 0%{?fedora}
%global qt_settings 1
%endif

%global examples 1

Name:    qt5-qtbase
Summary: Qt5 - QtBase components
Version: 5.15.18
Release: 1%{?dist}

License: LGPL-3.0-only OR GPL-3.0-only WITH Qt-GPL-exception-1.0
Url:     http://qt-project.org/
%global  majmin 5.15
Source0: https://download.qt.io/official_releases/qt/%{majmin}/%{version}/submodules/%{qt_module}-everywhere-opensource-src-%{version}.tar.xz

Source1: qtlogging.ini

Source5: qconfig-multilib.h

Source6: 10-qt5-check-opengl2.sh

Source10: macros.qt5-qtbase

Patch2: qtbase-multilib_optflags.patch

Patch3: qtbase-everywhere-src-5.15.6-private_api_warning.patch

Patch50: qtbase-opensource-src-5.8.0-QT_VERSION_CHECK.patch

Patch51: qtbase-hidpi_scale_at_192.patch

Patch52: qtbase-opensource-src-5.7.1-moc_macros.patch

Patch53: qtbase-everywhere-src-5.12.1-qt5gui_cmake_isystem_includes.patch

Patch54: qtbase-qmake_LFLAGS.patch

Patch55: qtbase-everywhere-src-5.14.2-no_relocatable.patch

Patch56: qtbase-everywhere-src-5.15.2-libglvnd.patch

Patch57: qt5-qtbase-cxxflag.patch

Patch58: qt5-qtbase-5.12.1-firebird.patch

Patch59: qt5-qtbase-5.12.1-firebird-4.0.0.patch

Patch60: qtbase-opensource-src-5.9.0-mysql.patch

Patch61: qtbase-5.15.10-work-around-pyside2-brokenness.patch

Patch90: %{name}-gcc11.patch

Patch100: kde-5.15-rollup-20251104.patch.gz
Source100: kde-5.15-rollup-20251104.patch.gz

Patch101: qtbase-5.15.10-fix-missing-qtsan-include.patch
Patch102: qtbase-QTBUG-111994.patch
Patch103: qtbase-QTBUG-112136.patch

Patch104: 0001-Update-SSL-trust-store-locations-for-modern-Red-Hat-.patch

Patch105: qtbase-openssl4-opaque-structs.patch

Patch150: 0001-Use-Wayland-by-default-on-GNOME.patch

Patch151: 0002-Add-enum-class-Qt-Appearance.patch
Patch152: 0003-Sync-and-assert-StandardPixmap-enums-in-QPlatformThe.patch
Patch153: 0004-QGtk3Theme-subscribe-to-theme-hint-changes.patch
Patch155: 0006-Re-implement-palette-standardPixmap-file-icons-fonts.patch
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

Patch180: qt5-qtbase-CVE-2026-19248.patch

Patch200: qtbase-use-qgnomeplatform-as-default-platform-theme-on-gnome.patch

%global __requires_exclude_from ^%{_qt5_plugindir}/platformthemes/.*$
%global __provides_exclude_from ^%{_qt5_plugindir}/.*\\.so$

%if 0%{?use_clang}
BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc-c++
BuildRequires: clang >= 3.7.0
%else
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
BuildRequires: pkgconfig(atspi-2)
BuildRequires: pkgconfig(dbus-1)
BuildRequires: pkgconfig(libdrm)
BuildRequires: pkgconfig(fontconfig)
BuildRequires: pkgconfig(gl)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(libproxy-1.0)
BuildRequires: pkgconfig(libsctp)
BuildRequires: pkgconfig(ice)
BuildRequires: pkgconfig(sm)
BuildRequires: pkgconfig(libpng)
BuildRequires: pkgconfig(libudev)
BuildRequires: openssl-devel
BuildRequires: pkgconfig(libpulse)
BuildRequires: pkgconfig(libpulse-mainloop-glib)
BuildRequires: pkgconfig(libinput)
BuildRequires: pkgconfig(libsystemd)
BuildRequires: pkgconfig(xcb-xkb) >= 1.10
BuildRequires: pkgconfig(xcb-util)
BuildRequires: pkgconfig(xkbcommon) >= 0.4.1
BuildRequires: pkgconfig(xkbcommon-x11) >= 0.4.1
BuildRequires: pkgconfig(xkeyboard-config)
%global vulkan 1
BuildRequires: pkgconfig(vulkan)
%if 0%{?fedora} || 0%{?rhel} > 6 || 0%{?oreon}
%global egl 1
BuildRequires: pkgconfig(egl)
BuildRequires: pkgconfig(gbm)
BuildRequires: pkgconfig(glesv2)
%global sqlite -system-sqlite
BuildRequires: pkgconfig(sqlite3) >= 3.7
%if 0%{?fedora} > 22 || 0%{?oreon}
%global harfbuzz -system-harfbuzz
BuildRequires: pkgconfig(harfbuzz) >= 0.9.42
%endif
BuildRequires: pkgconfig(icu-i18n)
%if 0%{?fedora} > 37 || 0%{?rhel} > 7 || 0%{?oreon}
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
BuildRequires: pkgconfig(xcb)
BuildRequires: pkgconfig(xcb-glx)
BuildRequires: pkgconfig(xcb-icccm)
BuildRequires: pkgconfig(xcb-image)
BuildRequires: pkgconfig(xcb-keysyms)
BuildRequires: pkgconfig(xcb-renderutil)
BuildRequires: pkgconfig(zlib)
BuildRequires: pkgconfig(libzstd)
BuildRequires: perl-generators
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
%if 0%{?fedora}
Conflicts: qt < 1:4.8.6-10
%endif
Requires(post): %{_sbindir}/update-alternatives
Requires(postun): %{_sbindir}/update-alternatives
%endif
%if 0%{?qt_settings}
Requires: qt-settings
%endif
Requires: %{name}-common = %{version}-%{release}

%if 0%{?rhel} || 0%{?oreon}
%global ibase -no-sql-ibase
%global tds -no-sql-tds
%endif

%global use_gold_linker -no-use-gold-linker

%description
Qt is a software toolkit for developing applications.

This package contains base tools, like string, xml, and network
handling.

%package common
Summary: Common files for Qt5
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
Obsoletes: %{name}-devel < 5.12.1-3
Requires: %{name}-devel%{?_isa} = %{version}-%{release}
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
%if 0%{?rhel} && 0%{?rhel} < 9
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

%package gui
Summary: Qt5 GUI-related libraries
Requires: %{name}%{?_isa} = %{version}-%{release}
%if 0%{?fedora} || 0%{?rhel} >= 8
Recommends: mesa-dri-drivers%{?_isa}
Recommends: qt5-qtwayland%{?_isa}
Recommends: qt5-qttranslations
%endif
Obsoletes: qt5-qtbase-x11 < 5.2.0
Provides:  qt5-qtbase-x11 = %{version}-%{release}
Obsoletes: adwaita-qt5 <= 1.4.2
Obsoletes: libadwaita-qt5 <= 1.4.2
Obsoletes: qgnomeplatform-qt5 <= 0.9.2
Provides:  qgnomeplatform-qt5 = %{version}-%{release}
Requires: glx-utils
%description gui
Qt5 libraries used for drawing widgets and OpenGL items.

%prep
%oreon_sha256
echo '%{source1_hash}  %{SOURCE1}' | sha256sum -c -
echo '%{source10_hash}  %{SOURCE10}' | sha256sum -c -
echo '%{source100_hash}  %{SOURCE100}' | sha256sum -c -
echo '%{source5_hash}  %{SOURCE5}' | sha256sum -c -
echo '%{source6_hash}  %{SOURCE6}' | sha256sum -c -
%setup -q -n %{qt_module}-everywhere-src-%{version}

%patch -P3 -p1 -b .private_api_warning

%patch -P50 -p1 -b .QT_VERSION_CHECK
%patch -P52 -p1 -b .moc_macros
%patch -P53 -p1 -b .qt5gui_cmake_isystem_includes
%patch -P54 -p1 -b .qmake_LFLAGS
%patch -P55 -p1 -b .no_relocatable
%patch -P56 -p1 -b .libglvnd
%patch -P57 -p1 -b .qt5-qtbase-cxxflag
%if 0%{?fedora} < 35
%patch -P58 -p1 -b .firebird
%else
%patch -P59 -p1 -b .firebird
%endif
%if 0%{?fedora} > 27
%patch -P60 -p1 -b .mysql
%endif
%patch -P61 -p1

%patch -P90 -p1 -b .gcc11

%patch -P100 -p1
%patch -P101 -p1
%patch -P102 -p1
%patch -P103 -p1
%patch -P104 -p1
%if 0%{?fedora} >= 45 || 0%{?rhel} >= 11
%patch -P105 -p1
%endif

%if 0%{?fedora} > 30 || 0%{?rhel} > 8
%patch -P150 -p1 -b .use-wayland-on-gnome.patch
%endif
%if 0%{?fedora} > 38 || 0%{?rhel} > 9
%patch -P151 -p1
%patch -P152 -p1
%patch -P153 -p1
%patch -P155 -p1
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

%patch -P180 -p1

%if 0%{?fedora} < 39
%patch -P200 -p1
%endif

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

test -x configure || chmod +x configure

sed -i -e "s|^#!/usr/bin/env perl$|#!%{__perl}|" \
 bin/fixqt4headers.pl \
 bin/syncqt.pl \
 mkspecs/features/data/unix/findclasslist.pl

%build
%define _lto_cflags %{nil}

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

install -p -m644 -D %{SOURCE10} \
  %{buildroot}%{rpm_macros_dir}/macros.qt5-qtbase
sed -i \
  -e "s|@@NAME@@|%{name}|g" \
  -e "s|@@EPOCH@@|%{?epoch}%{!?epoch:0}|g" \
  -e "s|@@VERSION@@|%{version}|g" \
  -e "s|@@EVR@@|%{?epoch:%{epoch:}}%{version}-%{release}|g" \
  %{buildroot}%{rpm_macros_dir}/macros.qt5-qtbase

mkdir -p %{buildroot}%{_qt5_plugindir}/{designer,iconengines,script,styles}
mkdir -p %{buildroot}%{_sysconfdir}/xdg/QtProject

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
  mv %{buildroot}%{_qt5_headerdir}/QtCore/qconfig.h %{buildroot}%{_qt5_headerdir}/QtCore/qconfig-%{__isa_bits}.h
  install -p -m644 -D %{SOURCE5} %{buildroot}%{_qt5_headerdir}/QtCore/qconfig.h
%endif

%if 0%{?qtchooser}
  mkdir -p %{buildroot}%{_sysconfdir}/xdg/qtchooser
  pushd    %{buildroot}%{_sysconfdir}/xdg/qtchooser
  echo "%{_qt5_bindir}" >  5-%{__isa_bits}.conf
  echo "%{_qt5_prefix}" >> 5-%{__isa_bits}.conf
  touch default.conf 5.conf
  popd
%endif

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

%if 0%{?fedora} < 29 && 0%{?rhel} < 9
privat_header_file=%{buildroot}%{_qt5_headerdir}/QtCore/%{version}/QtCore/private/qconfig_p.h
grep -v QT_FEATURE_sse2 $privat_header_file > ${privat_header_file}.me
mv ${privat_header_file}.me ${privat_header_file}
cat >>${privat_header_file}<<EOF
EOF
%endif

mkdir -p %{buildroot}%{_qt5_headerdir}/QtXcb
install -m 644 src/plugins/platforms/xcb/*.h %{buildroot}%{_qt5_headerdir}/QtXcb/

rm -f %{buildroot}%{_qt5_libdir}/libQt5Bootstrap.*a
rm -f %{buildroot}%{_qt5_libdir}/libQt5Bootstrap.prl

%check
export PKG_CONFIG_PATH=%{buildroot}%{_libdir}/pkgconfig
test "$(pkg-config --modversion Qt5)" = "%{version}"
%if 0%{?tests}
export CTEST_OUTPUT_ON_FAILURE=1
export PATH=%{buildroot}%{_qt5_bindir}:$PATH
export LD_LIBRARY_PATH=%{buildroot}%{_qt5_libdir}
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
%{_qt5_archdatadir}/mkspecs/modules/qt_lib_*_private.pri
%exclude %{_qt5_headerdir}/*/%{version}/

%files private-devel
%{_qt5_headerdir}/*/%{version}/

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
%autochangelog
