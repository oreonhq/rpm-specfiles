# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash d10493b310df657ec6e719f2c3e49a2e9189bfe065e3ba4b9c339c586979d5bc
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name:           python-markupsafe
Version:        3.0.4
Release:        %{autorelease}
Summary:        Implements a XML/HTML/XHTML Markup safe string for Python
License:        BSD-3-Clause
URL:            https://palletsprojects.com/p/markupsafe/
Source0:        https://github.com/pallets/markupsafe/archive/%{version}/markupsafe-%{version}.tar.gz

BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc
BuildRequires:  python3-devel

%global _description %{expand:
MarkupSafe implements a text object that escapes characters so it is
safe to use in HTML and XML. Characters that have special meanings are
replaced so that they display as the actual characters. This mitigates
injection attacks, meaning untrusted user input can safely be displayed
on a page.}

%description %_description

%package -n python3-markupsafe
Summary:        %{summary}

%description -n python3-markupsafe %_description

%prep
%oreon_sha256
%autosetup -n markupsafe-%{version}
echo 'global-exclude *.c' >> MANIFEST.in
%pyproject_patch_dependency pytest-run-parallel:ignore

%generate_buildrequires
%pyproject_buildrequires -g tests

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files markupsafe

%check
%pytest

%files -n python3-markupsafe -f %{pyproject_files}
%doc CHANGES.rst README.md

%changelog
%autochangelog
