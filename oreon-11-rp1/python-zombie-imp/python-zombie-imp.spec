%global source0_hash c888321fbd942f1a3205c0923a2f21d3ed6e5ab6c2f6237abf43c147f37df97f
Name:           python-zombie-imp
Version:        0.0.4
Release:        1%{?dist}
Summary:        A copy of the `imp` module that was removed in Python 3.12
License:        Python-2.0.1
URL:            https://github.com/encukou/zombie-imp
Source0:        https://files.pythonhosted.org/packages/source/z/zombie_imp/zombie_imp-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 61.0
Requires:       python3-zombie-imp = %{version}-%{release}
# /oreon:deps
%description

%package -n python3-zombie-imp
Summary:        A copy of the `imp` module that was removed in Python 3.12
Provides:       deprecated()
%description -n python3-zombie-imp

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir zombie_imp-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-zombie-imp usr/lib/python3*/site-packages/zombie_imp* usr/lib64/python3*/site-packages/zombie_imp* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/zombie_imp* usr/lib64/python3*/site-packages/zombie_imp* usr/bin/*

%check

%tox
%files
%files -n python3-zombie-imp -f %{oreon_filedir}/python3-zombie-imp.list

%changelog

%autochangelog
