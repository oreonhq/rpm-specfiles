%global source0_hash 2846bbca9ed5bd4c12ace11863c63d605684a5d327235ba95ff63b856bfb9e0c

Name:           python-requests-kerberos
Version:        0.15.0
Release:        %autorelease
Summary:        A Kerberos authentication handler for python-requests
License:        ISC
URL:            https://github.com/requests/requests-kerberos
# Upstream considers Github not PyPI to be the authoritative source tarballs:
# https://github.com/requests/requests-kerberos/pull/78
Source:         %{url}/archive/v%{version}/requests-kerberos-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:	python3dist(pyspnego)
BuildRequires:	python3dist(pyspnego[kerberos])

%global _description %{expand:
Requests is an HTTP library, written in Python, for human beings. This library
adds optional Kerberos/GSSAPI authentication support and supports mutual
authentication.}

%description %_description

%package -n python3-requests-kerberos
Summary:        %{summary}

%description -n python3-requests-kerberos %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n requests-kerberos-%{version}
# avoid unnecessary coverage dependency
sed -i '/pytest-cov/d' requirements-test.txt

%generate_buildrequires
%pyproject_buildrequires requirements-test.txt

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l requests_kerberos

%check
%pytest -v tests

%files -n python3-requests-kerberos -f %{pyproject_files}
%doc README.rst AUTHORS HISTORY.rst

%changelog
%autochangelog
