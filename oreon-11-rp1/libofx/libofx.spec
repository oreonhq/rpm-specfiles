%global source0_hash ea9fa07759622ecc7f25b637fa8fb34d587af80607ca4389d25966a6a4f94ab9

Summary: A library for supporting Open Financial Exchange (OFX)
Name: libofx
Version: 0.10.9
Release: 9%{?dist}
URL: https://github.com/libofx/libofx
License: GPL-2.0-or-later
Source: %{url}/archive/%{version}/%{name}-%{version}.tar.gz
Patch0: fix-ftbfs-gcc4.7.diff
BuildRequires: gcc-c++
BuildRequires: opensp-devel
BuildRequires: curl-devel
BuildRequires: libxml++-devel
BuildRequires: make
BuildRequires: cmake

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

%files
%doc AUTHORS COPYING ChangeLog NEWS README totest.txt
%{_libdir}/libofx.so.7*
%{_datadir}/libofx/

%files -n ofx
%{_bindir}/ofx*

%files devel
%doc doc/ofx_sample_files
%{_includedir}/libofx/
%{_libdir}/pkgconfig/libofx.pc
%{_libdir}/libofx.so
%{_libdir}/cmake/%{name}/

%changelog
%autochangelog
