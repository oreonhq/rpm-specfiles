%global source0_hash cb0a70eb33bee5a0122df3e6856b1b98d9b00c6f175f55cbb3442bbc9cc2cd6f

#global commit 40746dae36452398649481fecad9cdc5f25cc80f
#global shortcommit %(c=%{commit}; echo ${c:0:7})

%if 0%{?commit:1}
%global source_folder %{name}-%{commit}
%else
%global source_folder %{name}-src-%{version}
%endif

Name:           qbs
# qbs was previously packaged as part of qt-creator, using the qt-creator version, hence the epoch bump
Epoch:          1
Version:        3.1.2
Release:        2%{?dist}
Summary:        Cross platform build tool
# Fails to build on i686
ExcludeArch:    i686

# See https://doc.qt.io/qbs/attributions.html
# -docs and -examples have a separate license tag
#               (    Qbs library and tools   )     (                  Shared functionality                  )     (               tests                )
License:        LGPL-3.0-only AND GPL-2.0-only AND LGPL-2.1-only WITH Qt-LGPL-exception-1.1 AND LGPL-3.0-only AND GPL-3.0-only WITH QT-GPL-exception-1.0
URL:            https://wiki.qt.io/qbs
%if 0%{?commit:1}
Source0:        https://code.qt.io/cgit/qbs/qbs.git/snapshot/qbs-%{commit}.tar.xz
%else
Source0:        https://download.qt.io/official_releases/%{name}/%{version}/%{name}-src-%{version}.tar.gz
%endif

Patch0:         qbs-fix-build-against-qt-6-10.patch
Patch1:         qbs-fix-build.patch

BuildRequires:  cmake
BuildRequires:  ninja-build
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Xml)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6Core5Compat)
BuildRequires:  cmake(Qt6Tools)
BuildRequires:  cmake(Qt6ToolsTools)
BuildRequires:  qt6-qtbase-private-devel

BuildRequires:  python3-lxml
BuildRequires:  python3-beautifulsoup4

# Needed for tests
BuildRequires:  glibc-static
%ifarch x86_64
BuildRequires:  libasan
BuildRequires:  libtsan
%endif
BuildRequires:  libstdc++-static

%description
Qbs is a tool that helps simplify the build process for developing projects
across multiple platforms. Qbs can be used for any software project, regardless
of programming language, toolkit, or libraries used.

Qbs is an all-in-one tool that generates a build graph from a high-level
project description (like qmake or CMake) and additionally undertakes the task
of executing the commands in the low-level build graph (like make).

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        examples
Summary:        Example projects using %{name}
# Automatically converted from old format: BSD-3-Clause - review is highly recommended.
License:        BSD-3-Clause
Requires:       %{name} = %{epoch}:%{version}-%{release}
BuildArch:      noarch

%description    examples
The %{name}-examples package contains example files for using %{name}.

%package        doc
Summary:        Developer Documentation files for %{name}
# Automatically converted from old format: GFDL - review is highly recommended.
License:        LicenseRef-Callaway-GFDL
BuildArch:      noarch

%description    doc
Developer Documentation files for %{name} for use with KDevelop or QtCreator.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{source_folder}

%build
%cmake_qt6 \
    -DQBS_LIB_INSTALL_DIR=%{_libdir} \
    -DQBS_PLUGINS_INSTALL_BASE=%{_lib} \
    -DWITH_UNIT_TESTS=ON \
    -DQBS_ENABLE_RPATH=OFF \
    -DQBS_INSTALL_QCH_DOCS=ON \
    -DQBS_DOC_INSTALL_DIR=%{_qt6_docdir}
%cmake_build

%install
%cmake_install
install -Dpm 0644 doc/man/qbs.1 %{buildroot}%{_mandir}/man1/qbs.1

# Remove python dmgbuild code, it only works on macOS (#1559529)
rm -rf %{buildroot}%{_datadir}/qbs/python/mac_alias/
rm -rf %{buildroot}%{_datadir}/qbs/python/ds_store/
rm -rf %{buildroot}%{_datadir}/qbs/python/dmgbuild/
rm -rf %{buildroot}%{_datadir}/qbs/python/biplist/
rmdir %{buildroot}%{_datadir}/qbs/python/
rm -f %{buildroot}%{_libexecdir}/qbs/dmgbuild

# Don't package tests
rm %{buildroot}%{_bindir}/tst_*
rm %{buildroot}%{_bindir}/clang-format-test

%check
%ctest || :

%files
%license LICENSE.LGPLv21 LICENSE.LGPLv3 LGPL_EXCEPTION.txt
%doc README.md
%{_bindir}/%{name}*
%{_libdir}/%{name}/
%{_libdir}/libqbs*.so.3.1*
%{_libexecdir}/qbs/
%{_datadir}/%{name}/
%{_mandir}/man1/%{name}.1*
%exclude %{_datadir}/%{name}/examples

%files devel
%{_includedir}/%{name}/
%{_libdir}/libqbs*.so

%files examples
%{_datadir}/%{name}/examples/

%files doc
%{_qt6_docdir}/qbs.qch

%changelog
%autochangelog
