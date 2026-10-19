%global source0_hash 3c065a1616972d04e8cc63d4b68dfa289e0977b521a11fed76e5973bc49ad75e
%{!?__global_ldflags: %global __global_ldflags -Wl,-z,relro}
%global incname ibmtss
Name:           tss2
Version:        2.5.0
Release:        1%{?dist}
Epoch:          1
Summary:        IBM's TCG Software Stack (TSS) for TPM 2.0 and related utilities
License:        BSD-3-Clause AND LicenseRef-TCGL
URL:            https://sourceforge.net/projects/ibmtpm20tss/
Source0:        https://sourceforge.net/projects/ibmtpm20tss/files/ibmtss%{version}.tar.gz
Requires:       openssl
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  openssl-devel
# /oreon:deps
%description
TSS2 is a user space Trusted Computing Group's Software Stack (TSS) for
TPM 2.0.  It implements the functionality equivalent to the TCG TSS
working group's ESAPI, SAPI, and TCTI layers (and perhaps more) but with
a hopefully far simpler interface.

It comes with about 120 "TPM tools" that can be used for rapid prototyping,
education and debugging. 

%package devel
Summary:        Development libraries and headers for IBM's TSS 2.0
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}
%description devel
Development libraries and headers for IBM's TSS 2.0. You will need this in
order to build TSS 2.0 applications.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

autoreconf -vi
%configure --disable-static --disable-tpm-1.2 --program-prefix=tss
CCFLAGS="%{optflags}" \
LNFLAGS="%{__global_ldflags}" \
%{make_build}
%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n tss2-devel -f %{oreon_filedir}/tss2-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.3.2-4
- Prepare for Oreon 11 (RP1)
