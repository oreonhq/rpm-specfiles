%global source0_hash 7d5d0167b2b1ba821647616af46a749d1c653740dd0d2415100fe26e27afdf41
Name:          python-appdirs
Version:       1.4.4
Release:        1%{?dist}
Summary:        Python module for determining platform-specific directories
License:       MIT
URL:           https://github.com/ActiveState/appdirs
Source0:        https://files.pythonhosted.org/packages/source/a/appdirs/appdirs-1.4.4.tar.gz
BuildArch:     noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-appdirs = %{version}-%{release}
# /oreon:deps
%description
A small Python module for determining appropriate " + " platform-specific
directories, e.g. a "user data dir".

%package -n python3-appdirs
Summary:        Python module for determining platform-specific directories
%description -n python3-appdirs
A small Python 3 module for determining appropriate " + " platform-specific
directories, e.g. a "user data dir".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n appdirs-%{version}
sed -i -e '1{\@^#!/usr/bin/env python@d}' appdirs.py

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-appdirs usr/lib/python3*/site-packages/appdirs* usr/lib64/python3*/site-packages/appdirs* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/appdirs* usr/lib64/python3*/site-packages/appdirs* usr/bin/*

%check

%{py3_test_envvars} %{python3} -m unittest discover
%files
%files -n python3-appdirs -f %{oreon_filedir}/python3-appdirs.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.4.4-1
- Prepare for Oreon 11 (RP1)
