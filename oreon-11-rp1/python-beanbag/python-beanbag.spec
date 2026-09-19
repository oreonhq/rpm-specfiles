%global source0_hash c6aa1e90ad229a6352e4e5f2d468b9cbf3522d74f7a6ac963e88cba769aaf780

Name:           python-beanbag
Version:        1.9.2
Release:        40%{?dist}
Summary:        A helper module for accessing REST APIs
License:        MIT
URL:            https://github.com/ajtowns/beanbag
BuildArch:      noarch

Source0:        https://pypi.python.org/packages/source/b/beanbag/beanbag-%{version}.tar.gz
# Python 3.6 changed the way it was handling the initialization of classes in a metaclass
# thus making tests to fail. This patch addresses the issue.
# Relevant info:
# http://bugs.python.org/issue23722
# https://docs.python.org/3/reference/datamodel.html#class-object-creation
# Patch sent upstream: https://github.com/ajtowns/beanbag/pull/10
Patch0:			py36-metaclass-compatibility.patch

# pytst 5.1+
# pytest.raises no longer supports strings as the second argument
# switch to context managers
Patch1:         pytest5.1-compatibility.patch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pytest
BuildRequires:  python3-requests

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

%check
%pytest

%files -n python3-beanbag
%doc README.rst
%license LICENSE
%{python3_sitelib}/beanbag*

%changelog
%autochangelog
