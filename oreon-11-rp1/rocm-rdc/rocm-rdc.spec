%global source0_hash d16c63fe6609d82d0fcd65e9953f60318d015275b8752d052a6ae20cd634c3e1
%global upstreamname rdc
%global rocm_release 7.1
%global rocm_patch 1
%global rocm_version %{rocm_release}.%{rocm_patch}
%global toolchain rocm
%global build_cxxflags %(echo %{optflags} | sed -e 's/-fstack-protector-strong/-Xarch_host -fstack-protector-strong/' -e 's/-fcf-protection/-Xarch_host -fcf-protection/' -e 's/-mtls-dialect=gnu2//')
%bcond_with debug
%if %{with debug}
%global build_type DEBUG
%else
%global build_type RelWithDebInfo
%endif
%global gpu_list %{rocm_gpu_list_default}
%global _gpu_list gfx1100
Name:           rocm-rdc
Version:        %{rocm_version}
Release:        1%{?dist}
Summary:        ROCm Data Center Tool
URL:            https://github.com/ROCm/%{upstreamname}
License:        MIT AND NCSA
Source0:        https://github.com/ROCm/%{upstreamname}/archive/%{toolchain}-%{version}.tar.gz#/%{upstreamname}-%{version}.tar.gz
ExclusiveArch:  x86_64
# oreon:deps
BuildRequires:  amdsmi-devel
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  grpc-devel
BuildRequires:  libcap-devel
BuildRequires:  libdrm-devel
BuildRequires:  protobuf-devel
BuildRequires:  python3dist(cppheaderparser)
BuildRequires:  rocm-comgr-devel
BuildRequires:  rocm-compilersupport-macros
BuildRequires:  rocm-rpm-macros
BuildRequires:  rocm-runtime-devel
# /oreon:deps
%description
ROCm Data Center Tool (RDC)
The ROCm Data Center Tool simplifies the administration and addresses
key infrastructure challenges in AMD GPUs in cluster and data center
environments. The main features are:

* GPU telemetry
* GPU statistics for jobs
* Integration with third-party tools
* Open source

%package devel
Summary:        The %{name} development package
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
The headers of libraries for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{upstreamname}-rocm-%{version}

# Use the system gRPC
sed -i -e 's@${GRPC_DESIRED_VERSION}@@' CMakeLists.txt
# Use the system Protobuf
sed -i -e 's@protobuf HINTS ${GRPC_ROOT} CONFIG@Protobuf@' CMakeLists.txt
# Location of call_op_set is a little different on Fedora
sed -i -e 's@grpcpp/impl/call_op_set.h@grpcpp/impl/codegen/call_op_set.h@' server/src/rdc_api_service.cc

%build

%cmake \
    -DGPU_TARGETS=%{gpu_list} \
    -DBUILD_FILE_REORG_BACKWARD_COMPATIBILITY=OFF \
    -DBUILD_RASLIB=OFF \
    -DBUILD_SHARED_LIBS=ON \
    -DBUILD_STANDALONE=ON \
    -DBUILD_RVS=OFF \
    -DCMAKE_BUILD_TYPE=%{build_type} \
    -DCMAKE_CXX_COMPILER=%rocmllvm_bindir/amdclang++ \
    -DCMAKE_C_COMPILER=%rocmllvm_bindir/amdclang \
    -DCMAKE_INSTALL_LIBDIR=%{_lib} \
    -DHIP_PLATFORM=amd \
    -DROCM_SYMLINK_LIBS=OFF \
    -DROCM_DIR=%{_prefix}
%cmake_build
%install
%cmake_install
rm -f %{buildroot}%{_prefix}/share/doc/rdc/LICENSE.md
%rocmllvm_bindir/llvm-strip %{buildroot}%{_libdir}/rdc/hsaco/*/*.hsaco
chmod a+x %{buildroot}%{_libexecdir}/rdc/authentication/*.sh
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n rocm-rdc-devel -f %{oreon_filedir}/rocm-rdc-devel.list

%changelog

%autochangelog
