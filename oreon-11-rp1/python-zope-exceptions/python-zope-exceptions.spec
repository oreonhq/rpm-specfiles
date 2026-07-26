%global source0_hash 00642014c4e584a5b6f518fc5b756b30bbcd0c6fac400d4af150c924355905f2

%global modname zope.exceptions
%global giturl  https://github.com/zopefoundation/zope.exceptions

# There is a test dependency loop, so we need a way to build this without tests
# zope.exceptions -> zope.testrunner-> zope.exceptions
%bcond tests 1

Summary:    Zope Exceptions
Name:       python-zope-exceptions
Version:    6.0
Release:    4%{?dist}
VCS:        git:%{giturl}.git
Source0:    %{giturl}/archive/%{version}/%{modname}-%{version}.tar.gz
License:    ZPL-2.1
BuildArch:  noarch
URL:        https://zopeexceptions.readthedocs.io/

%description
This package contains exception interfaces and implementations which are so
general purpose that they don't belong in Zope application-specific packages.

%package -n python3-zope-exceptions
Summary:    Zope Exceptions
BuildRequires:  python3-devel

%description -n python3-zope-exceptions
This package contains exception interfaces and implementations which are so
general purpose that they don't belong in Zope application-specific packages.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{modname}-%{version} -p1
# we don't have specific versions of setuptools available
sed -i -r 's/("| )setuptools == /\1setuptools >= /' pyproject.toml tox.ini

%generate_buildrequires
%pyproject_buildrequires %{?with_tests:-t}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files zope

%check
%pyproject_check_import
%if %{with tests}
%tox
%endif

%files -n python3-zope-exceptions -f %{pyproject_files}
%doc CHANGES.rst README.rst
%license COPYRIGHT.txt LICENSE.txt

%changelog
%autochangelog
