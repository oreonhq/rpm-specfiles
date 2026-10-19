%global source0_hash c652fbabd49c96e1626af248357c399fff4dd6d01a65116a4fbf7d8266085d74
%bcond_with toolchain_clang
%if %{with toolchain_clang}
%global toolchain clang
%endif
%bcond_without build_tests
%bcond check 1
%global forgeurl https://github.com/facebook/CacheLib
%global tag 2025.02.03.00
%global date %(echo %{tag} | sed -e 's|.00$||' | sed -e 's|\\.||g')
%global distprefix %{nil}
%forgemeta
%global major_ver 17
Name:           cachelib
Version:        %{major_ver}^%{date}
Release:        1%{?dist}
Summary:        Pluggable caching engine for scale high performance cache services
License:        Apache-2.0
URL:            %forgeurl
Source0:        %{forgeurl}/archive/v%{tag}/%{name}-%{tag}.tar.gz
Patch:          %{name}-fix-DeviceTest-FDP.diff
Patch:          %{name}-disable-binary_trace_gen.diff
Patch100:       %{name}-find-gtest.patch
Patch200:         %{name}-workaround-gcc-epel9-x86_64-bz2108665.patch
ExclusiveArch:  x86_64 aarch64 ppc64le
%if %{with toolchain_clang}
%else
%endif
%if %{with build_tests}
%endif
# oreon:deps
BuildRequires:  cmake
BuildRequires:  fbthrift-devel
BuildRequires:  fizz-devel
BuildRequires:  folly-devel
BuildRequires:  gcc-c++
BuildRequires:  gmock-devel
BuildRequires:  gtest-devel
BuildRequires:  libdwarf-devel
BuildRequires:  libzstd-devel
BuildRequires:  mvfst-devel
BuildRequires:  numactl-devel
BuildRequires:  tsl-sparse-map-devel
BuildRequires:  wangle-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description

%package devel
Summary:        %{summary}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake
%description devel

The %{name}-devel package contains libraries and header files for developing
applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n CacheLib-%{tag} -N
%autopatch -p1 -M 99
%if 0%{?el8}
%autopatch -p1 -m 100 -M 199
%endif
%ifarch x86_64
%if 0%{?el9}
%autopatch -p1 -m 200 -M 209
%endif
%endif

%build

pushd %{name}
%cmake \
%if %{with build_tests}
  -DBUILD_TESTS:BOOL=ON \
%else
  -DBUILD_TESTS:BOOL=OFF \
%endif
  -DCMAKE_BUILD_WITH_INSTALL_RPATH:BOOL=FALSE \
  -DCMAKE_INSTALL_DIR:PATH=%{_libdir}/cmake/%{name} \
  -DCONFIGS_INSTALL_DIR:STRING=%{_datadir}/%{name}/test_configs \
  -DINCLUDE_INSTALL_DIR:PATH=%{_includedir}/%{name} \
  -DCACHELIB_MAJOR_VERSION:STRING=%{major_ver} \
  -DPACKAGE_VERSION:STRING=%{major_ver}.%{date}
%cmake_build
%install
pushd %{name}
%cmake_install
%if %{with build_tests}
rm -rf %{buildroot}%{_prefix}/tests
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%endif
%if %{with check}
%check

pushd %{name}
%ctest
%endif
%files -f %{oreon_filedir}/main.list
%files -n cachelib-devel -f %{oreon_filedir}/cachelib-devel.list

%changelog

%autochangelog
