%global source0_hash a39ef3541d40d6edc972efb1860af195b540e5870fbc17bb707ac40efa389ab8
Name:           python-gitapi
Version:        1.1.0
Release:        1%{?dist}
Summary:        Pure-Python API to git, which uses the command-line interface
License:        MIT
URL:            https://bitbucket.org/haard/gitapi
Source0:        https://pypi.python.org/packages/source/g/gitapi/gitapi-%{version}a2.tar.gz
Source1:        LICENSE
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-gitapi = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-gitapi
Summary:        Pure-Python API to git, which uses the command-line interface
BuildRequires:  python3-devel
Requires:       git
%description -n python3-gitapi
Pure-Python API to git, which uses the command-line interface.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n gitapi-%{version}a2
cp %{SOURCE1} .
# Remove egg
# Apply patches
sed -i 's/\r$//' gitapi/testgitapi.py
# Correct end of line encoding for README.rst
sed -i 's/\r$//' README.rst

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-gitapi usr/lib/python3*/site-packages/gitapi* usr/lib64/python3*/site-packages/gitapi* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/gitapi* usr/lib64/python3*/site-packages/gitapi* usr/bin/*

%check

%pyproject_check_import
%files
%files -n python3-gitapi -f %{oreon_filedir}/python3-gitapi.list

%changelog

%autochangelog
