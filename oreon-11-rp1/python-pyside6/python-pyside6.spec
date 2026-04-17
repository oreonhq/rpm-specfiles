# Do not force clang as the C++ compiler for generated wrappers. Clang 16+ hits
# -Wcast-function-type-mismatch on thousands of shiboken-generated PyMethodDef lines.
# Libclang is still used for API parsing (LLVM_INSTALL_DIR / CMAKE_PREFIX_PATH).
%global toolchain gcc

%global _lto_cflags %{nil}
%global _smp_mflags -j1

# needed to ship deploy_lib template files
%global _python_bytecompile_errors_terminate_build 0

%global pypi_name pyside6
%global camel_name PySide6
%global qt6ver 6.10.3

Name:           python-%{pypi_name}
Version:        6.10.3
Release:        9%{?dist}
Summary:        Python bindings for the Qt 6 cross-platform application and UI framework

License:        LGPL-3.0-only OR GPL-3.0-only WITH Qt-GPL-exception-1.0
URL:            https://wiki.qt.io/Qt_for_Python

Source0:        https://download.qt.io/official_releases/QtForPython/%{pypi_name}/%{camel_name}-%{qt6ver}-src/pyside-setup-everywhere-src-%{version}.tar.xz
# for documentation generation
%global docs 0
%global qt_module qtbase
%global  majmin %(echo %{version} | cut -d. -f1-2)
# Optional doc-only qtbase submodule tarball when %%docs is enabled (see Fedora python-pyside6).

# Shipped in SRPM (avoid src.fedoraproject.org fetch flakiness in mock)
Patch0:         0001-Revert-Modify-headers-installation-for-CMake-builds.patch
Patch1:         0001-Always-link-to-python-libraries.patch
Patch2:         0001-Fix-installation.patch
Patch3:         0001-shiboken6-Fix-build-with-clang-22.patch

BuildRequires:  cmake
BuildRequires:  ninja-build
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  git
BuildRequires:  clang-devel
BuildRequires:  clang-tools-extra
BuildRequires:  llvm-devel
BuildRequires:  python3-numpy
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-wheel
BuildRequires:  python3-packaging

BuildRequires:  libxml2-devel
BuildRequires:  libxslt-devel
BuildRequires:  graphviz
BuildRequires:  python3-sphinx >= 7.4.7

%if 0%{?docs}
# for generating the documentation, see requirements-doc.txt
BuildRequires:  python3-sphinx-design >= 0.6.0
BuildRequires:  python3-sphinx-copybutton >= 0.5.2
BuildRequires:  python3-sphinx-tags >= 0.4
BuildRequires:  python3-sphinx-toolbox >= 3.7.0
BuildRequires:  python3-sphinx-reredirects >= 0.1.5
BuildRequires:  python3-myst-parser >= 3.0.1
BuildRequires:  python3-furo
%endif

# essential modules
BuildRequires:  cmake(Qt6Core) >= %{qt6ver}
BuildRequires:  cmake(Qt6Gui) >= %{qt6ver}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6ver}
BuildRequires:  cmake(Qt6Help) >= %{qt6ver}
BuildRequires:  cmake(Qt6Network) >= %{qt6ver}
BuildRequires:  cmake(Qt6Concurrent) >= %{qt6ver}
BuildRequires:  cmake(Qt6DBus) >= %{qt6ver}
BuildRequires:  cmake(Qt6Designer) >= %{qt6ver}
BuildRequires:  cmake(Qt6OpenGL) >= %{qt6ver}
BuildRequires:  cmake(Qt6OpenGLWidgets) >= %{qt6ver}
BuildRequires:  cmake(Qt6PrintSupport) >= %{qt6ver}
BuildRequires:  cmake(Qt6Qml) >= %{qt6ver}
BuildRequires:  cmake(Qt6Quick) >= %{qt6ver}
BuildRequires:  cmake(Qt6QuickControls2) >= %{qt6ver}
BuildRequires:  cmake(Qt6Xml) >= %{qt6ver}
BuildRequires:  cmake(Qt6Test) >= %{qt6ver}
BuildRequires:  cmake(Qt6Sql) >= %{qt6ver}
BuildRequires:  qt6-qtbase-mysql >= %{qt6ver}
BuildRequires:  qt6-qtbase-odbc >= %{qt6ver}
BuildRequires:  qt6-qtbase-postgresql >= %{qt6ver}
BuildRequires:  cmake(Qt6Svg) >= %{qt6ver}
BuildRequires:  cmake(Qt6SvgWidgets) >= %{qt6ver}
BuildRequires:  cmake(Qt6UiTools) >= %{qt6ver}

BuildRequires:  qt6-qtbase-gui >= %{qt6ver}
BuildRequires:  qt6-qtbase-static >= %{qt6ver}

# from qt6-qtbase for XKB
BuildRequires: pkgconfig(xcb-xkb) >= 1.10
BuildRequires: pkgconfig(xcb-util)
BuildRequires: pkgconfig(xkbcommon) >= 0.4.1
BuildRequires: pkgconfig(xkbcommon-x11) >= 0.4.1
BuildRequires: pkgconfig(xkeyboard-config)

# Add-On modules
BuildRequires:  cmake(Qt6Multimedia) >= %{qt6ver}
BuildRequires:  cmake(Qt6MultimediaWidgets) >= %{qt6ver}
BuildRequires:  cmake(Qt6Positioning) >= %{qt6ver}
BuildRequires:  cmake(Qt6Location) >= %{qt6ver}
BuildRequires:  cmake(Qt6NetworkAuth) >= %{qt6ver}
BuildRequires:  cmake(Qt6Nfc) >= %{qt6ver}
BuildRequires:  cmake(Qt6Quick3D) >= %{qt6ver}
BuildRequires:  cmake(Qt6QuickWidgets) >= %{qt6ver}
BuildRequires:  cmake(Qt6RemoteObjects) >= %{qt6ver}
BuildRequires:  cmake(Qt6Scxml) >= %{qt6ver}
BuildRequires:  cmake(Qt6Sensors) >= %{qt6ver}
BuildRequires:  cmake(Qt6SerialPort) >= %{qt6ver}
BuildRequires:  cmake(Qt6SerialBus) >= %{qt6ver}
BuildRequires:  cmake(Qt6StateMachine) >= %{qt6ver}
BuildRequires:  cmake(Qt6TextToSpeech) >= %{qt6ver}
BuildRequires:  cmake(Qt6Charts) >= %{qt6ver}
BuildRequires:  cmake(Qt6SpatialAudio) >= %{qt6ver}
BuildRequires:  cmake(Qt6DataVisualization) >= %{qt6ver}
BuildRequires:  cmake(Qt6Graphs) >= %{qt6ver}
BuildRequires:  qt6-qtgraphs-devel >= %{qt6ver}
BuildRequires:  cmake(Qt6Bluetooth) >= %{qt6ver}
BuildRequires:  cmake(Qt6WebChannel) >= %{qt6ver}
%ifarch %{qt6_qtwebengine_arches}
BuildRequires:  cmake(Qt6WebEngineCore) >= %{qt6ver}
BuildRequires:  cmake(Qt6WebEngineWidgets) >= %{qt6ver}
BuildRequires:  cmake(Qt6WebEngineQuick) >= %{qt6ver}
BuildRequires:  cmake(Qt6Pdf) >= %{qt6ver}
BuildRequires:  cmake(Qt6PdfWidgets) >= %{qt6ver}
BuildRequires:  cmake(Qt6WebView) >= %{qt6ver}
%endif
BuildRequires:  cmake(Qt6WebSockets) >= %{qt6ver}
BuildRequires:  cmake(Qt6HttpServer) >= %{qt6ver}
BuildRequires:  qt6-qthttpserver-devel >= %{qt6ver}
BuildRequires:  cmake(Qt63DCore) >= %{qt6ver}
BuildRequires:  cmake(Qt63DRender) >= %{qt6ver}
BuildRequires:  cmake(Qt63DInput) >= %{qt6ver}
BuildRequires:  cmake(Qt63DLogic) >= %{qt6ver}
BuildRequires:  cmake(Qt63DAnimation) >= %{qt6ver}
BuildRequires:  cmake(Qt63DExtras) >= %{qt6ver}

BuildRequires:  qt6-qtbase-private-devel >= %{qt6ver}

# Qt Tools
BuildRequires:  cmake(Qt6UiPlugin) >= %{qt6ver}
BuildRequires:  qt6-assistant >= %{qt6ver}
BuildRequires:  qt6-designer >= %{qt6ver}
BuildRequires:  qt6-doctools >= %{qt6ver}

# Tests / configure use a headless Wayland compositor (xwayland-run provides wlheadless-run)
BuildRequires:  xwayland-run
BuildRequires:  /usr/bin/wlheadless-run
BuildRequires:  mesa-dri-drivers

%description
PySide6 is the official Python module from the Qt for Python project, which
provides access to the complete Qt 6+ framework.


%package -n     python%{python3_pkgversion}-%{pypi_name}
Provides:       python%{python3_pkgversion}-%{camel_name} = %{version}-%{release}
Summary:        %{summary}
Requires:       qt6-qtgraphs%{?_isa} >= %{qt6ver}
Requires:       qt6-qthttpserver%{?_isa} >= %{qt6ver}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{camel_name}}

%description -n python%{python3_pkgversion}-%{pypi_name}
PySide6 is the official Python module from the Qt for Python project, which
provides access to the complete Qt 6 framework.


%package -n     python%{python3_pkgversion}-%{pypi_name}-devel
Requires:       pyside6-tools
Requires:       shiboken6
Summary:        Development files related to %{name}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}-devel}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{camel_name}-devel}

%description -n python%{python3_pkgversion}-%{pypi_name}-devel
%{summary}.


%package -n pyside6-tools
Requires:       qt6-qtbase-devel
Requires:       qt6-qtdeclarative-devel
Requires:       qt6-assistant
Requires:       qt6-designer
Requires:       qt6-linguist
Requires:       python3-%{pypi_name}
Summary:        PySide6 tools for the Qt 6 framework

%description -n pyside6-tools
PySide6 provides Python bindings for the Qt6 cross-platform application
and UI framework.


%package -n shiboken6
Summary:        Python / C++ bindings generator for %camel_name

%description -n shiboken6
Shiboken is the Python binding generator that Qt for Python uses to create the
PySide module, in other words, is the system we use to expose the Qt C++ API to
Python.


%package -n python%{python3_pkgversion}-shiboken6
Summary:        Python / C++ bindings libraries for %camel_name

%description -n python%{python3_pkgversion}-shiboken6
Shiboken is the Python binding generator that Qt for Python uses to create the
PySide module, in other words, is the system we use to expose the Qt C++ API to
Python.


%package -n python%{python3_pkgversion}-shiboken6-devel
Summary:        Python / C++ bindings helper module for %camel_name
Requires:       shiboken6
Requires:       python%{python3_pkgversion}-shiboken6

%description -n python%{python3_pkgversion}-shiboken6-devel
Shiboken is the Python binding generator that Qt for Python uses to create the
PySide module, in other words, is the system we use to expose the Qt C++ API to
Python.

%if 0%{?docs}
%package doc
Summary: Qt API Documentation in HTML and QCH format
%description doc
%{summary}.
%endif


%prep
%autosetup -p1 -n pyside-setup-everywhere-src-%{qt6ver}
# https://build.opensuse.org/package/view_file/KDE:Qt6/python3-pyside6/python3-pyside6.spec?expand=1
# Restore 6.6.1 RPATH value. rpmlint will complain otherwise
sed -i 's#${base}/../shiboken6/##' sources/pyside6/CMakeLists.txt

%if 0%{?docs}
# Generate documentation, requires qtbase sources as parameter
# sphinx-build output accepts several options of the format, default is html, use qthelp which calls qhelpgenerator for qch file generation
tar xf %{SOURCE1}
%endif

%build
# Compile generated C++ with GCC. The %%toolchain macro is not always wired into
# upstream CMake, so set CC/CXX explicitly (clang was producing -Wcast-function-type noise).
export CC=%{_bindir}/gcc
export CXX=%{_bindir}/g++
# %%_lto_cflags is only part of the picture. Default %%{build_*flags} still carry
# -flto=auto, and LTO plus Qt CMake -isystem wiring breaks #include_next from
# libstdc++ cstddef to the compiler stddef.h. Strip LTO and force the gcc fixed-
# header dir into both the environment and the CMake cache (Ninja ignores fresh
# CXXFLAGS after configure unless the cache carries them).
_gcc_incdir="$(%{_bindir}/gcc -print-file-name=include)"
export CFLAGS="%{build_cflags}"
export CXXFLAGS="%{build_cxxflags}"
export LDFLAGS="%{build_ldflags}"
CFLAGS="${CFLAGS//-flto=auto/}"; CFLAGS="${CFLAGS//-ffat-lto-objects/}"
CXXFLAGS="${CXXFLAGS//-flto=auto/}"; CXXFLAGS="${CXXFLAGS//-ffat-lto-objects/}"
LDFLAGS="${LDFLAGS//-flto=auto/}"; LDFLAGS="${LDFLAGS//-ffat-lto-objects/}"
_incfix="-I${_gcc_incdir} -idirafter ${_gcc_incdir}"
export CFLAGS="${_incfix} ${CFLAGS}"
export CXXFLAGS="${_incfix} ${CXXFLAGS}"
export C_INCLUDE_PATH="${_gcc_incdir}${C_INCLUDE_PATH:+:${C_INCLUDE_PATH}}"
export CPLUS_INCLUDE_PATH="${_gcc_incdir}${CPLUS_INCLUDE_PATH:+:${CPLUS_INCLUDE_PATH}}"
export CMAKE_BUILD_PARALLEL_LEVEL=1
export NINJAFLAGS="-j1"
mkdir -p "$(pwd)/tmp-pyside6-build"
export TMPDIR="$(pwd)/tmp-pyside6-build"

# https://src.fedoraproject.org/rpms/polyclipping/c/02c70e17ef9e9fcdfbc65021418a3e332e465b20?branch=rawhide
# Prior to Fedora 43, %%cmake set the nonstandard -DLIB_SUFFIX=... variable.
# cmake %["%{?_lib}" == "lib64" ? "-DLIB_SUFFIX=64" : ""]
%cmake_qt6 %["%{?_lib}" == "lib64" ? "-DLIB_SUFFIX=64" : ""] \
    -DCMAKE_C_COMPILER:FILEPATH=%{_bindir}/gcc \
    -DCMAKE_CXX_COMPILER:FILEPATH=%{_bindir}/g++ \
    -DCMAKE_BUILD_TYPE=None \
    -DSHIBOKEN_PYTHON_LIBRARIES=`pkgconf python3-embed --libs` \
    -DBUILD_TESTS=OFF \
    -DCMAKE_BUILD_RPATH_USE_ORIGIN:BOOL=ON \
    -DCMAKE_SKIP_INSTALL_RPATH:BOOL=ON \
    -DFORCE_LIMITED_API=no \
%if 0%{?docs}
    -DBUILD_DOCS:BOOL=ON \
    -DQT_SRC_DIR= %{qt_module}-everywhere-src-%{qt6ver} \
    -DFULLDOCSBUILD:BOOL=ON \
    -DDOC_OUTPUT_FORMAT=qthelp \
%endif
    -DNO_QT_TOOLS=yes \
    -DCMAKE_C_FLAGS:STRING="${CFLAGS}" \
    -DCMAKE_CXX_FLAGS:STRING="${CXXFLAGS}" \
    -DCMAKE_EXE_LINKER_FLAGS:STRING="${LDFLAGS}" \
    -DCMAKE_MODULE_LINKER_FLAGS:STRING="${LDFLAGS}" \
    -DCMAKE_SHARED_LINKER_FLAGS:STRING="${LDFLAGS}"

# Generate a build_history entry (for tests) manually, since we're performing
# a cmake build.
TODAY=$(date -Id)
mkdir build_history/$TODAY
echo $PWD/%{__cmake_builddir}/sources > build_history/$TODAY/build_dir.txt
export PYTHONPATH=$PWD/%{__cmake_builddir}/sources

%cmake_build
%if 0%{?docs}
# build api documentation
cd redhat-linux-build
ninja apidoc
%endif


%install
%cmake_install
%if 0%{?docs}
# install api documentation
cd redhat-linux-build
ninja apidocinstall
%endif

# Generate egg-info manually and install since we're performing a cmake build.
#
# Copy CMake configuration files from the BINARY dir back to the SOURCE dir so
# setuptools can find them.
cp %{__cmake_builddir}/sources/shiboken6/shibokenmodule/{*.py,*.txt} sources/shiboken6/shibokenmodule/
cp %{__cmake_builddir}/sources/pyside6/PySide6/*.py sources/pyside6/PySide6/
%{__python3} setup.py --qtpaths=/usr/%{_lib}/qt6/bin/qtpaths install_scripts --install-dir=%{buildroot}%{_bindir}
for name in PySide6 shiboken6 shiboken6_generator; do
  mkdir -p %{buildroot}%{python3_sitearch}/$name-%{version}-py%{python3_version}.egg-info
  cp -p $name.egg-info/{PKG-INFO,top_level.txt} \
        %{buildroot}%{python3_sitearch}/$name-%{version}-py%{python3_version}.egg-info/
  if [ -f $name.egg-info/entry_points.txt ]; then
    cp -p $name.egg-info/entry_points.txt %{buildroot}%{python3_sitearch}/$name-%{version}-py%{python3_version}.egg-info/
  fi
done

# Add symlinks for tools used by pyside_tool.py
mkdir -p %{buildroot}%{python3_sitelib}/%{camel_name}/Qt/libexec
ln -sf /usr/%{_lib}/qt6/libexec/{qmlcachegen,qmlimportscanner,qmltyperegistrar,rcc,uic} %{buildroot}%{python3_sitelib}/%{camel_name}/Qt/libexec
ln -sf /usr/%{_lib}/qt6/bin/{assistant,balsam,balsamui,designer,linguist,lrelease,lupdate,qmlformat,qmllint,qmlls,qsb} %{buildroot}%{python3_sitelib}/%{camel_name}

# Create scripts folders (this basically replicates prepare_packages() in build_scripts/main.py)
mkdir -p %{buildroot}%{python3_sitelib}/%{camel_name}/scripts
mv %{buildroot}%{_bindir}/{android_deploy.py,deploy_lib,deploy.py,metaobjectdump.py,project_lib,project.py,pyside_tool.py,qml.py,qtpy2cpp_lib,qtpy2cpp.py,requirements-android.txt} %{buildroot}%{python3_sitelib}/%{camel_name}/scripts
mkdir -p %{buildroot}%{python3_sitelib}/shiboken6_generator/scripts
mv %{buildroot}%{_bindir}/shiboken_tool.py %{buildroot}%{python3_sitelib}/shiboken6_generator/scripts

# Install shiboken6
mv redhat-linux-build/sources/shiboken6/generator/shiboken6 %{buildroot}%{python3_sitelib}/shiboken6_generator

# Fix CMake config files to use correct absolute paths (OpenSUSE solution)
# The upstream build is designed for wheel installation with relative paths,
# but for system installation we need absolute paths
sed -i 's#/typesystems#/share/PySide6/typesystems#g' %{buildroot}%{_libdir}/cmake/PySide6/*.cmake
sed -i 's#/glue#/share/PySide6/glue#g' %{buildroot}%{_libdir}/cmake/PySide6/*.cmake

# Fix all Python shebangs recursively
# -p preserves timestamps
# -n prevents creating ~backup files
# -i specifies the interpreter for the shebang
# Need to list files that do not match ^[a-zA-Z0-9_]+\.py$ explicitly!
%py3_shebang_fix %{buildroot}%{python3_sitelib}/%{camel_name}/scripts
%py3_shebang_fix %{buildroot}%{python3_sitelib}/shiboken6_generator/scripts

%check
# Do basic import test (even without the test bcond)
export LD_LIBRARY_PATH="%{buildroot}%{_libdir}"
%py3_check_import PySide6
%py3_check_import shiboken6


%files -n python%{python3_pkgversion}-%{pypi_name}
%license LICENSES/*
%doc README.md
%{_libdir}/libpyside6*.so.6.10*
%{python3_sitelib}/%{camel_name}/
%{python3_sitearch}/%{camel_name}-%{version}-py%{python3_version}.egg-info/

%files -n python%{python3_pkgversion}-%{pypi_name}-devel
%{_datadir}/PySide6/
%{_includedir}/PySide6/
%{_libdir}/libpyside6*.so
%{_libdir}/libpyside6remoteobjects.a
%{_libdir}/cmake/PySide6*
%{_libdir}/pkgconfig/pyside6.pc

%files -n pyside6-tools
%doc README.pyside*
%license LICENSES/*
%{_bindir}/pyside*
%{_libdir}/qt6/plugins/designer/libPySidePlugin.so

%files -n shiboken6
%doc README.shiboken6-generator.md
%license LICENSES/*
%{_libdir}/cmake/Shiboken6Tools/*

%files -n python%{python3_pkgversion}-shiboken6
%doc README.shiboken6.md
%license LICENSES/*
%{_libdir}/libshiboken6*.so.6.10*
%{python3_sitelib}/shiboken6/
%{python3_sitearch}/shiboken6-%{version}-py%{python3_version}.egg-info/

%files -n python%{python3_pkgversion}-shiboken6-devel
%{_bindir}/shiboken6*
%{_includedir}/shiboken6/
%{_libdir}/cmake/Shiboken6/
%{_libdir}/libshiboken6*.so
%{_libdir}/pkgconfig/shiboken6.pc
%{python3_sitelib}/shiboken6_generator/
%{python3_sitearch}/shiboken6_generator-%{version}-py%{python3_version}.egg-info/

%if 0%{?docs}
%files doc
%{_docdir}/
%endif

%changelog
* Fri Apr 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.10.3-9
- Vendor Rawhide patches in SRPM, BR qt6-qtgraphs-devel + qt6-qthttpserver-devel + xwayland-run

* Fri Apr 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.10.3-7
- Strip -flto from compile and link flags, pin GCC include dir on flags and CPLUS_INCLUDE_PATH, pass CMAKE_LANG_FLAGS and linker flags so Ninja gets cstddef working past Qt -isystem

* Thu Apr 16 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.10.3-6
- Append -idirafter GCC internal include so cstddef include_next finds stddef.h with Qt -isystem-heavy compile lines

* Wed Apr 15 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.10.3-5
- BuildRequires gcc-c++, export %%{build_cflags}/%%{build_cxxflags}, force CMAKE_C_CXX_COMPILER paths so cstddef finds gcc stddef.h in mock

* Wed Apr 15 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.10.3-4
- %%_lto_cflags nil, %%_smp_mflags -j1, NINJAFLAGS and CMAKE_BUILD_PARALLEL_LEVEL, TMPDIR under build for mock ninja reliability

* Thu Apr 09 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.10.3-3
- Build generated bindings with GCC (export CC/CXX) to avoid clang cast-function-type spam

* Thu Apr 09 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.10.3-2
- Reword commented Source1 note so rpmspec does not expand macros inside a comment

* Thu Apr 09 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.10.3-1
- Import Fedora rawhide python-pyside6 6.10.3-1, HTTPS Source0, Fedora patch URLs
