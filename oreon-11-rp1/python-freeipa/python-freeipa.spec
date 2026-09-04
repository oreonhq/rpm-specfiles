%global source0_hash 6320fbf6d31ce0a36d5aa315f6581a9872b5dfaf92060cc13d0f3b879596f66e

# Enable Python dependency generation
%{?python_enable_dependency_generator}

%global pypi_name python-freeipa
%global srcname freeipa

Name:           python-%{srcname}
Version:        1.0.10
Release:        1%{?dist}
Summary:        Lightweight FreeIPA client

License:        MIT
URL:            https://python-freeipa.readthedocs.io/
Source0:        https://github.com/opennode/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist requests}
BuildRequires:  %{py3_dist responses}
BuildRequires:  %{py3_dist setuptools}

%description
python-freeipa is lightweight FreeIPA client.

%package -n     python%{python3_pkgversion}-%{srcname}
Summary:        %{summary} for Python %{python3_version}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

%description -n python%{python3_pkgversion}-%{srcname}
python-freeipa is lightweight FreeIPA client.

This package provides the Python %{python3_version} variant.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

# Fix version
sed -e "s/version='1.0.6',/version='%{version}',/" -i setup.py

%build
%py3_build

%install
%py3_install

%check
%pytest src/python_freeipa/tests/*.py

%files -n python%{python3_pkgversion}-%{srcname}
%license LICENSE.md
%doc README.rst
%{python3_sitelib}/python_freeipa/
%{python3_sitelib}/python_freeipa-%{version}-py%{python3_version}.egg-info/

%changelog
%autochangelog
