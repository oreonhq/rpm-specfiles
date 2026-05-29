%global source0_hash 8af837949a2ec30b195389ac8a2b31bc49fe315050751b7d4d0d432bf7812a97

Name:             tpm-tools
Summary:          Management tools for the TPM hardware
Version:          1.3.9.2
Release:          %autorelease
License:          CPL-1.0
URL:              http://trousers.sourceforge.net
Source0:        http://downloads.sourceforge.net/trousers/tpm-tools-1.3.9.2.tar.gz
BuildRequires:    make gcc
BuildRequires:    trousers-devel openssl-devel opencryptoki-devel gettext-devel autoconf automake libtool
Patch0001:        0003-Allocate-OpenSSL-cipher-contexts-for-seal-unseal.patch
Patch0002:        0001-tpm_version-avoid-outputting-NULL-bytes-from-tpmVend.patch
Patch0003:        0001-tpm_version-avoid-outputting-undefined-data-on-stder.patch
Patch0004:        0001-tpm-tools-fix-outdated-function-signature-in-tpmUnse.patch

%description
tpm-tools is a group of tools to manage and utilize the Trusted Computing
Group's TPM hardware. TPM hardware can create, store and use RSA keys
securely (without ever being exposed in memory), verify a platform's
software state using cryptographic hashes and more.

%package        pkcs11
Summary:        Management tools using PKCS#11 for the TPM hardware
# opencryptoki is dlopen'd, the Requires won't get picked up automatically
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
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p1

%build
chmod +x ./bootstrap.sh
./bootstrap.sh
%configure --disable-static --disable-rpath --disable-silent-rules
%make_build

%install
%make_install
rm -f $RPM_BUILD_ROOT/%{_libdir}/libtpm_unseal.la

%ldconfig_scriptlets

%files
%license LICENSE
%doc README
%{_bindir}/tpm_*
%{_libdir}/libtpm_unseal.so.?.?.?
%{_libdir}/libtpm_unseal.so.?
%{_mandir}/man1/tpm_*
%{_mandir}/man8/tpm_*

%files pkcs11
%license LICENSE
%{_bindir}/tpmtoken_*
%{_mandir}/man1/tpmtoken_*

%files devel
%{_libdir}/libtpm_unseal.so
%{_includedir}/tpm_tools/
%{_mandir}/man3/tpmUnseal*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.3.9.2-1
- Prepare for Oreon 11 (RP1)
