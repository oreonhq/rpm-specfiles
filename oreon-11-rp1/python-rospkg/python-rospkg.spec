%global source0_hash 9341c8af5f547888ab484ee61b53d8447b6a52081222d2d5257757ab374c657f

%global srcname rospkg

Name:           python-%{srcname}
Version:        1.6.0
Release:        6%{?dist}
Summary:        Utilities for ROS package, stack, and distribution information

License:        BSD-3-Clause
URL:            http://ros.org/wiki/rospkg
Source0:        https://github.com/ros-infrastructure/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%description
The ROS packaging system simplifies development and distribution of code
libraries. It enables you to easily specify dependencies between code
libraries, easily interact with those libraries from the command-line, and
release your code for others to use.

%package doc
Summary:        Documentation for %{name}
BuildRequires:  make
BuildRequires:  python%{python3_pkgversion}-catkin-sphinx
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-sphinx

%description doc
HTML documentation for the '%{srcname}' Python module.

%package -n python%{python3_pkgversion}-%{srcname}
Summary:        Utilities for ROS package, stack, and distribution information
BuildRequires:  python%{python3_pkgversion}-catkin_pkg
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-distro
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-PyYAML
BuildRequires:  python%{python3_pkgversion}-setuptools
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}
Obsoletes:      python2-%{srcname} < 1.1.10-3

%if %{undefined __pythondist_requires}
Requires:       python%{python3_pkgversion}-catkin_pkg
Requires:       python%{python3_pkgversion}-distro
Requires:       python%{python3_pkgversion}-PyYAML
%endif

Suggests:       %{name}-doc = %{version}-%{release}

%description -n python%{python3_pkgversion}-%{srcname}
The ROS packaging system simplifies development and distribution of code
libraries. It enables you to easily specify dependencies between code
libraries, easily interact with those libraries from the command-line, and
release your code for others to use.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{srcname}-%{version}

find test -type f | xargs sed -i '1{s@^#!/usr/bin/env python@#!%{__python3}@}'

%build
%py3_build

%make_build -C doc html man SPHINXBUILD=sphinx-build-%{python3_version}
rm doc/_build/html/.buildinfo

%install
%py3_install

# backwards compatibility symbolic links
pushd %{buildroot}%{_bindir}
for i in *; do
  ln -s ./$i python3-$i
done
popd
install -p -m0644 -D doc/man/rosversion.1 %{buildroot}%{_mandir}/man1/rosversion.1

%check
%if 0%{?rhel}
export LANG=en_US.UTF-8
%endif

%pytest

%files doc
%doc doc/_build/html

%files -n python%{python3_pkgversion}-%{srcname}
%doc README.md
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info/
%{_bindir}/rosversion
%{_bindir}/python3-rosversion
%{_mandir}/man1/rosversion.1.*

%changelog
%autochangelog
