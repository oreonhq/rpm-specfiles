%global source0_hash a951bd163c7b80fc6b8c88d7668fb56abf91c152373e13c10666763238131307
%global multilib_archs x86_64 %{ix86} %{?mips} ppc64 ppc s390x s390 sparc64 sparcv9
%global multilib_basearchs x86_64 %{?mips64} ppc64 s390x sparc64
%ifarch s390x ppc64le aarch64 armv7hl riscv64
%global no_sse2  1
%endif
%if 0%{?rhel} && 0%{?rhel} < 9 || (0%{?oreon} >= 11)
%ifarch %{ix86}
%global no_sse2  1
%endif
%endif
%if 0%{?rhel} >= 10 || (0%{?oreon} >= 11)
%global wlheadless_compositor mutter
%else
%global wlheadless_compositor weston
%endif
%global platform linux-g++
%if 0%{?use_clang}
%global platform linux-clang
%endif
%global qt_module qtbase
%if 0%{?fedora} || (0%{?oreon} >= 11)
%global qt_settings 1
%endif
%global journald 1
%global examples 1
%if 0%{?unstable}
%global prerelease rc
%endif
Name:    qt6-qtbase
Summary:        Qt6 - QtBase components
Version: 6.12.0
Release:        1%{?dist}
License: LGPL-3.0-only OR GPL-3.0-only WITH Qt-GPL-exception-1.0
Url:     http://qt-project.org/
%global  majmin %(echo %{version} | cut -d. -f1-2)
%global  qt_version %(echo %{version} | cut -d~ -f1)
%if 0%{?unstable}
%else
Source0:        https://download.qt.io/official_releases/qt/%{majmin}/%{version}/submodules/%{qt_module}-everywhere-s%{prerelease}-%{version}.tar.xz
%endif
Source1:        qtlogging.ini
Source5:        qconfig-multilib.h
Source6:        10-qt6-check-opengl2.sh
Source10:        macros.qt6-qtbase
Patch1:        qtbase-CMake-Install-objects-files-into-ARCHDATADIR.patch
Patch2:        qtbase-use-only-major-minor-for-private-api-tag.patch
Patch50:        qtbase-version-check.patch
Patch51:        qtbase-moc-macros.patch
Patch54:        qtbase-cxxflag.patch
Patch56:        qtbase-mysql.patch
Patch58:        qtbase-libglvnd.patch
%global __requires_exclude_from ^%{_qt6_plugindir}/platformthemes/.*$
%global __provides_exclude_from ^%{_qt6_plugindir}/.*\\.so$
%if 0%{?use_clang}
%else
%endif
%if 0%{?fedora} || 0%{?epel} || (0%{?oreon} >= 11)
%else
Provides:      bundled(double-conversion)
%endif
%if 0%{?fedora} || 0%{?epel} || (0%{?oreon} >= 11)
%else
Provides:      bundled(libb2)
%endif
Provides:      bundled(emoji-segmenter)
%if 0%{?fedora} || 0%{?epel} || (0%{?oreon} >= 11)
%endif
%global dbus_linked 1
%global vulkan 1
%global egl 1
%global sqlite 1
%global pcre 1
%if 0%{?tests}
%endif
Requires:      qt6-filesystem
Requires: %{name}-common = %{version}-%{release}
%if 0%{?fedora} || 0%{?epel} || (0%{?oreon} >= 11)
%global ibase 1
%endif
# oreon:deps
BuildRequires:  (wlheadless-run and weston)
BuildRequires:  cmake
BuildRequires:  cups-devel
BuildRequires:  dbus-x11
BuildRequires:  desktop-file-utils
BuildRequires:  double-conversion-devel
BuildRequires:  findutils
BuildRequires:  firebird-devel
BuildRequires:  gcc-c++
BuildRequires:  libb2-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libmng-devel
BuildRequires:  libpq-devel
BuildRequires:  libtiff-devel
BuildRequires:  libzstd-devel
BuildRequires:  mariadb-connector-c-devel
BuildRequires:  mesa-dri-drivers
BuildRequires:  mtdev-devel
BuildRequires:  ninja-build
BuildRequires:  openssl-devel
BuildRequires:  perl
BuildRequires:  perl-generators
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(atspi-2)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(harfbuzz)
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(icu-i18n)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libglvnd)
BuildRequires:  pkgconfig(libinput)
BuildRequires:  pkgconfig(libpcre2-16)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libproxy-1.0)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libpulse-mainloop-glib)
BuildRequires:  pkgconfig(libsctp)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(sm)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(vulkan)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-cursor)
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
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  python3
BuildRequires:  qt6-rpm-macros
BuildRequires:  time
BuildRequires:  tslib-devel
BuildRequires:  unixODBC-devel
# /oreon:deps
%description
Qt is a software toolkit for developing applications.

This package contains base tools, like string, xml, and network
handling.

%package common
Summary: Common files for Qt6
Requires: %{name} = %{version}-%{release}
Obsoletes: qgnomeplatform-common <= 0.9.3
Provides:  qgnomeplatform-common = %{version}-%{release}
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
Requires: pkgconfig(xkbcommon)
Requires: pkgconfig(wayland-server)
Requires: pkgconfig(wayland-client)
Requires: pkgconfig(wayland-cursor)
Requires: pkgconfig(wayland-egl)
Requires: qt6-rpm-macros
%if 0%{?use_clang}
Requires: clang >= 3.7.0
%endif
%if 0%{?ibase}
Requires: %{name}-ibase%{?_isa} = %{version}-%{release}
%endif
Requires: %{name}-mysql%{?_isa} = %{version}-%{release}
Requires: %{name}-odbc%{?_isa} = %{version}-%{release}
Requires: %{name}-postgresql%{?_isa} = %{version}-%{release}
%description devel
%{summary}.

%package private-devel
Summary: Development files for %{name} private APIs
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

%if 0%{?ibase}
%package ibase
Summary: IBase driver for Qt6's SQL classes
BuildRequires: firebird-devel
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: libfbclient2%{?_isa}
%description ibase
%{summary}.
%endif

%package mysql
Summary: MySQL driver for Qt6's SQL classes
%if 0%{?fedora} > 27 || 0%{?rhel} > 8 || (0%{?oreon} >= 11)
BuildRequires: mariadb-connector-c-devel
%else
BuildRequires: mysql-devel
%endif
Requires: %{name}%{?_isa} = %{version}-%{release}
%description mysql
%{summary}.

%package odbc
Summary: ODBC driver for Qt6's SQL classes
BuildRequires: unixODBC-devel
Requires: %{name}%{?_isa} = %{version}-%{release}
%description odbc
%{summary}.

%package postgresql
Summary: PostgreSQL driver for Qt6's SQL classes
BuildRequires: libpq-devel
Requires: %{name}%{?_isa} = %{version}-%{release}
%description postgresql
%{summary}.

# debating whether to do 1 subpkg per library or not -- rex
%package gui
Summary: Qt6 GUI-related libraries
Requires: %{name}%{?_isa} = %{version}-%{release}
Recommends: mesa-dri-drivers%{?_isa}
Recommends: qt6-qttranslations
Obsoletes: adwaita-qt6 <= 1.4.2
Obsoletes: libadwaita-qt6 <= 1.4.2
Obsoletes: qgnomeplatform-qt6 <= 0.9.3
Provides:  qgnomeplatform-qt6 = %{version}-%{release}
Requires: glx-utils
%description gui
Qt6 libraries used for drawing widgets and OpenGL items.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | cut -d' ' -f1); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{qt_module}-everywhere-src-%{qt_version}%{?unstable:-%{prerelease}} -p1

# move some bundled libs to ensure they're not accidentally used
pushd src/3rdparty
mkdir UNUSED
mv harfbuzz-ng freetype libjpeg libpng sqlite zlib UNUSED/
popd

# builds failing mysteriously on f20
# ./configure: Permission denied
# check to ensure that can't happen -- rex
test -x configure || chmod +x configure

%build

%define _lto_cflags %{nil}
RPM_OPT_FLAGS=`echo $RPM_OPT_FLAGS | sed 's|-fexceptions||g'`
RPM_OPT_FLAGS="$RPM_OPT_FLAGS %{?qt6_arm_flag} %{?qt6_deprecated_flag} %{?qt6_null_flag}"
%if 0%{?use_clang}
RPM_OPT_FLAGS=`echo $RPM_OPT_FLAGS | sed 's|-fno-delete-null-pointer-checks||g'`
%endif
export CFLAGS="$CFLAGS $RPM_OPT_FLAGS"
export CXXFLAGS="$CXXFLAGS $RPM_OPT_FLAGS"
export LDFLAGS="$LDFLAGS $RPM_LD_FLAGS"
export MAKEFLAGS="%{?_smp_mflags}"
%cmake_qt6 -DCMAKE_POLICY_VERSION_MINIMUM=3.5 \
 -DFEATURE_accessibility=ON \
 -DFEATURE_fontconfig=ON \
 -DFEATURE_glib=ON \
 -DFEATURE_sse2=%{?no_sse2:OFF}%{!?no_sse2:ON} \
 -DFEATURE_icu=ON \
 -DFEATURE_enable_new_dtags=ON \
 -DFEATURE_emojisegmenter=ON \
 -DFEATURE_journald=%{?journald:ON}%{!?journald:OFF} \
 -DFEATURE_openssl_linked=ON \
 -DFEATURE_openssl_hash=ON \
 -DFEATURE_libproxy=ON \
 -DFEATURE_sctp=ON \
 -DFEATURE_separate_debug_info=OFF \
 -DFEATURE_reduce_relocations=OFF \
 -DFEATURE_relocatable=OFF \
 -DFEATURE_system_jpeg=ON \
 -DFEATURE_system_png=ON \
 -DFEATURE_system_zlib=ON \
 %{?ibase:-DFEATURE_sql_ibase=ON} \
 -DFEATURE_sql_odbc=ON \
 -DFEATURE_sql_mysql=ON \
 -DFEATURE_sql_psql=ON \
 -DFEATURE_sql_sqlite=ON \
 -DFEATURE_rpath=OFF \
 -DFEATURE_zstd=ON \
 -DFEATURE_elf_private_full_version=ON \
 %{?dbus_linked:-DFEATURE_dbus_linked=ON} \
 %{?pcre:-DFEATURE_system_pcre2=ON} \
 %{?sqlite:-DFEATURE_system_sqlite=ON} \
 -DBUILD_SHARED_LIBS=ON \
 -DQT_BUILD_EXAMPLES=%{?examples:ON}%{!?examples:OFF} \
 -DQT_INSTALL_EXAMPLES_SOURCES=%{?examples:ON}%{!?examples:OFF} \
 -DQT_BUILD_TESTS=%{?tests:ON}%{!?tests:OFF} \
 -DQT_QMAKE_TARGET_MKSPEC=%{platform}
%cmake_build
%install
%cmake_install
install -m644 -p -D %{SOURCE1} %{buildroot}%{_qt6_datadir}/qtlogging.ini
mkdir -p %{buildroot}%{_libdir}/pkgconfig
cat << EOF > %{buildroot}%{_libdir}/pkgconfig/Qt6.pc
prefix=%{_qt6_prefix}
archdatadir=%{_qt6_archdatadir}
bindir=%{_qt6_bindir}
datadir=%{_qt6_datadir}
docdir=%{_qt6_docdir}
examplesdir=%{_qt6_examplesdir}
headerdir=%{_qt6_headerdir}
importdir=%{_qt6_importdir}
libdir=%{_qt6_libdir}
libexecdir=%{_qt6_libexecdir}
moc=%{_qt6_libexecdir}/moc
plugindir=%{_qt6_plugindir}
qmake=%{_qt6_bindir}/qmake
settingsdir=%{_qt6_settingsdir}
sysconfdir=%{_qt6_sysconfdir}
translationdir=%{_qt6_translationdir}
Name: Qt6
Description: Qt6 Configuration
Version: 6.11.2
EOF
install -p -m644 -D %{SOURCE10} \
  %{buildroot}%{_rpmmacrodir}/macros.qt6-qtbase
sed -i \
  -e "s|@@NAME@@|%{name}|g" \
  -e "s|@@EPOCH@@|%{?epoch}%{!?epoch:0}|g" \
  -e "s|@@VERSION@@|%{version}|g" \
  -e "s|@@EVR@@|%{?epoch:%{epoch:}}%{version}-%{release}|g" \
  %{buildroot}%{_rpmmacrodir}/macros.qt6-qtbase
mkdir -p %{buildroot}%{_qt6_plugindir}/{designer,iconengines,script,styles}
mkdir -p %{buildroot}%{_sysconfdir}/xdg/QtProject
mkdir %{buildroot}%{_bindir}
pushd %{buildroot}%{_qt6_bindir}
for i in * ; do
  case "${i}" in
    qdbuscpp2xml|qdbusxml2cpp|qtpaths)
      ln -v  ${i} %{buildroot}%{_bindir}/${i}-qt6
      ;;
    *)
      ln -v  ${i} %{buildroot}%{_bindir}/${i}
      ;;
  esac
done
popd
%ifarch %{multilib_archs}
  mv %{buildroot}%{_qt6_headerdir}/QtCore/qconfig.h %{buildroot}%{_qt6_headerdir}/QtCore/qconfig-%{__isa_bits}.h
  install -p -m644 -D %{SOURCE5} %{buildroot}%{_qt6_headerdir}/QtCore/qconfig.h
%endif
pushd %{buildroot}%{_qt6_libdir}
for prl_file in libQt6*.prl ; do
  sed -i -e "/^QMAKE_PRL_BUILD_DIR/d" ${prl_file}
  if [ -f "$(basename ${prl_file} .prl).so" ]; then
    rm -fv "$(basename ${prl_file} .prl).la"
    sed -i -e "/^QMAKE_PRL_LIBS/d" ${prl_file}
  fi
done
popd
install -p -m755 -D %{SOURCE6} %{buildroot}%{_sysconfdir}/X11/xinit/xinitrc.d/10-qt6-check-opengl2.sh
mkdir -p %{buildroot}%{_qt6_headerdir}/QtXcb
install -m 644 src/plugins/platforms/xcb/*.h %{buildroot}%{_qt6_headerdir}/QtXcb/
rm %{buildroot}%{_qt6_libexecdir}/qt-android-runner.py
rm -r %{buildroot}%{_qt6_libdir}/cmake/Qt6/3rdparty/extra-cmake-modules/*.patch
rm -r %{buildroot}%{_qt6_mkspecsdir}/features/uikit
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export PKG_CONFIG_PATH=%{buildroot}%{_libdir}/pkgconfig
test "$(pkg-config --modversion Qt6)" = "%{qt_version}"
%if 0%{?tests}
export CTEST_OUTPUT_ON_FAILURE=1
export PATH=%{buildroot}%{_qt6_bindir}:$PATH
export LD_LIBRARY_PATH=%{buildroot}%{_qt6_libdir}
dbus-launch --exit-with-session \
%make_build sub-tests  -k ||:
wlheadless-run -c %{wlheadless_compositor} -- \
dbus-launch --exit-with-session \
time \
make check -k ||:
%endif
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n qt6-qtbase-common -f %{oreon_filedir}/qt6-qtbase-common.list
%files -n qt6-qtbase-devel -f %{oreon_filedir}/qt6-qtbase-devel.list
%files -n qt6-qtbase-private-devel -f %{oreon_filedir}/qt6-qtbase-private-devel.list
%files -n qt6-qtbase-examples -f %{oreon_filedir}/qt6-qtbase-examples.list
%files -n qt6-qtbase-static -f %{oreon_filedir}/qt6-qtbase-static.list
%files -n qt6-qtbase-ibase -f %{oreon_filedir}/qt6-qtbase-ibase.list
%files -n qt6-qtbase-mysql -f %{oreon_filedir}/qt6-qtbase-mysql.list
%files -n qt6-qtbase-odbc -f %{oreon_filedir}/qt6-qtbase-odbc.list
%files -n qt6-qtbase-postgresql -f %{oreon_filedir}/qt6-qtbase-postgresql.list
%files -n qt6-qtbase-gui -f %{oreon_filedir}/qt6-qtbase-gui.list

%changelog

%autochangelog
