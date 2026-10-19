%global source0_hash f9f336f2c815198bf4d0c9b949c7147bdff7449b97b26bd5275f2019f5861401
Name:           python-absl-py
Version:        2.5.0
Release:        1%{?dist}
Summary:        Abseil Python Common Libraries
License:        Apache-2.0
URL:            https://github.com/abseil/abseil-py/
Source0:        https://github.com/abseil/abseil-py//archive/v%{version}/abseil-py-%{version}.tar.gz
BuildArch:      noarch
%global common_description %{expand:
This repository is a collection of Python library code for building Python
applications. The code is collected from Google’s own Python code base, and has
been extensively tested and used in production.
Features:
  • Simple application startup
  • Distributed commandline flags system
  • Custom logging module with additional features
  • Testing utilities}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(hatchling) >= 1.26
Requires:       python3-absl-py = %{version}-%{release}
# /oreon:deps
%description %{common_description}

%package -n     python3-absl-py
Summary:        Abseil Python Common Libraries
%py_provides python3-absl
%description -n python3-absl-py %{common_description}

# Since we cannot run the full upstream test suite (see comments below), we
# start with the implicit default import “smoke test.” Then:
%prep
%global oreon_srcdir abseil-py-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-absl-py usr/lib/python3*/site-packages/absl_py* usr/lib64/python3*/site-packages/absl_py* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/absl_py* usr/lib64/python3*/site-packages/absl_py* usr/bin/*

%check

%{py3_test_envvars} %{python3} smoke_tests/sample_app.py --echo smoke 2>&1 |
  grep -F 'echo is smoke.'
%{py3_test_envvars} %{python3} smoke_tests/sample_test.py |
  grep -Fq 'msg_for_test'
%files
%files -n python3-absl-py -f %{oreon_filedir}/python3-absl-py.list

%changelog

%autochangelog
