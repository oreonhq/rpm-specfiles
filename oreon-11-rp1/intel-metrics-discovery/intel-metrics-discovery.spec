%global source0_hash aa68d6a1d532a63ed0e7c32bdd87f62d23dd72d7efaff7c9d906bbd65dcde94d

%global upstream_name metrics-discovery

Name: intel-metrics-discovery
Version: 1.14.182
Release: %autorelease
Summary: Shared library for Intel Metrics Discovery API
License: MIT
ExclusiveArch: x86_64
URL: https://github.com/intel/metrics-discovery
Source0: %{url}/archive/%{upstream_name}-%{version}.tar.gz

BuildRequires: make
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: pkgconfig
BuildRequires: libdrm-devel

%description
Intel Metrics Discovery Application Programming Interface creates an abstraction
level between Intel graphics hardware and applications, providing access to
detailed GPU performance data.

%package         devel
Summary:         Development files for %{name}
Requires:        %{name} = %{version}-%{release}

%description     devel
Intel Metrics Discovery Application Programming Interface creates an abstraction
level between Intel graphics hardware and applications, providing access to
detailed GPU performance data.

The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{upstream_name}-%{upstream_name}-%{version}

%build
%cmake \
   -DCMAKE_BUILD_TYPE=Release \
   -DCMAKE_INSTALL_PREFIX=/usr

%cmake_build

%install
%cmake_install

%files
%config(noreplace)
%{_libdir}/libigdmd.so.%{version}
%{_libdir}/libigdmd.so.1
%license LICENSE.md
%doc README.md

%files devel
%config(noreplace)
%{_libdir}/libigdmd.so
%{_includedir}/metrics_discovery_api.h
%{_libdir}/pkgconfig/libigdmd.pc

%changelog
%autochangelog
