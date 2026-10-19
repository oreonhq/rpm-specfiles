%global source0_hash c6aa1e90ad229a6352e4e5f2d468b9cbf3522d74f7a6ac963e88cba769aaf780
Name:           python-beanbag
Version:        1.9.2
Release:        1%{?dist}
Summary:        A helper module for accessing REST APIs
License:        MIT
URL:            https://github.com/ajtowns/beanbag
BuildArch:      noarch
Source0:        https://pypi.python.org/packages/source/b/beanbag/beanbag-%{version}.tar.gz
Patch0:			py36-metaclass-compatibility.patch
Patch1:         pytest5.1-compatibility.patch
# oreon:deps
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-requests
BuildRequires:  python3-setuptools
# /oreon:deps
%description
BeanBag is a simple module that lets you access REST APIs in an easy way. For
example:

>>> import beanbag
>>> github = beanbag.BeanBag("https://api.github.com")
>>> watchers = github.repos.ajtowns.beanbag.watchers()
>>> for w in watchers:
...     print(w["login"])

See http://beanbag.readthedocs.org/ for more information.

%package -n python3-beanbag
Summary:        A helper module for accessing REST APIs
%{?python_provide:%python_provide python3-beanbag}
Requires:  python3-requests
%description -n python3-beanbag
BeanBag is a simple module that lets you access REST APIs in an easy way. For
example:

>>> import beanbag
>>> github = beanbag.BeanBag("https://api.github.com")
>>> watchers = github.repos.ajtowns.beanbag.watchers()
>>> for w in watchers:
...     print(w["login"])
See http://beanbag.readthedocs.org/ for more information.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n beanbag-%{version}

# Fix compatibility with pytest 7.2.0
sed -i "s/py\.test/pytest/g" tests/test_attrdict.py tests/test_bbv1.py

%build

%py3_build
%install
%py3_install
%oreon_autofiles python3-beanbag usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%pytest
%files -f %{oreon_filedir}/main.list
%files -n python3-beanbag -f %{oreon_filedir}/python3-beanbag.list

%changelog

%autochangelog
