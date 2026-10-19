%global source0_hash 2ef152f25b682e59c3684d6d73d7c5a138495615f6b045e95266eb3d0bc0d04e
Name:      optee_client
Version:   4.9.0
Release:        1%{?dist}
Summary:        OP-TEE Client API and supplicant
License:   BSD
URL:       https://www.trustedfirmware.org/
Source0:        https://github.com/OP-TEE/optee_client/archive/%{version}/%{name}-%{version}.tar.gz
Patch1:    optee_client-fix-systemd-instdir.patch
ExclusiveArch: aarch64
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  libuuid-devel
BuildRequires:  make
BuildRequires:  systemd
# /oreon:deps
%description
OP-TEE is an open source Trusted Execution Enviroment (TEE) implementing the
Arm TrustZone technology.

The optee client provides the Linux userspace client APIs and supplicant for
communicating with OPTEE in the Arm TrustZone TEE.

%package devel
Summary:        Development files for optee_client
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
Development file for optee_client

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake -DRPMB_EMU=0
%cmake_build
%install
%cmake_install
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n optee_client-devel -f %{oreon_filedir}/optee_client-devel.list

%changelog

%autochangelog
