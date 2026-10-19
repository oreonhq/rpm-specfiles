%global source0_hash 7b632550ea1048fc10c741e46e2e3b093e5ca94dfa6209e9e0848800e247023b
%global multilib_archs x86_64 %{ix86} %{?mips} ppc64 ppc s390x s390 sparc64 sparcv9
%global multilib_basearchs x86_64 %{?mips64} ppc64 s390x sparc64
%if 0%{?fedora} < 29 && 0%{?rhel} < 9 || (0%{?oreon} >= 11)
%ifarch %{ix86}
%global no_sse2  -no-sse2
%endif
%endif
%if 0%{?fedora} < 30  || 0%{?rhel} > 6 || (0%{?oreon} >= 11)
%global no_feature_statx -no-feature-statx
%global no_feature_renameat2 -no-feature-renameat2
%endif
%if 0%{?rhel} && 0%{?rhel} > 6 || (0%{?oreon} >= 11)
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
%if 0%{?fedora} || (0%{?oreon} >= 11)
%global qt_settings 1
%endif
%global examples 1
Name:    qt5-qtbase
Summary:        Qt5 - QtBase components
Version: 5.15.18
Release:        1%{?dist}
License: LGPL-3.0-only OR GPL-3.0-only WITH Qt-GPL-exception-1.0
Url:     http://qt-project.org/
%global  majmin %(echo %{version} | cut -d. -f1-2)
Source0:        https://download.qt.io/archive/qt/%{majmin}/%{version}/submodules/%{qt_module}-everywhere-opensource-src-%{version}.tar.xz
Source1:        qtlogging.ini
Source5:        qconfig-multilib.h
Source6:        10-qt5-check-opengl2.sh
Source10:        macros.qt5-qtbase
Patch2:        qtbase-multilib_optflags.patch
Patch3:        qtbase-everywhere-src-5.15.6-private_api_warning.patch
Patch50:        qtbase-opensource-src-5.8.0-QT_VERSION_CHECK.patch
Patch51:        qtbase-hidpi_scale_at_192.patch
Patch52:        qtbase-opensource-src-5.7.1-moc_macros.patch
Patch53:        qtbase-everywhere-src-5.12.1-qt5gui_cmake_isystem_includes.patch
Patch54:        qtbase-qmake_LFLAGS.patch
Patch55:        qtbase-everywhere-src-5.14.2-no_relocatable.patch
Patch56:        qtbase-everywhere-src-5.15.2-libglvnd.patch
Patch57:        qt5-qtbase-cxxflag.patch
Patch58:        qt5-qtbase-5.12.1-firebird.patch
Patch59:        qt5-qtbase-5.12.1-firebird-4.0.0.patch
Patch60:        qtbase-opensource-src-5.9.0-mysql.patch
Patch61:        qtbase-5.15.10-work-around-pyside2-brokenness.patch
Patch90: %{name}-gcc11.patch
Patch100: kde-5.15-rollup-20251104.patch.gz
Source100: kde-5.15-rollup-20251104.patch.gz
Patch101:        qtbase-5.15.10-fix-missing-qtsan-include.patch
Patch102:        qtbase-QTBUG-111994.patch
Patch103:        qtbase-QTBUG-112136.patch
Patch104:        0001-Update-SSL-trust-store-locations-for-modern-Red-Hat-.patch
Patch150:        0001-Use-Wayland-by-default-on-GNOME.patch
Patch151:        0002-Add-enum-class-Qt-Appearance.patch
Patch152:        0003-Sync-and-assert-StandardPixmap-enums-in-QPlatformThe.patch
Patch153:        0004-QGtk3Theme-subscribe-to-theme-hint-changes.patch
Patch155:        0006-Re-implement-palette-standardPixmap-file-icons-fonts.patch
Patch157:        0008-Fix-checkbox-and-radiobutton-background-in-QGtk3Them.patch
Patch158:        0009-Cleanup-QGtk3Theme.patch
Patch159:        0010-Detect-appearance-by-colors-unless-GTK-theme-name-co.patch
Patch160:        0011-Change-parsing-log-output-in-QGtk3Json-from-qCDebug-.patch
Patch161:        0012-Document-QGtk3Interface.patch
Patch162:        0013-Document-QGtk3Storage.patch
Patch163:        0014-QGtk3Theme-Improve-fixed-font-delivery.patch
Patch164:        0015-QGtk3Theme-Do-not-default-Active-WindowText-to-butto.patch
Patch165:        0016-Fix-memory-leak-in-QGtk3Interface-themename.patch
Patch166:        0017-Fix-disabled-button-color-in-Linux-x11-wayland.patch
Patch167:        0018-Fix-inactive-palette-in-gtk3-theme.patch
Patch168:        0019-Fix-tooltip-palette-issue-in-gtk3-theme.patch
Patch169:        0020-QGtk3Theme-define-light-midlight-mid-dark-shadow-colors.patch
Patch200:        qtbase-use-qgnomeplatform-as-default-platform-theme-on-gnome.patch
Patch201:        qtbase-everywhere-src-5.15-libproxy-0.5-pkgconfig.patch
%global __requires_exclude_from ^%{_qt5_plugindir}/platformthemes/.*$
%global __provides_exclude_from ^%{_qt5_plugindir}/.*\\.so$
%if 0%{?use_clang}
%else
%endif
%global vulkan 1
%if 0%{?fedora} || 0%{?rhel} > 6 || (0%{?oreon} >= 11)
%global egl 1
%global sqlite -system-sqlite
%if 0%{?fedora} > 22 || (0%{?oreon} >= 11)
%global harfbuzz -system-harfbuzz
%endif
%if 0%{?fedora} > 37 || 0%{?rhel} > 7 || (0%{?oreon} >= 11)
%else
%endif
%global pcre -system-pcre
%else
%global pcre -qt-pcre
%endif
%if 0%{?tests}
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
%if 0%{?rhel} || (0%{?oreon} >= 11)
%global ibase -no-sql-ibase
%global tds -no-sql-tds
%endif
%global use_gold_linker -no-use-gold-linker
# oreon:deps
BuildRequires:  cups-devel
BuildRequires:  dbus-x11
BuildRequires:  desktop-file-utils
BuildRequires:  double-conversion-devel
BuildRequires:  findutils
BuildRequires:  firebird-devel
BuildRequires:  freetds-devel
BuildRequires:  gcc-c++
BuildRequires:  libjpeg-devel
BuildRequires:  libmng-devel
BuildRequires:  libpq-devel
BuildRequires:  libtiff-devel
BuildRequires:  make
BuildRequires:  mariadb-connector-c-devel
BuildRequires:  mesa-dri-drivers
BuildRequires:  openssl-devel
BuildRequires:  perl-generators
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(atspi-2)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(harfbuzz)
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(icu-i18n)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libinput)
BuildRequires:  pkgconfig(libpcre2-16)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libproxy-1.0)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libpulse-mainloop-glib)
BuildRequires:  pkgconfig(libsctp)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(sm)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(vulkan)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-glx)
BuildRequires:  pkgconfig(xcb-icccm)
BuildRequires:  pkgconfig(xcb-image)
BuildRequires:  pkgconfig(xcb-keysyms)
BuildRequires:  pkgconfig(xcb-renderutil)
BuildRequires:  pkgconfig(xcb-util)
BuildRequires:  pkgconfig(xcb-xkb)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xkbcommon-x11)
BuildRequires:  pkgconfig(xkeyboard-config)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  python3
BuildRequires:  qt5-rpm-macros
BuildRequires:  time
BuildRequires:  unixODBC-devel
BuildRequires:  xorg-x11-server-Xvfb
# /oreon:deps
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
%if 0%{?oreon} >= 11
BuildRequires: mysql-devel
%elif 0%{?rhel} && 0%{?rhel} < 9
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
%if 0%{?fedora} || 0%{?rhel} >= 8 || (0%{?oreon} >= 11)
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

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
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
gzip -dc %{PATCH100} | patch -p1
%patch -P101 -p1
%patch -P102 -p1
%patch -P103 -p1
%patch -P104 -p1
%patch -P201 -p1

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
%if 0%{?fedora} < 29 && 0%{?rhel} < 9 || (0%{?oreon} >= 11)
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
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

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
%files -f %{oreon_filedir}/main.list
%files -n qt5-qtbase-common -f %{oreon_filedir}/qt5-qtbase-common.list
%files -n qt5-qtbase-devel -f %{oreon_filedir}/qt5-qtbase-devel.list
%files -n qt5-qtbase-private-devel -f %{oreon_filedir}/qt5-qtbase-private-devel.list
%files -n qt5-qtbase-examples -f %{oreon_filedir}/qt5-qtbase-examples.list
%files -n qt5-qtbase-static -f %{oreon_filedir}/qt5-qtbase-static.list
%files -n qt5-qtbase-ibase -f %{oreon_filedir}/qt5-qtbase-ibase.list
%files -n qt5-qtbase-mysql -f %{oreon_filedir}/qt5-qtbase-mysql.list
%files -n qt5-qtbase-odbc -f %{oreon_filedir}/qt5-qtbase-odbc.list
%files -n qt5-qtbase-postgresql -f %{oreon_filedir}/qt5-qtbase-postgresql.list
%files -n qt5-qtbase-tds -f %{oreon_filedir}/qt5-qtbase-tds.list
%files -n qt5-qtbase-gui -f %{oreon_filedir}/qt5-qtbase-gui.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.15.18-2
- Import
