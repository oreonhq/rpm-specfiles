%global source0_hash b53f0c5c8c4ce17f05701a410ca9688f725ca380c9bc4640eacd0eadb1fea124
%bcond_with rc
%if %{with rc}
%global candidate rc2
%endif
Name:          tpm2-tss
Version:       4.2.0
Release:        1%{?dist}
Summary:        TPM2.0 Software Stack
License:       BSD-2-Clause
URL:           https://github.com/tpm2-software/tpm2-tss
Source0:        https://github.com/tpm2-software/%{name}/releases/download/%{version}/%{name}-%{version}.tar.gz
Source1:       tpm2-tss-systemd-sysusers.conf
Patch0:        tpm2-tss-3.0.0-doxygen.patch
%global udevrules_prefix 60-
%if %{with rc}
%endif
# oreon:deps
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  json-c-devel
BuildRequires:  libcurl-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  libusb1-devel
BuildRequires:  libuuid-devel
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig
BuildRequires:  systemd
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
tpm2-tss is a software stack supporting Trusted Platform Module(TPM) 2.0 system
APIs. It sits between TPM driver and applications, providing TPM2.0 specified
APIs for applications to access TPM module through kernel TPM drivers.

%package fapi
Summary:       High-level TPM2.0 Software Stack
Requires:      %{name}%{_isa} = %{version}-%{release}
%description fapi
tpm2-tss is a software stack supporting Trusted Platform Module(TPM) 2.0 system
APIs. It sits between TPM driver and applications, providing TPM2.0 specified
APIs for applications to access TPM module through kernel TPM drivers.

This package provides the high-level "Feature API" library.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{name}-%{version}%{?candidate:-%{candidate}} -p1

%build

%configure --disable-static --disable-silent-rules \
           --with-udevrulesdir=%{_udevrulesdir} --with-udevrulesprefix=%{udevrules_prefix} \
           --with-runstatedir=%{_rundir} --with-tmpfilesdir=%{_tmpfilesdir} --with-sysusersdir=%{_sysusersdir}
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%make_build
%install
%make_install
find %{buildroot}%{_libdir} -type f -name \*.la -delete
rm %{buildroot}%{_sysusersdir}/tpm2-tss.conf
install -p -D -m 0644 %{SOURCE1} %{buildroot}%{_sysusersdir}/tpm2-tss.conf
%ldconfig_scriptlets
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%package        devel
Summary:        Headers and libraries for building apps that use tpm2-tss 
Requires:       %{name}%{_isa} = %{version}-%{release}
Requires:       %{name}-fapi%{_isa} = %{version}-%{release}
%description    devel
This package contains headers and libraries required to build applications that
use tpm2-tss.

%files -f %{oreon_filedir}/main.list
%files -n tpm2-tss-fapi -f %{oreon_filedir}/tpm2-tss-fapi.list
%files -n tpm2-tss-devel -f %{oreon_filedir}/tpm2-tss-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 4.1.3-9
- Prepare for Oreon 11 (RP1)
%{_libdir}/libtss2-tcti-null.so
%{_libdir}/pkgconfig/tss2-tcti-null.pc
