%global source0_hash 0ff562ccd0560a8662a8761fadf99df6b73eb81979578912f31b97c8399c1bfb

%global srcname requests_ntlm

# EPEL 10 is missing flask at the moment
%if 0%{?rhel} >= 10
%bcond_with flask
%else
%bcond_without flask
%endif

Name:           python-%{srcname}
Version:        1.3.0
Release:        8%{?dist}
Summary:        NTLM module for python requests (requires md4, thus legacy OpenSSL settings)

License:        ISC
URL:            https://pypi.python.org/pypi/requests_ntlm
Source0:        https://github.com/requests/requests-ntlm/archive/v%{version}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

%global _description %{expand:
This package allows Python clients running on any operating system to provide
NTLM authentication to a supporting server.

With OpenSSL 3 or above, this needs to set the legacy OpenSSL provider in
order to support md4 in Python.}

%description %{_description}

%package -n     python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
# For tests
BuildRequires:  python3dist(pytest)
%if %{with flask}
BuildRequires:  python3dist(flask)
%endif

%description -n python3-%{srcname} %{_description}

Python 3 version.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n requests-ntlm-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{srcname}

%check
%python3 -m pytest --ignore=tests/functional/test_functional.py --ignore=tests/test_server.py -vv -k 'not (TestRequestsNtlm and not username)'

%if %{with flask}
# see https://github.com/jborean93/ntlm-auth/issues/22
cat > openssl.cnf << EOF
openssl_conf = openssl_init

[openssl_init]
providers = provider_sect

[provider_sect]
default = default_sect
legacy = legacy_sect

[default_sect]
activate = 1

[legacy_sect]
activate = 1
EOF
export OPENSSL_CONF=${PWD}/openssl.cnf
%python3 -m tests.test_server &
%python3 -m pytest --ignore=tests/functional/test_functional.py --ignore=tests/test_server.py -vv -k '(TestRequestsNtlm and not username)'
%endif

%files -n python3-%{srcname} -f %{pyproject_files}
%doc CONTRIBUTORS.rst README.rst

%changelog
%autochangelog
