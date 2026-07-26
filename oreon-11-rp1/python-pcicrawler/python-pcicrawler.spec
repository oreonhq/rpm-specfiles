%global source0_hash 9e6c12b10e4adc9271f7331da4b673d0cb9a6c9e48bba00cd5b7954ada1690a5

# Created by pyp2rpm-3.3.5
%global pypi_name pcicrawler

%global common_description %{expand:
pcicrawler is a CLI tool to display/filter/export information about PCI or PCI
Express devices and their topology.}

Name:           python-%{pypi_name}
Version:        1.0.0
Release:        19%{?dist}
Summary:        Display/filter/export information about PCI or PCI Express devices

License:        MIT
URL:            https://github.com/facebook/pcicrawler
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  sed
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
%{common_description}

%package -n     %{pypi_name}
Summary:        %{summary}
%if 0%{?fedora} == 32 || 0%{?rhel} == 8
%py_provides    python3-%{pypi_name}
%endif

%description -n %{pypi_name}
%{common_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info
# Remove unnecessary shebang
sed -e '\|#!/usr/bin/env python|d' -i */*.py

%build
%py3_build

%install
%py3_install

%files -n %{pypi_name}
%doc README.md
%{_bindir}/pcicrawler
%{python3_sitelib}/pci_lib
%{python3_sitelib}/pci_vpd_lib
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
%autochangelog
