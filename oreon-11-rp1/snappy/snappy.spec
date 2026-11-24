# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 90f74bc1fbf78a6c56b3c4a082a05103b3a56bb17bca1a27e052ea11723292dc
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%bcond gbench %[ !0%{?rhel} ]
%bcond gtest %[ !0%{?rhel} ]

Name:           snappy
Version:        1.2.2
Release:        1%{?dist}
Summary:        Fast compression and decompression library

License:        BSD-3-Clause
URL:            https://github.com/google/snappy
Source0:        https://github.com/google/snappy/releases/download/%{version}/%{name}-%{version}.tar.gz

Patch0:         %{name}-thirdparty.patch

Patch1:         %{name}-do-not-disable-rtti.patch

BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc-c++
BuildRequires:  cmake
%{?with_gbench:BuildRequires:  google-benchmark-devel}
%{?with_gtest:BuildRequires:  gtest-devel}

%description
Snappy is a compression/decompression library. It does not aim for maximum 
compression, or compatibility with any other compression library; instead, it 
aims for very high speeds and reasonable compression. For instance, compared to 
the fastest mode of zlib, Snappy is an order of magnitude faster for most 
inputs, but the resulting compressed files are anywhere from 20% to 100% 
bigger. 

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%oreon_sha256
%autosetup

%build
%cmake -DCMAKE_CXX_STANDARD=17 %{!?with_gbench:-DSNAPPY_BUILD_BENCHMARKS=OFF} %{!?with_gtest:-DSNAPPY_BUILD_TESTS=OFF}
%cmake_build

cat << EOF >snappy.pc
prefix=%{_prefix}
exec_prefix=%{_exec_prefix}
includedir=%{_includedir}
libdir=%{_libdir}

Name: %{name}
Description: A fast compression/decompression library
Version: %{version}
Cflags: -I\${includedir}
Libs: -L\${libdir} -lsnappy
EOF

%install
rm -rf %{buildroot}
chmod 644 *.txt AUTHORS COPYING NEWS README.md
%cmake_install
install -m644 -D snappy.pc %{buildroot}%{_libdir}/pkgconfig/snappy.pc
rm -rf %{buildroot}%{_datadir}/doc/snappy/
rm -rf %{buildroot}%{_datadir}/doc/snappy-devel/

%check
%ctest

%ldconfig_scriptlets

%files
%license COPYING
%doc AUTHORS NEWS README.md
%{_libdir}/libsnappy.so.*

%files devel
%doc format_description.txt framing_format.txt
%{_includedir}/snappy*.h
%{_libdir}/libsnappy.so
%{_libdir}/pkgconfig/snappy.pc
%{_libdir}/cmake/Snappy/

%changelog
%autochangelog
