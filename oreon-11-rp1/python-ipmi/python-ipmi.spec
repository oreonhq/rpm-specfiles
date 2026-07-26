%global source0_hash c0428bbdfd42969e9586cb73b21c276fa9686cbac4e2bf4dd27669c533065149

%global pypi_name python-ipmi
%global srcname ipmi

Name:           python-%{srcname}
Version:        0.5.5
Release:        8%{?dist}
Summary:        Pure python IPMI library
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            https://github.com/kontron/python-ipmi
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%?python_enable_dependency_generator

BuildRequires: python3-devel
BuildRequires: python3dist(markdown)
BuildRequires: python3dist(setuptools)

%description
Pure Python IPMI Library.

%package -n     python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
Pure Python IPMI Library.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version} -p1
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

find . -type f -name "*.py" -exec sed -i '/^#![  ]*\/usr\/bin\/env.*$/ d' {} ';'

%build
%py3_build

%install
%py3_install 

%check
export PYTHONPATH=$RPM_BUILD_ROOT/%{python3_sitelib}

%files -n python3-%{srcname}
%doc README.rst
%{_bindir}/ipmitool.py
%{python3_sitelib}/pyipmi
%{python3_sitelib}/*-py%{python3_version}.egg-info

%changelog
%autochangelog
