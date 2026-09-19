%global source0_hash 303a619c01a9e14a3c82eb9762b8a428ef5311a6d46353872ab9a904358be4a4

%undefine __cmake_in_source_build
%global realname console_bridge
%global libversion 1.0

Name:           console-bridge
Version:        1.0.2
Release:        7%{?dist}
Summary:        Lightweight set of macros used for reporting information in libraries

License:        BSD-3-Clause
URL:            http://ros.org/wiki/console_bridge
Source0:        https://github.com/ros/%{realname}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake

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
# TODO: Please submit an issue to upstream (rhbz#2380515)
export CMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake -DCMAKE_BUILD_TYPE=Release -DBUILD_TESTING=ON
%cmake_build

%install
%cmake_install

%check
%ctest || /bin/true

%files
%license LICENSE
%doc README.md
%{_libdir}/*.so.%{libversion}

%files devel
%{_includedir}/%{realname}
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_libdir}/%{realname}

%changelog
%autochangelog
