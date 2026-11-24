# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash b1ac1515e84fa4c31dc10ad1a7800c0f305a1a3887b4b4e6e1980ceda4f50173
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name:           python-sphinxygen
Version:        1.0.12
Release:        1%{?dist}
Summary:        A script to read Doxygen XML output and emit ReST for Sphinx

License:        ISC
URL:            https://gitlab.com/drobilla/sphinxygen
Source0:        %{url}/-/archive/v%{version}/sphinxygen-v%{version}.tar.gz

Patch:          0001-Fix-tests-with-doxygen-1.14.patch

BuildRequires: oreon-rpm-macros
BuildRequires:  sed
BuildRequires:  python3-devel
%if 0%{?fedora}
BuildRequires:  doxygen
BuildRequires:  python3dist(html5lib)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(sphinx)
%endif

BuildArch: noarch

%global _description %{expand:
Sphinxygen is a Python module/script that generates Sphinx markup to describe
a C API, from an XML description extracted by Doxygen.}

%description %_description

%package -n python3-sphinxygen
Summary:        %{summary}

%description -n python3-sphinxygen %_description

%prep
%oreon_sha256
%autosetup -p1 -n sphinxygen-v%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files sphinxygen
chmod 644 %{buildroot}%{python3_sitelib}/sphinxygen/sphinxygen.py
sed -i '/^#!\/usr\/bin/d' %{buildroot}%{python3_sitelib}/sphinxygen/sphinxygen.py

mkdir -p %{buildroot}%{_mandir}/man1
install -Dpm 0644 doc/sphinxygen.1 -t %{buildroot}%{_mandir}/man1/

%check
%if 0%{?fedora}
%pytest test
%else
%pyproject_check_import
%endif

%files -n python3-sphinxygen -f %{pyproject_files}
%doc README.md NEWS
%{_bindir}/sphinxygen
%{_mandir}/man1/sphinxygen.1*
 
%changelog
%autochangelog
