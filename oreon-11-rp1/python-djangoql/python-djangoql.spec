%global source0_hash 4f053d0128e28f412926e2da902735f4bdcbab5c08d43be4dfefd747fca2e96e

%global pypi_name djangoql

Name:           python-%{pypi_name}
Version:        0.17.1
Release:        16%{?dist}
Summary:        DjangoQL: Advanced search language for Django

License:        MIT
URL:            https://github.com/ivelum/djangoql
Source0:        %{pypi_source}

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:	python3-django
BuildRequires:	pyproject-rpm-macros
%py_provides python3-%{pypi_name}

%description
Advanced search language for Django, with auto-completion.
Supports logical operators, parenthesis, table joins,
works with any Django models.

%package -n python3-%{pypi_name}
Summary:        %{summary}
Requires:	python3-ply

%description -n python3-%{pypi_name}
Advanced search language for Django, with auto-completion.
Supports logical operators, parenthesis, table joins,
works with any Django models.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files djangoql

%check
PYTHONPATH=$(pwd) %{__python3} test_project/manage.py test core.tests

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.rst

%changelog
%autochangelog
