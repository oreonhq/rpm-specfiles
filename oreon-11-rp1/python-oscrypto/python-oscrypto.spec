%global source0_hash 5855d4cc18172513c6b2c6dde00b89731faa907c7003d4965862f2f2e0fb9ae4

# main package is archful to run tests everywhere but produces noarch packages
%global debug_package %{nil}
%bcond check 0
%global pname oscrypto
%global forgeurl https://github.com/wbond/oscrypto
%global commit 1547f535001ba568b239b8797465536759c742a3
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate 20230823
%global version0 1.3.0

%global desc %{expand:
Currently the following features are implemented. Many of these should only be
used for integration with existing/legacy systems.

* TLSv1.x socket wrappers
* Exporting OS trust roots
* Encryption/decryption
* Generating public/private key pairs
* Generating DH parameters
* Signing and verification
* Loading and normalizing DER and PEM formatted keys
* Key derivation
* Random byte generation
}

Name: python-%{pname}
Version: %{version0}^%{commitdate}git%{shortcommit}
Release: 1%{?dist}
Summary: Compiler-free Python crypto library backed by the OS
License: MIT
URL: %{forgeurl}
Source0: %{url}/archive/%{commit}/oscrypto-%{shortcommit}.tar.gz

%description %{desc}

%package -n python3-%{pname}
Summary: %{summary}
BuildRequires: python3-devel
%if %{with check}
BuildRequires: ca-certificates
BuildRequires: python3-asn1crypto
BuildRequires: python3-pytest
BuildRequires: python3-pytest-xdist
BuildRequires: openssl-libs
%endif
BuildArch: noarch
Requires: ca-certificates
Requires: openssl-libs

%description -n python3-%{pname} %{desc}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n oscrypto-%{commit}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pname}

%if %{with check}
%check
export SSL_CERT_FILE=/etc/pki/ca-trust/extracted/openssl/ca-bundle.trust.crt
export OPENSSL_ENABLE_SHA1_SIGNATURES=1 
# run only non-network tests
%pytest -k 'not TLSTests'
%endif

%files -n python3-%{pname} -f %{pyproject_files}
%license LICENSE
%doc readme.md

%changelog
%autochangelog
