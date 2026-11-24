# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash d03ceb89cb322a8fd706d4fb91940737b6642aa36998fe130a9bc96c985eff32
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name:           python-attrs
Version:        26.1.0
Release:        1%{?dist}
Summary:        Classes Without Boilerplate

License:        MIT
URL:            https://github.com/python-attrs/attrs
Source0:        https://files.pythonhosted.org/packages/source/a/attrs/attrs-26.1.0.tar.gz

BuildArch:      noarch
BuildRequires: oreon-rpm-macros
BuildRequires:  python3-devel

%description
attrs is a Python package that lets you write classes without boilerplate.

%package -n     python3-attrs
Summary:        %{summary}

%description -n python3-attrs
attrs is a Python package that lets you write classes without boilerplate.

%prep
%oreon_sha256
%autosetup -p1 -n attrs-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files '*' +auto

%check
%_pyproject_check_import_allow_no_modules -t

%files -n python3-attrs -f %{pyproject_files}

%changelog
%autochangelog
