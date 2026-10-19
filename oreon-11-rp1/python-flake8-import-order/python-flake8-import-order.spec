%global source0_hash 133b3c55497631e4235074fc98a95078bba817832379f22a31f0ad2455bcb0b2
%global srcname flake8-import-order
%bcond_with pylama
Name:           python-%{srcname}
Version:        0.19.2
Release:        1%{?dist}
Summary:        Flake8 plugin for checking order of imports in Python code
License:        LGPL-3.0-only
URL:            https://github.com/PyCQA/%{srcname}
Source0:        https://files.pythonhosted.org/packages/source/f/flake8_import_order/flake8_import_order-%{version}.tar.gz
Patch0:         flake8-import-order-0.9.2-nolama.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-flake8-import-order = %{version}-%{release}
# /oreon:deps
%description
%{summary}.

%package     -n python%{python3_pkgversion}-%{srcname}
Summary:        Flake8 plugin for checking order of imports in Python code
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-flake8
BuildRequires:  python%{python3_pkgversion}-pycodestyle
BuildRequires:  python%{python3_pkgversion}-asttokens
Requires:       python%{python3_pkgversion}-flake8
Requires:       python%{python3_pkgversion}-pycodestyle
Requires:       python%{python3_pkgversion}-asttokens
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}
%description -n python%{python3_pkgversion}-%{srcname}
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n flake8_import_order-%{version}
%if ! %{with pylama}
%patch -P0 -p1
rm tests/test_pylama_linter.py
%endif

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles main usr/lib/python3*/site-packages/flake8_import_order* usr/lib64/python3*/site-packages/flake8_import_order* usr/bin/*

%check

%if ! %{with pylama}
mv flake8_import_order/pylama_linter.py flake8_import_order/pylama_linter.NOT
%endif
%pytest -v
%files
%files -n python3-flake8-import-order -f %{oreon_filedir}/python3-flake8-import-order.list

%changelog

%autochangelog
