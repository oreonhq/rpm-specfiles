%global source0_hash b7d92fe4b767aac2935ffb7bff9c88d528ce8a05a3767d093748f14388622636

%bcond_without docs

Name:     open62541
Version:  1.5.0
Release:  1%{?dist}
Summary:  OPC UA implementation
License:  MPL-2.0
URL:      http://open62541.org
Source0:  https://github.com/open62541/open62541/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: cmake
BuildRequires: gcc
BuildRequires: graphviz
BuildRequires: libbpf-devel
BuildRequires: make
BuildRequires: openssl-devel
BuildRequires: python3

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

%autosetup -n %{name}-%{version} -p1

%build
# The version is usually extracted from the git tag, which is not available in the tarball.
# Therefore we need to set it manually.
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

#  -DUA_BUILD_EXAMPLES=ON \

%cmake_build
%if %{with docs}
cd %{__cmake_builddir}
%make_build doc
%endif

%install
%cmake_install

%if %{with docs}
cd %{__cmake_builddir}
# Remove build files not belonging to docs
rm -rf doc/CMakeFiles doc/Makefile doc/*.cmake
cd -
%endif

%ldconfig_scriptlets

%files
%license LICENSE
%doc README.md SECURITY.md
%{_libdir}/libopen62541.so.1*

%files devel
%license LICENSE LICENSE-CC0
%doc FEATURES.md
%{_libdir}/libopen62541.so
%{_libdir}/pkgconfig/open62541.pc
%{_includedir}/%{name}/
%{_libdir}/cmake/%{name}/
%dir %{_datadir}/%{name}/
%{_datadir}/%{name}/certs/
%{_datadir}/%{name}/generate_*
%{_datadir}/%{name}/nodeset_compiler/
%{_datadir}/%{name}/schema/

%if %{with docs}
%files doc
%doc %{__cmake_builddir}/doc/*
%doc examples/
%endif

%changelog
%autochangelog
