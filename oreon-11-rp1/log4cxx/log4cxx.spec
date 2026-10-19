%global source0_hash 6a2e40dfa6b81a9a814ef2083d181b254f88324efff678368e5e61188a58fd3d
%global sover 15
Name: log4cxx
Version: 1.8.0
Release:        1%{?dist}
Summary:        A port to C++ of the Log4j project
License: Apache-2.0
URL: http://logging.apache.org/log4cxx/index.html
Source0:        http://www.apache.org/dist/logging/log4cxx/%{version}/apache-%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  apr-devel
BuildRequires:  apr-util-devel
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  openldap-devel
# /oreon:deps
%description
Log4cxx is a popular logging package written in C++. One of its distinctive
features is the notion of inheritance in loggers. Using a logger hierarchy it
is possible to control which log statements are output at arbitrary
granularity. This helps reduce the volume of logged output and minimize the
cost of logging.

%package devel
Requires: %{name}%{?_isa} = %{version}-%{release}
Summary: Header files for Log4xcc - a port to C++ of the Log4j project
%description devel
Header files and documentation you can use to develop with %{name}.

%package doc
Summary: Documentation for %{name}
BuildArch: noarch
%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir apache-%{name}-%{version}
%oreon_prep
%build

%cmake -DBUILD_SITE=ON
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%ctest
%files -f %{oreon_filedir}/main.list
%files -n log4cxx-devel -f %{oreon_filedir}/log4cxx-devel.list
%files -n log4cxx-doc -f %{oreon_filedir}/log4cxx-doc.list

%changelog

%autochangelog
