%global source0_hash 5d720a204c2a58645d6f7643af15d563a712dad98c9d32c1ed913377daa6ac39
Name:           czmq
Version:        4.2.1
Release:        1%{?dist}
Summary:        High-level C binding for 0MQ (ZeroMQ)
License:        MPL-2.0
URL:            http://czmq.zeromq.org
Source0:        https://github.com/zeromq/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  asciidoc
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libuuid-devel
BuildRequires:  perl(File::Basename)
BuildRequires:  perl-interpreter
BuildRequires:  pkgconfig(libzmq)
BuildRequires:  xmlto
# /oreon:deps
%description
CZMQ has the following goals:
  i) To wrap the ZeroMQ core API in semantics that are natural and lead to
     shorter, more readable applications.
 ii) To hide the differences between versions of ZeroMQ.
iii) To provide a space for development of more sophisticated API semantics.

%package devel
Summary:        Development files for the czmq package
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
This package contains files needed to develop applications using czmq.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure --with-docs
%make_build
%cmake -DCZMQ_BUILD_STATIC:BOOL=OFF
%cmake_build
%install
%make_install install-dist_apiDATA
rm -f %{buildroot}%{_libdir}/libczmq.{a,la}
%cmake_install
%oreon_autofiles czmq-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%files -f %{oreon_filedir}/main.list
%files -n czmq-devel -f %{oreon_filedir}/czmq-devel.list

%changelog

%autochangelog
