%global source0_hash 956e6e2cc822c63af4c323bf86464f1186171314e67e9c5153f58bd875538470
Name:          openapv
Release:        1%{?dist}
Version:       1.1.1.0
Summary:        Open Advanced Professional Video Codec
License:       BSD-3-Clause
URL:           https://github.com/AcademySoftwareFoundation/openapv
Source0:        https://github.com/AcademySoftwareFoundation/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:        %{name}-fix-md5-hash-mismatch-on-big-endian.patch
Patch1:        %{name}-version.patch
Requires:      %{name}-libs%{?_isa} = %{version}-%{release}
%global somaj %{lua:t={} for f in string.gmatch(macros['version'], "([^.]*)(.?)") do table.insert(t,f) end print(t[2])}
%global sover %{lua:t={} for f in string.gmatch(macros['version'], "([^.]*)(.?)") do table.insert(t,f) end print(string.format("%s.%s.%s",t[2],t[3],t[4]))}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  ninja-build
# /oreon:deps
%description
OpenAPV provides the reference implementation of the APV codec which can
be used to record professional-grade video and associated metadata
without quality degradation.

%package  devel
Summary:  Development files for %{name}
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
%description devel
The openapv-devel package contains the header files needed
to develop programs that use openapv.

%package libs
Summary: Shared libraries for openapv
%description libs
The openapv-libs package contains the shared library files

%prep
%oreon_prep
%build

%cmake \
        -G Ninja \
        -DCMAKE_BUILD_TYPE=RelWithDebInfo \
        -DCMAKE_SKIP_INSTALL_RPATH=ON \
        -DOAPV_APP_STATIC_BUILD=OFF
%cmake_build
%install
%cmake_install
rm -v %{buildroot}%{_libdir}/oapv/liboapv.a
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%ctest
%files -f %{oreon_filedir}/main.list
%files -n openapv-devel -f %{oreon_filedir}/openapv-devel.list
%files -n openapv-libs -f %{oreon_filedir}/openapv-libs.list

%changelog

%autochangelog
