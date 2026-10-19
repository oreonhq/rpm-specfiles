%global source0_hash cf7951baf253c0537b3397e4ce3ff13930542abcb6ffc3b9cb082af88f95c300
%bcond_without docs
Name:     open62541
Version:  1.5.8
Release:        1%{?dist}
Summary:        OPC UA implementation
License:  MPL-2.0
URL:      http://open62541.org
Source0:        https://github.com/open62541/open62541/archive/v%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  graphviz
BuildRequires:  libbpf-devel
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  python3
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinx-rtd-theme)
# /oreon:deps
%description
open62541 is a C-based library (linking with C++ projects is possible)
with all necessary tools to implement dedicated OPC UA clients and servers,
or to integrate OPC UA-based communication into existing applications.

%package  devel
Summary:  Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%if %{with docs}
%package   doc
Summary:   Documentation for %{name}
BuildArch: noarch
BuildRequires: python3dist(sphinx)
BuildRequires: python3dist(sphinx-rtd-theme)
%description doc
The %{name}-doc package contains documentation for %{name}.
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

%cmake \
  -DOPEN62541_VERSION=v%{version} \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo \
  -DCMAKE_INSTALL_LIBDIR=%{_libdir} \
  -DUA_ENABLE_DA=ON \
  -DUA_ENABLE_DISCOVERY=ON \
  -DUA_ENABLE_DISCOVERY_SEMAPHORE=ON \
  -DUA_ENABLE_ENCRYPTION_OPENSSL=ON \
  -DUA_ENABLE_JSON_ENCODING=ON \
  -DUA_ENABLE_METHODCALLS=ON \
  -DUA_ENABLE_PARSING=ON \
  -DUA_ENABLE_NODEMANAGEMENT=ON \
  -DUA_ENABLE_PUBSUB=ON \
  -DUA_ENABLE_PUBSUB_ETH_UADP=ON \
  -DUA_ENABLE_PUBSUB_FILE_CONFIG=ON \
  -DUA_ENABLE_PUBSUB_INFORMATIONMODEL=ON \
  -DUA_ENABLE_PUBSUB_MONITORING=ON \
  -DUA_ENABLE_SUBSCRIPTIONS=ON \
  -DUA_ENABLE_SUBSCRIPTIONS_EVENTS=ON \
  %nil
%cmake_build
%if %{with docs}
cd %{__cmake_builddir}
%make_build doc
%endif
%install
%cmake_install
%if %{with docs}
cd %{__cmake_builddir}
rm -rf doc/CMakeFiles doc/Makefile doc/*.cmake
cd -
%endif
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n open62541-devel -f %{oreon_filedir}/open62541-devel.list
%files -n open62541-doc -f %{oreon_filedir}/open62541-doc.list

%changelog

%autochangelog
