%global source0_hash 893f708a0bf4b5529d555ffcee390e940e932fcf90261f682604475a76cd0247
%bcond gbench %[ !0%{?rhel} ]
%bcond gtest %[ !0%{?rhel} ]
Name:           snappy
Version:        1.3.1
Release:        1%{?dist}
Summary:        Fast compression and decompression library
License:        BSD-3-Clause
URL:            https://github.com/google/snappy
Source0:        https://github.com/google/snappy/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:         %{name}-thirdparty.patch
Patch1:         %{name}-do-not-disable-rtti.patch
%{?with_gbench:BuildRequires:  google-benchmark-devel}
%{?with_gtest:BuildRequires:  gtest-devel}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  google-benchmark-devel
BuildRequires:  gtest-devel
# /oreon:deps
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
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
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
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%ctest
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n snappy-devel -f %{oreon_filedir}/snappy-devel.list

%changelog

%autochangelog
