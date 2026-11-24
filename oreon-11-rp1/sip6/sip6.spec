# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 009944b78e896c52f00c894fd2ff7917145d69ca4fceb5d4ebc89a92efd571b8
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%global pypi_name sip

Name:           sip6
Version:        6.17.3
Release:        %{autorelease}
Summary:        SIP - Python/C++ Bindings Generator
%py_provides    python3-sip6

License:        BSD-2-Clause
URL:            https://github.com/Python-SIP/sip
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires: oreon-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  gcc-c++

BuildRequires:  python3-pytest

%global _description %{expand:
SIP is a collection of tools that makes it very easy to create Python bindings
for C and C++ libraries.  It was originally developed in 1998 to create PyQt,
the Python bindings for the Qt toolkit, but can be used to create bindings for
any C or C++ library.  For example it is also used to generate wxPython, the
Python bindings for wxWidgets.}

%description %_description

%prep
%oreon_sha256
%autosetup -n %{pypi_name}-%{version} -p 1

%generate_buildrequires
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_buildrequires

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l sipbuild

%check
%pytest

%files -f %{pyproject_files}
%doc README.md
%{_bindir}/sip*

%changelog
%autochangelog
