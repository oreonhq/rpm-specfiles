%global source0_hash 9ca126da9273664dd23a3ccd0c9bebceb7bb534bddd743db31caf6a5a6d4a9e6

%{?mingw_package_header}

%global qt_module qtwebkit
%global pre alpha4

#global commit bd0657f98aff85b9f06d85a8cf4da6a27f61a56e
#global shortcommit %(c=%{commit}; echo ${c:0:7})

%if 0%{?commit:1}
%global source_folder %{qt_module}-%{commit}
%else
%global source_folder %{qt_module}-%{version}%{?pre:-%{pre}}
%endif

## NOTE: Lots of files in various subdirectories have the same name (such as
## "LICENSE") so this short macro allows us to distinguish them by using their
## directory names (from the source tree) as prefixes for the files.
%global add_to_license_files() \
        mkdir -p _license_files ; \
        cp -p %1 _license_files/$(echo '%1' | sed -e 's!/!.!g')

Name:           mingw-qt5-%{qt_module}
Version:        5.212.0
Release:        0.42%{?pre:.%pre}%{?commit:.git%{shortcommit}}%{?dist}
Summary:        Qt5 for Windows - QtWebKit component

License:        LGPL-2.1-only OR GPL-3.0-only WITH Qt-GPL-exception-1.0
URL:            https://github.com/qtwebkit/qtwebkit

%if 0%{?commit:1}
Source0:        https://github.com/%{qt_module}/%{qt_module}/archive/%{commit}/%{qt_module}-%{commit}.tar.xz
%else
Source0:        https://github.com/%{qt_module}/%{qt_module}/releases/download/%{qt_module}-%{version}%{?pre:-%pre}/%{qt_module}-%{version}%{?pre:-%pre}.tar.xz
%endif

# Don't override import lib suffix
Patch1:         qtwebkit_libsuffix.patch
# Backport python 3.9 build fix
Patch2:         qtwebkit_python.patch
# Fix build with bison 3.7
Patch3:         qtwebkit-bison37.patch
# From https://github.com/WebKit/WebKit/commit/c7d19a492d97f9282a546831beb918e03315f6ef
# Ruby 3.2 removes Object#=~ completely
Patch4:         webkit-offlineasm-warnings-ruby27.patch
# Correctly test ICU return status with U_SUCCESS rather than comparing to U_ZERO_ERROR which fails on warnings
Patch5:         qtwebkit_icu-success.patch
# Fix gcc13 build
Patch6:         qtwebkit_gcc13.patch
# Fix build against recent libxml2
Patch7:         qtwebkit_libxml.patch
# Fix gcc14 build
Patch8:         qtwebkit-fix-build-gcc14.patch
# Switch to -std=c++17 (fixes build with recent icu)
# Drop backported c++14 stl features om StdLibExtras.h
Patch9:         qtwebkit-c++17.patch
# Raise cmake minimum version
Patch10:        qtwebkit_cmakever.patch
# Fix build against gcc15
Patch11:        qtwebkit_gcc15.patch

BuildArch:      noarch

BuildRequires:  bison
BuildRequires:  cmake
BuildRequires:  flex
BuildRequires:  gperf
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  python3
BuildRequires:  ruby-devel
BuildRequires:  rubygems
# workaround bad embedded png files, https://bugzilla.redhat.com/1639422
BuildRequires:  findutils
BuildRequires:  pngcrush

BuildRequires:  mingw32-filesystem >= 96
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-pkg-config

BuildRequires:  mingw32-dlfcn
BuildRequires:  mingw32-fontconfig
BuildRequires:  mingw32-icu
BuildRequires:  mingw32-libjpeg-turbo
BuildRequires:  mingw32-libpng
BuildRequires:  mingw32-libwebp
BuildRequires:  mingw32-libxslt
BuildRequires:  mingw32-qt5-qtbase
BuildRequires:  mingw32-qt5-qtdeclarative
BuildRequires:  mingw32-qt5-qtsensors
BuildRequires:  mingw32-qt5-qtlocation
BuildRequires:  mingw32-qt5-qtmultimedia
BuildRequires:  mingw32-qt5-qtwebchannel
BuildRequires:  mingw32-sqlite
BuildRequires:  mingw32-zlib

BuildRequires:  mingw64-filesystem >= 96
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-pkg-config

BuildRequires:  mingw64-dlfcn
BuildRequires:  mingw64-angleproject
BuildRequires:  mingw64-fontconfig
BuildRequires:  mingw64-icu
BuildRequires:  mingw64-libjpeg-turbo
BuildRequires:  mingw64-libpng
BuildRequires:  mingw64-libwebp
BuildRequires:  mingw64-libxslt
BuildRequires:  mingw64-qt5-qtbase
BuildRequires:  mingw64-qt5-qtdeclarative
BuildRequires:  mingw64-qt5-qtsensors
BuildRequires:  mingw64-qt5-qtlocation
BuildRequires:  mingw64-qt5-qtmultimedia
BuildRequires:  mingw64-qt5-qtwebchannel
BuildRequires:  mingw64-sqlite
BuildRequires:  mingw64-zlib

%description
This package contains the Qt software toolkit for developing
cross-platform applications.

This is the Windows version of Qt, for use in conjunction with the
Fedora Windows cross-compiler.

# Win32
%package -n mingw32-qt5-%{qt_module}
Summary:        Qt5 for Windows - QtWebkit component
Provides:       bundled(angle)
Provides:       bundled(brotli)
Provides:       bundled(woff2)

%description -n mingw32-qt5-%{qt_module}
This package contains the Qt software toolkit for developing
cross-platform applications.

This is the Windows version of Qt, for use in conjunction with the
Fedora Windows cross-compiler.

# Win64
%package -n mingw64-qt5-%{qt_module}
Summary:        Qt5 for Windows - QtWebkit component
Provides:       bundled(angle)
Provides:       bundled(brotli)
Provides:       bundled(woff2)

%description -n mingw64-qt5-%{qt_module}
This package contains the Qt software toolkit for developing
cross-platform applications.

This is the Windows version of Qt, for use in conjunction with the
Fedora Windows cross-compiler.

%{?mingw_debug_package}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{source_folder}

# find/fix pngs with "libpng warning: iCCP: known incorrect sRGB profile"
find -name \*.png | xargs -n1 pngcrush -ow -fix

%build
# Make sure the native pkg-config files aren't used (RPM sets this environment variable automatically)
unset PKG_CONFIG_PATH

# Reduce debuginfo verbosity to decrease memory usage
mingw32_cflags_="%(echo %mingw32_cflags | sed 's/-g /-g1 /')"
mingw64_cflags_="%(echo %mingw64_cflags | sed 's/-g /-g1 /')"

# -D_WIN32_WINNT=0x0600 Needed for GetTickCount64
export MINGW32_CFLAGS="$mingw32_cflags_ -D_WIN32_WINNT=0x0600"
export MINGW32_CXXFLAGS="$mingw32_cflags_ -D_WIN32_WINNT=0x0600"
export MINGW64_CFLAGS="$mingw64_cflags_ -D_WIN32_WINNT=0x0600"
export MINGW64_CXXFLAGS="$mingw64_cflags_ -D_WIN32_WINNT=0x0600"

# TODO
# --  USE_LIBHYPHEN                             OFF
%mingw_cmake -DPORT=Qt \
    -DRUBY_CONFIG_INCLUDE_DIR:PATH=/usr/include \
    -DRUBY_LIBRARY:FILEPATH=/usr/lib64/libruby.so \
    -DRUBY_INCLUDE_DIR:PATH=/usr/include

%mingw_make_build

%install
%mingw_make_install

# Copy over and rename various files for %%license inclusion
%add_to_license_files Source/JavaScriptCore/COPYING.LIB
%add_to_license_files Source/JavaScriptCore/icu/LICENSE
%add_to_license_files Source/ThirdParty/ANGLE/LICENSE
%add_to_license_files Source/ThirdParty/ANGLE/src/third_party/compiler/LICENSE
%add_to_license_files Source/ThirdParty/ANGLE/src/third_party/murmurhash/LICENSE
%add_to_license_files Source/WebCore/icu/LICENSE
%add_to_license_files Source/WebCore/LICENSE-APPLE
%add_to_license_files Source/WebCore/LICENSE-LGPL-2
%add_to_license_files Source/WebCore/LICENSE-LGPL-2.1
%add_to_license_files Source/WebInspectorUI/UserInterface/External/CodeMirror/LICENSE
%add_to_license_files Source/WebInspectorUI/UserInterface/External/Esprima/LICENSE
%add_to_license_files Source/WTF/icu/LICENSE
%add_to_license_files Source/WTF/wtf/dtoa/COPYING
%add_to_license_files Source/WTF/wtf/dtoa/LICENSE

# Move executables installed to the wrong location
mv %{buildroot}%{mingw32_libdir}/qt5/bin/*.exe %{buildroot}%{mingw32_bindir}
mv %{buildroot}%{mingw64_libdir}/qt5/bin/*.exe %{buildroot}%{mingw64_bindir}
rmdir %{buildroot}%{mingw32_libdir}/qt5/bin/
rmdir %{buildroot}%{mingw64_libdir}/qt5/bin/

# Win32
%files -n mingw32-qt5-%{qt_module}
%license LICENSE.LGPLv21 _license_files/*
%{mingw32_bindir}/QtWebNetworkProcess.exe
%{mingw32_bindir}/QtWebProcess.exe
%{mingw32_bindir}/QtWebStorageProcess.exe
%{mingw32_bindir}/Qt5WebKit.dll
%{mingw32_bindir}/Qt5WebKitWidgets.dll
%{mingw32_includedir}/qt5/QtWebKit/
%{mingw32_includedir}/qt5/QtWebKitWidgets/
%{mingw32_libdir}/libQt5WebKit.dll.a
%{mingw32_libdir}/libQt5WebKitWidgets.dll.a
%{mingw32_libdir}/cmake/Qt5WebKit/
%{mingw32_libdir}/cmake/Qt5WebKitWidgets/
%{mingw32_libdir}/pkgconfig/Qt5WebKit.pc
%{mingw32_libdir}/pkgconfig/Qt5WebKitWidgets.pc
%{mingw32_libdir}/qt5/qml/QtWebKit/
%{mingw32_datadir}/qt5/mkspecs/modules/qt_lib_webkit.pri
%{mingw32_datadir}/qt5/mkspecs/modules/qt_lib_webkit_private.pri
%{mingw32_datadir}/qt5/mkspecs/modules/qt_lib_webkitwidgets.pri
%{mingw32_datadir}/qt5/mkspecs/modules/qt_lib_webkitwidgets_private.pri

# Win64
%files -n mingw64-qt5-%{qt_module}
%license LICENSE.LGPLv21 _license_files/*
%{mingw64_bindir}/QtWebNetworkProcess.exe
%{mingw64_bindir}/QtWebProcess.exe
%{mingw64_bindir}/QtWebStorageProcess.exe
%{mingw64_bindir}/Qt5WebKit.dll
%{mingw64_bindir}/Qt5WebKitWidgets.dll
%{mingw64_includedir}/qt5/QtWebKit/
%{mingw64_includedir}/qt5/QtWebKitWidgets/
%{mingw64_libdir}/libQt5WebKit.dll.a
%{mingw64_libdir}/libQt5WebKitWidgets.dll.a
%{mingw64_libdir}/cmake/Qt5WebKit/
%{mingw64_libdir}/cmake/Qt5WebKitWidgets/
%{mingw64_libdir}/pkgconfig/Qt5WebKit.pc
%{mingw64_libdir}/pkgconfig/Qt5WebKitWidgets.pc
%{mingw64_libdir}/qt5/qml/QtWebKit/
%{mingw64_datadir}/qt5/mkspecs/modules/qt_lib_webkit.pri
%{mingw64_datadir}/qt5/mkspecs/modules/qt_lib_webkit_private.pri
%{mingw64_datadir}/qt5/mkspecs/modules/qt_lib_webkitwidgets.pri
%{mingw64_datadir}/qt5/mkspecs/modules/qt_lib_webkitwidgets_private.pri

%changelog
%autochangelog
