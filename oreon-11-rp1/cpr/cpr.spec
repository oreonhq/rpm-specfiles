%global source0_hash b9b529b47083bfe80bba855ca5308d12d767ae7c7b629aef5ef018c4343cf62b
Name:           cpr
Version:        1.14.2
Release:        1%{?dist}
Summary:        C++ Requests: Curl for People, a spiritual port of Python Requests
License:        MIT
URL:            https://github.com/libcpr/cpr
Source0:        https://github.com/lib%{name}/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libcurl-devel
BuildRequires:  ninja-build
BuildRequires:  openssl-devel
# /oreon:deps
%description
C++ Requests is a simple wrapper around libcurl inspired by the excellent Python
Requests project.

Despite its name, libcurl's easy interface is anything but, and making mistakes,
misusing it is a common source of error and frustration. Using the more
expressive language facilities of C++17 (or C++11 in case you use cpr < 1.10.0),
this library captures the essence of making network calls into a few concise
idioms.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       libcurl-devel
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake -DCPR_USE_SYSTEM_CURL=ON
%cmake_build
%install
%cmake_install
%oreon_autofiles cpr-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n cpr-devel -f %{oreon_filedir}/cpr-devel.list

%changelog

%autochangelog
