# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 3a289eded586c26d06c1387de72c7bf7c809527a70d51ba6401fe61059b19626

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap
%global libso_major 2

Name:           sdbus-cpp
Version:        2.3.1
Release:        1%{?dist}
Summary:        High-level C++ D-Bus library

License:        LGPL-2.1-only
URL:            https://github.com/Kistler-Group/sdbus-cpp
Source0:        https://github.com/Kistler-Group/sdbus-cpp/archive/v%{version}/sdbus-cpp-%{version}.tar.gz

BuildRequires:  cmake >= 3.14
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(libsystemd) >= 238
BuildRequires:  pkgconfig(gmock) >= 1.10.0

%description
High-level C++ D-Bus library for Linux designed to provide easy-to-use
yet powerful API in modern C++


%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for %{name}.


%package devel-doc
Summary:        Developer documentation for %{name}
BuildArch:      noarch
BuildRequires:  doxygen
Requires:       %{name}-devel = %{version}-%{release}

%description devel-doc
Developer documentation for %{name}


%package tools
Summary:        Stub code generator for sdbus-c++
Requires:       %{name}%{?_isa} = %{version}-%{release}
BuildRequires:  pkgconfig(expat)
BuildRequires:  oreon-rpm-macros
Obsoletes:      %{name}-xml2cpp < %{version}-%{release}

%description tools
The stub code generator for generating the adapter and proxy interfaces
out of the D-Bus IDL XML description.


%package tests
Summary:        Tests for %{name}
Requires:       %{name}

%description tests
%{summary}


%prep
%oreon_sha256

%autosetup -p1


%build
%cmake \
    -DCMAKE_BUILD_TYPE=Release \
    -DSDBUSCPP_BUILD_CODEGEN=ON \
    -DSDBUSCPP_BUILD_DOCS=ON \
    -DSDBUSCPP_BUILD_DOXYGEN_DOCS=ON \
    -DSDBUSCPP_BUILD_TESTS=ON \
    -DSDBUSCPP_TESTS_INSTALL_PATH=%{_libexecdir}/installed-tests/
%cmake_build
%cmake_build --target doc


%check
%ctest -E "sdbus-c\+\+-integration-tests"


%install
%cmake_install
mkdir -p %{buildroot}%{_datadir}/dbus-1/system.d/
mv %{buildroot}%{_sysconfdir}/dbus-1/system.d/org.sdbuscpp.integrationtests.conf %{buildroot}%{_datadir}/dbus-1/system.d/
rm -rf %{buildroot}%{_sysconfdir}
rm %{buildroot}%{_docdir}/sdbus-c++/COPYING


%files
%license COPYING
%license COPYING-LGPL-Exception
%dir %{_docdir}/sdbus-c++
%doc %{_docdir}/sdbus-c++/AUTHORS
%doc %{_docdir}/sdbus-c++/ChangeLog
%doc %{_docdir}/sdbus-c++/NEWS
%doc %{_docdir}/sdbus-c++/README.md
%{_libdir}/libsdbus-c++.so.%{libso_major}{,.*}


%files devel
%license COPYING
%license COPYING-LGPL-Exception
%{_libdir}/pkgconfig/sdbus-c++.pc
%{_libdir}/pkgconfig/sdbus-c++-tools.pc
%{_libdir}/libsdbus-c++.so
%{_includedir}/sdbus-c++/
%dir %{_libdir}/cmake/sdbus-c++
%{_libdir}/cmake/sdbus-c++/*.cmake


%files devel-doc
%license COPYING
%license COPYING-LGPL-Exception
%doc %{_docdir}/sdbus-c++/*
%exclude %{_docdir}/sdbus-c++/AUTHORS
%exclude %{_docdir}/sdbus-c++/ChangeLog
%exclude %{_docdir}/sdbus-c++/NEWS
%exclude %{_docdir}/sdbus-c++/README.md


%files tools
%license COPYING
%license COPYING-LGPL-Exception
%{_bindir}/sdbus-c++-xml2cpp
%dir %{_libdir}/cmake/sdbus-c++-tools
%{_libdir}/cmake/sdbus-c++-tools/*.cmake


%files tests
%license COPYING
%license COPYING-LGPL-Exception
%{_datadir}/dbus-1/system.d/org.sdbuscpp.integrationtests.conf
%{_libexecdir}/installed-tests/sdbus*


