%global source0_hash 36a2f13859f3e2a9c74d1d4064f8d406689b0201e25968aba952010ed73bfec2

#Enable gpg signature verification
%bcond gpgcheck 1

Name:          pkcs11-provider
Version:       1.2.0
Release:       %autorelease
Summary:       A PKCS#11 provider for OpenSSL 3.0+
License:       Apache-2.0
URL:           https://github.com/latchset/pkcs11-provider
Source0:        https://github.com/latchset/pkcs11-provider/releases/download/v1.2.0/pkcs11-provider-1.2.0.tar.xz
%if %{with gpgcheck}
Source1:        https://github.com/latchset/pkcs11-provider/releases/download/v1.2.0/pkcs11-provider-1.2.0.tar.xz.asc
Source2:       simo_redhat.asc
%endif
Source3:       pkcs11-provider.conf
# https://github.com/latchset/pkcs11-provider/pull/689
Patch1:        0001-Fix-i686-build-failures-in-cipher.c.patch


BuildRequires: openssl-devel >= 3.0.7
BuildRequires: gcc
BuildRequires: meson
%if %{with gpgcheck}
BuildRequires: gnupg2
%endif

# for tests
BuildRequires: nss-devel
BuildRequires: nss-softokn
BuildRequires: nss-softokn-devel
BuildRequires: nss-tools
BuildRequires: openssl
BuildRequires: softhsm
BuildRequires: opensc
BuildRequires: p11-kit-devel
BuildRequires: gnutls-utils
BuildRequires: xz
BuildRequires: expect


%description
This is an Openssl 3.x provider to access Hardware or Software Tokens using
the PKCS#11 Cryptographic Token Interface.
This code targets version 3.0 of the interface but should be backwards
compatible to previous versions as well.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%if %{with gpgcheck}
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%endif

%autosetup -p1


%build
%meson
%meson_build


%install
%meson_install
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/pki/tls/openssl.d
install -m644 '%{SOURCE3}' \
        $RPM_BUILD_ROOT/%{_sysconfdir}/pki/tls/openssl.d/pkcs11-provider.conf



%check
# do not run them in parrallel with %%{?_smp_mflags}
%meson_test --num-processes 1 --timeout-multiplier 4


%files
%license COPYING
%{_mandir}/man7/provider-pkcs11.*
%doc README.md
%{_libdir}/ossl-modules/pkcs11.so
%config(noreplace) %{_sysconfdir}/pki/tls/openssl.d/pkcs11-provider.conf

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.2.0-1
- Prepare for Oreon 11 (RP1)
