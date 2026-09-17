%global source0_hash b5a27a425e16b7e0057cd15b298162eb41ff3f2bcf5b967053e8926a457a3243

Name:           CuraEngine_grpc_definitions
Version:        0.1.0
Release:        16%{?dist}
Summary:        gRPC Proto Definitions for CuraEngine
License:        MIT
URL:            https://github.com/Ultimaker/CuraEngine_grpc_definitions
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:         CuraEngine_grpc_definitions-installfix.patch
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
%if !%{defined fc40} && !%{defined fc41}
ExcludeArch:    %{ix86}
%endif
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  grpc-devel
BuildRequires:  asio-grpc-devel
BuildRequires:  protobuf-devel
BuildRequires:  zlib-devel
BuildRequires:  openssl-devel
BuildRequires:  c-ares-devel
BuildRequires:  re2-devel
BuildRequires:  abseil-cpp-devel

%description
This package contains the gRPC proto definitions for CuraEngine. These
definitions are used to generate the gRPC code for the CuraEngine gRPC
plugin system.

%package        devel
Summary:        Development files for CuraEngine_grpc_definitions
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The CuraEngine_grpc_definitions-devel package contains libraries and header
files for developing applications that use CuraEngine_grpc_definitions.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{version} -p1

%build
CURAENGINE_PROTOS=`find . |grep "\.proto" | paste -sd ";"`

%cmake -DGRPC_PROTOS="$CURAENGINE_PROTOS"
%cmake_build

%install
%cmake_install

pushd %__cmake_builddir/generated
mkdir -p %{buildroot}%{_includedir}/cura/plugins/
cp -a cura/plugins/* %{buildroot}%{_includedir}/cura/plugins/
popd

%check
# no tests

%files
%license LICENSE
%doc README.md
%{_libdir}/libcuraengine_grpc_definitions.so.*

%files devel
%{_includedir}/cura/plugins
%{_libdir}/libcuraengine_grpc_definitions.so

%changelog
%autochangelog
