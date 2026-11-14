# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: MIT

%global source0_hash 8809a4df6fe08279b39a8890669506ed3158e0617855ac9aff098fcbe772ae4c

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: python3-pyproject-metadata
Version: 0.12.1
Release: 1%{?dist}
Summary: Dataclass for PEP 621 metadata
License: MIT
URL: https://github.com/pypa/pyproject-metadata
Source0: https://files.pythonhosted.org/packages/4f/76/1cae539918a7b1746d624c2f01560b793c22cd8c081157505bb9bbf0e34d/pyproject_metadata-%{version}.tar.gz
BuildArch: noarch
Provides: python3dist(pyproject-metadata) = %{version}

BuildRequires: oreon-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-build
BuildRequires: python3-installer
BuildRequires: python3-flit-core
Requires: python3
Requires: python3-packaging

%description
PEP 621 metadata as a typed dataclass.

%prep
%oreon_sha256
%autosetup -n pyproject_metadata-%{version}

%build
python3 -m build --wheel --no-isolation

%install
python3 -m installer --destdir %{buildroot} dist/*.whl
%oreon_filelist

%check
python3 -c 'import pyproject_metadata'

%files -f %{_builddir}/%{name}.files

%changelog
%autochangelog
