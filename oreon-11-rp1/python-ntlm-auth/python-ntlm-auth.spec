%global source0_hash 849f4a35376e55cde48cf8a4c2c0cfafe5f10d2ae280e211c6434e0ad5e5b64f

%global srcname ntlm-auth

Name:           python-%{srcname}
Version:        1.5.0
Release:        21%{?dist}
Summary:        Python 3 compatible NTLM library (requires md4, thus legacy OpenSSL settings)

License:        MIT
URL:            https://pypi.python.org/pypi/ntlm-auth
Source:         https://github.com/jborean93/ntlm-auth/archive/v%{version}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  %{py3_dist setuptools}
# For tests
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist requests}
BuildRequires:  %{py3_dist cryptography}

%global _description %{expand:
This package allows Python clients running on any operating system to provide
NTLM authentication to a supporting server.

With OpenSSL 3 or above, the legacy OpenSSL provider needs to be set in
order to support md4 in Python.}

%description %{_description}

%package -n     python3-%{srcname}
Summary:        %{summary}
Obsoletes:      python3-ntlm3 < 1.0.3-1
Provides:       python3-ntlm3 = %{version}-%{release}

%description -n python3-%{srcname} %{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%check
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

%pytest

%files -n python3-%{srcname}
%doc CHANGES.md README.md
%license LICENSE
%{python3_sitelib}/ntlm_auth-*.egg-info/
%{python3_sitelib}/ntlm_auth/

%changelog
%autochangelog
