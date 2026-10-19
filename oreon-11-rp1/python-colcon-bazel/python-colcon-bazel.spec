%global source0_hash a09baa677044e6174e7b90eefdec3971f2fb80984a1304f87d59d91d5eb4282b
%global srcname colcon-bazel
Name:           python-%{srcname}
Version:        0.1.0
Release:        1%{?dist}
Summary:        Extension for colcon to support Bazel packages
License:        Apache-2.0
URL:            https://colcon.readthedocs.io
Source0:        https://github.com/colcon/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz
Patch0:         %{name}-0.1.0-python-39.patch
Patch1:         %{name}-0.1.0-regex-escapes.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  python3-colcon-argcomplete
BuildRequires:  python3-colcon-core
BuildRequires:  python3-devel
BuildRequires:  python3-pyparsing
BuildRequires:  python3-pytest
BuildRequires:  python3-setuptools
# /oreon:deps
%description
An extension for colcon-core to support Bazel projects.

%package -n python%{python3_pkgversion}-%{srcname}
Summary:        Extension for colcon to support Bazel packages
BuildRequires:  python%{python3_pkgversion}-colcon-argcomplete
BuildRequires:  python%{python3_pkgversion}-colcon-core >= 0.3.9
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pyparsing
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-setuptools >= 30.3.0
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}
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
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%{__python3} -m pytest \
    --ignore=test/test_spell_check.py \
    --ignore=test/test_flake8.py \
    test
%files -f %{oreon_filedir}/main.list
%files -n python3-colcon-bazel -f %{oreon_filedir}/python3-colcon-bazel.list

%changelog

%autochangelog
