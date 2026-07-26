%global source0_hash e72378fcea8f90ccab874836a61f1783092a900c965e52587c1307e38b2e2153

%global project_name flask-oidc
%global mod_name flask_oidc

Name:           python-%{project_name}
Version:        2.4.0
Release:        5%{?dist}
Summary:        OpenID Connect extension for Flask

License:        BSD-2-Clause
URL:            https://github.com/fedora-infra/flask-oidc
Source0:        %pypi_source %{mod_name}

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-responses

%global _description %{expand:
OpenID Connect support for Flask.
This library should work with any standards compliant
OpenID Connect provider. It has been tested with
Ipsilon.}

%description %_description

%package -n python3-%{project_name}
Summary:        %{summary}

%description -n python3-%{project_name} %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{mod_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{mod_name}

%check
%pytest -k "not test_accept_token_no_token"

%files -n python3-%{project_name} -f %{pyproject_files}
%doc README.rst
%license LICENSES/BSD-2-Clause.txt

%changelog
%autochangelog
