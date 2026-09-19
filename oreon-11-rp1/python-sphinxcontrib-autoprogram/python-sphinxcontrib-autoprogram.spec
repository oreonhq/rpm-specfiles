%global source0_hash e27c34c3abda19e655f3ba19573f66901e5287cc75fc19bb13685756dc4d7c69

%global pypi_name sphinxcontrib-autoprogram
%global pypi_shortname autoprogram

Name:           python-%{pypi_name}
Version:        0.1.9
Release:        12%{?dist}
Summary:        Sphinx extension for documenting CLI programs

License:        LicenseRef-Callaway-BSD
URL:            https://sphinxcontrib-autoprogram.readthedocs.io/en/stable/
Source0:        https://github.com/sphinx-contrib/%{pypi_shortname}/archive/refs/tags/%{version}.tar.gz
Patch0:         python-sphinxcontrib-autoprogram-test.patch

BuildArch:      noarch

BuildRequires:  python3-sphinx

BuildRequires:  python3-setuptools
BuildRequires:  python3-devel
BuildRequires:  python3-six

%generate_buildrequires
%pyproject_buildrequires -t

%description
This extension provides an automated way to document CLI programs.
It scans ArgumentParser objects and then expands it into a set of
program and option directives.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

Requires:       python3-sphinx >= 1.2
Requires:       python3-six
%description -n python3-%{pypi_name}
This extension provides an automated way to document CLI programs.
It scans ArgumentParser objects and then expands it into a set of
program and option directives.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p 1 -n %{pypi_shortname}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
# Must do the subpackages' install first because the scripts in /usr/bin are
# overwritten with every setup.py install.
%py3_install

%check
%{py3_test_envvars} %{python3} -m unittest -v sphinxcontrib.autoprogram.suite

%files -n python3-%{pypi_name}
%doc README.rst
%license LICENSE
%{python3_sitelib}/sphinxcontrib
%{python3_sitelib}/sphinxcontrib_autoprogram-%{version}-py%{python3_version}-nspkg.pth
%{python3_sitelib}/sphinxcontrib_autoprogram-%{version}-py%{python3_version}.egg-info

%changelog
%autochangelog
