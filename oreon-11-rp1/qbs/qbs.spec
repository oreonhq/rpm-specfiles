%global source0_hash 5d8b58a5fb60c83a311331aa10d90536e4d4cb28d5078d3554edd807a5af9a8f
%if 0%{?commit:1}
%global source_folder %{name}-%{commit}
%else
%global source_folder %{name}-src-%{version}
%endif
Name:           qbs
Epoch:          1
Version:        3.3.1
Release:        1%{?dist}
Summary:        Cross platform build tool
ExcludeArch:    i686
License:        LGPL-3.0-only AND GPL-2.0-only AND LGPL-2.1-only WITH Qt-LGPL-exception-1.1 AND LGPL-3.0-only AND GPL-3.0-only WITH QT-GPL-exception-1.0
URL:            https://wiki.qt.io/qbs
%if 0%{?commit:1}
Source0:        https://download.qt.io/official_releases/%{name}/%{version}/%{name}-src-%{version}.tar.gz
%else
%endif
Patch0:         qbs-fix-build-against-qt-6-10.patch
Patch1:         qbs-fix-build.patch
%ifarch x86_64
%endif
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Core5Compat)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6Tools)
BuildRequires:  cmake(Qt6ToolsTools)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Xml)
BuildRequires:  gcc-c++
BuildRequires:  glibc-static
BuildRequires:  libstdc++-static
BuildRequires:  make
BuildRequires:  ninja-build
BuildRequires:  python3-beautifulsoup4
BuildRequires:  python3-lxml
BuildRequires:  qt6-qtbase-private-devel
# /oreon:deps
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
License:        BSD-3-Clause
Requires:       %{name} = %{epoch}:%{version}-%{release}
BuildArch:      noarch
%description    examples
The %{name}-examples package contains example files for using %{name}.

%package        doc
Summary:        Developer Documentation files for %{name}
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
rm -rf %{buildroot}%{_datadir}/qbs/python/mac_alias/
rm -rf %{buildroot}%{_datadir}/qbs/python/ds_store/
rm -rf %{buildroot}%{_datadir}/qbs/python/dmgbuild/
rm -rf %{buildroot}%{_datadir}/qbs/python/biplist/
rmdir %{buildroot}%{_datadir}/qbs/python/
rm -f %{buildroot}%{_libexecdir}/qbs/dmgbuild
rm %{buildroot}%{_bindir}/tst_*
rm %{buildroot}%{_bindir}/clang-format-test
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%ctest || :
%files -f %{oreon_filedir}/main.list
%files -n qbs-devel -f %{oreon_filedir}/qbs-devel.list
%files -n qbs-examples -f %{oreon_filedir}/qbs-examples.list
%files -n qbs-doc -f %{oreon_filedir}/qbs-doc.list

%changelog

%autochangelog
