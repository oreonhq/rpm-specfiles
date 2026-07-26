%global source0_hash 9ca126da9273664dd23a3ccd0c9bebceb7bb534bddd743db31caf6a5a6d4a9e6

# The additional linker flags break binary qt5-qtwebkits packages.
# https://bugzilla.redhat.com/show_bug.cgi?id=2046931
%undefine _package_note_flags

%global qt_module qtwebkit

%global _hardened_build 1

%global prerel alpha4
%global prerel_tag -%{prerel}

## NOTE: Lots of files in various subdirectories have the same name (such as
## "LICENSE") so this short macro allows us to distinguish them by using their
## directory names (from the source tree) as prefixes for the files.
%global add_to_license_files() \
        mkdir -p _license_files ; \
        cp -p %1 _license_files/$(echo '%1' | sed -e 's!/!.!g')

Name:           qt5-%{qt_module}
Version:        5.212.0
Release:        0.98%{?prerel}%{?dist}
Summary:        Qt5 - QtWebKit components

License:        LGPL-2.0-only AND BSD-3-Clause
URL:            https://github.com/qtwebkit/qtwebkit
Source0:        https://github.com/qtwebkit/qtwebkit/releases/download/%{qt_module}-%{version}%{?prerel_tag}/%{qt_module}-%{version}%{?prerel_tag}.tar.xz

# Patch for new CMake policy CMP0071 to explicitly use old behaviour.
Patch2:         qtwebkit-5.212.0_cmake_cmp0071.patch
Patch3:         qtwebkit-5.212.0-json.patch
Patch4:         qtwebkit-bison37.patch
Patch5:         qt5-qtwebkit-glib-2.68.patch
Patch6:         qtwebkit-icu68.patch
# From https://github.com/WebKit/WebKit/commit/c7d19a492d97f9282a546831beb918e03315f6ef
# Ruby 3.2 removes Object#=~ completely
Patch7:         webkit-offlineasm-warnings-ruby27.patch
Patch8:         qtwebkit-cstdint.patch
Patch9:         qtwebkit-fix-build-gcc14.patch
Patch10:        qtwebkit-icu76.patch

# Enable RISC-V (riscv64)
Patch11:        https://github.com/qtwebkit/qtwebkit/commit/d9824ec806b6c6171862a7ba758fc28e6a20aada.patch
# Fix FTBFS
Patch12:        qtwebkit-ftbfs-gcc16.patch

BuildRequires: make
BuildRequires:  bison
BuildRequires:  cmake
BuildRequires:  flex
BuildRequires:  pkgconfig(fontconfig)
%if 0%{?rhel} != 8
BuildRequires:  pkgconfig(libwoff2dec)
%endif
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  gperf
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-app-1.0)
BuildRequires:  hyphen-devel
BuildRequires:  pkgconfig(icu-i18n) pkgconfig(icu-uc)
BuildRequires:  libjpeg-devel
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(xcomposite)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(libxslt)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(gstreamer-gl-1.0)
BuildRequires:  pkgconfig(gstreamer-mpegts-1.0)
BuildRequires:  perl-generators
BuildRequires:  perl(File::Copy)
BuildRequires:  python3
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtdeclarative-devel
%if ! 0%{?bootstrap}
BuildRequires:  qt5-qtlocation-devel
BuildRequires:  qt5-qtsensors-devel
BuildRequires:  qt5-qtwebchannel-devel
%endif
BuildRequires:  pkgconfig(ruby)
BuildRequires:  rubygems
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(zlib)
# workaround bad embedded png files, https://bugzilla.redhat.com/1639422
BuildRequires:  findutils
BuildRequires:  pngcrush

BuildRequires:  qt5-qtbase-private-devel
%{?_qt5:Requires: %{_qt5}%{?_isa} = %{_qt5_version}}
BuildRequires:  qt5-qtdeclarative-private-devel
%{?_qt5:Requires: qt5-qtdeclarative%{?_isa} = %{_qt5_version}}

# filter qml provides
%global __provides_exclude_from ^%{_qt5_archdatadir}/qml/.*\\.so$

# We're supposed to specify versions here, but these crap Google libs don't do
# normal releases. Accordingly, they're not suitable to be system libs.
Provides:       bundled(angle)
Provides:       bundled(brotli)
Provides:       bundled(woff2)

%description
%{summary}

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       qt5-qtbase-devel%{?_isa}
Requires:       qt5-qtdeclarative-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%if 0%{?docs}
%package doc
Summary: API documentation for %{name}
BuildRequires: qt5-qdoc
BuildRequires: qt5-qhelpgenerator
BuildArch: noarch

%description doc
%{summary}.
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{qt_module}-%{version}%{?prerel_tag}

# find/fix pngs with "libpng warning: iCCP: known incorrect sRGB profile"
find -name \*.png | xargs -n1 pngcrush -ow -fix

# ppc64le failed once with
# make[2]: *** No rule to make target 'Source/WebCore/Resources/textAreaResizeCorner.png', needed by 'Source/WebKit/qrc_WebCore.cpp'.  Stop.
test -f Source/WebCore/Resources/textAreaResizeCorner.png

%build
# TODO: Please submit an issue to upstream (rhbz#2381397)
export CMAKE_POLICY_VERSION_MINIMUM=3.5
# QT is known not to work properly with LTO at this point.  Some of the issues
# are being worked on upstream and disabling LTO should be re-evaluated as
# we update this change.  Until such time...
# Disable LTO
%define _lto_cflags %{nil}
%define _package_note_flags %{nil}

# The following changes of optflags ietc. are adapted from webkitgtk4 package, which
# is mostly similar to this one...
#
# Increase the DIE limit so our debuginfo packages can be size-optimized.
# This previously decreased the size for x86_64 from ~5G to ~1.1G, but as of
# 2022 it's more like 850 MB -> 675 MB. This requires lots of RAM on the
# builders, so only do this for x86_64 and aarch64 to avoid overwhelming
# builders with less RAM.
# https://bugzilla.redhat.com/show_bug.cgi?id=1456261
%global _dwz_max_die_limit_x86_64 250000000
%global _dwz_max_die_limit_aarch64 250000000

# Require 32 GB of RAM per vCPU for debuginfo processing. 16 GB is not enough.
%global _find_debuginfo_opts %limit_build -m 32768

# Decrease debuginfo even on ix86 because of:
# https://bugs.webkit.org/show_bug.cgi?id=140176
%ifarch s390 s390x %{arm} %{ix86} ppc %{power64} %{mips} riscv64
# Decrease debuginfo verbosity to reduce memory consumption even more
%global optflags %(echo %{optflags} | sed 's/-g /-g1 /')
%endif

%ifarch ppc
# Use linker flag -relax to get WebKit build under ppc(32) with JIT disabled
%global optflags %{optflags} -Wl,-relax
%endif

CFLAGS="${CFLAGS:-%optflags}" ; export CFLAGS ;
CXXFLAGS="${CXXFLAGS:-%optflags} -fpermissive" ; export CXXFLAGS ;
%{?__global_ldflags:LDFLAGS="${LDFLAGS:-%__global_ldflags}" ; export LDFLAGS ;}

%ifarch riscv64
export LDFLAGS="${LDFLAGS} -latomic"
%endif

# We cannot use default cmake macro here as it overwrites some settings queried
# by qtwebkit cmake from qmake
%cmake \
       -DPORT=Qt \
       -DCMAKE_BUILD_TYPE=Release \
       -DENABLE_TOOLS=OFF \
       -DCMAKE_C_FLAGS_RELEASE:STRING="-DNDEBUG" \
       -DCMAKE_CXX_FLAGS_RELEASE:STRING="-DNDEBUG" \
       -DCMAKE_VERBOSE_MAKEFILE:BOOL=ON \
       -DLIBEXEC_INSTALL_DIR=%{_qt5_libexecdir} \
       -DECM_MKSPECS_INSTALL_DIR=%{_qt5_archdatadir}/mkspecs/modules \
       -DQML_INSTALL_DIR=%{_qt5_archdatadir}/qml \
       -DKDE_INSTALL_INCLUDEDIR=%{_qt5_headerdir} \
%ifarch s390 s390x ppc %{power64} riscv64
       -DENABLE_JIT=OFF \
%endif
%ifarch s390 s390x ppc %{power64}
       -DUSE_SYSTEM_MALLOC=ON \
%endif
       %{?docs:-DGENERATE_DOCUMENTATION=ON} \
       -DPYTHON_EXECUTABLE:PATH="%{__python3}"

%cmake_build

%if 0%{?docs}
%make_build docs
%endif

%install
%cmake_install

find %{buildroot} -name '*.la' -exec rm -f {} ';'

# fix pkgconfig files
#sed -i '/Name/a Description: Qt5 WebKit module' %{buildroot}%{_libdir}/pkgconfig/Qt5WebKit.pc
#sed -i "s,Cflags: -I%{_qt5_libdir}/qt5/../../include/qt5/Qt5WebKit,Cflags: -I%{_qt5_headerdir}/QtWebKit,g" %{buildroot}%{_libdir}/pkgconfig/Qt5WebKit.pc
# strictly speaking, this isn't *wrong*, but can made more readable, so let's do that
sed -i "s,Libs: -L%{_qt5_libdir}/qt5/../ -lQt5WebKit,Libs: -L%{_qt5_libdir} -lQt5WebKit ,g" %{buildroot}%{_libdir}/pkgconfig/Qt5WebKit.pc

#sed -i '/Name/a Description: Qt5 WebKitWidgets module' %{buildroot}%{_libdir}/pkgconfig/Qt5WebKitWidgets.pc
#sed -i "s,Cflags: -I%{_qt5_libdir}/qt5/../../include/qt5/Qt5WebKitWidgets,Cflags: -I%{_qt5_headerdir}/QtWebKitWidgets,g" %{buildroot}%{_libdir}/pkgconfig/Qt5WebKitWidgets.pc
sed -i "s,Libs: -L%{_qt5_libdir}/qt5/../ -lQt5WebKitWidgets,Libs: -L%{_qt5_libdir} -lQt5WebKitWidgets ,g" %{buildroot}%{_libdir}/pkgconfig/Qt5WebKitWidgets.pc

# Finally, copy over and rename various files for %%license inclusion
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

%check
# verify Qt5WebKit cflags non-use of -I/.../Qt5WebKit
export PKG_CONFIG_PATH=%{buildroot}%{_libdir}/pkgconfig
test -z "$(pkg-config --cflags Qt5WebKit | grep Qt5WebKit)"

%ldconfig_scriptlets

%files
%license LICENSE.LGPLv21 _license_files/*
%{_qt5_libdir}/libQt5WebKit.so.5*
%{_qt5_libdir}/libQt5WebKitWidgets.so.5*
%{_qt5_libexecdir}/QtWebNetworkProcess
%{_qt5_libexecdir}/QtWebPluginProcess
%{_qt5_libexecdir}/QtWebProcess
%{_qt5_libexecdir}/QtWebStorageProcess
%{_qt5_archdatadir}/qml/QtWebKit/

%files devel
%{_qt5_headerdir}/Qt*/
%{_qt5_libdir}/libQt5*.so
%{_qt5_libdir}/cmake/Qt5*/
%{_qt5_libdir}/pkgconfig/Qt5*.pc
%{_qt5_archdatadir}/mkspecs/modules/*.pri

%if 0%{?docs}
%files doc
%{_qt5_docdir}/qtwebkit.qch
%{_qt5_docdir}/qtwebkit/
%endif

%changelog
%autochangelog
