# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 c981cb0a3fd84e8602d7afc209522773b94c1c2446a3c710a75b06fe1beae329
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

%global         srcname     pyopenssl

Name:           pyOpenSSL
Version:        25.3.0
Release:        %autorelease
Summary:        Python wrapper module around the OpenSSL library
License:        Apache-2.0
URL:            https://pyopenssl.readthedocs.org/
Source0:        https://files.pythonhosted.org/packages/source/p/pyopenssl/pyopenssl-25.3.0.tar.gz

Patch:          0001-Limit-list-of-elliptic-curves-tested-to-those-in-Fed.patch

BuildArch:      noarch

BuildRequires:  make
BuildRequires:  openssl
BuildRequires:  python3-devel

%global _description %{expand:
High-level wrapper around a subset of the OpenSSL library, includes among others
 * SSL.Connection objects, wrapping the methods of Python's portable
   sockets
 * Callbacks written in Python
 * Extensive error-handling mechanism, mirroring OpenSSL's error codes}

%description %{_description}


%package -n python3-pyOpenSSL
Summary: Python 3 wrapper module around the OpenSSL library
Obsoletes: pyOpenSSL < 19.0.0-5
Provides: pyOpenSSL = %{version}-%{release}

%description -n python3-pyOpenSSL %{_description}

%package doc
Summary: Documentation for pyOpenSSL
BuildArch: noarch

%description doc
Documentation for pyOpenSSL

%prep
%oreon_verify_sources
%autosetup -p1 -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires -x docs,test

%build
%pyproject_wheel

%{__make} -C doc html SPHINXBUILD=sphinx-build-3

%install
%pyproject_install
%pyproject_save_files OpenSSL

# Cleanup sphinx .buildinfo file before packaging
rm doc/_build/html/.buildinfo

%check
%pyproject_check_import
%pytest -k "not test_sign_verify_with_text" -k "not test_sign_verify"

%files -n python3-pyOpenSSL -f %{pyproject_files}
%license LICENSE
%doc README.rst

%files doc
%license LICENSE
%doc CHANGELOG.rst doc/_build/html

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 25.3.0-1
- Prepare for Oreon 11 (RP1)
