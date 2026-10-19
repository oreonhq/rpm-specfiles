%global source0_hash dc7051a0db5f2bd48665a990d3ec1cc305a466a77358ca4492826f41f283601e
%global debug_package %{nil}
%global pypi_name crcmod
%global pypi_version 1.7
%global common_description %{expand:
The software in this package is a Python module for generating objects that
compute the Cyclic Redundancy Check (CRC).}
Name:           python-%{pypi_name}
Version:        %{pypi_version}
Release:        1%{?dist}
Summary:        CRC Generator
License:        MIT
URL:            http://crcmod.sourceforge.net/
Source0:        https://files.pythonhosted.org/packages/source/p/python-crcmod/python-crcmod-%{version}.tar.gz
# oreon:deps
BuildRequires:  python3-devel
BuildRequires:  python3-docs
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(sphinx)
BuildRequires:  sed
# /oreon:deps
%description
%{common_description}

%package -n     python3-%{pypi_name}
Summary:        CRC Generator
%description -n python3-%{pypi_name}
%{common_description}

%package -n python-%{pypi_name}-doc
Summary:        crcmod documentation
BuildArch:      noarch
%description -n python-%{pypi_name}-doc
Documentation for crcmod

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{pypi_version}
# Use local intersphinx inventory
sed -r \
    -e "s|\{'http://docs.python.org/': None\}|{'python': ('%{_docdir}/python3-docs/html', None)}|" \
    -i docs/source/conf.py

%build

%py3_build
PYTHONPATH=${PWD} sphinx-build-3 docs/source html
rm -rf html/.{doctrees,buildinfo}
%install
%py3_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

for test in test/*; do
  PYTHONPATH="%{buildroot}%{python3_sitearch}" %python3 $test
done
%files -f %{oreon_filedir}/main.list
%files -n python3-crcmod -f %{oreon_filedir}/python3-crcmod.list
%files -n python-crcmod-doc -f %{oreon_filedir}/python-crcmod-doc.list

%changelog

%autochangelog
