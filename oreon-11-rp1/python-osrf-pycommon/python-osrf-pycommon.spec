%global source0_hash be3aa5ae07c8709ee51ec8dd8dc0a5e4f36ced16e437f953edd8739bf1be460f

%global srcname osrf_pycommon
%global pkgname osrf-pycommon

Name:           python-%{pkgname}
Version:        2.1.5
Release:        7%{?dist}
Summary:        Commonly needed Python modules used by software developed at OSRF

# The entire source code is ASL 2.0 except parts of osrf_pycommon/terminal_color/windows.py which is BSD
License:        Apache-2.0 AND BSD-3-Clause
URL:            http://osrf-pycommon.readthedocs.org/
Source0:        https://github.com/osrf/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz

# Don't attempt to query a webserver for intersphinx inventory
Patch0:         osrf_pycommon-2.0.0-intersphinx.patch

BuildArch:      noarch

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
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-devel
%if 0%{?rhel} && 0%{?rhel} < 9
BuildRequires:  python%{python3_pkgversion}-importlib-metadata
%endif
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

%check
%pytest tests -k 'not test_code_format'

%files doc
%license LICENSE
%doc docs/_build/html

%files -n python%{python3_pkgversion}-%{pkgname}
%license LICENSE
%doc CHANGELOG.rst README.md
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info/
%{_mandir}/man1/%{srcname}.1.gz

%changelog
%autochangelog
