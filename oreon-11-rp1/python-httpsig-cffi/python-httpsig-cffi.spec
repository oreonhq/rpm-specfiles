%global source0_hash 12b61008cd21cb18986de743959d63caaf8ac5b3cf3ee1d49fd1c53fe4f5d47a

Summary:        Secure HTTP request signing using the HTTP Signature draft specification
Name:           python-httpsig-cffi
Version:        15.0.0
Release:        32%{?dist}
License:        MIT
URL:            https://github.com/hawkowl/httpsig_cffi
Source0:        https://files.pythonhosted.org/packages/source/h/httpsig-cffi/httpsig_cffi-%{version}.tar.gz
Patch0:         0001-Fix-cryptography-deprecation-warnings-1.patch
Patch1:         0001-Disable-SHA1-signing-tests.patch
BuildArch:      noarch 
BuildRequires:  python3-devel
BuildRequires:  python3dist(cryptography)
BuildRequires:  python3dist(requests)
BuildRequires:  python3dist(six)
BuildRequires:  python3-pytest
%description
Sign HTTP requests with secure signatures according to the IETF HTTP
Signatures specification (Draft 3_). This is a fork of the fork of the
original module that was made to fully support both RSA and HMAC
schemes as well as unit test both schemes to prove they work. This
particular fork moves from PyCrypto to Cryptography, which provides
PyPy support.

%package -n     python3-httpsig-cffi
Summary:        %{summary}
Requires:       python3dist(cryptography)
Requires:       python3dist(requests)
Requires:       python3dist(six)
%description -n python3-httpsig-cffi
Sign HTTP requests with secure signatures according to the IETF HTTP
Signatures specification (Draft 3_). This is a fork of the fork of the
original module that was made to fully support both RSA and HMAC
schemes as well as unit test both schemes to prove they work. This
particular fork moves from PyCrypto to Cryptography, which provides
PyPy support.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%if 0%{?fedora} > 40
%autosetup -p1 -n httpsig_cffi-%{version}
%else
%autosetup -N -n httpsig_cffi-%{version}
%autopatch -p1 0
%endif

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l httpsig_cffi

%check
%pyproject_check_import
%{pytest} --color=yes

%files -n python3-httpsig-cffi -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
