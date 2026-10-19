%global source0_hash 8b852bb5aa6e7d8564f9e81394055395dd1d1936d38dfd3a17792a02bebd7af0
Name:           fmt
Version:        12.2.0
Release:        1%{?dist}
License:        MIT
Summary:        Small, safe and fast formatting library for C++
URL:            https://github.com/fmtlib/%{name}
Source0:        https://github.com/fmtlib/fmt/archive/refs/tags/%{version}.tar.gz#/fmt-%{version}.tar.gz
Provides:       cppformat = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      cppformat < %{?epoch:%{epoch}:}%{version}-%{release}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
# /oreon:deps
%description
C++ Format is an open-source formatting library for C++. It can be used as a
safe alternative to printf or as a fast alternative to IOStreams.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       %{name}-static = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       cppformat-devel = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      cppformat-devel < %{?epoch:%{epoch}:}%{version}-%{release}
%description    devel
This package contains the header file for using %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake -G Ninja \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DCMAKE_POSITION_INDEPENDENT_CODE:BOOL=ON \
    -DFMT_CMAKE_DIR:STRING=%{_libdir}/cmake/%{name} \
    -DFMT_LIB_DIR:STRING=%{_libdir}
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%ctest
%files -f %{oreon_filedir}/main.list
%files -n fmt-devel -f %{oreon_filedir}/fmt-devel.list

%changelog

%autochangelog
