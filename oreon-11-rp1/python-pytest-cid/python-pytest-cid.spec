%global source0_hash 3d6fcfe0c9ce4cc3935952b824091e109aa99f98068dd8cf27d0067914681feb
%global pypi_name pytest-cid
%global common_description %{expand:
This module is a plugin for the popular Python testing framework pytest. It
compares data structures containing matching CIDs of different versions and
encoding.}
Name:          python-%{pypi_name}
Version:       1.1.2
Release:        1%{?dist}
BuildArch:     noarch
Summary:        Pytest plugin to compare CIDs
License:       MPL-2.0
URL:           https://github.com/ntninja/pytest-cid
Source0:        https://files.pythonhosted.org/packages/source/p/pytest_cid/pytest_cid-%{version}.tar.gz
Patch1:        python-pytest-cid-0001-Relax-dependencies.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-pytest-cid = %{version}-%{release}
# /oreon:deps
%description %{common_description}

%package -n python3-%{pypi_name}
Summary:        Pytest plugin to compare CIDs
%description -n python3-%{pypi_name} %{common_description}

%prep
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles main usr/lib/python3*/site-packages/pytest_cid* usr/lib64/python3*/site-packages/pytest_cid* usr/bin/*

%check

%pytest
%files
%files -n python3-pytest-cid -f %{oreon_filedir}/python3-pytest-cid.list

%changelog

%autochangelog
