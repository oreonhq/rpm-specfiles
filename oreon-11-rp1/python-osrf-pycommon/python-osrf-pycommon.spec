%global source0_hash be3aa5ae07c8709ee51ec8dd8dc0a5e4f36ced16e437f953edd8739bf1be460f
%global srcname osrf_pycommon
%global pkgname osrf-pycommon
Name:           python-%{pkgname}
Version:        2.1.5
Release:        1%{?dist}
Summary:        Commonly needed Python modules used by software developed at OSRF
License:        Apache-2.0 AND BSD-3-Clause
URL:            http://osrf-pycommon.readthedocs.org/
Source0:        https://github.com/osrf/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz
Patch0:         osrf_pycommon-2.0.0-intersphinx.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-setuptools
BuildRequires:  python3-sphinx
# /oreon:deps
%description
osrf_pycommon is a python package which contains commonly used Python
boilerplate code and patterns. Things like ANSI terminal coloring, capturing
colored output from programs using sub-process, or even a simple logging system
which provides some nice functionality over the built-in Python logging system.

The functionality provided here should be generic enough to be reused in
arbitrary scenarios and should avoid bringing in dependencies which are not
part of the standard Python library. Where possible Windows and Linux/OS X
should be supported, and where it cannot it should be gracefully degrading.

%package doc
Summary:        API Documentation for the osrf_pycommon Python modules
BuildRequires:  make
BuildRequires:  python%{python3_pkgversion}-sphinx
%description doc
HTML documentation generated from osrf_pycommon sources to be used in
developing software which uses osrf_pycommon.

%package -n python%{python3_pkgversion}-%{pkgname}
Summary:        Commonly needed Python modules used by software developed at OSRF
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-setuptools
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pkgname}}
Suggests:       %{name}-doc = %{version}-%{release}
%description -n python%{python3_pkgversion}-%{pkgname}
osrf_pycommon is a python package which contains commonly used Python
boilerplate code and patterns. Things like ANSI terminal coloring, capturing
colored output from programs using sub-process, or even a simple logging system
which provides some nice functionality over the built-in Python logging system.

The functionality provided here should be generic enough to be reused in
arbitrary scenarios and should avoid bringing in dependencies which are not
part of the standard Python library. Where possible Windows and Linux/OS X
should be supported, and where it cannot it should be gracefully degrading.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{srcname}-%{version}

# Don't install the package.xml
sed -i "\\|'share/' + package_name, \\['package.xml'\\]|d" setup.py

# Don't install the resource marker
sed -i "\\|('share/ament_index/resource_index/packages',|$!{
  N
  \\|('share/ament_index/resource_index/packages',\n *\\['resource/' + package_name\\])|d
  }" setup.py

%build

%py3_build
%make_build -C docs html man SPHINXBUILD=sphinx-build-%{python3_version}
rm docs/_build/html/.buildinfo
%install
%py3_install
install -p -m0644 -D docs/_build/man/%{srcname}.1 %{buildroot}%{_mandir}/man1/%{srcname}.1
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%pytest tests -k 'not test_code_format'
%files -f %{oreon_filedir}/main.list
%files -n python-osrf-pycommon-doc -f %{oreon_filedir}/python-osrf-pycommon-doc.list
%files -n python3-osrf-pycommon -f %{oreon_filedir}/python3-osrf-pycommon.list

%changelog

%autochangelog
