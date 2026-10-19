%global source0_hash 07a940fae3683a18a31898ffb1fd86a52d255063ec94f2be89249afeb5fdc18e
%global srcname colcon-argcomplete
Name:           python-%{srcname}
Version:        0.3.3
Release:        1%{?dist}
Summary:        Completion for colcon command lines using argcomplete
License:        Apache-2.0
URL:            https://colcon.readthedocs.io
Source0:        https://github.com/colcon/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz
Patch0:         %{name}-0.3.0-data-files.patch
Patch1:         %{name}-0.3.1-use-root-argument.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-setuptools
# /oreon:deps
%description
An extension for colcon-core to provide command line completion using
argcomplete.

%package -n python%{python3_pkgversion}-%{srcname}
Summary:        Completion for colcon command lines using argcomplete
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-setuptools >= 30.3.0
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}
%if %{undefined __pythondist_requires}
Requires:       python%{python3_pkgversion}-argcomplete
Requires:       python%{python3_pkgversion}-colcon-core
%endif # __pythondist_requires
%description -n python%{python3_pkgversion}-%{srcname}
An extension for colcon-core to provide command line completion using
argcomplete.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{srcname}-%{version}

%build

BUILD_DEBIAN_PACKAGE=1 \
    %py3_build
%install
BUILD_DEBIAN_PACKAGE=1 \
    %py3_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%{__python3} -m pytest \
    --ignore=test/test_spell_check.py \
    --ignore=test/test_flake8.py \
    test
%files -f %{oreon_filedir}/main.list
%files -n python3-colcon-argcomplete -f %{oreon_filedir}/python3-colcon-argcomplete.list

%changelog

%autochangelog
