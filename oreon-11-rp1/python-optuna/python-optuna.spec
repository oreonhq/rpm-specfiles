%global source0_hash d91817e2079825557bd2e97de2e8c9ae260bfc99b32712502aef8a5095b2d2c0

# Created by pyp2rpm-3.3.10
%global pypi_name optuna

Name:           python-%{pypi_name}
Version:        4.7.0
Release:        1%{?dist}
Summary:        A hyperparameter optimization framework

License:        MIT AND BSD-3-Clause AND SunPro
URL:            https://optuna.org/
Source0:        %{pypi_source}

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(alembic)
BuildRequires:  python3dist(colorlog)
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(pyyaml)
BuildRequires:  python3dist(sqlalchemy)
BuildRequires:  python3dist(tqdm)

BuildArch:      noarch

%description
Optuna is an automatic hyperparameter optimization software framework,
particularly designed for machine learning. It features an imperative,
define-by-run style user API. Thanks to our define-by-run API, the
code written with Optuna enjoys high modularity, and the user of
Optuna can dynamically construct the search spaces for the hyperparameters.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Optuna is an automatic hyperparameter optimization software framework,
particularly designed for machine learning. It features an imperative,
define-by-run style user API. Thanks to our define-by-run API, the
code written with Optuna enjoys high modularity, and the user of
Optuna can dynamically construct the search spaces for the hyperparameters.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

# Tests require fakeredis, not in Fedora

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{_bindir}/optuna
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}.dist-info/

%changelog
%autochangelog
