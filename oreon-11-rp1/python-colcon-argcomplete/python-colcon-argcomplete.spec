%global source0_hash 07a940fae3683a18a31898ffb1fd86a52d255063ec94f2be89249afeb5fdc18e

%global srcname colcon-argcomplete

Name:           python-%{srcname}
Version:        0.3.3
Release:        27%{?dist}
Summary:        Completion for colcon command lines using argcomplete

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://colcon.readthedocs.io
Source0:        https://github.com/colcon/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz

# Taken from sources - disables install of data files per setuptools version
Patch0:         %{name}-0.3.0-data-files.patch
# Submitted upstream - uses the 'root' argument to setup.py install properly
Patch1:         %{name}-0.3.1-use-root-argument.patch

BuildArch:      noarch

%description
An extension for colcon-core to provide command line completion using
argcomplete.

%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
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

%check
%{__python3} -m pytest \
    --ignore=test/test_spell_check.py \
    --ignore=test/test_flake8.py \
    test

%files -n python%{python3_pkgversion}-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/colcon_argcomplete/
%{python3_sitelib}/colcon_argcomplete-%{version}-py%{python3_version}.egg-info/
%{_datadir}/colcon_argcomplete/

%changelog
%autochangelog
