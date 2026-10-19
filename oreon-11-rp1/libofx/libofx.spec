%global source0_hash ea9fa07759622ecc7f25b637fa8fb34d587af80607ca4389d25966a6a4f94ab9
Summary:        A library for supporting Open Financial Exchange (OFX)
Name: libofx
Version: 0.10.9
Release:        9%{?dist}
URL: https://github.com/libofx/libofx
License: GPL-2.0-or-later
Source0:        https://github.com/%{name}/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Patch0: fix-ftbfs-gcc4.7.diff
# oreon:deps
BuildRequires:  cmake
BuildRequires:  curl-devel
BuildRequires:  gcc-c++
BuildRequires:  libxml++-devel
BuildRequires:  make
BuildRequires:  opensp-devel
# /oreon:deps
%description
This is the LibOFX library.  It is a API designed to allow applications to
very easily support OFX command responses, usually provided by financial
institutions.  See http://www.ofx.net/ofx/default.asp for details and
specification. 

%package -n ofx
Summary: Tools for manipulating OFX data
Requires: %{name}%{?_isa} = %{version}-%{release}
%description -n ofx
The ofx package contains tools for manipulating OFX data from the
command line; they are often used when testing libofx.

%package devel
Summary: Development files needed for accessing OFX data
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
The libofx-devel contains the header files and libraries necessary
for building applications that use libofx.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1 -b .gcc47

chmod 644 ./doc/ofx_sample_files/*

%build

export CXXFLAGS="$CXXFLAGS -std=c++17"
%cmake -DCMAKE_INSTALL_LIBDIR=%{_lib}
%cmake_build
%install
%cmake_install
rm -rf $RPM_BUILD_ROOT%{_libdir}/lib*.la $RPM_BUILD_ROOT%{_datadir}/doc
%ldconfig_scriptlets
%oreon_autofiles ofx usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n ofx -f %{oreon_filedir}/ofx.list
%files -n libofx-devel -f %{oreon_filedir}/libofx-devel.list

%changelog

%autochangelog
