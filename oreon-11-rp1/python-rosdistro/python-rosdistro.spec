%global source0_hash aeb1b2f5c065b79840df979f2c4e11ee05328eb6e86e8df9111019a4f0e42260

%global srcname rosdistro

Name:           python-%{srcname}
Version:        1.0.1
Release:        7%{?dist}
Summary:        File format for managing ROS Distributions

License:        BSD-3-Clause AND MIT
URL:            http://www.ros.org/wiki/rosdistro
Source0:        https://github.com/ros-infrastructure/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%description
The rosdistro tool allows you to get access to the full dependency tree and
the version control system information of all packages and repositories. To
increase performance, the rosdistro tool will automatically look for a cache
file on your local disk. If no cache file is found locally, it will try to
download the latest cache file from the server. The cache files are only used
to improve performance, and are not needed to get correct results. rosdistro
will automatically go to Github to find any dependencies that are not part
of the cache file. Note that operation without a cache file can be very slow,
depending on your own internet connection and the response times of Github.
The rosdistro tool will always write the latest dependency information to a
local cache file, to speed up performance for the next query.

%package doc
Summary:        HTML documentation for '%{name}'
BuildRequires:  make
BuildRequires:  python%{python3_pkgversion}-catkin-sphinx
BuildRequires:  python%{python3_pkgversion}-sphinx

%description doc
HTML documentation for the '%{srcname}' python module

%package -n python%{python3_pkgversion}-%{srcname}
Summary:        File format for managing ROS Distributions
BuildRequires:  git
BuildRequires:  python%{python3_pkgversion}-catkin_pkg
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-PyYAML
BuildRequires:  python%{python3_pkgversion}-rospkg
BuildRequires:  python%{python3_pkgversion}-setuptools
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}
Obsoletes:      python2-%{srcname} < 0.7.4-4

%if %{undefined __pythondist_requires}
Requires:       python%{python3_pkgversion}-catkin_pkg
Requires:       python%{python3_pkgversion}-PyYAML
Requires:       python%{python3_pkgversion}-rospkg
Requires:       python%{python3_pkgversion}-setuptools
%endif

Suggests:       %{name}-doc = %{version}-%{release}

%description -n python%{python3_pkgversion}-%{srcname}
The rosdistro tool allows you to get access to the full dependency tree and
the version control system information of all packages and repositories. To
increase performance, the rosdistro tool will automatically look for a cache
file on your local disk. If no cache file is found locally, it will try to
download the latest cache file from the server. The cache files are only used
to improve performance, and are not needed to get correct results. rosdistro
will automatically go to Github to find any dependencies that are not part
of the cache file. Note that operation without a cache file can be very slow,
depending on your own internet connection and the response times of Github.
The rosdistro tool will always write the latest dependency information to a
local cache file, to speed up performance for the next query.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{srcname}-%{version}

%build
%py3_build

PYTHONPATH=$PWD/src \
  %make_build -C doc html SPHINXBUILD=sphinx-build-%{python3_version} SPHINXAPIDOC=sphinx-apidoc-%{python3_version}
rm doc/_build/html/.buildinfo

%install
%py3_install

# backwards compatibility symbolic links
pushd %{buildroot}%{_bindir}
for i in *; do
  ln -s ./$i python%{python3_pkgversion}-$i
done
popd

%check
%pytest -k 'not test_manifest_providers' test

%files doc
%license LICENSE.txt
%doc doc/_build/html

%files -n python%{python3_pkgversion}-%{srcname}
%license LICENSE.txt
%doc README.md
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info/
%{_bindir}/rosdistro_build_cache
%{_bindir}/rosdistro_freeze_source
%{_bindir}/rosdistro_migrate_to_rep_141
%{_bindir}/rosdistro_migrate_to_rep_143
%{_bindir}/rosdistro_reformat
%{_bindir}/python%{python3_pkgversion}-rosdistro_build_cache
%{_bindir}/python%{python3_pkgversion}-rosdistro_freeze_source
%{_bindir}/python%{python3_pkgversion}-rosdistro_migrate_to_rep_141
%{_bindir}/python%{python3_pkgversion}-rosdistro_migrate_to_rep_143
%{_bindir}/python%{python3_pkgversion}-rosdistro_reformat

%changelog
%autochangelog
