%global source0_hash 1aa8e7304b2e171a90d64dd269b648cacac4e46fe5de54ac0db24776c0c4a19f

%global pypi_name asteval

Name:           python-%{pypi_name}
Version:        1.0.6
Release:        5%{?dist}
Summary:        Evaluator of Python expression using ast module

License:        MIT
URL:            http://github.com/newville/asteval
Source0:        %{pypi_source}
BuildArch:      noarch

%description
ASTEVAL is a safe(ish) evaluator of Python expressions and statements,
using Python's ast module. The idea is to provide a simple, safe, and robust
miniature mathematical language that can handle user-input. The emphasis here
is on mathematical expressions, and so many functions from numpy are imported
and used if available.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-cov)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(setuptools-scm)

%description -n python3-%{pypi_name}
ASTEVAL is a safe(ish) evaluator of Python expressions and statements,
using Python's ast module. The idea is to provide a simple, safe, and robust
miniature mathematical language that can handle user-input. The emphasis here
is on mathematical expressions, and so many functions from numpy are imported
and used if available.

%package -n python-%{pypi_name}-doc
Summary:        The %{name} documentation

BuildRequires:  python3-sphinx

%description -n python-%{pypi_name}-doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info
sed -i -e '/^#!\//, 1d' asteval/asteval.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel
PYTHONPATH=${PWD} sphinx-build-3 doc html
rm -rf html/.{doctrees,buildinfo} html/_static/empty

%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}

%check
%pytest -v tests

%files -n %files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.rst

%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE

%changelog
%autochangelog
