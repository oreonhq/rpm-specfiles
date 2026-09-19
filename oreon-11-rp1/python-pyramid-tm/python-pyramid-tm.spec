%global source0_hash beab987c6f7390fbaedf9e157e211d5ec6591d9cf6295a73cbaa89a9e67350a7

%global modname pyramid_tm
%global sum A package which allows Pyramid requests to join the active transaction
%global desc pyramid_tm is a package which allows Pyramid requests to join the\
active transaction as provided by the transaction\
http://pypi.python.org/pypi/transaction\
\
See http://docs.pylonsproject.org/projects/pyramid_tm/dev/\
or docs/index.rst in this distribution for detailed documentation.

Name:           python-pyramid-tm
Version:        2.6
Release:        7%{?dist}
Summary:        %{sum}

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            http://pypi.python.org/pypi/pyramid_tm
Source0:        https://github.com/Pylons/pyramid_tm/archive/%{version}/%{modname}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
#BuildRequires:  python3-setuptools
#BuildRequires:  python3-pyramid >= 1.5
#BuildRequires:  python3-transaction >= 2.0
#BuildRequires:  python3-nose
#BuildRequires:  python3-coverage
#BuildRequires:  python3-webtest

%description
%{desc}

%package -n python3-pyramid-tm
Summary:        %{sum}

%{?python_provide:%python_provide python3-pyramid-tm}

Requires:       python3-pyramid >= 1.5
Requires:       python3-transaction >= 2.0

%description -n python3-pyramid-tm
pyramid_tm is a package which allows Pyramid requests to join the
active transaction as provided by the transaction
http://pypi.python.org/pypi/transaction

See http://docs.pylonsproject.org/projects/pyramid_tm/dev/
or docs/index.rst in this distribution for detailed documentation.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{modname}-%{version}

# Make sure that setuptools picks the right version of zope.interface (el6)
#awk 'NR==1{print "import __main__; __main__.__requires__ = __requires__ = [\"zope.interface>=3.8\"]; import pkg_resources"}1' setup.py > setup.py.tmp
#mv setup.py.tmp setup.py

# Remove bundled egg info
#rm -rf %{modname}.egg-info

#rm docs/.gitignore

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files -l pyramid_tm

%check
%{py3_test_envvars} %{python3} -m unittest

%files -n python3-pyramid-tm -f %{pyproject_files}
%doc README.rst docs CONTRIBUTORS.txt CHANGES.rst
%license LICENSE.txt COPYRIGHT.txt

%changelog
%autochangelog
