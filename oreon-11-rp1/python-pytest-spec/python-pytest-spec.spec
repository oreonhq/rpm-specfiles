%global source0_hash 66b1400a63c2903ffdd838569f6dd2c2acc24ade695b554d8e5fe1c756af83a2

# Created by pyp2rpm-3.1.2
%global pypi_name pytest-spec
%global modname pytest_spec
%global desc Pytest plugin to display test execution output like a SPECIFICATION.\
Available features:\
- Format output to look like specification.\
- Group tests by classes and files\
- Failed, passed and skipped are marked and colored.\
- Remove test_ and underscores for every test.

Name:           python-%{pypi_name}
Version:        5.2.0
Release:        3%{?dist}
Summary:        Pytest plugin to display test execution output like a SPECIFICATION

License:        GPL-2.0-or-later
URL:            https://github.com/pchomik/pytest-spec
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
%{desc}

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)
BuildRequires:  pyproject-rpm-macros
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%{desc}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version}
# Guidelines don't allow to run linting operations
rm -rf setup.cfg
%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{modname}

%check
%pytest -v test/*

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc CHANGES.txt README.md
%license LICENSE.txt

%changelog
%autochangelog
