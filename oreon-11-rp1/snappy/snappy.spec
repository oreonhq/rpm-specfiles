%global source0_hash 90f74bc1fbf78a6c56b3c4a082a05103b3a56bb17bca1a27e052ea11723292dc

# Drop google-benchmark, gtest on RHEL
%bcond gbench %[ !0%{?rhel} ]
%bcond gtest %[ !0%{?rhel} ]

Name:           snappy
Version:        1.2.2
Release:        6%{?dist}
Summary:        Fast compression and decompression library

License:        BSD-3-Clause
URL:            https://github.com/google/snappy
Source0:        https://github.com/google/snappy/archive/refs/tags/%{version}/%{name}-%{version}.tar.gz

# Remove dependency on bundled gtest and google-benchmark.
Patch0:         %{name}-thirdparty.patch

# Do not forcibly disable RTTI
Patch1:         %{name}-do-not-disable-rtti.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++
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
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup


%build
# gtest 1.17.0 requires C++17 or later
%cmake -DCMAKE_CXX_STANDARD=17 %{!?with_gbench:-DSNAPPY_BUILD_BENCHMARKS=OFF} %{!?with_gtest:-DSNAPPY_BUILD_TESTS=OFF}
%cmake_build

# create pkgconfig file
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
* Mon Apr 20 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.2.2-6
- Fix Source0 URL (GitHub tag archive)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.2.2-5
- Prepare for Oreon 11 (RP1)
