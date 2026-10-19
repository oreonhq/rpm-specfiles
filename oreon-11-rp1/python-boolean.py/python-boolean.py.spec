%global source0_hash 60cbc4bad079753721d32649545505362c754e121570ada4658b852a3a318d95
%global pypi_name boolean.py
Name:           python-%{pypi_name}
Version:        5.0
Release:        1%{?dist}
Summary:        Define boolean algebras, and create and parse boolean expressions
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/bastikr/boolean.py
Source0:        https://files.pythonhosted.org/packages/source/b/boolean_py/boolean_py-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-boolean.py = %{version}-%{release}
# /oreon:deps
%description

%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        Define boolean algebras, and create and parse boolean expressions
%description -n python%{python3_pkgversion}-%{pypi_name}

Python 3 version.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir boolean_py-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles main usr/lib/python3*/site-packages/boolean.py* usr/lib64/python3*/site-packages/boolean.py* usr/bin/*

%check

%pyproject_check_import
%pytest
%files
%files -n python3-boolean.py -f %{oreon_filedir}/python3-boolean.py.list

%changelog

%autochangelog
