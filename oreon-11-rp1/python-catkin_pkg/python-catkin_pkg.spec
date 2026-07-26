%global source0_hash 32c0410cb815497a0253838ca8f7d222d345a3bbd189fa4e61374a8f77c42709

%global srcname catkin_pkg

Name:           python-%{srcname}
Version:        1.1.0
Release:        3%{?dist}
Summary:        Library for retrieving information about catkin packages

License:        BSD-3-Clause
URL:            https://github.com/ros-infrastructure/catkin_pkg
Source0:        https://github.com/ros-infrastructure/catkin_pkg/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%description
%{summary}

%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-dateutil
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-docutils
BuildRequires:  python%{python3_pkgversion}-packaging
BuildRequires:  python%{python3_pkgversion}-pyparsing
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-setuptools
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

%if %{undefined __pythondist_requires}
Requires:       python%{python3_pkgversion}-dateutil
Requires:       python%{python3_pkgversion}-docutils
Requires:       python%{python3_pkgversion}-packaging
Requires:       python%{python3_pkgversion}-pyparsing
Requires:       python%{python3_pkgversion}-setuptools
%endif

%if !0%{?rhel} || 0%{?rhel} >= 8
Suggests:       %{name}-doc = %{version}-%{release}
%endif

%description -n python%{python3_pkgversion}-%{srcname}
%{summary}

%package doc
Summary:        HTML documentation for %{name}
BuildRequires:  make
BuildRequires:  python%{python3_pkgversion}-sphinx

%description doc
HTML API documentation for the Python module '%{srcname}'

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{srcname}-%{version}

%build
%py3_build

PYTHONPATH=$PWD/build/lib \
  PYTHONDONTWRITEBYTECODE=1 \
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
%pytest test -k 'not linter'

%files doc
%license LICENSE
%doc doc/_build/html

%files -n python%{python3_pkgversion}-%{srcname}
%license LICENSE
%doc CHANGELOG.rst README.rst
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info/
%{_bindir}/catkin_create_pkg
%{_bindir}/catkin_find_pkg
%{_bindir}/catkin_generate_changelog
%{_bindir}/catkin_package_version
%{_bindir}/catkin_prepare_release
%{_bindir}/catkin_tag_changelog
%{_bindir}/catkin_test_changelog
%{_bindir}/python%{python3_pkgversion}-catkin_create_pkg
%{_bindir}/python%{python3_pkgversion}-catkin_find_pkg
%{_bindir}/python%{python3_pkgversion}-catkin_generate_changelog
%{_bindir}/python%{python3_pkgversion}-catkin_package_version
%{_bindir}/python%{python3_pkgversion}-catkin_prepare_release
%{_bindir}/python%{python3_pkgversion}-catkin_tag_changelog
%{_bindir}/python%{python3_pkgversion}-catkin_test_changelog

%changelog
%autochangelog
