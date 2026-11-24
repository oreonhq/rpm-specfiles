# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 814da89a9a7603b7e4d85c487c7381656fa83632f20065e5ed782ab1dbbb5083
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%global _description %{expand:
An extension to use emoji codes in your Sphinx documentation.}

Name:           python-sphinxemoji
Version:        0.3.2
Release:        %{autorelease}
Summary:        Use emoji codes in your Sphinx documentation

License:        BSD-3-Clause
URL:            https://pypi.org/pypi/sphinxemoji
Source0:        %{pypi_source sphinxemoji}

BuildArch:      noarch

%description %_description

%package -n python3-sphinxemoji
Summary:        %{summary}
BuildRequires: oreon-rpm-macros
BuildRequires:  python3-devel

%description -n python3-sphinxemoji %_description

%prep
%oreon_sha256
%autosetup -n sphinxemoji-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files sphinxemoji

%check

%files -n python3-sphinxemoji -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
