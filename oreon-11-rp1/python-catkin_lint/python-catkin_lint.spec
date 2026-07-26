%global source0_hash 40abf9fc402e13467f96fa5b284c0c0e4184e8b8976a76dfc3175db4ddde8ef4

%global srcname catkin_lint

Name:           python-%{srcname}
Version:        1.6.22
Release:        14%{?dist}
Summary:        Check catkin packages for common errors

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        https://github.com/fkie/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz
# https://github.com/fkie/catkin_lint/pull/111
# https://github.com/fkie/catkin_lint/issues/110
# https://bugzilla.redhat.com/show_bug.cgi?id=2259550
# Handle ntpath.isabs change in Python 3.13
Patch:          0001-Handle-changed-ntpath.isabs-behaviour-in-Python-3.13.patch

BuildArch:      noarch

%description
catkin_lint checks package configurations for the catkin build system of ROS.
It runs a static analysis of the package.xml and CMakeLists.txt files in your
package, and it will detect and report a number of common problems.

%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-catkin_pkg
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-lxml
BuildRequires:  python%{python3_pkgversion}-nose2
BuildRequires:  python%{python3_pkgversion}-rosdistro
BuildRequires:  python%{python3_pkgversion}-rospkg
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-setuptools_scm
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

%if %{undefined __pythondist_requires}
Requires:       python%{python3_pkgversion}-catkin_pkg
Requires:       python%{python3_pkgversion}-lxml
%endif

%if !0%{?rhel} || 0%{?rhel} >= 8
Recommends:     python%{python3_pkgversion}-rosdep
Recommends:     python%{python3_pkgversion}-rosdistro
Recommends:     python%{python3_pkgversion}-rospkg
%endif

%description -n python%{python3_pkgversion}-%{srcname}
catkin_lint checks package configurations for the catkin build system of ROS.
It runs a static analysis of the package.xml and CMakeLists.txt files in your
package, and it will detect and report a number of common problems.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{srcname}-%{version}

%build
SETUPTOOLS_SCM_PRETEND_VERSION=%{version} \
  %py3_build
mv build/scripts-%{python3_version}/%{srcname} build/scripts-%{python3_version}/%{srcname}-%{python3_version}
ln -s %{srcname}-%{python3_version} build/scripts-%{python3_version}/%{srcname}-3
ln -s %{srcname}-%{python3_version} build/scripts-%{python3_version}/%{srcname}

%install
SETUPTOOLS_SCM_PRETEND_VERSION=%{version} \
  %py3_install

install -p -D -m0644 shell/bash/%{srcname} %{buildroot}%{_sysconfdir}/bash_completion.d/%{srcname}

%check
%{__python3} -m nose2 test

%files -n python%{python3_pkgversion}-%{srcname}
%license LICENSE
%doc changelog.txt README.rst
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info/
%{_bindir}/%{srcname}
%{_bindir}/%{srcname}-3
%{_bindir}/%{srcname}-%{python3_version}
%{_datadir}/bash-completion/completions/%{srcname}
%{_datadir}/fish/vendor_completions.d/%{srcname}.fish
%{_sysconfdir}/bash_completion.d/%{srcname}

%changelog
%autochangelog
