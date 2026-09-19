%global source0_hash f58e04673453a709e59a04e80f411c327c0555304c210e84272febbcff1de7fd

%global pypi_name aiosqlite

Name:           python-%{pypi_name}
Version:        0.22.1
Release:        2%{?dist}
Summary:        Asyncio bridge to the standard SQLite3 module

License:        MIT
URL:            https://github.com/jreese/aiosqlite
Source0:        %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
aiosqlite AsyncIO bridge to the standard SQLite3 module for Python 3.5+.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
aiosqlite AsyncIO bridge to the standard SQLite3 module for Python 3.5+.

%generate_buildrequires
%pyproject_buildrequires -r

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%check
%{py3_test_envvars} %{python3} -m %{pypi_name}.tests

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc CHANGELOG.md README.rst

%changelog
%autochangelog
