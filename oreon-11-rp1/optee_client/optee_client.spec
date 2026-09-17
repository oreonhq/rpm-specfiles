%global source0_hash 2ef152f25b682e59c3684d6d73d7c5a138495615f6b045e95266eb3d0bc0d04e

Name:      optee_client
Version:   4.9.0
Release:   1%{?dist}
Summary:   OP-TEE Client API and supplicant
License:   BSD
URL:       https://www.trustedfirmware.org/
Source:    https://github.com/OP-TEE/optee_client/archive/%{version}/%{name}-%{version}.tar.gz
Patch1:    optee_client-fix-systemd-instdir.patch

# TrustZone is an ARM specific technology
ExclusiveArch: aarch64
BuildRequires: cmake
BuildRequires: gcc
BuildRequires: libuuid-devel
BuildRequires: make
BuildRequires: systemd

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

%autosetup -p1

%build
%cmake -DRPMB_EMU=0
%cmake_build

%install
%cmake_install

%ldconfig_scriptlets

%files
%license LICENSE
%{_sbindir}/tee-supplicant
%{_libdir}/libckteec.so.0*
%{_libdir}/libseteec.so.0*
%{_libdir}/libteeacl.so.0*
%{_libdir}/libteec.so.2*
%{_udevrulesdir}/*optee-udev.rules
%{_unitdir}/tee-supplicant@.service

%files devel
%{_includedir}/ck_debug.h
%{_includedir}/pkcs11*.h
%{_includedir}/se_tee.h
%{_includedir}/tee*.h
%{_libdir}/pkgconfig/tee*.pc
%{_libdir}/libckteec.so
%{_libdir}/libseteec.so
%{_libdir}/libteeacl.so
%{_libdir}/libteec.so

%changelog
%autochangelog
