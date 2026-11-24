# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 5c5d0a3b48ceee0b48485e0c26037c0acd7d29765ca3fbb5cb3831d347423220
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%global srcname ptyprocess

%bcond_without tests

Name:           python-ptyprocess
Version:        0.7.0
Release:        1%{?dist}
Summary:        Run a subprocess in a pseudo terminal

License:        ISC
URL:            https://github.com/pexpect/ptyprocess
Source0:        https://files.pythonhosted.org/packages/source/p/ptyprocess/ptyprocess-%{version}.tar.gz
Patch0:         75.patch
Patch1:         84.patch

BuildArch:      noarch

%description
Launch a subprocess in a pseudo terminal (pty), and interact with both the
process and its pty.

%package -n python3-ptyprocess
Summary:        Run a subprocess in a pseudo terminal
%{?python_provide:%python_provide python3-%{srcname}}
BuildRequires: oreon-rpm-macros
BuildRequires:  python3-devel
%if %{with tests}
BuildRequires:  python3-pytest
%endif

%description -n python3-ptyprocess
Launch a subprocess in a pseudo terminal (pty), and interact with both the
process and its pty.

%prep
%oreon_sha256
%autosetup -p1 -n ptyprocess-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files ptyprocess

%if %{with tests}
%check
%{__python3} -m pytest -v
%endif

%files -n python3-ptyprocess -f %{pyproject_files}
%license LICENSE
%doc README.rst

%changelog
%autochangelog
