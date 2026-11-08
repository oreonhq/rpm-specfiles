# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name:           orbscli
Version:        1.0.0
Release:        1%{?dist}
Summary:        Oreon Build Service Command Line Interface
License:        GPL-3.0-or-later
URL:            https://tarballs.oreonhq.com/orbscli-%{version}.tar.gz
Source0:        orbscli-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(wheel)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  oreon-rpm-macros

Requires:       python3-rpm
Requires:       git

%description
Interacts with Oreon Build Service and helps with maintenance.

%prep
%autosetup -n orbscli-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files orbscli policy plancmd planner specadd stackbump orespec scan repair chain_metadata cabal repoclosure

%check
%{python3} -c "import orbscli, policy, planner, specadd, plancmd"

%files -f %{pyproject_files}
%{_bindir}/orbscli

%changelog
%autochangelog
