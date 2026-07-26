%global source0_hash ceb6fe4ee6f2f356196506814f4a7d22f7f232fb194e6d3cff91182a9c8480d3

%global srcname rosdep

Name:           python-%{srcname}
Version:        0.26.0
Release:        5%{?dist}
Summary:        ROS System Dependency Installer

License:        BSD-3-Clause
URL:            http://ros.org/wiki/%{srcname}
Source0:        https://github.com/ros-infrastructure/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz

# Merged upstream as ros-infrastructure/rosdep#1012
Patch0:         intersphinx-mapping.patch
# Merged upstream as ros-infrastructure/rosdep/1020
Patch1:         drop-aggressive-asserts.patch

BuildArch:      noarch

%description
rosdep is a command-line tool for installing system dependencies. For
end-users, rosdep helps you install system dependencies for software that
you are building from source. For developers, rosdep simplifies the problem
of installing system dependencies on different platforms. Instead of having to
figure out which Debian package on Ubuntu Oneiric contains Boost, you can just
specify a dependency on 'boost'.

%package doc
Summary:        HTML documentation for '%{name}'
BuildRequires:  make
BuildRequires:  python%{python3_pkgversion}-catkin-sphinx
BuildRequires:  python%{python3_pkgversion}-sphinx

%description doc
HTML documentation for the '%{srcname}' python module

%package -n python%{python3_pkgversion}-%{srcname}
Summary:        ROS System Dependency Installer
BuildRequires:  npm
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  rubygems
Requires:       python-srpm-macros
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

%if !0%{?rhel} || 0%{?rhel} >= 8
Recommends:     python%{python3_pkgversion}-pip
Recommends:     python%{python3_pkgversion}-rpm
Suggests:       %{name}-doc = %{version}-%{release}
Suggests:       npm
Suggests:       rubygems
%endif

%description -n python%{python3_pkgversion}-%{srcname}
rosdep is a command-line tool for installing system dependencies. For
end-users, rosdep helps you install system dependencies for software that
you are building from source. For developers, rosdep simplifies the problem
of installing system dependencies on different platforms. Instead of having to
figure out which Debian package on Ubuntu Oneiric contains Boost, you can just
specify a dependency on 'boost'.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

PYTHONPATH=$PWD/src %make_build -C doc man html SPHINXBUILD=sphinx-build-%{python3_version}
rm doc/_build/html/.buildinfo

%install
%pyproject_install
%pyproject_save_files -l rosdep2

#echo -n > py3_bins
for f in `ls %{buildroot}%{_bindir}`; do
    mv %{buildroot}%{_bindir}/$f %{buildroot}%{_bindir}/$f-%{python3_version}
    ln -s $f-%{python3_version} %{buildroot}%{_bindir}/$f-3
    ln -s $f-%{python3_version} %{buildroot}%{_bindir}/$f
    echo -e "%{_bindir}/$f\n%{_bindir}/$f-3\n%{_bindir}/$f-%{python3_version}" >> %{pyproject_files}
done

install -D -p -m 0644 doc/man/rosdep.1 %{buildroot}%{_mandir}/man1/rosdep.1
install -D -p -m 0644 /dev/null %{buildroot}%{_sysconfdir}/ros/rosdep/sources.list.d/20-default.list

# Cannot currently run all of the tests because some need to query Github
%check
%pytest -m 'not online and not linter'

%files doc
%license LICENSE
%doc doc/_build/html

%files -n python%{python3_pkgversion}-%{srcname} -f %{pyproject_files}
%doc README.md
%{_mandir}/man1/%{srcname}.1.gz
%dir %{_sysconfdir}/ros/rosdep/
%dir %{_sysconfdir}/ros/rosdep/sources.list.d/
%ghost %{_sysconfdir}/ros/rosdep/sources.list.d/20-default.list

%changelog
%autochangelog
