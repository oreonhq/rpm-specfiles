%global source1_hash 839ffaa8cb9b9d279f06f63f531ca6a1b64b0a0f3e098453346f36a48635558e
%global source0_hash edac03680f8a4a1c5c1d609a10e3f41e1a129e38ff5158f0c8deaedc719fb127
Name:           libtpms
Version:        0.10.2
Release:        1%{?dist}
Summary:        Library providing Trusted Platform Module (TPM) functionality
License:        BSD-3-Clause AND LicenseRef-TCGL
URL:            https://github.com/stefanberger/libtpms
Source0:        https://github.com/stefanberger/libtpms/archive/refs/tags/v0.10.2.tar.gz#/libtpms-0.10.2.tar.gz
Source1:        https://github.com/stefanberger/libtpms/releases/download/v0.10.2/v0.10.2.tar.gz.asc#/libtpms-0.10.2.tar.gz.asc
Source2:        gpgkey-B818B9CADF9089C2D5CEC66B75AD65802A0B4211.asc
Patch0001:      0001-Fix-a-compilation-error-in-TPMLIB_GetPlaintext.patch
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  coreutils
BuildRequires:  gawk
BuildRequires:  gcc-c++
BuildRequires:  gnupg2
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig
BuildRequires:  sed
# /oreon:deps
%description
A library providing TPM functionality for VMs. Targeted for integration
into Qemu.

%package        devel
Summary:        Include files for libtpms
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description   devel
Libtpms header files and documentation.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

%build

NOCONFIGURE=1 ./autogen.sh
%configure --disable-static --with-tpm2 --with-openssl
%make_build
%install
%make_install
find %{buildroot} -type f -name '*.la' -print -delete
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

make check
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n libtpms-devel -f %{oreon_filedir}/libtpms-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.10.2-3
- Prepare for Oreon 11 (RP1)
