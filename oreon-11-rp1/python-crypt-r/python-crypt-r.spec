%global source0_hash 5bd46ad51f5b7fe5f0ecf49d8ba2cafd6fbd43aa3bb5efbcaa6b44df6340c1a6
Name:           python-crypt-r
Version:        3.13.1
Release:        1%{?dist}
Summary:        A copy of the `crypt` module that was removed in Python 3.13
License:        Python-2.0.1
URL:            https://github.com/fedora-python/crypt_r
Source0:        https://files.pythonhosted.org/packages/source/c/crypt_r/crypt_r-%{version}.tar.gz
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 61
Requires:       python3-crypt-r = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-crypt-r
Summary:        A copy of the `crypt` module that was removed in Python 3.13
%description -n python3-crypt-r

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir crypt_r-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-crypt-r usr/lib/python3*/site-packages/crypt_r* usr/lib64/python3*/site-packages/crypt_r* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/crypt_r* usr/lib64/python3*/site-packages/crypt_r* usr/bin/*

%check

%{py3_test_envvars} %{python3} tests/test_crypt_r.py
%files
%files -n python3-crypt-r -f %{oreon_filedir}/python3-crypt-r.list

%changelog

%autochangelog

