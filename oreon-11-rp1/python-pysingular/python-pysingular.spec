%global source0_hash cda8c9df3a365cc8eed901c5d76ed5757bd4c49a68225c345954afea91941f18
Name:           python-pysingular
Version:        0.9.7
Release:        1%{?dist}
Summary:        Python interface to Singular
License:        GPL-2.0-or-later
URL:            https://github.com/sebasguts/PySingular
VCS:            git:%{url}.git
Source0:        https://github.com/sebasguts/PySingular/archive/v%{version}/PySingular-%{version}.tar.gz
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-pysingular = %{version}-%{release}
# /oreon:deps
%description
This package contains a basic interface to call Singular from python.  It is
meant to be used in the Jupyter interface to Singular.

%package     -n python3-pysingular
Summary:        Python 3 interface to Singular
%description -n python3-pysingular
This package contains a basic interface to call Singular from python.  It is
meant to be used in the Jupyter interface to Singular.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir PySingular-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pysingular usr/lib/python3*/site-packages/pysingular* usr/lib64/python3*/site-packages/pysingular* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pysingular* usr/lib64/python3*/site-packages/pysingular* usr/bin/*

%files
%files -n python3-pysingular -f %{oreon_filedir}/python3-pysingular.list

%changelog

%autochangelog
