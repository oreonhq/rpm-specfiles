%global source0_hash 7d9b1ef25b10eece48fdf29d8ac52f9b6252abff983ac614ade4f3276294019e

# Created by pyp2rpm-3.2.3
%global pypi_name croniter

Name:           python-%{pypi_name}
Version:        5.0.1
Release:        7%{?dist}
Summary:        Iteration for datetime object with cron like format

License:        MIT
URL:            https://github.com/kiorky/croniter
Source0:        %{pypi_source}
# Maintainers, please upstream
Patch0:         python-croniter-rm-python-mock-usage.diff
BuildArch:      noarch

%global _description %{expand:
croniter provides iteration for the datetime object with a cron like format.}

%description %_description

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
 
Requires:       python3-dateutil
%description -n python3-%{pypi_name} %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{pypi_name}-%{version}

sed -i '/-e ./d' requirements/base.txt

%generate_buildrequires
%pyproject_buildrequires -t

# Remove reundant script header to avoid rpmlint warnings
find -name \*.py -exec sed -i '/\/usr\/bin\/env python/{d;q}' {} +

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%check
%tox

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.rst

%changelog
%autochangelog
