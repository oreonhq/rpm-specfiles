%global source0_hash 130a5daceab9ad534924252ddf70482aa2c96662b3a3825a7d30981d03b76a26
Name:           python-logfury
Version:        1.0.1
Release:        20%{?dist}
Summary:        Library for logging of method calls for Python
License:        BSD-3-Clause
URL:            https://github.com/ppolewicz/logfury
Source0:        https://files.pythonhosted.org/packages/source/l/logfury/logfury-%{version}.tar.gz
BuildArch:      noarch
Patch0:         relax-setuptools_scm.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-logfury = %{version}-%{release}
# /oreon:deps
%description
%{summary}.

%package -n python3-logfury
Summary:        Library for logging of method calls for Python
%description -n python3-logfury
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir logfury-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-logfury usr/lib/python3*/site-packages/logfury* usr/lib64/python3*/site-packages/logfury* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/logfury* usr/lib64/python3*/site-packages/logfury* usr/bin/*

%check

%pyproject_check_import
%files
%files -n python3-logfury -f %{oreon_filedir}/python3-logfury.list

%changelog

%autochangelog
