%global source0_hash 9e6c12b10e4adc9271f7331da4b673d0cb9a6c9e48bba00cd5b7954ada1690a5
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
Source0:        https://files.pythonhosted.org/packages/source/p/python-pcicrawler/python-pcicrawler-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  sed
# /oreon:deps
%description
%{common_description}

%package -n     %{pypi_name}
Summary:        Display/filter/export information about PCI or PCI Express devices
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
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n pcicrawler -f %{oreon_filedir}/pcicrawler.list

%changelog

%autochangelog
