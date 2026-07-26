%global source0_hash c006a85e7c60107c7cc6da1b184b5c719f6dd7202098196dfa6e55df669b59bf

%global reltag post1

%if 0%{?fedora} > 33 || 0%{?rhel} > 8
%global with_py2 0
%else
%global with_py2 1
%endif

Name:			python-oauth2
Summary:		Python support for improved oauth
Version:		1.9.0
Release:		39.%{reltag}%{?dist}
License:		MIT
Source0:		http://pypi.python.org/packages/source/o/oauth2/oauth2-%{version}.%{reltag}.tar.gz
# https://github.com/pmakowski/python-oauth2/commit/7002422bb39bc137713933bc2e55251853830fcc
Patch1:			python-oauth2-1.9.0-CVE-2013-4346.patch
URL:			http://pypi.python.org/pypi/oauth2/
BuildArch:		noarch
%if 0%{?with_py2}
BuildRequires:		python2-devel, python2-setuptools
%endif
BuildRequires:		python3-devel
BuildRequires:		python3-setuptools
# These are the test requires, but since we don't run the tests, we disable them here.
# BuildRequires:	python2-mock, python2-httplib2, python2-coverage
%if 0%{?with_py2}
Requires:		python2-httplib2
%endif

%description
Oauth2 was originally forked from Leah Culver and Andy Smith's oauth.py 
code. Some of the tests come from a fork by Vic Fryzel, while a revamped 
Request class and more tests were merged in from Mark Paschal's fork. A 
number of notable differences exist between this code and its forefathers:

- 100% unit test coverage.
- The DataStore object has been completely ripped out. While creating unit 
  tests for the library I found several substantial bugs with the 
  implementation and confirmed with Andy Smith that it was never fully 
  baked.
- Classes are no longer prefixed with OAuth.
- The Request class now extends from dict.
- The library is likely no longer compatible with Python 2.3.
- The Client class works and extends from httplib2. It's a thin wrapper 
  that handles automatically signing any normal HTTP request you might 
  wish to make.

%if 0%{?with_py2}
%package -n python2-oauth2
Summary:        Python support for improved oauth
%{?python_provide:%python_provide python2-oauth2}

%description -n python2-oauth2
Oauth2 was originally forked from Leah Culver and Andy Smith's oauth.py 
code. Some of the tests come from a fork by Vic Fryzel, while a revamped 
Request class and more tests were merged in from Mark Paschal's fork. A 
number of notable differences exist between this code and its forefathers:

- 100% unit test coverage.
- The DataStore object has been completely ripped out. While creating unit 
  tests for the library I found several substantial bugs with the 
  implementation and confirmed with Andy Smith that it was never fully 
  baked.
- Classes are no longer prefixed with OAuth.
- The Request class now extends from dict.
- The library is likely no longer compatible with Python 2.3.
- The Client class works and extends from httplib2. It's a thin wrapper 
  that handles automatically signing any normal HTTP request you might 
  wish to make.
%endif

%package -n python3-oauth2
Summary:        Python support for improved oauth
%{?python_provide:%python_provide python3-oauth2}

%description -n python3-oauth2
Oauth2 was originally forked from Leah Culver and Andy Smith's oauth.py 
code. Some of the tests come from a fork by Vic Fryzel, while a revamped 
Request class and more tests were merged in from Mark Paschal's fork. A 
number of notable differences exist between this code and its forefathers:

- 100% unit test coverage.
- The DataStore object has been completely ripped out. While creating unit 
  tests for the library I found several substantial bugs with the 
  implementation and confirmed with Andy Smith that it was never fully 
  baked.
- Classes are no longer prefixed with OAuth.
- The Request class now extends from dict.
- The library is likely no longer compatible with Python 2.3.
- The Client class works and extends from httplib2. It's a thin wrapper 
  that handles automatically signing any normal HTTP request you might 
  wish to make.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n oauth2-%{version}.%{reltag}
%patch -P1 -p1 -b .CVE-2013-4346

%build
%if 0%{?with_py2}
%py2_build
%endif
%py3_build

%install
%if 0%{?with_py2}
%py2_install
%endif
%py3_install

# Do not package the "tests"
%if 0%{?with_py2}
rm -rf %{buildroot}%{python2_sitelib}/tests/
%endif
rm -rf %{buildroot}%{python3_sitelib}/tests/

%check
# Tests try to access the network, which doesn't work in koji.
# export PYTHONPATH=$RPM_BUILD_ROOT/%%{python_sitelib}
# %%{__python} setup.py test

%if 0%{?with_py2}
%files -n python2-oauth2
%doc PKG-INFO
%{python2_sitelib}/*
%endif

%files -n python3-oauth2
%doc PKG-INFO
%{python3_sitelib}/*

%changelog
%autochangelog
