%global source0_hash 5f6fb23a6c2f87ebc570dc2aa1d64d100c36b4abe0279ffa16805289532de34b

%{?mingw_package_header}

# Disable debuginfo subpackages and debugsource packages for now to use old logic
%undefine _debugsource_packages
%undefine _debuginfo_subpackages

# Override the __debug_install_post argument as this package
# contains both native as well as cross compiled binaries
%global __debug_install_post %%{mingw_debug_install_post}; %{_bindir}/find-debuginfo.sh %{?_missing_build_ids_terminate_build:--strict-build-id} %{?_find_debuginfo_opts} "%{_builddir}/%%{?buildsubdir}" %{nil}

%global qt_module qtbase
#global pre rc

#global commit d725239c3e09c2b740a093265f6a9675fd2f8524
#global shortcommit %(c=%{commit}; echo ${c:0:7})

%if 0%{?commit:1}
%global source_folder %{qt_module}-%{commit}
%else
%global source_folder %{qt_module}-everywhere-src-%{version}%{?pre:-%{pre}}
%endif

# first two digits of version
%define release_version %(echo %{version} | awk -F. '{print $1"."$2}')

Name:           mingw-qt5-qtbase
Version:        5.15.18
Release:        2%{?dist}
Summary:        Qt5 for Windows - QtBase component

# See LGPL_EXCEPTIONS.txt, for exception details
License:        LGPL-3.0-only OR GPL-3.0-only WITH Qt-GPL-exception-1.0
URL:            http://qt.io/

%if 0%{?commit:1}
Source0:        https://github.com/qt/%{qt_module}/archive/%{commit}/%{qt_module}-everywhere-src-%{commit}.tar.gz
%else
Source0:        https://download.qt.io/archive/qt/%{release_version}/%{version}%{?pre:-%pre}/submodules/%{qt_module}-everywhere-opensource-src-%{version}%{?pre:-%pre}.tar.xz
%endif

# Add profile for for mingw to match our environment
Patch1:          qt5-qtbase-mingw-profile.patch

# Unbundle angle
Patch2:          qt5-qtbase-external-angle.patch

# Avoid conflicts between the static qtmain library and the one provided by mingw-qt4.
# The mkspecs profile is already updated by Adjust-win32-g-mkspecs-profile.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=1092465
Patch3:         qt5-qtbase-qt5main.patch

# Upstream always wants the host libraries to be static instead of shared.
# This violates the packaging guidelines so disable this 'feature'.
Patch4:         qt5-qtbase-dynamic-hostlib.patch

# Fix qmake to create implibs with .dll.a extension for MinGW
Patch5:         qt5-qtbase-importlib-ext.patch

# https://github.com/Martchus/PKGBUILDs/issues/11
Patch6:         qt5-qtbase-cmake-macros.patch

# Use versioned python shebang
Patch7:         qt5-qtbase-python3.patch

# The --static flags should be used to detect static libraries with pkg-config.
# Ignore failing tests
Patch8:         qt5-qtbase-pkgconfig.patch

# Fix iconv test condition
Patch9:         qt5-qtbase-iconv.patch

# Don't use bundled zlib when cross-compiling
Patch10:        qt5-qtbase-zlib-cross.patch

# Fix linking against the static version of Qt
Patch11:        qt5-qtbase-static-linking.patch

# Fix installing pkg-config files (fixes silent errors resulting in empty pkg-config files)
Patch12:        qt5-qtbase-fix-installing-pc-files.patch

# Prevent debug library names in pkg-config files
Patch13:        qt5-qtbase-prevent-debug-library-names-in-pkg-config-files.patch

# Don't use relocatable heuristics to guess prefix when using -no-feature-relocatable (#1823118)
Patch14:        qt5-qtbase-no-relocatable.patch

# Restart spnego authentication if handles are null, even if challenge is not
# Fixes crash when authenticating twice to the same target
Patch15:        qt5-qtbase-spnego.patch

# Fix undefined references when building Qt5Bootstrap
Patch16:        qt5-qtbase-bootstrap.patch

# Fix issues building with gcc-11
Patch17:        %{name}-gcc11.patch

# Fix build with openssl-linked
Patch18:        qt5-qtbase-link-openssl.patch

# Fix missing qtsan_impl include
Patch19:        qtbase-5.15.8-fix-missing-qtsan-include.patch

# Fix linking against static harfbuzz
Patch20:        qtbase-fix-linking-against-static-harfbuzz.patch

# https://invent.kde.org/qt/qt/qtbase, kde/5.15 branch
# git diff v5.15.15-lts-lgpl..HEAD | gzip > kde-5.15-rollup-$(date +%Y%m%d).patch.gz
# patch100 in lookaside cache due to large'ish size -- rdieter
Source100: kde-5.15-rollup-20251104.patch.gz

BuildRequires:  gcc-c++
BuildRequires:  gzip
BuildRequires:  make
BuildRequires:  perl-interpreter
# For Qt5Bootstrap
BuildRequires:  pkgconfig(zlib)

BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-pkg-config
BuildRequires:  mingw32-dlfcn
BuildRequires:  mingw32-vulkan-headers
BuildRequires:  mingw32-angleproject >= 0-0.16.git8613f49
BuildRequires:  mingw32-angleproject-static >= 0-0.16.git8613f49
BuildRequires:  mingw32-bzip2
BuildRequires:  mingw32-bzip2-static
BuildRequires:  mingw32-dbus
BuildRequires:  mingw32-dbus-static
BuildRequires:  mingw32-freetype
BuildRequires:  mingw32-freetype-static
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
BuildRequires:  mingw32-postgresql
BuildRequires:  mingw32-postgresql-static
BuildRequires:  mingw32-sqlite
BuildRequires:  mingw32-sqlite-static
BuildRequires:  mingw32-win-iconv
BuildRequires:  mingw32-win-iconv-static
BuildRequires:  mingw32-winpthreads
BuildRequires:  mingw32-winpthreads-static
BuildRequires:  mingw32-zlib
BuildRequires:  mingw32-zlib-static
BuildRequires:  mingw32-zstd

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-pkg-config
BuildRequires:  mingw64-dlfcn
BuildRequires:  mingw64-vulkan-headers
BuildRequires:  mingw64-angleproject >= 0-0.16.git8613f49
BuildRequires:  mingw64-angleproject-static >= 0-0.16.git8613f49
BuildRequires:  mingw64-bzip2
BuildRequires:  mingw64-bzip2-static
BuildRequires:  mingw64-dbus
BuildRequires:  mingw64-dbus-static
BuildRequires:  mingw64-freetype
BuildRequires:  mingw64-freetype-static
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
BuildRequires:  mingw64-postgresql
BuildRequires:  mingw64-postgresql-static
BuildRequires:  mingw64-sqlite
BuildRequires:  mingw64-sqlite-static
BuildRequires:  mingw64-win-iconv
BuildRequires:  mingw64-win-iconv-static
BuildRequires:  mingw64-winpthreads
BuildRequires:  mingw64-winpthreads-static
BuildRequires:  mingw64-zlib
BuildRequires:  mingw64-zlib-static
BuildRequires:  mingw64-zstd

%description
This package contains the Qt software toolkit for developing
cross-platform applications.

This is the Windows version of Qt, for use in conjunction with the
Fedora Windows cross-compiler.

# Win32
%package -n mingw32-qt5-qtbase
Summary:        Qt5 for Windows - QtBase component
# This package contains the cross-compiler setup for qmake
Requires:       mingw32-qt5-qmake = %{version}-%{release}
# Public headers require vulkan/vulkan.h
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
# This package contains the cross-compiler setup for qmake
Requires:       mingw64-qt5-qmake = %{version}-%{release}
# Public headers require vulkan/vulkan.h
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
# RPM automatically sets the environment variable PKG_CONFIG_PATH to point to
# the native pkg-config files, which we don't want when cross-compiling.
unset PKG_CONFIG_PATH

# Generic configure arguments
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

# The odd paths for the -hostbindir argument are on purpose.
# The qtchooser tool assumes that the tools 'qmake', 'moc' and others are all
# available in the same folder with these exact file names.
# Put these in a dedicated folder to prevent conflicts with the mingw-qt (Qt4).
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

###############################################################################
srcdir=`pwd`

# NOTE: Adding setting LD_LIBRARY_PATH as host tools are executed during the
# build which are linked against the built libQt5Bootstrap.so.

# Win32
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

###############################################################################
# Win64
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

# Drop unneeded files
find %{buildroot} -name '*.la' -delete

rm -f %{buildroot}%{_prefix}/%{mingw32_target}/lib/libQt5Bootstrap.a
rm -f %{buildroot}%{_prefix}/%{mingw32_target}/lib/libQt5BootstrapDBus.a
rm -f %{buildroot}%{_prefix}/%{mingw64_target}/lib/libQt5Bootstrap.a
rm -f %{buildroot}%{_prefix}/%{mingw64_target}/lib/libQt5BootstrapDBus.a

# Add qtchooser support
mkdir -p %{buildroot}%{_sysconfdir}/xdg/qtchooser
echo "%{_prefix}/%{mingw32_target}/bin/qt5" >  %{buildroot}%{_sysconfdir}/xdg/qtchooser/mingw32-qt5.conf
echo "%{mingw32_prefix}" >> %{buildroot}%{_sysconfdir}/xdg/qtchooser/mingw32-qt5.conf
echo "%{_prefix}/%{mingw64_target}/bin/qt5" >  %{buildroot}%{_sysconfdir}/xdg/qtchooser/mingw64-qt5.conf
echo "%{mingw64_prefix}" >> %{buildroot}%{_sysconfdir}/xdg/qtchooser/mingw64-qt5.conf

# Create lib/qt5/mkspecs/features, used by other packages
mkdir -p %{buildroot}%{mingw32_libdir}/qt5/mkspecs/features
mkdir -p %{buildroot}%{mingw64_libdir}/qt5/mkspecs/features

# Manually install qmake and other native tools so we don't depend anymore on
# the version of the native Fedora Qt and also fix issues as illustrated at
# http://stackoverflow.com/questions/6592931/building-for-windows-under-linux-using-qt-creator
#
# Also make sure the tools can be found by CMake
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_prefix}/%{mingw32_target}/bin
mkdir -p %{buildroot}%{_prefix}/%{mingw64_target}/bin

for tool in qmake moc rcc uic qdbuscpp2xml qdbusxml2cpp syncqt.pl; do
    ln -s ../%{mingw32_target}/bin/qt5/$tool %{buildroot}%{_bindir}/%{mingw32_target}-$tool-qt5
    ln -s ../%{mingw64_target}/bin/qt5/$tool %{buildroot}%{_bindir}/%{mingw64_target}-$tool-qt5
done

ln -s %{mingw32_target}-qmake-qt5 %{buildroot}%{_bindir}/mingw32-qmake-qt5
ln -s %{mingw64_target}-qmake-qt5 %{buildroot}%{_bindir}/mingw64-qmake-qt5

# Win32
%files -n mingw32-qt5-qtbase
%license LICENSE.LGPL*
%{mingw32_bindir}/Qt5Concurrent.dll
%{mingw32_bindir}/Qt5Core.dll
%{mingw32_bindir}/Qt5DBus.dll
%{mingw32_bindir}/Qt5Gui.dll
%{mingw32_bindir}/Qt5Network.dll
%{mingw32_bindir}/Qt5OpenGL.dll
%{mingw32_bindir}/Qt5PrintSupport.dll
%{mingw32_bindir}/Qt5Sql.dll
%{mingw32_bindir}/Qt5Test.dll
%{mingw32_bindir}/Qt5Widgets.dll
%{mingw32_bindir}/Qt5Xml.dll
%{mingw32_libdir}/libQt5Concurrent.dll.a
%{mingw32_libdir}/libQt5Core.dll.a
%{mingw32_libdir}/libQt5DBus.dll.a
%{mingw32_libdir}/libQt5Gui.dll.a
%{mingw32_libdir}/libQt5Network.dll.a
%{mingw32_libdir}/libQt5OpenGL.dll.a
%{mingw32_libdir}/libQt5PrintSupport.dll.a
%{mingw32_libdir}/libQt5Sql.dll.a
%{mingw32_libdir}/libQt5Test.dll.a
%{mingw32_libdir}/libQt5Widgets.dll.a
%{mingw32_libdir}/libQt5Xml.dll.a
%{mingw32_libdir}/libqt5main.a
%{mingw32_libdir}/pkgconfig/Qt5Concurrent.pc
%{mingw32_libdir}/pkgconfig/Qt5Core.pc
%{mingw32_libdir}/pkgconfig/Qt5DBus.pc
%{mingw32_libdir}/pkgconfig/Qt5Gui.pc
%{mingw32_libdir}/pkgconfig/Qt5Network.pc
%{mingw32_libdir}/pkgconfig/Qt5OpenGL.pc
%{mingw32_libdir}/pkgconfig/Qt5OpenGLExtensions.pc
%{mingw32_libdir}/pkgconfig/Qt5PrintSupport.pc
%{mingw32_libdir}/pkgconfig/Qt5Sql.pc
%{mingw32_libdir}/pkgconfig/Qt5Test.pc
%{mingw32_libdir}/pkgconfig/Qt5Widgets.pc
%{mingw32_libdir}/pkgconfig/Qt5Xml.pc
%dir %{mingw32_libdir}/qt5/
%dir %{mingw32_libdir}/qt5/mkspecs
%dir %{mingw32_libdir}/qt5/mkspecs/features
%dir %{mingw32_libdir}/qt5/plugins
%dir %{mingw32_libdir}/qt5/plugins/bearer
%{mingw32_libdir}/qt5/plugins/bearer/qgenericbearer.dll
%dir %{mingw32_libdir}/qt5/plugins/generic
%{mingw32_libdir}/qt5/plugins/generic/qtuiotouchplugin.dll
%dir %{mingw32_libdir}/qt5/plugins/imageformats
%{mingw32_libdir}/qt5/plugins/imageformats/qgif.dll
%{mingw32_libdir}/qt5/plugins/imageformats/qico.dll
%{mingw32_libdir}/qt5/plugins/imageformats/qjpeg.dll
%dir %{mingw32_libdir}/qt5/plugins/platforms
%{mingw32_libdir}/qt5/plugins/platforms/qoffscreen.dll
%{mingw32_libdir}/qt5/plugins/platforms/qminimal.dll
%{mingw32_libdir}/qt5/plugins/platforms/qwindows.dll
%dir %{mingw32_libdir}/qt5/plugins/platformthemes/
%{mingw32_libdir}/qt5/plugins/platformthemes/qxdgdesktopportal.dll
%dir %{mingw32_libdir}/qt5/plugins/printsupport
%{mingw32_libdir}/qt5/plugins/printsupport/windowsprintersupport.dll
%dir %{mingw32_libdir}/qt5/plugins/sqldrivers
%{mingw32_libdir}/qt5/plugins/sqldrivers/qsqlite.dll
%{mingw32_libdir}/qt5/plugins/sqldrivers/qsqlodbc.dll
%{mingw32_libdir}/qt5/plugins/sqldrivers/qsqlpsql.dll
%dir %{mingw32_libdir}/qt5/plugins/styles
%{mingw32_libdir}/qt5/plugins/styles/qwindowsvistastyle.dll
%{mingw32_libdir}/cmake/Qt5/
%{mingw32_libdir}/cmake/Qt5AccessibilitySupport/
%{mingw32_libdir}/cmake/Qt5BootstrapDBus/
%{mingw32_libdir}/cmake/Qt5Core/
%{mingw32_libdir}/cmake/Qt5Concurrent/
%{mingw32_libdir}/cmake/Qt5DBus/
%{mingw32_libdir}/cmake/Qt5DeviceDiscoverySupport/
%{mingw32_libdir}/cmake/Qt5EdidSupport/
%{mingw32_libdir}/cmake/Qt5EventDispatcherSupport/
%{mingw32_libdir}/cmake/Qt5FbSupport/
%{mingw32_libdir}/cmake/Qt5FontDatabaseSupport/
%{mingw32_libdir}/cmake/Qt5Gui/
%{mingw32_libdir}/cmake/Qt5Network/
%{mingw32_libdir}/cmake/Qt5OpenGL/
%{mingw32_libdir}/cmake/Qt5OpenGLExtensions/
%{mingw32_libdir}/cmake/Qt5PlatformCompositorSupport/
%{mingw32_libdir}/cmake/Qt5PrintSupport/
%{mingw32_libdir}/cmake/Qt5Sql/
%{mingw32_libdir}/cmake/Qt5Test/
%{mingw32_libdir}/cmake/Qt5ThemeSupport/
%{mingw32_libdir}/cmake/Qt5VulkanSupport/
%{mingw32_libdir}/cmake/Qt5Widgets/
%{mingw32_libdir}/cmake/Qt5WindowsUIAutomationSupport/
%{mingw32_libdir}/cmake/Qt5Xml/
%dir %{mingw32_libdir}/metatypes
%{mingw32_libdir}/metatypes/qt5core_metatypes.json
%{mingw32_libdir}/metatypes/qt5gui_metatypes.json
%{mingw32_libdir}/metatypes/qt5widgets_metatypes.json
%dir %{mingw32_includedir}/qt5/
%{mingw32_includedir}/qt5/*
%{mingw32_docdir}/qt5/

%files -n mingw32-qt5-qmake
%{_bindir}/%{mingw32_target}-moc-qt5
%{_bindir}/%{mingw32_target}-qdbuscpp2xml-qt5
%{_bindir}/%{mingw32_target}-qdbusxml2cpp-qt5
%{_bindir}/%{mingw32_target}-qmake-qt5
%{_bindir}/%{mingw32_target}-rcc-qt5
%{_bindir}/%{mingw32_target}-syncqt.pl-qt5
%{_bindir}/%{mingw32_target}-uic-qt5
%{_bindir}/mingw32-qmake-qt5
%dir %{_prefix}/%{mingw32_target}/bin/qt5/
%{_prefix}/%{mingw32_target}/bin/qt5/fixqt4headers.pl
%{_prefix}/%{mingw32_target}/bin/qt5/moc
%{_prefix}/%{mingw32_target}/bin/qt5/qdbuscpp2xml
%{_prefix}/%{mingw32_target}/bin/qt5/qdbusxml2cpp
%{_prefix}/%{mingw32_target}/bin/qt5/qlalr
%{_prefix}/%{mingw32_target}/bin/qt5/qmake
%{_prefix}/%{mingw32_target}/bin/qt5/qvkgen
%{_prefix}/%{mingw32_target}/bin/qt5/rcc
%{_prefix}/%{mingw32_target}/bin/qt5/syncqt.pl
%{_prefix}/%{mingw32_target}/bin/qt5/tracegen
%{_prefix}/%{mingw32_target}/bin/qt5/uic
%{_prefix}/%{mingw32_target}/lib/libQt5Bootstrap.so.5*
%{_prefix}/%{mingw32_target}/lib/libQt5BootstrapDBus.so.5*
%{mingw32_datadir}/qt5/

# qtchooser
%dir %{_sysconfdir}/xdg/qtchooser/
# not editable config files, so not using %%config here
%{_sysconfdir}/xdg/qtchooser/mingw32-qt5.conf

%files -n mingw32-qt5-qtbase-devel
%{_prefix}/%{mingw32_target}/lib/libQt5Bootstrap.so
%{_prefix}/%{mingw32_target}/lib/libQt5Bootstrap.prl
%{_prefix}/%{mingw32_target}/lib/libQt5BootstrapDBus.so
%{_prefix}/%{mingw32_target}/lib/libQt5BootstrapDBus.prl

%files -n mingw32-qt5-qtbase-static
%{mingw32_libdir}/*.a
%{mingw32_libdir}/*.prl
%exclude %{mingw32_libdir}/*.dll.a
%dir %{mingw32_libdir}/qt5/plugins
%dir %{mingw32_libdir}/qt5/plugins/bearer
%{mingw32_libdir}/qt5/plugins/bearer/libqgenericbearer.a
%{mingw32_libdir}/qt5/plugins/bearer/qgenericbearer.prl
%dir %{mingw32_libdir}/qt5/plugins/generic
%{mingw32_libdir}/qt5/plugins/generic/libqtuiotouchplugin.a
%{mingw32_libdir}/qt5/plugins/generic/qtuiotouchplugin.prl
%dir %{mingw32_libdir}/qt5/plugins/imageformats
%{mingw32_libdir}/qt5/plugins/imageformats/libqgif.a
%{mingw32_libdir}/qt5/plugins/imageformats/qgif.prl
%{mingw32_libdir}/qt5/plugins/imageformats/libqico.a
%{mingw32_libdir}/qt5/plugins/imageformats/qico.prl
%{mingw32_libdir}/qt5/plugins/imageformats/libqjpeg.a
%{mingw32_libdir}/qt5/plugins/imageformats/qjpeg.prl
%dir %{mingw32_libdir}/qt5/plugins/platforms
%{mingw32_libdir}/qt5/plugins/platforms/libqoffscreen.a
%{mingw32_libdir}/qt5/plugins/platforms/qoffscreen.prl
%{mingw32_libdir}/qt5/plugins/platforms/libqminimal.a
%{mingw32_libdir}/qt5/plugins/platforms/qminimal.prl
%{mingw32_libdir}/qt5/plugins/platforms/libqwindows.a
%{mingw32_libdir}/qt5/plugins/platforms/qwindows.prl
%dir %{mingw32_libdir}/qt5/plugins/platformthemes/
%{mingw32_libdir}/qt5/plugins/platformthemes/libqxdgdesktopportal.a
%{mingw32_libdir}/qt5/plugins/platformthemes/qxdgdesktopportal.prl
%dir %{mingw32_libdir}/qt5/plugins/printsupport
%{mingw32_libdir}/qt5/plugins/printsupport/libwindowsprintersupport.a
%{mingw32_libdir}/qt5/plugins/printsupport/windowsprintersupport.prl
%dir %{mingw32_libdir}/qt5/plugins/sqldrivers
%{mingw32_libdir}/qt5/plugins/sqldrivers/libqsqlite.a
%{mingw32_libdir}/qt5/plugins/sqldrivers/qsqlite.prl
%{mingw32_libdir}/qt5/plugins/sqldrivers/libqsqlodbc.a
%{mingw32_libdir}/qt5/plugins/sqldrivers/qsqlodbc.prl
%{mingw32_libdir}/qt5/plugins/sqldrivers/libqsqlpsql.a
%{mingw32_libdir}/qt5/plugins/sqldrivers/qsqlpsql.prl
%dir %{mingw32_libdir}/qt5/plugins/styles
%{mingw32_libdir}/qt5/plugins/styles/libqwindowsvistastyle.a
%{mingw32_libdir}/qt5/plugins/styles/qwindowsvistastyle.prl

# Win64
%files -n mingw64-qt5-qtbase
%license LICENSE.LGPL*
%{mingw64_bindir}/Qt5Concurrent.dll
%{mingw64_bindir}/Qt5Core.dll
%{mingw64_bindir}/Qt5DBus.dll
%{mingw64_bindir}/Qt5Gui.dll
%{mingw64_bindir}/Qt5Network.dll
%{mingw64_bindir}/Qt5OpenGL.dll
%{mingw64_bindir}/Qt5PrintSupport.dll
%{mingw64_bindir}/Qt5Sql.dll
%{mingw64_bindir}/Qt5Test.dll
%{mingw64_bindir}/Qt5Widgets.dll
%{mingw64_bindir}/Qt5Xml.dll
%{mingw64_libdir}/libQt5Concurrent.dll.a
%{mingw64_libdir}/libQt5Core.dll.a
%{mingw64_libdir}/libQt5DBus.dll.a
%{mingw64_libdir}/libQt5Gui.dll.a
%{mingw64_libdir}/libQt5Network.dll.a
%{mingw64_libdir}/libQt5OpenGL.dll.a
%{mingw64_libdir}/libQt5PrintSupport.dll.a
%{mingw64_libdir}/libQt5Sql.dll.a
%{mingw64_libdir}/libQt5Test.dll.a
%{mingw64_libdir}/libQt5Widgets.dll.a
%{mingw64_libdir}/libQt5Xml.dll.a
%{mingw64_libdir}/libqt5main.a
%{mingw64_libdir}/pkgconfig/Qt5Concurrent.pc
%{mingw64_libdir}/pkgconfig/Qt5Core.pc
%{mingw64_libdir}/pkgconfig/Qt5DBus.pc
%{mingw64_libdir}/pkgconfig/Qt5Gui.pc
%{mingw64_libdir}/pkgconfig/Qt5Network.pc
%{mingw64_libdir}/pkgconfig/Qt5OpenGL.pc
%{mingw64_libdir}/pkgconfig/Qt5OpenGLExtensions.pc
%{mingw64_libdir}/pkgconfig/Qt5PrintSupport.pc
%{mingw64_libdir}/pkgconfig/Qt5Sql.pc
%{mingw64_libdir}/pkgconfig/Qt5Test.pc
%{mingw64_libdir}/pkgconfig/Qt5Widgets.pc
%{mingw64_libdir}/pkgconfig/Qt5Xml.pc
%dir %{mingw64_libdir}/qt5/
%dir %{mingw64_libdir}/qt5/mkspecs
%dir %{mingw64_libdir}/qt5/mkspecs/features
%dir %{mingw64_libdir}/qt5/plugins
%dir %{mingw64_libdir}/qt5/plugins/bearer
%{mingw64_libdir}/qt5/plugins/bearer/qgenericbearer.dll
%dir %{mingw64_libdir}/qt5/plugins/generic
%{mingw64_libdir}/qt5/plugins/generic/qtuiotouchplugin.dll
%dir %{mingw64_libdir}/qt5/plugins/imageformats
%{mingw64_libdir}/qt5/plugins/imageformats/qgif.dll
%{mingw64_libdir}/qt5/plugins/imageformats/qico.dll
%{mingw64_libdir}/qt5/plugins/imageformats/qjpeg.dll
%dir %{mingw64_libdir}/qt5/plugins/platforms
%{mingw64_libdir}/qt5/plugins/platforms/qoffscreen.dll
%{mingw64_libdir}/qt5/plugins/platforms/qminimal.dll
%{mingw64_libdir}/qt5/plugins/platforms/qwindows.dll
%dir %{mingw64_libdir}/qt5/plugins/platformthemes/
%{mingw64_libdir}/qt5/plugins/platformthemes/qxdgdesktopportal.dll
%dir %{mingw64_libdir}/qt5/plugins/printsupport
%{mingw64_libdir}/qt5/plugins/printsupport/windowsprintersupport.dll
%dir %{mingw64_libdir}/qt5/plugins/sqldrivers
%{mingw64_libdir}/qt5/plugins/sqldrivers/qsqlite.dll
%{mingw64_libdir}/qt5/plugins/sqldrivers/qsqlodbc.dll
%{mingw64_libdir}/qt5/plugins/sqldrivers/qsqlpsql.dll
%dir %{mingw64_libdir}/qt5/plugins/styles
%{mingw64_libdir}/qt5/plugins/styles/qwindowsvistastyle.dll
%{mingw64_libdir}/cmake/Qt5/
%{mingw64_libdir}/cmake/Qt5AccessibilitySupport/
%{mingw64_libdir}/cmake/Qt5BootstrapDBus/
%{mingw64_libdir}/cmake/Qt5Core/
%{mingw64_libdir}/cmake/Qt5Concurrent/
%{mingw64_libdir}/cmake/Qt5DBus/
%{mingw64_libdir}/cmake/Qt5DeviceDiscoverySupport/
%{mingw64_libdir}/cmake/Qt5EdidSupport/
%{mingw64_libdir}/cmake/Qt5EventDispatcherSupport/
%{mingw64_libdir}/cmake/Qt5FbSupport/
%{mingw64_libdir}/cmake/Qt5FontDatabaseSupport/
%{mingw64_libdir}/cmake/Qt5Gui/
%{mingw64_libdir}/cmake/Qt5Network/
%{mingw64_libdir}/cmake/Qt5OpenGL/
%{mingw64_libdir}/cmake/Qt5OpenGLExtensions/
%{mingw64_libdir}/cmake/Qt5PlatformCompositorSupport/
%{mingw64_libdir}/cmake/Qt5PrintSupport/
%{mingw64_libdir}/cmake/Qt5Sql/
%{mingw64_libdir}/cmake/Qt5Test/
%{mingw64_libdir}/cmake/Qt5ThemeSupport/
%{mingw64_libdir}/cmake/Qt5VulkanSupport/
%{mingw64_libdir}/cmake/Qt5Widgets/
%{mingw64_libdir}/cmake/Qt5WindowsUIAutomationSupport/
%{mingw64_libdir}/cmake/Qt5Xml/
%dir %{mingw64_libdir}/metatypes
%{mingw64_libdir}/metatypes/qt5core_metatypes.json
%{mingw64_libdir}/metatypes/qt5gui_metatypes.json
%{mingw64_libdir}/metatypes/qt5widgets_metatypes.json
%dir %{mingw64_includedir}/qt5/
%{mingw64_includedir}/qt5/*
%{mingw64_docdir}/qt5/

%files -n mingw64-qt5-qmake
%{_bindir}/%{mingw64_target}-moc-qt5
%{_bindir}/%{mingw64_target}-qdbuscpp2xml-qt5
%{_bindir}/%{mingw64_target}-qdbusxml2cpp-qt5
%{_bindir}/%{mingw64_target}-qmake-qt5
%{_bindir}/%{mingw64_target}-rcc-qt5
%{_bindir}/%{mingw64_target}-syncqt.pl-qt5
%{_bindir}/%{mingw64_target}-uic-qt5
%{_bindir}/mingw64-qmake-qt5
%dir %{_prefix}/%{mingw64_target}/bin/qt5/
%{_prefix}/%{mingw64_target}/bin/qt5/fixqt4headers.pl
%{_prefix}/%{mingw64_target}/bin/qt5/moc
%{_prefix}/%{mingw64_target}/bin/qt5/qdbuscpp2xml
%{_prefix}/%{mingw64_target}/bin/qt5/qdbusxml2cpp
%{_prefix}/%{mingw64_target}/bin/qt5/qlalr
%{_prefix}/%{mingw64_target}/bin/qt5/qmake
%{_prefix}/%{mingw64_target}/bin/qt5/qvkgen
%{_prefix}/%{mingw64_target}/bin/qt5/rcc
%{_prefix}/%{mingw64_target}/bin/qt5/syncqt.pl
%{_prefix}/%{mingw64_target}/bin/qt5/tracegen
%{_prefix}/%{mingw64_target}/bin/qt5/uic
%{_prefix}/%{mingw64_target}/lib/libQt5Bootstrap.so.5*
%{_prefix}/%{mingw64_target}/lib/libQt5BootstrapDBus.so.5*
%{mingw64_datadir}/qt5/

# qtchooser
%dir %{_sysconfdir}/xdg/qtchooser/
# not editable config files, so not using %%config here
%{_sysconfdir}/xdg/qtchooser/mingw64-qt5.conf

%files -n mingw64-qt5-qtbase-devel
%{_prefix}/%{mingw64_target}/lib/libQt5Bootstrap.so
%{_prefix}/%{mingw64_target}/lib/libQt5Bootstrap.prl
%{_prefix}/%{mingw64_target}/lib/libQt5BootstrapDBus.so
%{_prefix}/%{mingw64_target}/lib/libQt5BootstrapDBus.prl

%files -n mingw64-qt5-qtbase-static
%{mingw64_libdir}/*.a
%{mingw64_libdir}/*.prl
%exclude %{mingw64_libdir}/*.dll.a
%dir %{mingw64_libdir}/qt5/plugins
%dir %{mingw64_libdir}/qt5/plugins/bearer
%{mingw64_libdir}/qt5/plugins/bearer/libqgenericbearer.a
%{mingw64_libdir}/qt5/plugins/bearer/qgenericbearer.prl
%dir %{mingw64_libdir}/qt5/plugins/generic
%{mingw64_libdir}/qt5/plugins/generic/libqtuiotouchplugin.a
%{mingw64_libdir}/qt5/plugins/generic/qtuiotouchplugin.prl
%dir %{mingw64_libdir}/qt5/plugins/imageformats
%{mingw64_libdir}/qt5/plugins/imageformats/libqgif.a
%{mingw64_libdir}/qt5/plugins/imageformats/qgif.prl
%{mingw64_libdir}/qt5/plugins/imageformats/libqico.a
%{mingw64_libdir}/qt5/plugins/imageformats/qico.prl
%{mingw64_libdir}/qt5/plugins/imageformats/libqjpeg.a
%{mingw64_libdir}/qt5/plugins/imageformats/qjpeg.prl
%dir %{mingw64_libdir}/qt5/plugins/platforms
%{mingw64_libdir}/qt5/plugins/platforms/libqoffscreen.a
%{mingw64_libdir}/qt5/plugins/platforms/qoffscreen.prl
%{mingw64_libdir}/qt5/plugins/platforms/libqminimal.a
%{mingw64_libdir}/qt5/plugins/platforms/qminimal.prl
%{mingw64_libdir}/qt5/plugins/platforms/libqwindows.a
%{mingw64_libdir}/qt5/plugins/platforms/qwindows.prl
%dir %{mingw64_libdir}/qt5/plugins/platformthemes/
%{mingw64_libdir}/qt5/plugins/platformthemes/libqxdgdesktopportal.a
%{mingw64_libdir}/qt5/plugins/platformthemes/qxdgdesktopportal.prl
%dir %{mingw64_libdir}/qt5/plugins/printsupport
%{mingw64_libdir}/qt5/plugins/printsupport/libwindowsprintersupport.a
%{mingw64_libdir}/qt5/plugins/printsupport/windowsprintersupport.prl
%dir %{mingw64_libdir}/qt5/plugins/sqldrivers
%{mingw64_libdir}/qt5/plugins/sqldrivers/libqsqlite.a
%{mingw64_libdir}/qt5/plugins/sqldrivers/qsqlite.prl
%{mingw64_libdir}/qt5/plugins/sqldrivers/libqsqlodbc.a
%{mingw64_libdir}/qt5/plugins/sqldrivers/qsqlodbc.prl
%{mingw64_libdir}/qt5/plugins/sqldrivers/libqsqlpsql.a
%{mingw64_libdir}/qt5/plugins/sqldrivers/qsqlpsql.prl
%dir %{mingw64_libdir}/qt5/plugins/styles
%{mingw64_libdir}/qt5/plugins/styles/libqwindowsvistastyle.a
%{mingw64_libdir}/qt5/plugins/styles/qwindowsvistastyle.prl

%changelog
%autochangelog
