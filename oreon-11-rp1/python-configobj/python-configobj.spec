%global source0_hash 03c881bbf23aa07bccf1b837005975993c4ab4427ba57f959afdd9d1a2386848
Name:           python-configobj
Version:        5.0.9
Release:        1%{?dist}
Summary:        Config file reading, writing, and validation
License:        BSD-3-Clause
URL:            http://configobj.readthedocs.org/
Source0:        https://pypi.python.org/packages/source/c/configobj/configobj-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-configobj = %{version}-%{release}
# /oreon:deps
%description

%package     -n python%{python3_pkgversion}-configobj
Summary:        Config file reading, writing, and validation
%description -n python%{python3_pkgversion}-configobj

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir configobj-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles main usr/lib/python3*/site-packages/configobj* usr/lib64/python3*/site-packages/configobj* usr/bin/*

%check

%pyproject_check_import
export PYTHONPATH=$(pwd)/build/lib
%{__python3} src/tests/configobj_doctests.py
%{__python3} -m configobj.validate
%pytest -c setup.cfg --color=yes
%files
%files -n python3-configobj -f %{oreon_filedir}/python3-configobj.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.0.9-9
- Prepare for Oreon 11 (RP1)
