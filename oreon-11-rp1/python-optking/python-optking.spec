%global source0_hash 05aa6079f4cebef9fbe8cc36c7315123afeb53fb3feed959f98d963060e1085c
%{?!oreon_bootstrap:%global oreon_bootstrap %{nil}}
%oreon_bootstrap
%bcond tests 1
Name:           python-optking
Version:        0.3.0
Release:        6%{?dist}
Summary:        A Python version of the PSI4 geometry optimization program by R.A. King
License:        BSD-3-Clause
URL:            https://github.com/psi-rking/optking
Source0:        https://github.com/psi-rking/optking/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
%if %{with tests}
%endif
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-optking = %{version}-%{release}
# /oreon:deps
%description
optking (also known as pyoptking) is a rewrite of the c++ optking
module in psi4. This rewrite was undertaken to enable future
development and for use with recent interoperability efforts
(e.g. MolSSI QCArchive and QCDB). optking is focused on optimization
of molecular geometries: finding minima, transition states, and
reaction paths. Current work is focused especially on expanding the
reaction path methods.

%package -n     python3-optking
Summary:        A Python version of the PSI4 geometry optimization program by R.A. King
%{?python_provide:%python_provide python3-optking}
%description -n python3-optking
optking (also known as pyoptking) is a rewrite of the c++ optking
module in psi4. This rewrite was undertaken to enable future
development and for use with recent interoperability efforts
(e.g. MolSSI QCArchive and QCDB). optking is focused on optimization
of molecular geometries: finding minima, transition states, and
reaction paths. Current work is focused especially on expanding the
reaction path methods.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n optking-%{version}
# Remove bundled egg-info
rm -rf optking.*-info
# Remove test that requires internet access to pubchem
\rm optking/tests/test_frozen_internals.py

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-optking usr/lib/python3*/site-packages/optking* usr/lib64/python3*/site-packages/optking* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/optking* usr/lib64/python3*/site-packages/optking* usr/bin/*

%check

%pyproject_check_import -e *.tests.*
%if %{with tests}
%pytest -m "not long" optking
%endif
%files
%files -n python3-optking -f %{oreon_filedir}/python3-optking.list

%changelog

%autochangelog
