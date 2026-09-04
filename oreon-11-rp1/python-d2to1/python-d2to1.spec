%global source0_hash 49ef2d16862b3efdc81fc5c32eac373b984945cde5fc02bb01a0a11ff03dd825

%global srcname d2to1

Name: python-%{srcname}
Version: 0.2.12
Release: 41.post1%{?dist}
Summary: Allows using distutils2-like setup.cfg files with setup.py
License: BSD-3-Clause

URL: http://pypi.python.org/pypi/d2to1
#Source0: http://pypi.python.org/packages/source/d/d2to1/%{srcname}-%{version}.tar.gz
Source0: https://pypi.python.org/packages/source/d/d2to1/d2to1-0.2.12.post1.tar.gz

# Compatibility with the newer setuptools
Patch:   setuptools-compatibility.patch

BuildArch: noarch

%global _description\
d2to1 allows using distutils2-like setup.cfg files for a package's metadata\
with a distribute/setuptools setup.py script. It works by providing a\
distutils2-formatted setup.cfg file containing all of a package's metadata,\
and a very minimal setup.py which will slurp its arguments from the setup.cfg.

%description %_description

%package -n python3-d2to1
Summary: Allows using distutils2-like setup.cfg files with setup.py
%{?python_provide:%python_provide python3-d2to1}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
Requires:  python3-setuptools

%description -n python3-d2to1 %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%dnl %setup -q -n %{srcname}-%{version}
%autosetup -n %{srcname}-%{version}.post1 -p1

find . -name '*.py' | xargs sed -i '1s|^#!python|#!%{__python3}|'

%build
%py3_build

%install
%py3_install

%files -n python3-d2to1
%doc CHANGES.rst README.rst
%license LICENSE
%{python3_sitelib}/*

%changelog
%autochangelog
