%global source0_hash 6ad40e04e32e2677917de0dfc39891f8220552cf0e084e2ec21260228f73c560
Name: ctk
Version: 2026.09.02
%global soname_version 0.1
Release:        1%{?dist}
Summary:        The Commmon Toolkit for biomedical imaging
License: Apache-2.0
URL: https://commontk.org/
Source0:        https://github.com/commontk/CTK/archive/%{version}/CTK-%{version}.tar.gz
Patch: ctk-0.1.20171224git71799c2-fix_qreal_cast.patch
Patch: 0001-fix-for-dcmtk-3.6.9.patch
Obsoletes: ctk-doc < 0.1-45
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(dcmtk)
BuildRequires:  cmake(qt5multimedia)
BuildRequires:  cmake(qt5uitools)
BuildRequires:  cmake(qt5xmlpatterns)
BuildRequires:  cmake(qtconfiguration)
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
# /oreon:deps
%description

This package contains the CTK Core library.

%package dicom
Summary: Library of high-level classes for querying PACS and local databases
Requires: ctk%{?_isa} = %{version}-%{release}
Requires: ctk-widgets%{?_isa} = %{version}-%{release}
%description dicom

DICOM library provides high-level classes supporting query and retrieve
operations from PACS and local databases. It includes Qt widgets to easily
set-up a server connection and to send queries and view the results.

%package plugin-framework
Summary: A dynamic component system for C++
Requires: ctk%{?_isa} = %{version}-%{release}
%description plugin-framework

The Plugin Framework is a dynamic component system for C++, modeled after the
OSGi specifications. It enable a development model where applications are
(dynamically) composed of many different (reusable) components following a
service oriented approach.

%package widgets
Summary: A collection of Qt widgets for biomedical imaging applications
Requires: ctk%{?_isa} = %{version}-%{release}
%description widgets

The Widgets library is a collection of Qt widgets for usage in biomedical
imaging applications.

%package devel
Summary: Development files for the Common Toolkit
Requires: ctk%{?_isa} = %{version}-%{release}
Requires: ctk-dicom%{?_isa} = %{version}-%{release}
Requires: ctk-plugin-framework%{?_isa} = %{version}-%{release}
Requires: ctk-widgets%{?_isa} = %{version}-%{release}
Requires: dcmtk-devel%{?_isa}
Requires: qt5-qtbase-devel%{?_isa}
Requires: qt5-qtxmlpatterns-devel%{?_isa}
Requires: qt5-qtmultimedia-devel%{?_isa}
Requires: qt5-qttools-static%{?_isa}
%description devel

This package contains files for development of CTK applications.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n CTK-%{version} -p1

# Change EOL encoding
tr -d '\r' < README.md > README
mv -vf README README.md

# fix for cmake v4, which removes compatibility with cmake <3.5
for f in "Utilities/DGraph/CMakeLists.txt" "CMake/ctkCheckoutRepo.cmake.in" "CMake/ctkDashboardScript.TEMPLATE.cmake" "CMake/ctkMacroSetupQt.cmake" "CMakeLists.txt" "Libs/Core/CMake/TestBFD/CMakeLists.txt"
do
    echo "** ${f} **"
    grep -n "cmake_minimum_required" "${f}"
    sed -i 's/cmake_minimum_required(VERSION.*)/cmake_minimum_required(VERSION 3.10)/' "${f}"
    grep -n "cmake_minimum_required" "${f}"
done

%build

%cmake \
    -GNinja \
    -DCMAKE_PREFIX_PATH=%{_libdir}/cmake/InsightToolkit \
    -DCTK_SUPERBUILD=OFF \
    -DCTK_INSTALL_LIB_DIR=%{_libdir} \
    -DCTK_INSTALL_CMAKE_DIR=%{_libdir}/cmake/ctk \
    -DCTK_INSTALL_PLUGIN_DIR=%{_libdir}/ctk/plugins \
    -DCTK_INSTALL_QTPLUGIN_DIR=%{_qt5_plugindir} \
    -DCTK_ENABLE_DICOM=ON \
    -DCTK_ENABLE_PluginFramework=ON \
    -DCTK_ENABLE_Widgets=ON \
    -DDOCUMENTATION_TARGET_IN_ALL=OFF \
    -DBUILD_TESTING:BOOL=OFF
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
