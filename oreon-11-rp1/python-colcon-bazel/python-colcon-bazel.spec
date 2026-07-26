%global source0_hash a09baa677044e6174e7b90eefdec3971f2fb80984a1304f87d59d91d5eb4282b

%global srcname colcon-bazel

Name:           python-%{srcname}
Version:        0.1.0
Release:        30%{?dist}
Summary:        Extension for colcon to support Bazel packages

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://colcon.readthedocs.io
Source0:        https://github.com/colcon/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz

# Submitted upstream as colcon/colcon-bazel#15
Patch0:         %{name}-0.1.0-python-39.patch
# Submitted upstream as colcon/colcon-bazel#16
Patch1:         %{name}-0.1.0-regex-escapes.patch

BuildArch:      noarch

%description
An extension for colcon-core to support Bazel projects.

%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-colcon-argcomplete
BuildRequires:  python%{python3_pkgversion}-colcon-core >= 0.3.9
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pyparsing
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-setuptools >= 30.3.0
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

%if !0%{?rhel} || 0%{?rhel} >= 8
BuildRequires:  python%{python3_pkgversion}-pytest-asyncio
%endif

%if %{undefined __pythondist_requires}
Requires:       python%{python3_pkgversion}-colcon-core >= 0.3.9
Requires:       python%{python3_pkgversion}-colcon-library-path
Requires:       python%{python3_pkgversion}-pyparsing
%endif

%description -n python%{python3_pkgversion}-%{srcname}
An extension for colcon-core to support Bazel projects.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%check
%{__python3} -m pytest \
    --ignore=test/test_spell_check.py \
    --ignore=test/test_flake8.py \
    test

%files -n python%{python3_pkgversion}-%{srcname}
%license LICENSE
%doc README.md
%{python3_sitelib}/colcon_bazel/
%{python3_sitelib}/colcon_bazel-%{version}-py%{python3_version}.egg-info/

%changelog
%autochangelog
