%global source0_hash 303a619c01a9e14a3c82eb9762b8a428ef5311a6d46353872ab9a904358be4a4
%undefine __cmake_in_source_build
%global realname console_bridge
%global libversion 1.0
Name:           console-bridge
Version:        1.0.2
Release:        1%{?dist}
Summary:        Lightweight set of macros used for reporting information in libraries
License:        BSD-3-Clause
URL:            http://ros.org/wiki/console_bridge
Source0:        https://github.com/ros/%{realname}/archive/%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
# /oreon:deps
%description
A very lightweight set of macros that can be used for reporting information 
in libraries. The logged information can be forwarded to other systems.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{realname}-%{version}

%build

export CMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake -DCMAKE_BUILD_TYPE=Release -DBUILD_TESTING=ON
%cmake_build
%install
%cmake_install
%oreon_autofiles console-bridge-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%ctest || /bin/true
%files -f %{oreon_filedir}/main.list
%files -n console-bridge-devel -f %{oreon_filedir}/console-bridge-devel.list

%changelog

%autochangelog
