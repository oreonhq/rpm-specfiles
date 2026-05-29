%global source0_hash 36d83229c360d694c1ce968f985375aa4e1d15b262ca4f8c354e53ea99fe9195

%global oqs_version 0.8.0
%global liboqs_min_version 0.12.0-1
Name:       oqsprovider
Version:    %{oqs_version}
Release:    5%{?dist}
Summary:    oqsprovider is an OpenSSL provider for quantum-safe algorithms based on liboqs

License:    Apache-2.0 AND MIT
URL:        https://github.com/open-quantum-safe/oqs-provider.git
Source0:        https://github.com/open-quantum-safe/oqs-provider/archive/refs/tags/0.8.0.tar.gz
Source1:    oqsprovider.conf

# https://github.com/open-quantum-safe/oqs-provider/pull/603
Patch01:    01-remove-prenist.patch
# https://github.com/open-quantum-safe/oqs-provider/pull/606
Patch02:    02-mlkem1024-hybrid.patch
Patch03:    03-iana-kem-only.patch

Requires: liboqs >= %{liboqs_min_version}
Requires: openssl
BuildRequires: ninja-build
BuildRequires: cmake
BuildRequires: gcc
BuildRequires: liboqs-devel
BuildRequires: openssl-devel
BuildRequires: liboqs >= %{liboqs_min_version}

%description
oqs-provider fully enables quantum-safe cryptography for KEM key
establishment in TLS1.3 including management of such keys via the OpenSSL (3.0)
provider interface and hybrid KEM schemes. Also, QSC signatures including CMS
functionality are available via the OpenSSL EVP interface. Key persistence is
provided via the encode/decode mechanism and X.509 data structures.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -T -b 0 -p1 -n oqs-provider-%{oqs_version}

%build
%cmake -GNinja -DCMAKE_BUILD_TYPE=Debug -DOQS_KEM_ENCODERS=ON -LAH ..
%cmake_build

%check
%ifnarch i686
cd "%{_vpath_builddir}"
OPENSSL_CONF=/dev/null ctest -V
%endif

%install
mkdir -p $RPM_BUILD_ROOT/%{_libdir}/ossl-modules
install %{_vpath_builddir}/lib/oqsprovider.so $RPM_BUILD_ROOT/%{_libdir}/ossl-modules
(cd $RPM_BUILD_ROOT/%{_libdir}/ossl-modules/ && ln -s oqsprovider.so oqsprovider.so.%{oqs_version})
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/pki/tls/openssl.d
install -m644 '%{SOURCE1}' \
        $RPM_BUILD_ROOT/%{_sysconfdir}/pki/tls/openssl.d/oqsprovider.conf

%files
%license LICENSE.txt
%{_libdir}/ossl-modules/oqsprovider.so.%{oqs_version}
%{_libdir}/ossl-modules/oqsprovider.so
%config(noreplace) %{_sysconfdir}/pki/tls/openssl.d/oqsprovider.conf

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.8.0-5
- Import
