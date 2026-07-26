%global source0_hash 1204462b6e63b89b04414bb0311d43e233c31bb6603b68bb4d82da84cbf67fe2

%global pypi_name presets
%global pypi_version 0.1.3

Name:           python-%{pypi_name}
Version:        %{pypi_version}
Release:        9%{?dist}
Summary:        A python module to manipulate default parameters of a module's functions

License:        ISC
URL:            http://github.com/bmcfee/presets
Source0:        https://github.com/bmcfee/presets/archive/%{version}/presets-%{version}.tar.gz
# https://github.com/bmcfee/presets/pull/16
Patch0:         importlib.patch
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(six)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-cov)

%description
A python module to manipulate default parameters of a module's functions

%package -n     python3-%{pypi_name}
Summary:        %{summary}

Requires:       python3dist(numpydoc)
Requires:       python3dist(six)
%description -n python3-%{pypi_name}
A python module to manipulate default parameters of a module's functions

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{pypi_version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name} -l
sed -e '1d' -i %{buildroot}%{python3_sitelib}/presets/__init__.py
sed -e '1d' -i %{buildroot}%{python3_sitelib}/presets/version.py

%check
%pytest

%files -n python3-%{pypi_name} -f %{pyproject_files}

%changelog
%autochangelog
