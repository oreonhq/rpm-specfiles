# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 94892b2192a4919f995654d3547b10fa270d14c4284abba397d180c651b31991


%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap
Name:           pyproject-rpm-macros
Summary:        RPM macros for PEP 517 Python packages
# SPDX
License:        MIT

%bcond tests 1
%bcond pytest_xdist 1
%bcond tox_tests 1

# The idea is to follow the spirit of semver
# Given version X.Y.Z:
#   Increment X and reset Y.Z when there is a *major* incompatibility
#   Increment Y and reset Z when new macros or features are added
#   Increment Z when this is a bugfix or a cosmetic change
# Dropping support for EOL Fedoras is *not* considered a breaking change
Version:        1.24.0
Release:        1%{?dist}

# Macro files
Source0:        macros.pyproject
Source1:        macros.aaa-pyproject-srpm

# Implementation files, Python
Source2:        pyproject_buildrequires.py
Source3:        pyproject_convert.py
Source4:        pyproject_dependency_overrides.py
Source5:        pyproject_patch_metadata.py
Source6:        pyproject_preprocess_record.py
Source7:        pyproject_requirements_txt.py
Source8:        pyproject_save_files.py
Source9:        pyproject_verify_license.py
Source10:        pyproject_wheel.py

# Implementation files, Lua
Source11:        pyproject_getopt.lua

# Tests
Source12:        compare_mandata.py
Source13:        test_dependency_overrides.py
Source14:        test_pyproject_buildrequires.py
Source15:        test_pyproject_evals.py
Source16:        test_pyproject_getopt.lua
Source17:        test_pyproject_getopt_consistency.py
Source18:        test_pyproject_getopt_parser.py
Source19:        test_pyproject_requirements_txt.py
Source20:        test_pyproject_save_files.py
Source21:        test_pyproject_verify_license.py

# Test data
Source22:        pyproject_buildrequires_testcases.yaml
Source23:        pyproject_save_files_test_data.yaml
Source24:        test_RECORD

# Metadata
Source25:        README.md
Source26:        LICENSE

URL:            https://src.fedoraproject.org/rpms/pyproject-rpm-macros

BuildArch:      noarch

%if %{with tests}
BuildRequires:  python3dist(pytest)
%if %{with pytest_xdist}
BuildRequires:  python3dist(pytest-xdist)
%endif
BuildRequires:  python3dist(pyyaml)
BuildRequires:  python3dist(packaging)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
%if %{with tox_tests}
BuildRequires:  python3dist(tox-current-env) >= 0.0.16
%endif
BuildRequires:  (python3dist(wheel) if python3dist(setuptools) < 71)
BuildRequires:  (python3dist(tomli) if python3 < 3.11)
%endif

# We build on top of those:
BuildRequires:  python-rpm-macros
BuildRequires:  python-srpm-macros
BuildRequires:  python3-rpm-macros
Requires:       python-rpm-macros
Requires:       python-srpm-macros
Requires:       python3-rpm-macros
Requires:       pyproject-srpm-macros = %{?epoch:%{epoch}:}%{version}-%{release}

# We use the following tools outside of coreutils
Requires:       /usr/bin/find
Requires:       /usr/bin/sed

# This package requires the %%generate_buildrequires functionality.
# It has been introduced in RPM 4.15 (4.14.90 is the alpha of 4.15).
# What we need is rpmlib(DynamicBuildRequires), but that is impossible to (Build)Require.
# Also, we need to avoid 4.19.90..4.19.91-7 due to rhbz#2284187
Requires:       ((rpm-build >= 4.14.90 with (rpm-build < 4.19.90 or rpm-build >= 4.19.91-8)) if rpm-build)
BuildRequires:  rpm-build >= 4.14.90
BuildRequires:  oreon-rpm-macros

%description
These macros allow projects that follow the Python packaging specifications
to be packaged as RPMs.

They work for:

* traditional Setuptools-based projects that use the setup.py file,
* newer Setuptools-based projects that have a setup.cfg file,
* general Python projects that use the PEP 517 pyproject.toml file
  (which allows using any build system, such as setuptools, flit or poetry).

These macros replace %%py3_build and %%py3_install,
which only work with setup.py.


%package -n pyproject-srpm-macros
Summary:        Minimal implementation of %%pyproject_buildrequires
Requires:       (pyproject-rpm-macros = %{?epoch:%{epoch}:}%{version}-%{release} if pyproject-rpm-macros)
Requires:       (rpm-build >= 4.14.90 if rpm-build)

%description -n pyproject-srpm-macros
This package contains a minimal implementation of %%pyproject_buildrequires.
When used in %%generate_buildrequires, it will generate BuildRequires
for pyproject-rpm-macros. When both packages are installed, the full version
takes precedence.


%prep
%oreon_sha256

# Allows working on file names, as sources have no meaningful numbers
%setup -c -T
cp -p %{sources} .

%generate_buildrequires
# nothing to do, this is here just to assert we have that functionality

%build
# nothing to do, sources are not buildable

%install
mkdir -p %{buildroot}%{_rpmmacrodir}
mkdir -p %{buildroot}%{_rpmconfigdir}/oreon
mkdir -p %{buildroot}%{_rpmluadir}/oreon/rpm
install -pm 644 macros.pyproject %{buildroot}%{_rpmmacrodir}/
install -pm 644 macros.aaa-pyproject-srpm %{buildroot}%{_rpmmacrodir}/
install -pm 644 pyproject_getopt.lua %{buildroot}%{_rpmluadir}/oreon/rpm/
install -pm 644 pyproject_buildrequires.py %{buildroot}%{_rpmconfigdir}/oreon/
install -pm 644 pyproject_convert.py %{buildroot}%{_rpmconfigdir}/oreon/
install -pm 644 pyproject_save_files.py  %{buildroot}%{_rpmconfigdir}/oreon/
install -pm 644 pyproject_preprocess_record.py %{buildroot}%{_rpmconfigdir}/oreon/
install -pm 644 pyproject_requirements_txt.py %{buildroot}%{_rpmconfigdir}/oreon/
install -pm 644 pyproject_wheel.py %{buildroot}%{_rpmconfigdir}/oreon/
install -pm 644 pyproject_patch_metadata.py %{buildroot}%{_rpmconfigdir}/oreon/
install -pm 644 pyproject_dependency_overrides.py %{buildroot}%{_rpmconfigdir}/oreon/
install -pm 644 pyproject_verify_license.py %{buildroot}%{_rpmconfigdir}/oreon/


%if %{with tests}
%check
export HOSTNAME="rpmbuild"  # to speedup tox in network-less mock, see rhbz#1856356
%pytest -vv --doctest-modules %{?with_pytest_xdist:-n auto} %{!?with_tox_tests:-k "not tox"}

# brp-compress is provided as an argument to get the right directory macro expansion
%{python3} compare_mandata.py -f %{_rpmconfigdir}/brp-compress
%endif


%files
%{_rpmmacrodir}/macros.pyproject
%{_rpmconfigdir}/oreon/pyproject_buildrequires.py
%{_rpmconfigdir}/oreon/pyproject_convert.py
%{_rpmconfigdir}/oreon/pyproject_save_files.py
%{_rpmconfigdir}/oreon/pyproject_preprocess_record.py
%{_rpmconfigdir}/oreon/pyproject_requirements_txt.py
%{_rpmconfigdir}/oreon/pyproject_wheel.py
%{_rpmconfigdir}/oreon/pyproject_patch_metadata.py
%{_rpmconfigdir}/oreon/pyproject_dependency_overrides.py
%{_rpmconfigdir}/oreon/pyproject_verify_license.py
%{_rpmluadir}/oreon/rpm/pyproject_getopt.lua

%doc README.md
%license LICENSE

%files -n pyproject-srpm-macros
%{_rpmmacrodir}/macros.aaa-pyproject-srpm
%license LICENSE


