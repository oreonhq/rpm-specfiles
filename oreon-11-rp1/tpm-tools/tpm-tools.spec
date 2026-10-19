%global source0_hash 8af837949a2ec30b195389ac8a2b31bc49fe315050751b7d4d0d432bf7812a97
Name:             tpm-tools
Summary:        Management tools for the TPM hardware
Version:          1.3.9.2
Release:        1%{?dist}
License:          CPL-1.0
URL:              http://trousers.sourceforge.net
Source0:        https://downloads.sourceforge.net/trousers/%{name}-%{version}.tar.gz
Patch0001:        0003-Allocate-OpenSSL-cipher-contexts-for-seal-unseal.patch
Patch0002:        0001-tpm_version-avoid-outputting-NULL-bytes-from-tpmVend.patch
Patch0003:        0001-tpm_version-avoid-outputting-undefined-data-on-stder.patch
Patch0004:        0001-tpm-tools-fix-outdated-function-signature-in-tpmUnse.patch
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  gettext-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  opencryptoki-devel
BuildRequires:  openssl-devel
BuildRequires:  trousers-devel
# /oreon:deps
%description
tpm-tools is a group of tools to manage and utilize the Trusted Computing
Group's TPM hardware. TPM hardware can create, store and use RSA keys
securely (without ever being exposed in memory), verify a platform's
software state using cryptographic hashes and more.

%package        pkcs11
Summary:        Management tools using PKCS#11 for the TPM hardware
Requires:       opencryptoki-libs%{?_isa}
%description    pkcs11
tpm-tools-pkcs11 is a group of tools that use the TPM PKCS#11 token. All data
contained in the PKCS#11 data store is protected by the TPM (keys,
certificates, etc.). You can import keys and certificates, list out the
objects in the data store, and protect data.

%package        devel
Summary:        Files to use the library routines supplied with tpm-tools
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
tpm-tools-devel is a package that contains the libraries and headers necessary
for developing tpm-tools applications.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

chmod +x ./bootstrap.sh
./bootstrap.sh
%configure --disable-static --disable-rpath --disable-silent-rules
%make_build
%install
%make_install
rm -f $RPM_BUILD_ROOT/%{_libdir}/libtpm_unseal.la
%ldconfig_scriptlets
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n tpm-tools-pkcs11 -f %{oreon_filedir}/tpm-tools-pkcs11.list
%files -n tpm-tools-devel -f %{oreon_filedir}/tpm-tools-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.3.9.2-1
- Prepare for Oreon 11 (RP1)
