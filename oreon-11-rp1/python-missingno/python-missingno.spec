%global source0_hash 48be5708007e304432528cfe458eaf3f15c6cab15cd1d5065721e084d887d964
%bcond_without tests
%global desc %{expand: \
Messy datasets? Missing values? missingno provides a small toolset
of flexible and easy-to-use missing data visualizations and utilities
that allows you to get a quick visual summary of the completeness
(or lack thereof) of your dataset.}
Name:           python-missingno
Version:        0.5.2
Release:        1%{?dist}
Summary:        Missing data visualization module for Python
License:        MIT
URL:            https://github.com/ResidentMario/missingno
Source0:        https://github.com/ResidentMario/missingno/archive/%{version}/missingno-%{version}.tar.gz
BuildArch:      noarch
ExcludeArch: %{ix86}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-missingno = %{version}-%{release}
# /oreon:deps
%description
%{desc}

%package -n python3-missingno
Summary:        Missing data visualization module for Python
BuildRequires: python3-devel
BuildRequires: python3dist(setuptools)
BuildRequires: quilt
%description -n python3-missingno
%{desc}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n missingno-%{version}

find . -type f -name "*.py" -exec sed -i '/^#![  ]*\/usr\/bin\/env.*$/ d' {} ';'

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-missingno usr/lib/python3*/site-packages/missingno* usr/lib64/python3*/site-packages/missingno* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/missingno* usr/lib64/python3*/site-packages/missingno* usr/bin/*

%check

mkdir -p ~/.config/matplotlib/
echo "backend: Agg" > ~/.config/matplotlib/matplotlibrc
export PYTHONPATH=".:$RPM_BUILD_ROOT/%{python3_sitelib}"
%{pytest} tests/test_util.py
%files
%files -n python3-missingno -f %{oreon_filedir}/python3-missingno.list

%changelog

%autochangelog
