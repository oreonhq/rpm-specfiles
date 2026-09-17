%global source0_hash 187c85836f5b2f27fb1e8d77c7f1f2939725f1f6498b742b0dd569ba30965fd2

%global sover 15

Name: log4cxx
Version: 1.6.1
Release: %autorelease
Summary: A port to C++ of the Log4j project

License: Apache-2.0
URL: http://logging.apache.org/log4cxx/index.html
Source0: http://www.apache.org/dist/logging/log4cxx/%{version}/apache-%{name}-%{version}.tar.gz

BuildRequires: apr-devel
BuildRequires: apr-util-devel
BuildRequires: cmake
BuildRequires: doxygen
BuildRequires: gcc-c++
BuildRequires: openldap-devel

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

%autosetup -n apache-%{name}-%{version}

%build
%cmake -DBUILD_SITE=ON
%cmake_build

%install
%cmake_install

%check
%ctest

%files
%{_libdir}/liblog4cxx.so.%{sover}*

%doc NOTICE
%license LICENSE

%files devel
%{_includedir}/log4cxx
%{_libdir}/liblog4cxx.so
%{_libdir}/pkgconfig/liblog4cxx.pc
%{_libdir}/cmake/log4cxx

%files doc
%license LICENSE
%doc %{_vpath_builddir}/src/site/html/

%changelog
%autochangelog
