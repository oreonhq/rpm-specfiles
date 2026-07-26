%global source0_hash 9fb7b770c34d449320e47a3c7d792c2e30958a9c9a8466936de20915d31caa75

%global pypi_name pyftdi

Name:           python-%{pypi_name}
Version:        0.57.1
Release:        4%{?dist}
Summary:        Python support for FTDI devices

License:        BSD-3-Clause
URL:            https://github.com/eblot/pyftdi
Source0:        %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
PyFtdi aims at providing a user-space driver for modern FTDI devices.

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  %{py3_dist Sphinx}
BuildRequires:  %{py3_dist sphinx_rtd_theme}
BuildRequires:  %{py3_dist sphinxcontrib-autoprogram}
BuildRequires:  %{py3_dist sphinx-autodoc-typehints}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
PyFtdi aims at providing a user-space driver for modern FTDI devices.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel
pushd .
cd pyftdi/doc
sphinx-build -M html . ../../build -W
rm ../../build/html/.buildinfo
popd

%install
%pyproject_install
# Docs are in module, remove them as they were built to HTML and packaged as such
rm -rf %{buildroot}%{python3_sitelib}/%{pypi_name}/doc %{buildroot}%{python3_sitelib}/%{pypi_name}/INSTALL

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md build/html/*
%{_bindir}/*.py
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}*.dist-info/

%changelog
%autochangelog
