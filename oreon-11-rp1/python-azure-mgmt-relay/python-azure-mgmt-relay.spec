%global source0_hash d9f987cf2998b8a354f331b2a71082c049193f1e1cd345812e14b9b821365acb

%global         srcname     azure-mgmt-relay

Name:           python-%{srcname}
Version:        0.1.0
Release:        %autorelease
Summary:        Microsoft Azure Relay Client Library for Python
License:        MIT
URL:            https://pypi.org/project/%{srcname}/
Source0:        %{pypi_source %{srcname} %{version} zip}

BuildArch:      noarch

Epoch:          1

BuildRequires:  python3-devel

%global _description %{expand:
Microsoft Azure Relay Client Library for Python}

%description %{_description}

%package -n python3-%{srcname}
Summary:        %{summary}
%description -n python3-%{srcname} %{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}

# Remove the custom wheel builder.
sed -i '/azure-namespace-package/d' setup.cfg
rm -f azure_bdist_wheel.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

# PEP 420 allows implicit namespace packaging without additional __init__.py
# files. Remove unneccessary __init__.py that conflicts with other packages.
rm -rf %{buildroot}%{python3_sitelib}/azure/{__init__.py,__pycache__}
rm -rf %{buildroot}%{python3_sitelib}/azure/mgmt/{__init__.py,__pycache__}

%pyproject_save_files azure

%check
%pyproject_check_import

%if %{with tests}
%pytest
%endif

%files -n python3-%{srcname}
%doc README.rst HISTORY.rst
%{python3_sitelib}/azure/mgmt/relay
%{python3_sitelib}/azure_mgmt_relay-%{version}.dist-info

%changelog
%autochangelog
