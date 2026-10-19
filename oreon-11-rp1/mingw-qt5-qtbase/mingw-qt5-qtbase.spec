%global source0_hash 7b632550ea1048fc10c741e46e2e3b093e5ca94dfa6209e9e0848800e247023b
%{?mingw_package_header}
%undefine _debugsource_packages
%undefine _debuginfo_subpackages
%global __debug_install_post %%{mingw_debug_install_post}; %{_bindir}/find-debuginfo.sh %{?_missing_build_ids_terminate_build:--strict-build-id} %{?_find_debuginfo_opts} "%{_builddir}/%%{?buildsubdir}" %{nil}
%global qt_module qtbase
%if 0%{?commit:1}
%global source_folder %{qt_module}-%{commit}
%else
%global source_folder %{qt_module}-everywhere-src-%{version}%{?pre:-%{pre}}
%endif
%define release_version %(echo %{version} | awk -F. '{print $1"."$2}')
Name:           mingw-qt5-qtbase
Version:        5.15.18
Release:        1%{?dist}
Summary:        Qt5 for Windows - QtBase component
License:        LGPL-3.0-only OR GPL-3.0-only WITH Qt-GPL-exception-1.0
URL:            http://qt.io/
%if 0%{?commit:1}
Source0:        https://download.qt.io/archive/qt/%{release_version}/%{version}/submodules/%{qt_module}-everywhere-opensource-src-%{version}.tar.xz
%else
%endif
Patch1:          qt5-qtbase-mingw-profile.patch
Patch2:          qt5-qtbase-external-angle.patch
Patch3:         qt5-qtbase-qt5main.patch
Patch4:         qt5-qtbase-dynamic-hostlib.patch
Patch5:         qt5-qtbase-importlib-ext.patch
Patch6:         qt5-qtbase-cmake-macros.patch
Patch7:         qt5-qtbase-python3.patch
Patch8:         qt5-qtbase-pkgconfig.patch
Patch9:         qt5-qtbase-iconv.patch
Patch10:        qt5-qtbase-zlib-cross.patch
Patch11:        qt5-qtbase-static-linking.patch
Patch12:        qt5-qtbase-fix-installing-pc-files.patch
Patch13:        qt5-qtbase-prevent-debug-library-names-in-pkg-config-files.patch
Patch14:        qt5-qtbase-no-relocatable.patch
Patch15:        qt5-qtbase-spnego.patch
Patch16:        qt5-qtbase-bootstrap.patch
Patch17:        %{name}-gcc11.patch
Patch18:        qt5-qtbase-link-openssl.patch
Patch19:        qtbase-5.15.8-fix-missing-qtsan-include.patch
Patch20:        qtbase-fix-linking-against-static-harfbuzz.patch
Source100: kde-5.15-rollup-20251104.patch.gz
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  gzip
BuildRequires:  make
BuildRequires:  mingw32-angleproject
BuildRequires:  mingw32-angleproject-static
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-bzip2
BuildRequires:  mingw32-bzip2-static
BuildRequires:  mingw32-dbus
BuildRequires:  mingw32-dbus-static
BuildRequires:  mingw32-dlfcn
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-freetype
BuildRequires:  mingw32-freetype-static
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-harfbuzz
BuildRequires:  mingw32-harfbuzz-static
BuildRequires:  mingw32-libjpeg-turbo
BuildRequires:  mingw32-libjpeg-turbo-static
BuildRequires:  mingw32-libpng
BuildRequires:  mingw32-libpng-static
BuildRequires:  mingw32-openssl
BuildRequires:  mingw32-openssl-static
BuildRequires:  mingw32-pcre2
BuildRequires:  mingw32-pcre2-static
BuildRequires:  mingw32-pkg-config
BuildRequires:  mingw32-postgresql
BuildRequires:  mingw32-postgresql-static
BuildRequires:  mingw32-sqlite
BuildRequires:  mingw32-sqlite-static
BuildRequires:  mingw32-vulkan-headers
BuildRequires:  mingw32-win-iconv
BuildRequires:  mingw32-win-iconv-static
BuildRequires:  mingw32-winpthreads
BuildRequires:  mingw32-winpthreads-static
BuildRequires:  mingw32-zlib
BuildRequires:  mingw32-zlib-static
BuildRequires:  mingw32-zstd
BuildRequires:  mingw64-angleproject
BuildRequires:  mingw64-angleproject-static
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-bzip2
BuildRequires:  mingw64-bzip2-static
BuildRequires:  mingw64-dbus
BuildRequires:  mingw64-dbus-static
BuildRequires:  mingw64-dlfcn
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-freetype
BuildRequires:  mingw64-freetype-static
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-harfbuzz
BuildRequires:  mingw64-harfbuzz-static
BuildRequires:  mingw64-libjpeg-turbo
BuildRequires:  mingw64-libjpeg-turbo-static
BuildRequires:  mingw64-libpng
BuildRequires:  mingw64-libpng-static
BuildRequires:  mingw64-openssl
BuildRequires:  mingw64-openssl-static
BuildRequires:  mingw64-pcre2
BuildRequires:  mingw64-pcre2-static
BuildRequires:  mingw64-pkg-config
BuildRequires:  mingw64-postgresql
BuildRequires:  mingw64-postgresql-static
BuildRequires:  mingw64-sqlite
BuildRequires:  mingw64-sqlite-static
BuildRequires:  mingw64-vulkan-headers
BuildRequires:  mingw64-win-iconv
BuildRequires:  mingw64-win-iconv-static
BuildRequires:  mingw64-winpthreads
BuildRequires:  mingw64-winpthreads-static
BuildRequires:  mingw64-zlib
BuildRequires:  mingw64-zlib-static
BuildRequires:  mingw64-zstd
BuildRequires:  perl-interpreter
BuildRequires:  pkgconfig(zlib)
# /oreon:deps
%description
This package contains the Qt software toolkit for developing
cross-platform applications.

This is the Windows version of Qt, for use in conjunction with the
Fedora Windows cross-compiler.

# Win32
%package -n mingw32-qt5-qtbase
Summary:        Qt5 for Windows - QtBase component
Requires:       mingw32-qt5-qmake = %{version}-%{release}
Requires:       mingw32-vulkan-headers
BuildArch:      noarch
%description -n mingw32-qt5-qtbase
This package contains the Qt software toolkit for developing
cross-platform applications.

This is the Windows version of Qt, for use in conjunction with the
Fedora Windows cross-compiler.

%package -n mingw32-qt5-qmake
Summary:       Qt5 for Windows build environment
%description -n mingw32-qt5-qmake
This package contains the build environment for cross compiling
applications with the Fedora Windows Qt Library and cross-compiler.

%package -n mingw32-qt5-qtbase-devel
Summary:       Qt5 for Windows build environment
Requires:      mingw32-qt5-qtbase = %{version}-%{release}
%description -n mingw32-qt5-qtbase-devel
Contains the files required to get various Qt tools built
which are part of the mingw-qt5-qttools package

%package -n mingw32-qt5-qtbase-static
Summary:       Static version of the mingw32-qt5-qtbase library
Requires:      mingw32-qt5-qtbase = %{version}-%{release}
Requires:      mingw32-angleproject-static
Requires:      mingw32-libjpeg-turbo-static
Requires:      mingw32-libpng-static
Requires:      mingw32-harfbuzz-static
Requires:      mingw32-pcre2-static
Requires:      mingw32-win-iconv-static
Requires:      mingw32-winpthreads-static
Requires:      mingw32-zlib-static
BuildArch:     noarch
%description -n mingw32-qt5-qtbase-static
Static version of the mingw32-qt5 library.

# Win64
%package -n mingw64-qt5-qtbase
Summary:        Qt5 for Windows - QtBase component
Requires:       mingw64-qt5-qmake = %{version}-%{release}
Requires:       mingw64-vulkan-headers
BuildArch:      noarch
%description -n mingw64-qt5-qtbase
This package contains the Qt software toolkit for developing
cross-platform applications.

This is the Windows version of Qt, for use in conjunction with the
Fedora Windows cross-compiler.

%package -n mingw64-qt5-qmake
Summary:       Qt for Windows build environment
%description -n mingw64-qt5-qmake
This package contains the build environment for cross compiling
applications with the Fedora Windows Qt Library and cross-compiler.

%package -n mingw64-qt5-qtbase-devel
Summary:       Qt5 for Windows build environment
Requires:      mingw64-qt5-qtbase = %{version}-%{release}
%description -n mingw64-qt5-qtbase-devel
Contains the files required to get various Qt tools built
which are part of the mingw-qt5-qttools package

%package -n mingw64-qt5-qtbase-static
Summary:       Static version of the mingw64-qt5-qtbase library
Requires:      mingw64-qt5-qtbase = %{version}-%{release}
Requires:      mingw64-angleproject-static
Requires:      mingw64-libjpeg-turbo-static
Requires:      mingw64-libpng-static
Requires:      mingw64-harfbuzz-static
Requires:      mingw64-pcre2-static
Requires:      mingw64-win-iconv-static
Requires:      mingw64-winpthreads-static
Requires:      mingw64-zlib-static
BuildArch:     noarch
%description -n mingw64-qt5-qtbase-static
Static version of the mingw64-qt5-qtbase library.

%{?mingw_debug_package}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -N -n %{source_folder}
%autopatch -M 100 -p1

gunzip -c %SOURCE100 | patch -p1

# Remove bundled ANGLE
rm -rf src/3rdparty/angle include/QtANGLE/{EGL,GLES2,KHR}
# Remove bundled libraries
rm -rf src/3rdparty/{freetype,libjpeg,libpng,pcre2,sqlite,zlib}
# TODO harfbuzz,harfbuzz-ng

%build

unset PKG_CONFIG_PATH
qt_configure_args_generic="\
    -xplatform mingw-w64-g++ \
    -verbose \
    -opensource \
    -confirm-license \
    -release \
    -force-debug-info \
    -make tools \
    -nomake examples \
    -pkg-config \
    -sql-sqlite \
    -openssl-linked \
    -iconv \
    -opengl dynamic\
    -no-direct2d \
    -no-feature-relocatable \
    -system-freetype \
    -system-harfbuzz \
    -system-libjpeg \
    -system-libpng \
    -system-pcre \
    -system-sqlite \
    -system-zlib"
qt_configure_args_win32="\
    -hostprefix %{_prefix}/%{mingw32_target} \
    -hostbindir %{_prefix}/%{mingw32_target}/bin/qt5 \
    -hostlibdir %{_prefix}/%{mingw32_target}/lib \
    -hostdatadir %{mingw32_datadir}/qt5 \
    -prefix %{mingw32_prefix} \
    -bindir %{mingw32_bindir} \
    -archdatadir %{mingw32_libdir}/qt5 \
    -datadir %{mingw32_datadir}/qt5 \
    -docdir %{mingw32_docdir}/qt5 \
    -examplesdir %{mingw32_datadir}/qt5/examples \
    -headerdir %{mingw32_includedir}/qt5 \
    -libdir %{mingw32_libdir} \
    -plugindir %{mingw32_libdir}/qt5/plugins \
    -sysconfdir %{mingw32_sysconfdir} \
    -translationdir %{mingw32_datadir}/qt5/translations \
    -device-option CROSS_COMPILE=%{mingw32_target}-"
qt_configure_args_win64="\
    -hostprefix %{_prefix}/%{mingw64_target} \
    -hostbindir %{_prefix}/%{mingw64_target}/bin/qt5 \
    -hostlibdir %{_prefix}/%{mingw64_target}/lib \
    -hostdatadir %{mingw64_datadir}/qt5 \
    -prefix %{mingw64_prefix} \
    -bindir %{mingw64_bindir} \
    -archdatadir %{mingw64_libdir}/qt5 \
    -datadir %{mingw64_datadir}/qt5 \
    -docdir %{mingw64_docdir}/qt5 \
    -examplesdir %{mingw64_datadir}/qt5/examples \
    -headerdir %{mingw64_includedir}/qt5 \
    -libdir %{mingw64_libdir} \
    -plugindir %{mingw64_libdir}/qt5/plugins \
    -sysconfdir %{mingw64_sysconfdir} \
    -translationdir %{mingw64_datadir}/qt5/translations \
    -device-option CROSS_COMPILE=%{mingw64_target}-"
srcdir=`pwd`
rm -rf ../build_%{name}_static_win32
mkdir ../build_%{name}_static_win32
pushd ../build_%{name}_static_win32
$srcdir/configure -static $qt_configure_args_win32 $qt_configure_args_generic
LD_LIBRARY_PATH=$PWD/lib %make_build
popd
rm -rf ../build_%{name}_shared_win32
mkdir ../build_%{name}_shared_win32
pushd ../build_%{name}_shared_win32
$srcdir/configure -shared $qt_configure_args_win32 $qt_configure_args_generic
LD_LIBRARY_PATH=$PWD/lib %make_build
popd
rm -rf ../build_%{name}_static_win64
mkdir ../build_%{name}_static_win64
pushd ../build_%{name}_static_win64
$srcdir/configure -static $qt_configure_args_win64 $qt_configure_args_generic
LD_LIBRARY_PATH=$PWD/lib %make_build
popd
rm -rf ../build_%{name}_shared_win64
mkdir ../build_%{name}_shared_win64
pushd ../build_%{name}_shared_win64
$srcdir/configure -shared $qt_configure_args_win64 $qt_configure_args_generic
LD_LIBRARY_PATH=$PWD/lib %make_build
popd
%install
make install -C ../build_%{name}_static_win32 INSTALL_ROOT=%{buildroot}
make install -C ../build_%{name}_shared_win32 INSTALL_ROOT=%{buildroot}
make install -C ../build_%{name}_static_win64 INSTALL_ROOT=%{buildroot}
make install -C ../build_%{name}_shared_win64 INSTALL_ROOT=%{buildroot}
find %{buildroot} -name '*.la' -delete
rm -f %{buildroot}%{_prefix}/%{mingw32_target}/lib/libQt5Bootstrap.a
rm -f %{buildroot}%{_prefix}/%{mingw32_target}/lib/libQt5BootstrapDBus.a
rm -f %{buildroot}%{_prefix}/%{mingw64_target}/lib/libQt5Bootstrap.a
rm -f %{buildroot}%{_prefix}/%{mingw64_target}/lib/libQt5BootstrapDBus.a
mkdir -p %{buildroot}%{_sysconfdir}/xdg/qtchooser
echo "%{_prefix}/%{mingw32_target}/bin/qt5" >  %{buildroot}%{_sysconfdir}/xdg/qtchooser/mingw32-qt5.conf
echo "%{mingw32_prefix}" >> %{buildroot}%{_sysconfdir}/xdg/qtchooser/mingw32-qt5.conf
echo "%{_prefix}/%{mingw64_target}/bin/qt5" >  %{buildroot}%{_sysconfdir}/xdg/qtchooser/mingw64-qt5.conf
echo "%{mingw64_prefix}" >> %{buildroot}%{_sysconfdir}/xdg/qtchooser/mingw64-qt5.conf
mkdir -p %{buildroot}%{mingw32_libdir}/qt5/mkspecs/features
mkdir -p %{buildroot}%{mingw64_libdir}/qt5/mkspecs/features
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_prefix}/%{mingw32_target}/bin
mkdir -p %{buildroot}%{_prefix}/%{mingw64_target}/bin
for tool in qmake moc rcc uic qdbuscpp2xml qdbusxml2cpp syncqt.pl; do
    ln -s ../%{mingw32_target}/bin/qt5/$tool %{buildroot}%{_bindir}/%{mingw32_target}-$tool-qt5
    ln -s ../%{mingw64_target}/bin/qt5/$tool %{buildroot}%{_bindir}/%{mingw64_target}-$tool-qt5
done
ln -s %{mingw32_target}-qmake-qt5 %{buildroot}%{_bindir}/mingw32-qmake-qt5
ln -s %{mingw64_target}-qmake-qt5 %{buildroot}%{_bindir}/mingw64-qmake-qt5
%oreon_autofiles mingw32-qt5-qtbase usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw32-qt5-qmake usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw32-qt5-qtbase-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles mingw32-qt5-qtbase-static usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-qt5-qtbase usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-qt5-qmake usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-qt5-qtbase-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles mingw64-qt5-qtbase-static usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-qt5-qtbase -f %{oreon_filedir}/mingw32-qt5-qtbase.list
%files -n mingw32-qt5-qmake -f %{oreon_filedir}/mingw32-qt5-qmake.list
%files -n mingw32-qt5-qtbase-devel -f %{oreon_filedir}/mingw32-qt5-qtbase-devel.list
%files -n mingw32-qt5-qtbase-static -f %{oreon_filedir}/mingw32-qt5-qtbase-static.list
%files -n mingw64-qt5-qtbase -f %{oreon_filedir}/mingw64-qt5-qtbase.list
%files -n mingw64-qt5-qmake -f %{oreon_filedir}/mingw64-qt5-qmake.list
%files -n mingw64-qt5-qtbase-devel -f %{oreon_filedir}/mingw64-qt5-qtbase-devel.list
%files -n mingw64-qt5-qtbase-static -f %{oreon_filedir}/mingw64-qt5-qtbase-static.list

%changelog

%autochangelog
