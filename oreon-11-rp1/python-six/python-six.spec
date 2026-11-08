# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash ff70335d468e7eb6ec65b95b99d3a2836546063f63acc5171de367e834932a81

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap
# tests are enabled by default
%bcond_without tests

Name:           python-six
Version:        1.17.0
Release:        2%{?dist}
Summary:        Python 2 and 3 compatibility utilities

# SPDX
License:        MIT
URL:            https://github.com/benjaminp/six
Source0:        https://files.pythonhosted.org/packages/source/s/six/six-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros

%if %{with tests}
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-tkinter
BuildRequires:  oreon-rpm-macros
%endif

%global _description %{expand:
Six is a Python 2 and 3 compatibility library. It provides utility functions
for smoothing over the differences between the Python versions with the goal
of writing Python code that is compatible on both Python versions.}

# generated BuildRequires, refresh with: orbscli plan bake
BuildRequires: python3-devel
BuildRequires: python3dist(packaging)
BuildRequires: python3dist(pip) >= 19
BuildRequires: python3dist(setuptools) >= 40.8

%description %{_description}


%package -n python%{python3_pkgversion}-six
Summary:        %{summary}

%description -n python%{python3_pkgversion}-six %{_description}


%prep
%oreon_sha256

%autosetup -p1 -n six-%{version}


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l six


%check
%pyproject_check_import
%if %{with tests}
%pytest
%endif


%files -n python%{python3_pkgversion}-six -f %{pyproject_files}
%doc README.rst documentation/index.rst


