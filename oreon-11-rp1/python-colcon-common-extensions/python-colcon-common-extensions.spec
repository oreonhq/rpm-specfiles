%global source0_hash f3b2e939f201e949486324cb0145216be478b7160d882017c5fb4210851cd316

%global srcname colcon-common-extensions

Name:           python-%{srcname}
Version:        0.3.0
Release:        17%{?dist}
Summary:        Meta package aggregating colcon-core and common extensions

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://colcon.readthedocs.io
Source0:        https://github.com/colcon/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%description
A meta package aggregating colcon-core as well as a set of common extensions.

%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools >= 30.3.0
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

%if %{undefined __pythondist_requires}
Requires:       python%{python3_pkgversion}-colcon-argcomplete
Requires:       python%{python3_pkgversion}-colcon-bash
Requires:       python%{python3_pkgversion}-colcon-cd
Requires:       python%{python3_pkgversion}-colcon-cmake
Requires:       python%{python3_pkgversion}-colcon-core
Requires:       python%{python3_pkgversion}-colcon-defaults
Requires:       python%{python3_pkgversion}-colcon-devtools
Requires:       python%{python3_pkgversion}-colcon-library-path
Requires:       python%{python3_pkgversion}-colcon-metadata
Requires:       python%{python3_pkgversion}-colcon-notification
Requires:       python%{python3_pkgversion}-colcon-output
Requires:       python%{python3_pkgversion}-colcon-package-information
Requires:       python%{python3_pkgversion}-colcon-package-selection
Requires:       python%{python3_pkgversion}-colcon-parallel-executor
Requires:       python%{python3_pkgversion}-colcon-powershell
Requires:       python%{python3_pkgversion}-colcon-python-setup-py
Requires:       python%{python3_pkgversion}-colcon-recursive-crawl
Requires:       python%{python3_pkgversion}-colcon-ros
Requires:       python%{python3_pkgversion}-colcon-test-result
Requires:       python%{python3_pkgversion}-colcon-zsh
%endif

%if !0%{?rhel} || 0%{?rhel} >= 8
Recommends:     python%{python3_pkgversion}-colcon-override-check
%endif

%description -n python%{python3_pkgversion}-%{srcname}
A meta package aggregating colcon-core as well as a set of common extensions.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%files -n python%{python3_pkgversion}-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/colcon_common_extensions/
%{python3_sitelib}/colcon_common_extensions-%{version}-py%{python3_version}.egg-info/

%changelog
%autochangelog
