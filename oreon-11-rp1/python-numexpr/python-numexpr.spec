%global source0_hash d85f1c1b41dd26585f452ed446b11a3d6d52ffe735ca0fd56b5d5e02df910ae1
Summary:        Fast numerical array expression evaluator for Python and NumPy
Name:           python-numexpr
Version:        2.14.2
Release:        1%{?dist}
URL:            https://github.com/pydata/numexpr
License:        MIT
Source0:        https://github.com/pydata/numexpr/archive/v%{version}/numexpr-%{version}.tar.gz
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  python3-devel
BuildRequires:  python3-numpy
BuildRequires:  python3-setuptools
# /oreon:deps
%description

%package -n python3-numexpr
Summary:        Fast numerical array expression evaluator for Python and NumPy
Requires:       python3-numpy >= 1.6
%description -n python3-numexpr

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir numexpr-%{version}
%oreon_prep
%build

%py3_build
%install
%py3_install
chmod 0755 %{buildroot}%{python3_sitearch}/numexpr/cpuinfo.py
sed -i "1s|/usr/bin/env python$|%{python3}|" %{buildroot}%{python3_sitearch}/numexpr/cpuinfo.py
%oreon_autofiles python3-numexpr usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

pushd build/lib.linux*
%py3_test_envvars %python3 -c 'import numexpr, sys; sys.exit(not numexpr.test().wasSuccessful())'
popd
%files -f %{oreon_filedir}/main.list
%files -n python3-numexpr -f %{oreon_filedir}/python3-numexpr.list

%changelog

%autochangelog
