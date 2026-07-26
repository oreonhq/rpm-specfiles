%global source0_hash eac2cd25a3d38d7fac82c44827bf314e07d8f5426621aa16e5750972debaaf07

%global pypi_name vulture
%global common_desc \
Vulture finds unused classes, functions and variables in your code. \
This helps you cleanup and find errors in your programs. If you run it \
on both your library and test suite you can find untested code. \
Due to Python’s dynamic nature, static code analyzers like vulture \
are likely to miss some dead code. Also, code that is only called \
implicitly may be reported as unused. Nonetheless, vulture can be a \
very helpful tool for higher code quality.

Name:           python-%{pypi_name}
Version:        2.14
Release:        4%{?dist}
Summary:        Find dead code

License:        MIT
URL:            https://github.com/jendrikseipp/vulture
Source0:        %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
%{common_desc}

%package -n	python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(toml)
BuildRequires:  python3dist(pint)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-cov)
%description -n	python3-%{pypi_name}
%{common_desc}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version}
sed -i '1{/^#!/d}' vulture/*.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files -l %{pypi_name}

%check
%pytest -v tests

%files -n %files -n python3-%{pypi_name} -f %{pyproject_files}
%doc CHANGELOG.md README.md
%license LICENSE.txt
%{_bindir}/%{pypi_name}

%changelog
%autochangelog
