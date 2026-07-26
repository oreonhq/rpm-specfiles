%global source0_hash 0a9670ff384d4dc8cabc8a48a46d5bf4d3433a4fd32ae55aebb6a74d7ce37742

# Commit corresponding to release 2.14.1
%global commit c9dc01f16be159a809d73ea54c8f6cf31a735812
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           cppmyth
Version:        2.17.6
Release:        5%{?dist}
Summary:        Client interface for the MythTV backend

License:        GPL-2.0-or-later
URL:            https://github.com/janbar/%{name}/
Source0:        %{url}/archive/%{shortcommit}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(zlib)

%description
This project is intended to create a easy client interface for the MythTV
backend. Its development started from January 2014 and today the API supports
the protocol version of MythTV 0.26 to 0.29.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for developing
applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{commit}

%build
%cmake -DCMAKE_INSTALL_LIBDIR=%{_lib} -DCMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake_build

%install
%cmake_install

%files
%doc README
%{_libdir}/*.so.*

%files devel
%{_includedir}/%{name}/
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
%autochangelog
