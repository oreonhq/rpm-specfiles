%global source0_hash 72b3bde64e5d778694b0cf68178aed03d15e15477116add3fb773e581f9518ff
Name:           python-deprecation
Version:        2.1.0
Release:        1%{?dist}
Summary:        A library to handle automated deprecations
License:        Apache-2.0
URL:            https://deprecation.readthedocs.io/
Source0:        https://files.pythonhosted.org/packages/source/d/deprecation/deprecation-%{version}.tar.gz
Patch:          deprecation-2.1.0-unittest2.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-deprecation = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-deprecation
Summary:        A library to handle automated deprecations
%description -n python3-deprecation

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n deprecation-%{version} -p1
# Remove pre-built HTML documentation to show that its pre-compiled and
# pre-minified JavaScript is not packaged.
rm -rv docs/_build/

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-deprecation usr/lib/python3*/site-packages/deprecation* usr/lib64/python3*/site-packages/deprecation* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/deprecation* usr/lib64/python3*/site-packages/deprecation* usr/bin/*

%check

%{py3_test_envvars} %{python3} -m unittest discover -v
%files
%files -n python3-deprecation -f %{oreon_filedir}/python3-deprecation.list

%changelog

%autochangelog
