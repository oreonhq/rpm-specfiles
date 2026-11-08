# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 37dd54208da7e1cd875388217d5e00ebd4179249f90fb72437e91a35459a0ad3

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap
%global modname dateutil

Name:           python-%{modname}
Version:        2.9.0.post0
Release:        1%{?dist}
Epoch:          1
Summary:        Powerful extensions to the standard datetime module

# According to the LICENSE file:
# - Apache-2.0 applies to all contributions after 2017-12-01, as well as
#   all contributions that have been re-licensed.
# - BSD-3-Clause applies to all code, even that also covered by Apache-2.0
License:        (Apache-2.0 AND BSD-3-Clause) OR BSD-3-Clause

URL:            https://github.com/dateutil/dateutil
Source0:        https://files.pythonhosted.org/packages/source/p/python-dateutil/python-dateutil-%{version}.tar.gz
Source10:       https://files.pythonhosted.org/packages/source/m/markupsafe/markupsafe-3.0.4.tar.gz

Provides:  deprecated()

# Allow setuptools-scm dependency greater than v8.0
Patch:        relax-setuptools_scm-requires.patch

# Fix dateutil module import in sphinx config file
Patch:        fix-sphinx-import.patch

# Remove ctypes mock from sphinx config file
# seems to be incompatible with Python 3.15
# https://github.com/dateutil/dateutil/issues/1472
Patch:        remove-ctypes-mock.patch

# Fix test compatibility with pytest >= 9.1 (non-Collection parametrize)
# https://github.com/dateutil/dateutil/pull/1523
Patch:        fix-pytest-9.1-parametrize.patch

# when bootstrapping dateutil-freezegun, we cannot run tests
%bcond tests 1

BuildArch:      noarch
BuildRequires:  python3-devel

# For docs
BuildRequires:  make
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3-markupsafe
BuildRequires:  python3dist(sphinx-rtd-theme)

# For tests
%if %{with tests}
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(freezegun)
BuildRequires:  python3dist(hypothesis)
BuildRequires:  python3dist(six)
BuildRequires:  oreon-rpm-macros
%endif

%global _description \
The dateutil module provides powerful extensions to the standard datetime\
module available in Python.

# generated BuildRequires, refresh with: orbscli plan bake
BuildRequires: (python3dist(tomli) if python3-devel < 3.11)
BuildRequires: pyproject-rpm-macros
BuildRequires: python3dist(packaging)
BuildRequires: python3dist(pip) >= 19
BuildRequires: python3dist(setuptools)
BuildRequires: python3dist(setuptools-scm)
BuildRequires: python3dist(six) >= 1.5
BuildRequires: python3dist(wheel)

%description %_description


%package -n python3-%{modname}
Summary:        %summary
Requires:       tzdata

Provides:  deprecated()

%description -n python3-%{modname}  %_description


%package doc
Summary: API documentation for python-dateutil
%description doc
This package contains %{summary}.


%prep
%oreon_sha256

%autosetup -p1 -n %{name}-%{version}

iconv --from=ISO-8859-1 --to=UTF-8 NEWS > NEWS.new
mv NEWS.new NEWS


%build
%pyproject_wheel
echo '2e9ad7dd851bf45fab9f75cbff4cb493fee9979e8d8c7c9c3ee119022518edd6  %{SOURCE10}' | sha256sum -c -
tar -xzf %{SOURCE10} -C %{_builddir}
export PYTHONPATH="%{_builddir}/markupsafe-3.0.4/src${PYTHONPATH:+:$PYTHONPATH}"
make -C docs html


%install
%pyproject_install
%pyproject_save_files %{modname} -l


%check
%pyproject_check_import -e dateutil.tz.win -e dateutil.tzwin

%if %{with tests}
# test_tzlocal_local_time_trim_colon fails in Copr only :/
%pytest -W ignore::pytest.PytestUnknownMarkWarning \
  %{?copr_projectname:-k "not test_tzlocal_local_time_trim_colon"}
%endif


%files -n python3-%{modname} -f %{pyproject_files}
%doc NEWS README.rst


%files doc
%license LICENSE
%doc docs/_build/html


